import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

type Difference = {
  domain: number;
  topic: string;
  id: string;
  title: string;
  hint: string;
  confusion: string;
  rule: string;
  table?: [string, string][];
};

type Data = {
  domains: Record<string, string>;
  labels: Record<string, string>;
  differences: Difference[];
};

const HERE = import.meta.dirname;
const OUTPUT = join(HERE, "..", "site", "diferencias.html");
const data: Data = JSON.parse(readFileSync(join(HERE, "data", "differences.json"), "utf8"));
const template = readFileSync(join(HERE, "templates", "differences.html"), "utf8");

const ESCAPES: Record<string, string> = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#x27;" };
const esc = (text: string): string => text.replace(/[&<>"']/g, (c) => ESCAPES[c]);
const pad = (n: number): string => String(n).padStart(2, "0");

function card(d: Difference, number: number): string {
  let rows = "";
  if (d.table?.length) {
    const body = d.table.map(([situation, answer]) => `              <tr><th scope="row">${esc(situation)}</th><td>${esc(answer)}</td></tr>`).join("\n");
    rows = `
            <table class="mapa">
              <caption class="sr">Qué servicio responde a cada situación</caption>
              <tbody>
${body}
              </tbody>
            </table>`;
  }
  return `        <article class="diferencia" id="${d.id}" data-dif="${d.id}">
          <div class="dif-cabeza">
            <span class="numero">${pad(number)}</span>
            <div class="dif-titular">
              <h3><a href="#${d.id}">${esc(d.title)}</a></h3>
              <p><strong class="pista">${esc(d.hint)}</strong></p>
            </div>
            <label class="dominada">
              <input type="checkbox" data-dominada="${d.id}" aria-label="Marcar como dominada: ${esc(d.title)}">
              <span>Dominada</span>
            </label>
          </div>
          <div class="dif-cuerpo">
            <p class="confusion"><span class="rotulo">Dónde se confunde:</span> ${esc(d.confusion)}</p>
            <p class="regla">${esc(d.rule)}</p>${rows}
            <p class="tema-pie">${esc(d.topic)}</p>
          </div>
        </article>`;
}

const sections: string[] = [];
const index: string[] = [];
const counts: number[] = [];
let next = 1;

for (const domain of [1, 2, 3, 4]) {
  const items = data.differences.filter((d) => d.domain === domain);
  const name = esc(data.domains[String(domain)]);
  const range = `${pad(next)}–${pad(next + items.length - 1)}`;
  sections.push(`      <section class="dominio" id="dominio-${domain}" data-dominio="${domain}">
        <h2>${name} <span class="conteo">${range}</span></h2>
        <div class="lista-diferencias">
${items.map((d, i) => card(d, next + i)).join("\n")}
        </div>
      </section>`);
  const links = items
    .map((d, i) => `              <li><a href="#${d.id}" data-indice="${d.id}"><span class="indice-num">${pad(next + i)}</span> ${esc(data.labels[d.id])}</a></li>`)
    .join("\n");
  index.push(`          <li class="indice-dominio" data-indice-dominio="${domain}">
            <a class="indice-dominio-titulo" href="#dominio-${domain}">${name} <span class="indice-rango">${range}</span></a>
            <ul>
${links}
            </ul>
          </li>`);
  counts.push(items.length);
  next += items.length;
}

const total = data.differences.length;
const html = template
  .replaceAll("{{total}}", String(total))
  .replace("{{index}}", () => index.join("\n"))
  .replace("{{domains}}", () => sections.join("\n"));

writeFileSync(OUTPUT, html);
console.log(`diferencias.html: ${total} diferencias en 4 dominios (${counts.join(", ")})`);
