import { readFileSync } from "node:fs";
import { join } from "node:path";

const KEY = "f42d097b2239e1408b611e91d388c718";
const HOST = "cloud-practitioner.sintitulo.dev";
const sitemap = readFileSync(join(import.meta.dirname, "..", "site", "sitemap.xml"), "utf8");
const urlList = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);

const response = await fetch("https://api.indexnow.org/IndexNow", {
  method: "POST",
  headers: { "Content-Type": "application/json; charset=utf-8" },
  body: JSON.stringify({ host: HOST, key: KEY, keyLocation: `https://${HOST}/${KEY}.txt`, urlList }),
});
console.log(`${response.status} ${response.statusText} · ${urlList.length} URLs`);
