# Cuaderno AZ-900

Sitio estático para estudiar el examen **Microsoft AZ-900** en español mexicano.
Gratis, sin cuentas y sin backend: el avance de cada visitante vive en su propio navegador.

Destino: **az900.sintitulo.dev** (Vercel, sin build step).

## Qué hay

| Archivo | Estado | Contenido |
|---|---|---|
| `index.html` | listo | Portada: diferencia destacada, cómo funciona la práctica, método y guía de OnVUE |
| `practica.html` | pendiente | Diagnóstico de 20, repaso espaciado, simulacro de 30 y práctica por tema |
| `diferencias.html` | listo | Las 33 diferencias clave, con dónde se confunden, la regla y la pista |
| `generar-diferencias.py` | listo | Contenido de las diferencias; regenera `diferencias.html` |
| `js/anim.js` | listo | Aparición de secciones al hacer scroll |
| `metodo.html` | pendiente | El método completo |
| `examen.html` | pendiente | Guía de OnVUE y logística |
| `css/site.css` | listo | Sistema de estilos completo, con View Transitions entre páginas |
| `js/preguntas.js` | pendiente | Banco de 118 preguntas y 31 conceptos |
| `js/app.js` | pendiente | Repaso espaciado y progreso en localStorage |

## Principios

- **Sin cuentas, sin correo, sin rastreo.** El progreso se guarda en `localStorage` del visitante.
- **Preguntas propias.** Ninguna se copia del examen real ni del Practice Assessment de Microsoft.
- **Fecha de verificación visible.** El temario cambia; el pie dice contra qué versión se verificó.

## Deploy

Sitio estático puro, sin dependencias ni build:

```bash
cd ~/personal/az900-sitio
vercel            # preview
vercel --prod     # producción
```

Al crear el proyecto, Vercel pregunta por el framework: **Other**, sin comando de build
y con el directorio raíz del repositorio como salida.

Después:

1. Agregar el dominio `az900.sintitulo.dev` en Settings → Domains y apuntar el CNAME en GoDaddy.
2. Activar **Web Analytics** en la pestaña Analytics del proyecto. El script ya está en las
   cinco páginas, apuntando a `/_vercel/insights/script.js`. Si el panel muestra una ruta
   distinta al activarlo, hay que reemplazar ese `src` en las cinco páginas.
3. Comprobar que llegan datos: al visitar el sitio debe aparecer una petición a
   `/_vercel/insights/view` en la pestaña de red del navegador.

`vercel.json` trae `cleanUrls` (las URL quedan sin `.html`), caché de una hora para
`css/` y `js/`, y tres cabeceras de seguridad. Los enlaces internos todavía apuntan a
`*.html`, así que Vercel los redirige; conviene limpiarlos en algún momento.

## Analítica y privacidad

Vercel Web Analytics **no usa cookies de terceros**: identifica con un hash derivado de la
petición que se descarta a las 24 horas, y guarda datos agregados (URL, referente, país,
sistema operativo, navegador y tipo de dispositivo). No permite reconstruir la sesión de
una persona ni cruzarla entre sitios.

Por eso el pie del sitio dice exactamente eso y no promete "sin rastreo" a secas. Si algún
día se cambia de herramienta, hay que revisar esa línea en las cinco páginas.

El avance de estudio de cada visitante vive solo en su `localStorage` y nunca viaja a
ningún servidor.

## Indexación

- **Google**: propiedad de dominio `sintitulo.dev` en Search Console (TXT en GoDaddy),
  que cubre todos los subdominios. Enviar `https://az900.sintitulo.dev/sitemap.xml`.
- **Bing** (y con él Edge, DuckDuckGo y Yahoo): Bing Webmaster Tools permite importar
  la propiedad desde Search Console.
- **Brave**: no tiene consola de webmaster ni acepta sitemaps. Solo envío manual de
  URLs sueltas en https://search.brave.com/submit-url; conviene mandar la portada,
  práctica y diferencias, no las cinco.
- **IndexNow**: `python3 indexnow.py` avisa a Bing, Yandex, Seznam y Naver de los
  cambios. La clave vive en el archivo `.txt` de la raíz; si se borra, el aviso se
  rechaza.

Cada página lleva canónica absoluta y Open Graph. `404.html` es la página de error
propia y está marcada con `noindex`.

## Origen

El material viene de `~/personal/az900-estudio/` (bitácoras de sesiones y de errores) y del
cuaderno interactivo que se usó para estudiar. Los bocetos de dirección visual están en
`~/personal/az900-estudio/diseno/`.
