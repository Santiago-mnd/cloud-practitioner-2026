# Plan para un cuaderno del CLF-C02

Este plan sale de los archivos `00` a `05` de esta carpeta y del sitio del AZ-900 (`~/personal/az900-sitio/`), revisado el 24-sep-2026. No se construyó nada. Las decisiones abiertas del final son de Santiago y aquí no se toman.

## 1. Tamaño del banco de preguntas

### Punto de partida

| | AZ-900 (sitio publicado) | CLF-C02 |
|---|---|---|
| Objetivos oficiales | 57 bullets | 135 puntos: 88 de habilidad y 47 de conocimiento |
| Dominios | 3 | 4 |
| Banco | 169 preguntas | por definir |
| Preguntas por objetivo | ≈ 3 | por definir |
| Diagnóstico | 20 preguntas | por definir |
| Simulacro | 30 preguntas en unos 35 minutos, cupos 8/12/10 | por definir |
| Examen real | — | 65 preguntas en 90 min; 50 con puntaje |

Los 47 puntos de conocimiento son casi siempre el paraguas de las habilidades de su misma tarea (ver `01-exam-outline.md`). Por eso la unidad de cobertura que conviene usar son las **88 habilidades**, más los pocos puntos de conocimiento que ninguna habilidad nombra, como D2.3.4 (IAM Identity Center).

### Propuesta: 240 preguntas, repartidas según los pesos

| Dominio | Peso | Preguntas | Habilidades | Preguntas por habilidad | Preguntas por punto (135) |
|---|---:|---:|---:|---:|---:|
| D1 · Conceptos de la nube | 24% | 58 | 12 | 4.8 | 3.2 |
| D2 · Seguridad y cumplimiento | 30% | 72 | 21 | 3.4 | 2.3 |
| D3 · Tecnología y servicios | 34% | 81 | 37 | 2.2 | 1.4 |
| D4 · Facturación, precios y soporte | 12% | 29 | 18 | 1.6 | 1.0 |
| **Total** | 100% | **240** | 88 | 2.7 | 1.8 |

Por qué 240:

1. **Escala con el AZ-900.** Allá fueron unas 3 preguntas por objetivo. Con 88 habilidades y un promedio de 2.7, el total queda en 240.
2. **Alcanza para simulacros completos sin repetir mucho.** Con simulacros de 65 preguntas, 240 da para unos 3.7 simulacros distintos. El AZ-900 tenía 169 para simulacros de 30 (5.6).
3. **Llena el hueco de lo gratuito.** Lo oficial gratis trae solo 20 preguntas; lo de suscripción, según AWS, más de 225 (ver `03-official-resources.md`). Un banco de 240 iguala ese volumen sin costo para quien estudia.

La tensión que deja el reparto proporcional: D1 tiene pocas habilidades y muchas preguntas, mientras D3 y D4 quedan delgados (1.6 preguntas por habilidad en D4). Dos formas de manejarlo:

- **Proporcional con piso** (la de la tabla): mínimo una pregunta por habilidad y por cada punto de conocimiento suelto. Cabe en los 240, porque D3 tiene 81 preguntas para 37 habilidades y D4 tiene 29 para 18. El sobrante de D1 va a lo que tiene más señal: CAF, pilares de Well-Architected y las 7 R.
- **Cobertura primero**: mínimo dos preguntas por habilidad y luego ajustar a los pesos. Eso lleva a unas 300 (72/90/102/36), un 25% más de trabajo.

### Diagnóstico, simulacro y diferencias

- **Diagnóstico:** 20 preguntas con cupos 5/6/7/2 (los pesos aplicados a 20), como en el AZ-900.
- **Simulacro:** 65 preguntas en 90 minutos con cupos 16/19/22/8, para practicar el ritmo real (unos 83 segundos por pregunta). El Official Practice Exam, que tiene ese formato, es de suscripción.
- **Diferencias publicadas:** de los 110 pares candidatos de `04-trap-pairs.md`, quedarse con 35 a 45, repartidos por peso y con prioridad a los que marca la comunidad. El AZ-900 publicó 34.

## 2. Qué se reusa del sitio del AZ-900 y qué cambia

| Pieza | Qué se reusa | Qué cambia |
|---|---|---|
| `css/site.css`, `js/anim.js`, `js/cabecera.js` | Todo | Nada, salvo que se quiera otra identidad visual (ver preguntas adicionales) |
| `js/practica.js` (motor) | Repaso espaciado (`INTERVALOS`, `PESO_CAJA`), diagnóstico, simulacro, práctica por tema y progreso en `localStorage` | Cuatro dominios en lugar de tres; `CUPO_SIMULACRO` de 30 a 65 preguntas; clave de `localStorage` propia (hoy es `az900:practica:avance`); mapa `DIFERENCIA_DE_TEMA` nuevo |
| `js/preguntas.js` | El esquema de cada pregunta (`id`, `tp`, `q`, `o`, `a`, `e`, `c`) y el tono de `cert-notebook/docs/method.md` | Todo el contenido; `DOMINIOS` y `TEMAS` nuevos |
| `generar-diferencias.py` | El generador y los campos (dominio, tema, título, pista, confusión, regla, tabla) | Cuatro dominios y todo el contenido |
| `metodo.html` | Los cuatro pasos y «si quedan pocos días». La referencia de 700 sobre 1000 aplica igual. | Los ejemplos. La analogía de la cocina para IaaS, PaaS y SaaS pierde peso: el temario del CLF-C02 no nombra IaaS, PaaS ni SaaS; el equivalente es cómo cambia la responsabilidad entre EC2, RDS y Lambda (D2.1.6). |
| `examen.html` (OnVUE) | Casi toda la lista: prueba del sistema, Hyper-V y detección de máquinas virtuales (C6 de la comunidad lo confirma), VPN, cuarto, pantalla única. El proveedor es el mismo. | Agenda desde aws.training/Certification y no desde Microsoft Learn. **El resultado casi nunca aparece al terminar**: llega en hasta 5 días hábiles (la página del AZ-900 dice lo contrario). Botón para ver en inglés. ESL +30 solo en inglés. Supervisión en español con horario limitado. Dos reagendas por cita. Sin descansos en línea. La ventana de check-in de AWS está sin verificar. |
| `index.html` | La estructura: diferencia destacada, práctica, método, día del examen | **El argumento de credibilidad.** El AZ-900 dice «se presentó y se aprobó el 17 de septiembre de 2026». Aquí no se puede decir nada parecido (ver riesgo 1). Conteos, ejemplos y la línea «El primero de una serie». |
| Pie y aviso legal | Estructura, analítica y privacidad | Marcas de AWS en lugar de Microsoft; fecha de verificación contra la guía de AWS |
| `vercel.json`, `robots.txt`, `sitemap.xml`, `indexnow.py`, `404.html` | La configuración | Dominio, rutas y clave de IndexNow, si se publica |
| `bullets.md` y `cobertura.md` del AZ-900 | El método de auditoría | `01-exam-outline.md` ya es el equivalente de `bullets.md`. La auditoría de cobertura se hace cuando exista el banco. |

## 3. Riesgos

1. **Santiago no ha presentado este examen.** Todo el contenido saldría de documentación, no de experiencia. El sitio del AZ-900 se apoya en «lo presenté y lo aprobé»; aquí esa frase no existe. Los ejemplos de errores reales («esta se falla dos veces») tampoco: en el AZ-900 salieron de su bitácora de errores.
2. **La guía va atrás de AWS.** Los planes de soporte de la guía se descontinúan el 1-ene-2027; Migration Hub, Application Discovery Service y las bóvedas de Glacier están en mantenimiento; AppStream 2.0 y Application Migration Service cambiaron de nombre (ver `02-services.md`). Si AWS actualiza la guía en 2027, parte del banco se tendría que rehacer. AWS promete avisar con al menos un mes.
3. **Terminología en español sin confirmar.** No se sabe si el examen en español de Latinoamérica dice «equilibradores» o «balanceadores de carga», ni cómo traduce otros términos. Quien presente en español puede ver el inglés, pero el sitio tiene que decidir qué término usar.
4. **Mucho más temario.** 111 servicios dentro del alcance y 135 puntos, contra 57 bullets del AZ-900. Más preguntas implican más probabilidad de un error de hecho. Cada lote necesita verificación contra la documentación, no solo revisión de redacción.
5. **Pares verificados solo de forma automática.** Los 110 pares tienen fuente viva y términos presentes, pero la frase de cada diferencia es propia y falta leerla contra la fuente completa (ver `04-trap-pairs.md`).
6. **Material ajeno.** No se puede copiar ni parafrasear de cerca el Official Practice Question Set ni los simulacros de terceros que usa la comunidad. Las marcas de AWS exigen un aviso de no afiliación, como el de Microsoft en el AZ-900.
7. **Comunidad delgada.** Cuatro relatos en primera persona y ningún relato del examen en español. Reddit y Medium no se pudieron leer desde el VPS.
8. **Atención de Santiago.** El examen de Meta es el viernes 9-oct-2026 (según `cert-notebook/README.md`), a 15 días de hoy.
9. **Texto público.** Si el sitio es público, cada página pasa por `stop-slop` y `copy-editing`, como exige la regla global. Eso ya está contado en la fase 4.

## 4. Esfuerzo estimado por fase

Unidad: sesiones del builder (un prompt con su entregable y su reporte) más horas de revisión de Santiago. La referencia es el AZ-900: el sitio se armó entre el 17 y el 18-sep (primer commit el 18-sep a las 00:12) y se pulió hasta el 21-sep con tres auditorías, pero el banco ya existía porque venía del cuaderno de estudio. Aquí el banco se escribe desde cero, y por eso la fase 2 es la grande. La estimación es gruesa.

| Fase | Qué incluye | Sesiones del builder | Revisión de Santiago |
|---|---|---:|---:|
| 0. Decisiones | Las tres del brief y las dos adicionales | — | 15 a 30 min |
| 1. Diferencias y temas | Elegir 35 a 45 pares, leer cada fuente completa, redactar pista, confusión y regla; definir `TEMAS` por dominio | 1 a 2 | 1 h |
| 2. Banco | 240 preguntas en 4 lotes por dominio; cada lote con verificación de hechos contra la documentación y auditoría de cobertura contra `01-exam-outline.md` | 4 a 6 | 3 a 4 h (muestreo) |
| 3. Sitio | Motor con 4 dominios, portada, método, día del examen, práctica y diferencias; pie y avisos | 1 a 2 | 1 h |
| 4. Verificación y texto | `stop-slop` y `copy-editing` en todo el texto; accesibilidad y responsive como en las auditorías del AZ-900; prueba del motor | 1 a 2 | 1 h |
| 5. Publicación | Solo si es público: Vercel, dominio, Search Console, Bing, IndexNow | 0.5 | 15 min |
| **Total** | | **8 a 13** | **6.5 a 8 h** |

Con la opción de cobertura primero (unas 300 preguntas), la fase 2 sube a 5 u 8 sesiones.

## 5. Decisiones abiertas para Santiago

No se toman aquí. Van con lo que implica cada opción.

### 5.1 ¿Público en sintitulo.dev o interno para quienes lo pidieron?

| | Público en sintitulo.dev | Interno |
|---|---|---|
| Texto | Pasa por `stop-slop` y `copy-editing` completos | Puede ir con menos pulido |
| Credibilidad | Necesita un argumento que no sea «lo aprobé» (riesgo 1) | Quienes lo pidieron ya conocen a Santiago |
| Trabajo extra | Aviso de marcas, indexación, fase 5 | Ninguno de esos |
| Iteración | Cambios visibles para todos | Se ajusta con el feedback de quienes lo pidieron |
| Serie | Sería el segundo recurso de sintitulo.dev | No suma a la serie |

### 5.2 ¿Se arma en paralelo al examen de Meta (9-oct-2026) o después?

- **En paralelo:** compite por la atención de Santiago en las dos semanas previas a su examen. Las fases 1 y 2 piden revisión suya (unas 4 a 5 horas).
- **Después:** empezaría hacia el 10-oct-2026. Antes de construir conviene volver a revisar la guía y los planes de soporte, porque los datos de esta investigación son del 24-sep-2026.

### 5.3 ¿Se construye aquí o en una sesión en la nube?

- **Aquí (VPS):** tiene a la mano el sitio del AZ-900 y `cert-notebook`. Un sitio estático no pesa para el VPS. Como contexto: hoy Santiago decidió que `cert-notebook` se construye en el VPS y que la nube se usa para trabajo pesado.
- **En la nube:** necesita un repositorio con el brief, esta investigación y el código base del AZ-900. El banco se puede repartir en lotes por dominio que corren en paralelo. Sin ese repositorio, la sesión en la nube no tiene el contexto del sitio del AZ-900.

### Preguntas adicionales que surgieron

No estaban en el brief. Cambian cómo se construye:

1. **Base de código:** ¿copia adaptada de `az900-sitio`, o un examen más dentro del motor genérico de `cert-notebook` (un archivo de datos por examen)? `cert-notebook` es privado y lo está construyendo otro pane.
2. **Identidad visual:** ¿la misma del AZ-900, como parte de una serie, o una propia?

## 6. Decisiones de Santiago (24-sep-2026)

- **Audiencia:** público en sintitulo.dev.
- **Base de código:** copia de `az900-sitio`, en `~/personal/clf-c02-site/` (tomada del último commit, sin la clave de IndexNow del AZ-900).
- **Identidad visual:** la misma del AZ-900.
- **Banco:** 240 preguntas, proporcional con piso (58/72/81/29).
- **Cuándo y dónde:** ya, en el VPS, en paralelo al examen de Meta. Se construye por fases y se para al final de cada una para revisión.
- **Subdominio:** `cloud-practitioner.sintitulo.dev` (elegido el 24-sep-2026). El DNS se conecta en la fase 5, cuando el sitio esté completo.
