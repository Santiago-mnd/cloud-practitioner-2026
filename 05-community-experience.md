# Experiencia de quienes presentaron el CLF-C02

> **Fuente de comunidad.** Nada de este archivo es información oficial de AWS. Son relatos personales, con muestras pequeñas y sesgo de quien escribe después de aprobar. Sirven para priorizar, no para afirmar cómo es el examen.

Consultado el **24-sep-2026**.

## Qué se pudo leer y qué no

- **Leídos completos:** cuatro relatos en primera persona en DEV Community, tres hilos de AWS re:Post y un artículo de DEV escrito por un sitio comercial de práctica.
- **No se pudieron leer:** Reddit (r/AWSCertifications) y Medium devolvieron 403 desde el VPS, tanto con `curl` como con la herramienta de lectura web. Los artículos de Medium que aparecieron en la búsqueda quedan listados al final, sin usar su contenido.
- **Sin resultados en español:** no apareció ningún relato en primera persona de alguien que presentara el examen en español. Las búsquedas en español solo devolvieron cursos y bancos de preguntas de pago.

La muestra es chica: cuatro personas que aprobaron y dos incidentes del día del examen.

## Fuentes

| Id | Tipo | Fecha | Quién | Enlace |
|---|---|---|---|---|
| C1 | Relato, aprobó | 12-abr-2026 | Persona de 18 años, inicio de carrera en DevOps, con algo de AWS en el trabajo | https://dev.to/ayaanahmad/how-i-passed-the-aws-cloud-practitioner-clf-c02-3dmn |
| C2 | Relato, aprobó | 5-ene-2026 | Con experiencia previa en EC2 y S3 | https://dev.to/adehorizon/how-i-passed-the-aws-certified-cloud-practitioner-in-24-days-for-free-4c49 |
| C3 | Relato, aprobó con 795 | 23-jul-2025 | Desarrolladora que volvía tras tres años fuera | https://dev.to/angelareichi/my-aws-cloud-journey-begins-passing-clf-c02-and-aif-c01-mpg |
| C4 | Relato, aprobó (sin puntaje) | 19-may-2025 | Perfil técnico con experiencia previa en AWS | https://dev.to/jeromes_dev/passing-the-aws-clf-c02-certification-aws-cloud-practitioner-blog-o63 |
| C5 | Hilo de re:Post: incidente en OnVUE | hace unos 3 meses según re:Post (cerca de junio de 2026) | Candidato del CLF-C02 | https://repost.aws/questions/QUIRMEcoGwSNyWJd2rUDAeTQ/aws-certified-cloud-practitioner-exam-ended-due-to-onvue-invalid-code-after-following-proctor-instructions |
| C6 | Hilo de re:Post: OnVUE rechazó la laptop | hace unos 7 meses según re:Post (cerca de febrero de 2026) | Candidato del CLF-C02 | https://repost.aws/questions/QUtHkjmVbURfuhkB1bHiqB_g/clf-c02-aws-certified-cloud-practitioner-exam-in-physical-location |
| C7 | Hilo de re:Post: tiempo de resultados | 2024 | Candidato del CLF-C02 | https://repost.aws/questions/QUFslVRlk_RkuDvdTgXM6Z-g/it-s-been-3-days-since-i-took-my-exam-i-haven-t-received-my-aws-clf-exam-results-yet |
| C8 | Artículo de un sitio comercial de práctica | 14 de junio, año no indicado | nerdexam; no dice haber presentado el examen | https://dev.to/nerdexam/aws-certified-cloud-practitioner-clf-c02-whats-actually-tested-395 |

## Lo que dicen

### Temas que costaron o sorprendieron

- **Más peso del AWS CAF del esperado.** C1: el examen real tuvo «a much greater emphasis on the Cloud Adoption Framework than the practice exams». Una sola fuente, pero coincide con que el CAF tiene su propia tarea (D1.3) y la mayoría de los bancos de práctica le dedican poco.
- **Servicios de nombre parecido.** C2: «The exam loves tricky scenarios» y distinguir servicios que suenan igual fue lo difícil. C8 nombra los ejemplos: Inspector contra Macie contra GuardDuty, y EBS contra EFS contra S3. Los pares están en `04-trap-pairs.md`, marcados en la columna «Com.».
- **Modelo de responsabilidad compartida.** C8 dice que aparece seguido y que atrapa a quien adivina. Solo esa fuente, que además es comercial.
- **Facturación y planes de soporte.** C8 advierte que la gente se salta el dominio 4 por pesar 12%. Otra vez, fuente comercial.
- C3: «Some were confusing, but overall, the exam felt manageable.» Terminó en 30 minutos.

### Dificultad

- C1: el examen real se sintió más fácil que los simulacros de Tutorials Dojo.
- C3: manejable.
- C8 lo califica 1.5 de 5 y afirma que más de 80% aprueba a la primera tras dos semanas de estudio. **No es verificable:** AWS no publica tasas de aprobación y C8 vende práctica.
- Tiempo de preparación reportado: dos semanas con perfil técnico (C4), 24 días (C2), unos dos meses (C3). C4 recomienda sacar 90% o más en práctica antes de agendar.

### El día del examen

- **Resultado inmediato o no.** C3 vio el resultado al terminar el CLF-C02 (julio de 2025); su examen de AI Practitioner tardó 10 horas. En C7 alguien esperaba desde hacía 3 días y escribe que «la mayoría» lo recibe en 24 horas. La FAQ oficial dice que la mayoría de los exámenes no muestran el resultado en pantalla y que llega en máximo 5 días hábiles. Las dos cosas pasan.
- **OnVUE rechazó una laptop personal por «máquina virtual».** C6: el software de Pearson VUE confundió la laptop de casa con una máquina virtual corporativa y no hubo forma de cambiarlo; la persona se pasó a un centro de examen y aprobó. En el centro no se lleva computadora. Es la misma falla que la guía del AZ-900 describe con Hyper-V.
- **Cerrar OnVUE por indicación del supervisor terminó el examen.** C5: la persona preguntó si podía revisar las aplicaciones en segundo plano; el supervisor le dijo que cerrara y volviera a abrir la aplicación; al volver, OnVUE dio «Invalid Code» y el intento quedó registrado como reprobado. Otra respuesta del hilo, de la comunidad, dice que en casos técnicos AWS ha quitado el reprobado y perdonado la espera de 14 días, y que conviene escribir a soporte de AWS Training and Certification con el número de caso de Pearson VUE sin esperar la investigación.
- C1 lo presentó en línea desde casa a las 7 de la mañana, con revisión del cuarto y verificación del supervisor.

### Recursos que usaron

Los cuatro relatos mezclan lo oficial gratuito (AWS Cloud Practitioner Essentials, Skill Builder, AWS Cloud Quest, whitepapers de Overview y Well-Architected) con material de terceros: cursos de Stephane Maarek, simulacros de Tutorials Dojo, ExamPro, el curso de freeCodeCamp y tarjetas de Quizlet. C4 describe Cloud Practitioner Essentials como un curso de 7 horas; hoy la página oficial marca 12 h 45 min, así que el curso cambió después de ese relato.

## Qué implica para el cuaderno

- Los pares de servicios parecidos tienen más respaldo que cualquier otro tema para ser el centro del sitio, igual que en el AZ-900.
- La guía del día del examen del AZ-900 aplica casi completa, porque el proveedor es el mismo (Pearson VUE con OnVUE) y los dos incidentes reportados son de ese software.
- Falta evidencia de cómo se vive el examen en español. Cualquier afirmación del sitio sobre la traducción tendría que salir de la documentación oficial, no de la comunidad.

## Encontrados y no leídos (Medium, 403)

- https://medium.com/@emiliano.regazzoni/how-i-managed-to-pass-aws-exam-cloud-practitioner-clf-c02-without-any-cloud-experience-d458a7ef04f8
- https://medium.com/@tanvisaxena1901/how-i-passed-aws-certified-cloud-practitioner-along-with-notes-41cae78f819b
- https://younusraza909.medium.com/how-i-cracked-aws-cloud-practioner-exam-clf-c02-134a1bdd9475
- https://medium.com/@LearnWithBindu/my-experience-with-the-aws-cloud-practitioner-certification-exam-4c4f4f0350ad
- https://medium.com/@VedantDomadiya/how-i-passed-the-aws-certified-cloud-practitioner-clf-c02-exam-in-just-2-weeks-bf40418488e7
