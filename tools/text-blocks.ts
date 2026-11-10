import { readFileSync, writeFileSync } from "node:fs";
import { basename } from "node:path";
import { parse, HTMLElement, NodeType } from "node-html-parser";

export type Block = {
  id: string;
  kind: "inner" | "attr";
  attr?: string;
  original: string;
  files: string[];
};

export type Occurrence = { file: string; start: number; end: number; key: string };

const META_ATTRS = new Set([
  "description",
  "og:title",
  "og:description",
  "og:image:alt",
  "twitter:title",
  "twitter:description",
]);
const TEXT_ATTRS = ["alt", "aria-label", "title", "placeholder"];
const SKIP_TAGS = new Set(["script", "style", "svg", "head"]);

function hasDirectText(el: HTMLElement): boolean {
  return el.childNodes.some((n) => n.nodeType === NodeType.TEXT_NODE && n.rawText.trim() !== "");
}

function innerRange(source: string, el: HTMLElement): [number, number] {
  const [start, end] = el.range;
  const open = source.indexOf(">", start) + 1;
  const tag = el.rawTagName.toLowerCase();
  const close = source.toLowerCase().lastIndexOf(`</${tag}`, end);
  return [open, close];
}

export function collect(file: string, source: string): Occurrence[] {
  const root = parse(source, { comment: false });
  const found: Occurrence[] = [];

  const title = root.querySelector("title");
  if (title) {
    const [s, e] = innerRange(source, title);
    found.push({ file, start: s, end: e, key: `inner:${source.slice(s, e)}` });
  }
  for (const meta of root.querySelectorAll("meta")) {
    const name = meta.getAttribute("name") ?? meta.getAttribute("property") ?? "";
    if (!META_ATTRS.has(name)) continue;
    pushAttr(source, meta, "content", file, found);
  }

  const walk = (el: HTMLElement): void => {
    if (SKIP_TAGS.has(el.rawTagName?.toLowerCase())) return;
    for (const attr of TEXT_ATTRS) pushAttr(source, el, attr, file, found);
    if (el.rawTagName && el.rawTagName.toLowerCase() !== "body" && hasDirectText(el)) {
      const [s, e] = innerRange(source, el);
      found.push({ file, start: s, end: e, key: `inner:${source.slice(s, e)}` });
      for (const child of el.querySelectorAll("*")) {
        for (const attr of TEXT_ATTRS) pushAttr(source, child, attr, file, found);
      }
      return;
    }
    for (const child of el.childNodes) {
      if (child instanceof HTMLElement) walk(child);
    }
  };
  const body = root.querySelector("body");
  if (body) walk(body);
  return found;
}

function pushAttr(source: string, el: HTMLElement, attr: string, file: string, found: Occurrence[]): void {
  const value = el.getAttribute(attr);
  if (!value || !value.trim()) return;
  const [start, end] = el.range;
  const tag = source.slice(start, source.indexOf(">", start) + 1);
  const match = new RegExp(`\\s${attr.replace(/[-:]/g, "\\$&")}="([^"]*)"`).exec(tag);
  if (!match) return;
  const s = start + match.index + match[0].indexOf('"') + 1;
  found.push({ file, start: s, end: s + match[1].length, key: `attr:${attr}:${match[1]}` });
}

function extract(out: string, files: string[]): void {
  const blocks = new Map<string, Block>();
  for (const file of files) {
    const source = readFileSync(file, "utf8");
    for (const occ of collect(file, source)) {
      const existing = blocks.get(occ.key);
      if (existing) {
        if (!existing.files.includes(basename(file))) existing.files.push(basename(file));
        continue;
      }
      const [kind, ...rest] = occ.key.split(":");
      const isAttr = kind === "attr";
      blocks.set(occ.key, {
        id: `b${String(blocks.size + 1).padStart(3, "0")}`,
        kind: isAttr ? "attr" : "inner",
        attr: isAttr ? rest[0] : undefined,
        original: isAttr ? rest.slice(1).join(":") : rest.join(":"),
        files: [basename(file)],
      });
    }
  }
  writeFileSync(out, JSON.stringify([...blocks.values()], null, 2));
  console.log(`${blocks.size} bloques en ${out}`);
}

export const SVG = /<svg[\s\S]*?<\/svg>/g;
export const SVG_TOKEN = "⟦svg⟧";

export function restoreSvg(original: string, text: string): string {
  const svgs = original.match(SVG) ?? [];
  let i = 0;
  return text.replaceAll(SVG_TOKEN, () => svgs[i++] ?? SVG_TOKEN);
}

export function parseRewrites(text: string): Map<string, string> {
  const result = new Map<string, string>();
  const re = /^\[([bd]\d{3})\]\s?([\s\S]*?)(?=^\[[bd]\d{3}\]|^###|(?![\s\S]))/gm;
  for (const m of text.matchAll(re)) result.set(m[1], m[2].trim().replace(/^\((?:atributo [\w:-]+|titulo|pista|confusion|regla|tabla\d+a)\)\s*/, ""));
  return result;
}

function apply(blocksPath: string, rewritesPath: string, files: string[]): void {
  const blocks: Block[] = JSON.parse(readFileSync(blocksPath, "utf8"));
  const rewrites = parseRewrites(readFileSync(rewritesPath, "utf8"));
  const byKey = new Map(blocks.map((b) => [`${b.kind === "attr" ? `attr:${b.attr}` : "inner"}:${b.original}`, b]));
  let changed = 0;
  for (const file of files) {
    const source = readFileSync(file, "utf8");
    const occs = collect(file, source).sort((a, b) => b.start - a.start);
    let next = source;
    for (const occ of occs) {
      const block = byKey.get(occ.key);
      const raw = block && rewrites.get(block.id);
      const text = block && raw !== undefined ? restoreSvg(block.original, raw) : undefined;
      if (!block || text === undefined || text === block.original.trim()) continue;
      const lead = /^\s*/.exec(block.original)?.[0] ?? "";
      const trail = /\s*$/.exec(block.original)?.[0] ?? "";
      next = next.slice(0, occ.start) + lead + text + trail + next.slice(occ.end);
      changed++;
    }
    writeFileSync(file, next);
  }
  console.log(`${changed} reemplazos aplicados`);
}

export const AWS_TERM = /\b(?:AWS|Amazon)(?:\s+[A-Z][\w-]*)+|\b[A-Z][a-z]+[A-Z][\w]*\b|\b[A-Z]{2,}[\w-]*\b/g;
export const NUMBER = /\d+(?:[.,]\d+)?/g;

export function tagsOf(html: string): string[] {
  return [...html.matchAll(/<\/?[a-z][^>]*>/gi)].map((m) => m[0]);
}

export function terms(text: string, re: RegExp): string[] {
  const plain = text.replace(/<[^>]+>/g, " ").replace(/&#8209;/g, "-");
  return [...new Set(plain.match(re) ?? [])].sort();
}

export function plainLength(html: string): number {
  return html.replace(/<[^>]+>/g, "").replace(/&[#\w]+;/g, "x").length;
}

function check(blocksPath: string, rewritesPath: string, low: number, high: number): void {
  const blocks: Block[] = JSON.parse(readFileSync(blocksPath, "utf8"));
  const rewrites = parseRewrites(readFileSync(rewritesPath, "utf8"));
  const problems: string[] = [];
  for (const b of blocks) {
    const raw = rewrites.get(b.id);
    const text = raw === undefined ? undefined : restoreSvg(b.original, raw);
    if (text === undefined) {
      problems.push(`${b.id} falta en la reescritura`);
      continue;
    }
    if (!text.trim()) problems.push(`${b.id} quedó vacío`);
    const a = tagsOf(b.original).join(" ");
    const z = tagsOf(text).join(" ");
    if (a !== z) problems.push(`${b.id} cambió las etiquetas\n    antes: ${a}\n    ahora: ${z}`);
    if (b.kind === "attr" && text.includes('"')) problems.push(`${b.id} trae comillas dobles dentro de un atributo`);
    for (const [label, re] of [["cifras", NUMBER], ["términos", AWS_TERM]] as const) {
      const before = terms(b.original, re);
      const after = terms(text, re);
      const lost = before.filter((t) => !after.includes(t));
      const added = after.filter((t) => !before.includes(t));
      if (lost.length || added.length) {
        problems.push(`${b.id} ${label}: ${lost.length ? `faltan ${lost.join(", ")}` : ""}${lost.length && added.length ? "; " : ""}${added.length ? `nuevas ${added.join(", ")}` : ""}`);
      }
    }
    const ratio = plainLength(text) / Math.max(1, plainLength(b.original));
    if (plainLength(b.original) >= 40 && (ratio < low || ratio > high)) {
      problems.push(`${b.id} largo raro: ${Math.round(ratio * 100)} % del original`);
    }
  }
  const extra = [...rewrites.keys()].filter((id) => !blocks.some((b) => b.id === id));
  for (const id of extra) problems.push(`${id} no existe en los bloques`);
  console.log(problems.length ? problems.join("\n") : "sin problemas");
  console.log(`\n${blocks.length} bloques revisados, ${problems.length} avisos`);
}

function brief(blocksPath: string, file: string): void {
  const blocks: Block[] = JSON.parse(readFileSync(blocksPath, "utf8"));
  const pick = file === "shared" ? (x: Block) => x.files.length > 1 : (x: Block) => x.files.length === 1 && x.files[0] === file;
  for (const b of blocks.filter(pick)) {
    const where = b.kind === "attr" ? ` (atributo ${b.attr})` : "";
    console.log(`[${b.id}]${where} ${b.original.trim().replace(SVG, SVG_TOKEN)}`);
  }
}

if (import.meta.main) {
  const [command, ...args] = process.argv.slice(2);
  if (command === "extract") extract(args[0], args.slice(1));
  else if (command === "apply") apply(args[0], args[1], args.slice(2));
  else if (command === "check") check(args[0], args[1], Number(args[2] ?? "0.6"), Number(args[3] ?? "1.6"));
  else if (command === "brief") brief(args[0], args[1]);
  else {
    console.error("Uso: node text-blocks.ts extract|apply|check|brief ...");
    process.exit(1);
  }
}
