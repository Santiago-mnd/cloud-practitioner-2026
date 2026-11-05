# Las 45 diferencias contra la guía oficial

Cada diferencia publicada en `cloud-practitioner.sintitulo.dev/diferencias`, con el punto de la guía del CLF-C02 que cubre (ids de `01-exam-outline.md`) y lo que dice que la guía no dice.

Revisado el 24-sep-2026, después de dos auditorías independientes contra fuentes oficiales. Ninguna de las dos marcó una afirmación sin respaldo en las diferencias.

## Cómo leer la columna «Más allá de la guía»

La guía dice **qué** se evalúa: temas, servicios y ejemplos. No explica cómo funciona cada servicio. Para escribir una diferencia hace falta ese detalle, y sale de la documentación oficial de AWS del servicio. Esa columna marca los datos que no aparecen en la guía y de dónde salen. Hay tres tipos:

- **Detalle:** cómo funciona algo que la guía sí nombra. Es necesario para distinguir un servicio de otro.
- **Contexto:** información vigente que la guía todavía no refleja, como nombres nuevos o planes que se descontinúan. Se presenta como aclaración y no cambia la respuesta de examen.
- **Término:** un nombre que la guía no usa, aunque sí evalúa el tema. Por ejemplo, las «7 R».

«—» significa que todo lo que dice la diferencia está en la guía, en sus listas de servicios o en la definición del servicio.

## D1 · Conceptos de la nube

| Diferencia | Puntos de la guía | Más allá de la guía |
|---|---|---|
| Agilidad o elasticidad | D1.1.3 | — |
| Escala o gasto variable | D1.4.3, D1.4.8 | — |
| Los seis pilares | D1.2.1–D1.2.3 | Detalle: la definición de cada pilar y la herramienta Well-Architected (en la lista de servicios). Fuente: Well-Architected Framework. |
| CAF: perspectivas y resultados | D1.3.3 | Término: la guía nombra los cuatro resultados, pero no las seis perspectivas. Fuente: whitepaper del AWS CAF. |
| Las siete R | D1.3.4 | Término: la guía pide «estrategias de migración adecuadas», sin nombrar las 7 R. Fuente: AWS Prescriptive Guidance. |
| BYOL o licencia incluida | D1.4.5, D4.1.1 | Detalle: el ejemplo de Oracle SE2 en RDS. Fuente: documentación de RDS for Oracle. |
| Rightsizing o Auto Scaling | D1.4.6, D3.3.5 | Detalle: Compute Optimizer da recomendaciones (el servicio sí está en la lista). |

## D2 · Seguridad y cumplimiento

| Diferencia | Puntos de la guía | Más allá de la guía |
|---|---|---|
| De la nube o en la nube | D2.1.2–D2.1.5 | — |
| Responsabilidad por servicio | D2.1.6 | Detalle: además de EC2, RDS y Lambda (los ejemplos de la guía), menciona S3 y DynamoDB. Fuente: página oficial del modelo de responsabilidad compartida. |
| Controles compartidos | D2.1.5 | Término: controles heredados, compartidos y específicos del cliente. Fuente: la misma página. |
| CloudWatch, CloudTrail, Config | D2.2.8 | — |
| Artifact o Config | D2.2.4, D2.2.8 | — |
| Cinco servicios de seguridad | D2.2.6, D2.4.3 | Detalle: qué fuentes analiza GuardDuty y qué revisa Inspector. Detective y Macie están en la lista de servicios, pero no en el temario. |
| Shield, WAF, Firewall Manager | D2.4.3 | — |
| Claves, certificados, secretos | D2.2.7, D2.3.5 | Detalle: KMS, CloudHSM y ACM están en la lista de servicios; qué hace cada uno sale de su documentación. |
| En tránsito o en reposo | D2.2.2, D2.2.7 | — |
| Usuario o rol | D2.3.1, D2.3.5–D2.3.7 | — |
| IAM, Identity Center, Cognito | D2.3.4, D2.3.6, D2.3.10 | Contexto: Identity Center antes se llamaba AWS Single Sign-On. |
| Política de IAM o SCP | D2.3.7, D4.2.3 | Término: la guía no nombra las SCP; son la función de permisos de AWS Organizations, que sí está. |
| El usuario raíz | D2.3.2, D2.3.8, D2.3.9 | — |

## D3 · Tecnología y servicios en la nube

| Diferencia | Puntos de la guía | Más allá de la guía |
|---|---|---|
| Modelos de implementación | D3.1.3, D3.1.6 | — |
| Consola o código | D3.1.4, D3.1.5 | — |
| Región, AZ y periferia | D3.2.1–D3.2.8 | — |
| Familias de instancia | D3.3.2 | Detalle: la guía pone de ejemplo optimizada para cómputo y para almacenamiento; la tabla agrega uso general, memoria y computación acelerada. |
| ECS, EKS, Fargate, Lambda | D3.3.3, D3.3.4 | Detalle: el límite de 15 minutos de Lambda. |
| Balanceador o Auto Scaling | D3.3.5, D3.3.6 | — |
| Qué base de datos | D3.4.3–D3.4.6 | — (DocumentDB, Neptune y Redshift están en la lista de servicios). |
| DMS o SCT | D3.4.7 | — |
| Grupo de seguridad o ACL | D3.5.3 | — |
| Conectar redes | D3.5.5 | — (Transit Gateway y Client VPN están en la lista). |
| CloudFront, Accelerator, Route 53 | D3.2.1, D3.2.4, D3.5.4 | — (CloudFront y Global Accelerator están en la lista). |
| Bloque, archivo u objeto | D3.6.2, D3.6.4–D3.6.6, D3.6.8 | Detalle: EFS usa NFS y FSx for Windows usa SMB. Elastic Disaster Recovery está en la lista. |
| Clases de S3 | D3.6.3, D3.6.7, D4.1.2 | Detalle: tiempos de recuperación y número de zonas de cada clase. |
| Servicios de análisis | D3.7.4 | — (EMR y Redshift están en la lista). |
| Servicios de IA | D3.7.3 | — (todos están en la lista de machine learning). |
| SNS, SQS, EventBridge | D3.8.1, D3.8.2, D3.8.8, D3.8.9 | Contexto: Amazon Connect hoy se llama Amazon Connect Customer. |
| Escritorios, IoT, código | D3.8.4–D3.8.7, D3.8.11–D3.8.14 | Contexto: AppStream 2.0 hoy se llama WorkSpaces Applications. |

## D4 · Facturación, precios y soporte

| Diferencia | Puntos de la guía | Más allá de la guía |
|---|---|---|
| Opciones de compra | D4.1.1, D4.1.3 | Detalle: las reservas de capacidad se cobran a precio bajo demanda si no se combinan con Savings Plans o RI. |
| Savings Plans o RI | D4.1.4, D4.1.5 | Detalle: Compute Savings Plans cubre Fargate y Lambda. |
| Entrada y salida de datos | D4.1.6 | Detalle: la transferencia entre zonas de disponibilidad se cobra en los dos sentidos. Fuente: documentación de facturación. |
| Herramientas de costos | D4.2.5, D4.2.6, D4.2.8 | Detalle: las acciones de AWS Budgets. |
| Etiquetas de costos | D4.2.4, D4.2.8 | — |
| Organizations o Control Tower | D4.2.3, D4.2.7 | — (Control Tower está en la lista). |
| Planes de soporte | D4.3.2, D4.3.7 | Detalle: TAM y tiempos de respuesta de cada plan, de la copia archivada de la página oficial (27-ago-2025). Contexto: AWS descontinúa Developer, Business y Enterprise On-Ramp el 1-ene-2027. |
| A quién acudir | D4.3.6, D4.3.8–D4.3.10, D4.3.12, D4.3.13 | — |

## Resultado

- **Las 45 diferencias caen dentro de temas que la guía evalúa.** Ninguna trata de un servicio fuera del alcance.
- **Lo que va más allá es detalle, contexto o un término.** Todo tiene fuente oficial de AWS; nada sale de sitios de terceros ni de la comunidad.
- **El contexto se marca como tal.** Los nombres nuevos y los planes que se descontinúan aparecen como aclaración y no cambian la respuesta que pide el examen.

## Regla para el banco de preguntas

Cada pregunta tiene que apuntar a un punto de la guía, con su id, y la respuesta correcta tiene que respaldarse en documentación oficial de AWS. Nada de preguntas sobre servicios fuera del alcance ni sobre el contexto nuevo (nombres de 2025–2026, planes de soporte vigentes) como respuesta correcta.
