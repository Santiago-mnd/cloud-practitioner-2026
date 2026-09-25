# Cuaderno Cloud Practitioner

Sitio estático para estudiar el examen **AWS Certified Cloud Practitioner (CLF-C02)** en español mexicano.
Gratis, sin cuentas y sin backend: el avance de cada visitante vive en su propio navegador.

Destino: **cloud-practitioner.sintitulo.dev** (Vercel, proyecto `cloud-practitioner-2026`, sin build step).

Parte de una copia del sitio del AZ-900 (`~/personal/az900-sitio`, commit `c9b0198`); el primer commit de este
repositorio es esa copia intacta, para que el historial muestre qué cambió. La investigación y el plan viven en
`~/personal/clf-c02-estudio/`.

## Qué hay

| Archivo | Estado | Contenido |
|---|---|---|
| `index.html` | listo | Portada: diferencia de ejemplo, avance de la práctica, método y resumen de OnVUE |
| `diferencias.html` | listo | Las 45 diferencias, generadas por `generar-diferencias.py` |
| `generar-diferencias.py` | listo | Contenido de las diferencias; regenera `diferencias.html` |
| `metodo.html` | listo | El método de cuatro pasos, con ejemplos de AWS |
| `examen.html` | listo | Agenda, OnVUE, check-in y resultados, con las reglas de Pearson VUE para AWS |
| `practica.html` | en construcción | Aviso temporal; todavía no carga el motor de práctica |
| `js/preguntas.js`, `js/practica.js` | pendiente | Siguen siendo los del AZ-900; se reemplazan con el banco de 240 preguntas |
| `og.png`, `og-fuente.svg` | listo | Imagen para redes |
| `indexnow.py` | pendiente | Apunta al dominio nuevo, pero falta generar su clave |

## Principios

- **Sin cuentas, sin correo, sin rastreo entre sitios.** El progreso se guarda en `localStorage` del visitante.
- **Preguntas propias.** Ninguna se copia del examen real ni de las preguntas de práctica oficiales de AWS.
- **Fecha de verificación visible.** El temario cambia; el pie dice cuándo se verificó el contenido.
- **Todo texto público pasa por `stop-slop` y `copy-editing`.**

## Deploy

```bash
cd ~/personal/clf-c02-site
vercel --prod
```

El proyecto ya está enlazado (`.vercel/`) y el dominio verificado con un CNAME en GoDaddy.
`.vercelignore` excluye `.env*` y `.vercel`: `vercel link` crea un `.env.local` con un token que no debe publicarse.
