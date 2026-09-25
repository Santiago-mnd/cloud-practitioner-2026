# Brief: investigar el AWS Certified Cloud Practitioner (CLF-C02)

**Quién lo ejecuta:** Claude en el pane `aws`.
**Para qué:** a quienes le pidieron esto a Santiago les gustó su guía del AZ-900 (az900.sintitulo.dev) y quieren una igual para AWS. Antes de construir nada, necesitamos una investigación verificada y un plan.
**Alcance:** solo investigar y planear. No escribas preguntas, páginas ni código.

## Contexto que debes leer (solo lectura)

- `~/personal/cert-notebook/docs/method.md`: el método de estudio que funcionó en el AZ-900.
- `~/personal/az900-sitio/`: el sitio público del AZ-900 (portada, diferencias, método, día del examen y práctica). Es el formato que les gustó.
- `~/personal/az900-estudio/auditoria-banco/bullets.md` y `cobertura.md`: cómo se mapeó el banco contra los objetivos oficiales. Es el mismo trabajo que hay que preparar aquí.

No modifiques nada fuera de `~/personal/clf-c02-estudio/`. En especial no toques `cert-notebook`, `az900-*` ni `meta900-*`: otro pane está trabajando en ellos.

## Reglas

1. **Fuentes oficiales primero:** docs.aws.amazon.com, aws.amazon.com/certification y skillbuilder.aws. Las de la comunidad solo sirven para la experiencia real de quien presentó el examen, y se marcan como tales.
2. **Cada dato lleva su fuente:** URL y fecha de consulta. Si algo no se puede confirmar, dilo; no lo rellenes.
3. **Guía oficial:** https://docs.aws.amazon.com/es_es/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html. Tiene versión en Markdown y PDF; úsalas para copiar el temario completo sin perder nada.
4. Documentos en español de México. Nombres de archivo en inglés.
5. No dejes procesos corriendo al terminar.

## Entregables en `~/personal/clf-c02-estudio/`

1. **`00-research.md`, la logística del examen, verificada:** número de preguntas (con y sin puntaje), tipos de pregunta, duración, calificación para aprobar, precio en USD, idiomas (¿hay español?), modalidades (centro de examen y en línea), política de reintento, vigencia y recertificación, y descuentos oficiales (por ejemplo, el vale de 50% al aprobar otra certificación de AWS, si existe).
2. **`01-exam-outline.md`, el temario oficial completo:** los 4 dominios con su peso, cada tarea y cada punto de conocimiento y habilidad tal como los publica AWS, con un id por punto (D1.1.1, D1.1.2…). Al final, el total de puntos por dominio. Es el equivalente del `bullets.md` del AZ-900.
3. **`02-services.md`:** la lista oficial de servicios que entran y los que no, agrupada por categoría, más la sección de tecnologías y conceptos.
4. **`03-official-resources.md`:** los recursos gratuitos oficiales (cursos de Skill Builder, el set oficial de preguntas de práctica, Exam Prep y whitepapers), con qué cubre cada uno y cuánto dura.
5. **`04-trap-pairs.md`, pares trampa candidatos:** los servicios o conceptos que se confunden entre sí, cada uno con la diferencia en una línea y la liga a la documentación oficial que la respalda. Aparte, una tabla de equivalencias Azure ↔ AWS para lo que ya se explicó en el AZ-900 (por ejemplo, availability zones, grupos de recursos contra cuentas y Organizations, Azure Policy contra SCP, Advisor contra Trusted Advisor), marcando cuáles son equivalentes de verdad y cuáles solo se parecen.
6. **`05-community-experience.md`:** qué dicen quienes ya lo presentaron (temas que más costaron, sorpresas, dificultad), marcado como fuente de comunidad y con enlaces.
7. **`06-plan.md`:**
   - Tamaño estimado del banco de preguntas por dominio, proporcional a los pesos, con el razonamiento.
   - Qué se reusa tal cual del sitio del AZ-900 y qué cambia.
   - Riesgos: por ejemplo, que Santiago no ha presentado este examen y el contenido saldría de documentación, no de su experiencia.
   - Una estimación de esfuerzo por fase.
   - **Decisiones abiertas para Santiago, sin tomarlas tú:**
     - ¿Público en sintitulo.dev o interno para quienes lo pidieron?
     - ¿Se arma en paralelo al examen de Meta de Santiago (9-oct-2026) o después?
     - ¿Se construye aquí o en una sesión en la nube?

## Al terminar

Deja un resumen de 10 líneas como máximo con lo que encontraste, lo que no pudiste confirmar y las decisiones abiertas. Detente y espera a Santiago.
