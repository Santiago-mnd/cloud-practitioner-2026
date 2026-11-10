# Cuaderno Cloud Practitioner

[![Cuaderno Cloud Practitioner](site/og.png)](https://cloud-practitioner.sintitulo.dev)

## English

**Cuaderno Cloud Practitioner** is a free study site for the **AWS Certified Cloud Practitioner (CLF-C02)** exam. Read it in [English](https://cloud-practitioner.sintitulo.dev/en) or [Spanish](https://cloud-practitioner.sintitulo.dev). You can use it without an account or email address; your progress stays in your browser through `localStorage`.

### What you’ll find

- **45 key differences** between services or concepts that are easy to confuse. Each entry explains the confusion, what actually happens, and the hint that decides the answer.
- **A four-step study method** built around analogies, one hint per topic, an error log, and a timed practice exam.
- **An online exam guide** covering Pearson VUE OnVUE’s system test, virtual machines, VPNs, identification, check-in, and results.
- **Practice questions in development.** The planned bank of 240 original questions, diagnostic quiz, spaced review, and timed mock exam are not available yet.

### The exam

The exam has 65 questions and lasts 90 minutes; 50 questions count toward the score. A passing score is 700 out of 1,000, and the exam costs USD 100. It is available in English and Latin American Spanish, among other languages.

| Domain | Weight |
| --- | ---: |
| Cloud Concepts | 24% |
| Security and Compliance | 30% |
| Cloud Technology and Services | 34% |
| Billing, Pricing, and Support | 12% |

The study questions are original, with none copied from the real exam or AWS’s official practice set. The content draws on AWS documentation verified on September 24, 2026, with a source and date for each fact. Author Santiago (**santiagos.mx**) has not yet taken the CLF-C02 exam.

### Development and contributions

Development details are in the Spanish section below. To regenerate the differences and then the English pages, run this from the repository root:

```bash
cd tools && pnpm install && pnpm run build
```

The differences live in `tools/data/differences.json`; the English pages are generated from the Spanish pages using `tools/localize.ts` and `tools/i18n/en.json`. Issues are welcome in either language, especially for factual errors cited against AWS documentation or English phrasing that sounds unnatural.

### Trademarks and license

This project is not affiliated with, sponsored by, or endorsed by Amazon Web Services. AWS, Amazon Web Services, and AWS Certified Cloud Practitioner are trademarks of Amazon.com, Inc. or its affiliates.

The code in `site/css/`, `site/js/`, and `tools/` is licensed under [MIT](LICENSE). The site text, the differences, and `research/` are licensed under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT). You may use and adapt that content if you credit Santiago García Arellano and link to this repository.

## Español

Guía estática y gratuita, en español de México y con [versión en inglés](https://cloud-practitioner.sintitulo.dev/en), para estudiar el examen **AWS Certified Cloud Practitioner (CLF-C02)**. No requiere cuenta ni correo; tampoco rastrea entre sitios, y cada persona conserva su avance en el navegador mediante `localStorage`.

**Sitio:** [cloud-practitioner.sintitulo.dev](https://cloud-practitioner.sintitulo.dev)

## Qué encontrarás

- **45 diferencias clave:** pares de servicios o conceptos que suelen confundirse; cada entrada explica dónde está la confusión, qué ocurre en realidad y qué frase decide la respuesta.
- **Método de estudio de cuatro pasos:** analogía antes que dato, una pista por tema, bitácora de errores y simulacro con reloj.
- **Guía para el examen en línea con OnVUE de Pearson VUE:** prueba del sistema, máquinas virtuales, VPN, identificación, check-in y resultados. AWS envía el resultado en un plazo de hasta cinco días hábiles; no aparece al terminar el examen.
- **Práctica, en construcción:** se planea un banco de 240 preguntas propias, distribuido según el peso de cada dominio; incluirá diagnóstico de 20 preguntas, repaso espaciado y simulacro de 65 preguntas en 90 minutos. Aún no está disponible.

## El examen

El examen tiene 65 preguntas y dura 90 minutos; 50 preguntas cuentan para el puntaje. Se aprueba con 700 de 1000 puntos, cuesta 100 USD y está disponible en español (América Latina).

| Dominio | Peso |
| --- | ---: |
| Conceptos de la nube | 24 % |
| Seguridad y cumplimiento | 30 % |
| Tecnología y servicios | 34 % |
| Facturación, precios y soporte | 12 % |

Las preguntas del cuaderno son propias; ninguna se copia del examen real ni del set oficial de práctica de AWS. El autor, Santiago (**santiagos.mx**), todavía no ha presentado el CLF-C02; el contenido se basa en documentación oficial de AWS, verificada el 24 de septiembre de 2026, con fuente y fecha para cada dato.

Este es el segundo cuaderno de la serie. El primero preparó al autor para el examen AZ-900 de Microsoft, que presentó y aprobó; después, algunas personas que lo usaron pidieron una versión para AWS.

## Repositorio

- `tools/`: scripts en TypeScript que generan y traducen el sitio: `build-differences.ts` arma `diferencias.html` con `data/differences.json` y `templates/differences.html`; `localize.ts` genera `site/en/`; `text-blocks.ts` extrae y revisa textos; `indexnow.ts` avisa a los buscadores.
- `site/`: sitio estático en HTML, CSS y JavaScript, sin paso de compilación; Vercel lo despliega desde esta carpeta.
- `research/`: investigación y fuentes. Incluye la logística del examen (`00-research.md`), el temario oficial con 135 puntos identificados (`01-exam-outline.md`), servicios dentro y fuera del alcance (`02-services.md`), recursos oficiales gratuitos (`03-official-resources.md`), 110 pares trampa candidatos junto con una tabla de equivalencias Azure ↔ AWS (`04-trap-pairs.md`), experiencias de la comunidad identificadas como tales (`05-community-experience.md`) y el plan (`06-plan.md`).

Para servir el sitio en local:

```bash
cd site && pnpm dlx serve .
```

Para regenerar las diferencias y después las páginas en inglés (desde la raíz del repositorio):

```bash
cd tools && pnpm install && pnpm run build
```

Las diferencias se editan en `tools/data/differences.json`, nunca en `site/diferencias.html`. Cada una tiene `domain` (1 a 4), `topic`, `id` (ancla estable), `title`, `hint`, `confusion`, `rule` y, opcional, `table` con pares de situación y respuesta.

Después de un despliegue con páginas nuevas, `cd tools && pnpm run indexnow` avisa a Bing y a otros buscadores con las URLs de `site/sitemap.xml`.

Las páginas de `site/en/` no se editan a mano: salen de las páginas en español y del diccionario `tools/i18n/en.json`. Si cambias un texto en español, agrega su traducción al diccionario; `localize.ts` avisa qué falta.

## Contribuir

Se agradecen los issues que señalen errores de hechos con una cita de la documentación de AWS, así como términos en español que suenen raros.

## Aviso de marcas

Este proyecto no está afiliado a Amazon Web Services ni cuenta con su patrocinio o aval. AWS, Amazon Web Services y AWS Certified Cloud Practitioner son marcas de Amazon.com, Inc. o sus filiales.

## Licencia

El código (`site/css/`, `site/js/` y `tools/`) usa la licencia MIT; ver [`LICENSE`](LICENSE). Los textos (las páginas del sitio, las diferencias y `research/`) usan Creative Commons Atribución 4.0 Internacional; ver [`LICENSE-CONTENT`](LICENSE-CONTENT). Puedes usarlos y adaptarlos si das crédito a Santiago García Arellano con un enlace a este repositorio.

Si te sirvió, puedes dejarle una estrella al repositorio.