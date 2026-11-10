import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { collect, restoreSvg } from "./text-blocks.ts";

type Entry = { kind: "inner" | "attr"; attr?: string; es: string; en: string };

const SITE = "https://cloud-practitioner.sintitulo.dev";
const ROOT = join(import.meta.dirname, "..", "site");
const DICTIONARY = join(import.meta.dirname, "i18n", "en.json");

const ROUTES: Record<string, string> = {
  "/": "/en",
  "/metodo": "/en/method",
  "/examen": "/en/exam",
  "/practica": "/en/practice",
  "/diferencias": "/en/differences",
};

const PAGES: [string, string, string][] = [
  ["index.html", "en/index.html", "/"],
  ["metodo.html", "en/method.html", "/metodo"],
  ["examen.html", "en/exam.html", "/examen"],
  ["practica.html", "en/practice.html", "/practica"],
  ["diferencias.html", "en/differences.html", "/diferencias"],
];

const EXTERNAL: Record<string, string> = {
  "https://www.santiagos.mx/es/inicio": "https://santiagos.mx/en/",
};

const keyOf = (e: Pick<Entry, "kind" | "attr" | "es">): string =>
  e.kind === "attr" ? `attr:${e.attr}:${e.es}` : `inner:${e.es}`;

function translate(file: string, source: string, dictionary: Map<string, string>, missing: Set<string>, used: Set<string>): string {
  const occurrences = collect(file, source).sort((a, b) => b.start - a.start);
  let out = source;
  for (const occ of occurrences) {
    const original = source.slice(occ.start, occ.end);
    const key = occ.key.startsWith("inner:") ? `inner:${original.trim()}` : occ.key;
    const english = dictionary.get(key);
    if (english === undefined) {
      missing.add(`${file}: ${key.slice(0, 120)}`);
      continue;
    }
    used.add(key);
    const lead = /^\s*/.exec(original)?.[0] ?? "";
    const trail = /\s*$/.exec(original)?.[0] ?? "";
    out = out.slice(0, occ.start) + lead + restoreSvg(original, english) + trail + out.slice(occ.end);
  }
  return out;
}

function relink(html: string, spanishRoute: string): string {
  return html
    .split("\n")
    .map((line) => {
      if (line.includes('rel="alternate"')) return line;
      if (line.includes('class="idioma"')) {
        return line.replace(
          /<div class="idioma"[\s\S]*?<\/div>/,
          `<div class="idioma" role="group" aria-label="Language"><span class="idioma-actual" lang="en">EN</span><span aria-hidden="true">|</span><a href="${spanishRoute}" hreflang="es" lang="es">ES</a></div>`,
        );
      }
      let next = line
        .replace('<html lang="es-MX">', '<html lang="en-US">')
        .replace('content="es_MX"', 'content="en_US"')
        .replace(/(href|src)="(css|js)\//g, '$1="/$2/');
      next = next.replace(new RegExp(`${SITE}(/[a-z]*)(?=["#])`, "g"), (match, route: string) =>
        ROUTES[route] ? `${SITE}${ROUTES[route]}` : match,
      );
      next = next.replace(/href="(\/[a-z]*)(#[^"]*)?"/g, (match, route: string, hash = "") =>
        ROUTES[route] ? `href="${ROUTES[route]}${hash}"` : match,
      );
      for (const [from, to] of Object.entries(EXTERNAL)) next = next.replaceAll(`"${from}"`, `"${to}"`);
      return next;
    })
    .join("\n");
}

const entries: Entry[] = JSON.parse(readFileSync(DICTIONARY, "utf8"));
const dictionary = new Map(entries.map((e) => [keyOf(e), e.en]));
const missing = new Set<string>();
const used = new Set<string>();

const outputs = PAGES.map(([spanish, english, route]) => {
  const source = readFileSync(join(ROOT, spanish), "utf8");
  return [join(ROOT, english), relink(translate(spanish, source, dictionary, missing, used), route)] as const;
});

const unused = entries.filter((e) => !used.has(keyOf(e)));
if (unused.length) console.log(`${unused.length} entradas de en.json ya no aparecen en el sitio:\n${unused.map((e) => `  ${e.es.slice(0, 80)}`).join("\n")}`);
if (missing.size) {
  console.error(`Faltan ${missing.size} traducciones; no se escribió ninguna página:\n${[...missing].map((m) => `  ${m}`).join("\n")}`);
  process.exit(1);
}
for (const [target, html] of outputs) {
  mkdirSync(dirname(target), { recursive: true });
  writeFileSync(target, html);
}
console.log(`${PAGES.length} páginas en inglés escritas en site/en/`);
