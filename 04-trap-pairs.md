# Pares trampa candidatos para el CLF-C02

Servicios y conceptos que se confunden entre sí, cada uno con la diferencia en una línea y la documentación oficial que la respalda. Es una lista de candidatos: el AZ-900 terminó con 34 diferencias publicadas, y aquí hay más material del que conviene publicar (ver `06-plan.md`).

## Cómo se verificó

- Cada enlace se descargó el **24-sep-2026** (versión Markdown cuando docs.aws.amazon.com la ofrece) y un script comprobó que la página responde y contiene los términos clave del par. Los 110 pasaron.
- La frase de la diferencia es redacción propia. La comprobación automática confirma que la página habla de esos términos, no cada matiz de la frase. Antes de convertir un par en entrada del sitio hay que leer la fuente completa, como se hizo en el AZ-900.
- Nombres: se usa el de la guía del examen. Si el servicio cambió de nombre, se indica (detalle en `02-services.md`).
- La columna **Com.** marca con «sí» los pares que fuentes de comunidad citan como confusos o frecuentes (ver `05-community-experience.md`). Es una señal, no una prueba.

## D1 · Conceptos de la nube (12 pares)

| Id | Par | Diferencia | Fuente oficial | Com. |
|---|---|---|---|---|
| T001 | Agilidad **vs** Elasticidad | Agilidad es lanzar recursos nuevos en minutos para experimentar; elasticidad es que la capacidad crezca y se encoja con la demanda. | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html |  |
| T002 | Costo fijo (CapEx) **vs** Costo variable (OpEx) | CapEx es invertir por adelantado en centros de datos y servidores; en la nube pagas solo por lo que consumes. | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html |  |
| T003 | Alta disponibilidad (varias AZ) **vs** Varias regiones | Varias AZ protegen contra la falla de un centro de datos; varias regiones se eligen por recuperación de desastres, latencia o soberanía de datos. | https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html |  |
| T004 | Pilar Fiabilidad **vs** Pilar Eficiencia del rendimiento | Fiabilidad es que la carga haga su función correctamente y se recupere de fallas; eficiencia del rendimiento es usar los recursos adecuados para cumplir requisitos conforme cambian. | https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html |  |
| T005 | Pilar Optimización de costos **vs** Pilar Sostenibilidad | Costos busca evitar gasto innecesario; sostenibilidad busca reducir el impacto ambiental de la carga. | https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html |  |
| T006 | Perspectivas del AWS CAF **vs** Resultados de negocio del AWS CAF | Las seis perspectivas (negocio, personas, gobernanza, plataforma, seguridad, operaciones) agrupan capacidades; los resultados son lo que se obtiene (menos riesgo, mejor ESG, más ingresos, más eficiencia). | https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html | sí |
| T007 | Rehost **vs** Replatform | Rehost mueve la aplicación sin cambios (lift and shift); replatform hace ajustes puntuales, como pasar la base de datos a un servicio administrado. | https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html |  |
| T008 | Replatform **vs** Refactor | Replatform optimiza sin cambiar la arquitectura central; refactor rediseña la aplicación con capacidades nativas de la nube. | https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html |  |
| T009 | Retain **vs** Retire | Retain deja la aplicación donde está por ahora; retire la apaga porque ya no aporta valor. | https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html |  |
| T010 | Repurchase **vs** Rehost | Repurchase cambia el producto por otro, típicamente un SaaS; rehost conserva la misma aplicación y la mueve. | https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html |  |
| T011 | BYOL **vs** Licencia incluida | Con BYOL usas licencias que ya tienes; con licencia incluida el precio por hora ya trae la licencia del software. | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.Licensing.html |  |
| T012 | Dimensionamiento correcto (rightsizing) **vs** Escalado automático | Rightsizing elige el tipo y tamaño de instancia que corresponde al uso real; Auto Scaling cambia el número de instancias según la demanda. | https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.html |  |

## D2 · Seguridad y cumplimiento (26 pares)

| Id | Par | Diferencia | Fuente oficial | Com. |
|---|---|---|---|---|
| T013 | Seguridad DE la nube **vs** Seguridad EN la nube | AWS protege la infraestructura (hardware, red, instalaciones); el cliente protege lo que pone encima (datos, identidades, configuración, sistema operativo invitado). | https://aws.amazon.com/compliance/shared-responsibility-model/ | sí |
| T014 | Responsabilidad en EC2 **vs** Responsabilidad en servicios abstractos (S3, DynamoDB) | En EC2 el cliente parcha el sistema operativo invitado; en los servicios abstractos AWS opera infraestructura, sistema operativo y plataforma. | https://aws.amazon.com/compliance/shared-responsibility-model/ | sí |
| T015 | Controles heredados **vs** Controles compartidos | Los heredados vienen completos de AWS (físicos y ambientales); en los compartidos cada parte cubre su capa (parches, configuración, capacitación). | https://aws.amazon.com/compliance/shared-responsibility-model/ | sí |
| T016 | Amazon CloudWatch **vs** AWS CloudTrail | CloudWatch mide cómo se comportan los recursos (métricas, logs, alarmas); CloudTrail registra quién hizo qué llamada a la API. | https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html |  |
| T017 | AWS CloudTrail **vs** AWS Config | CloudTrail responde quién hizo el cambio; Config guarda cómo estaba configurado cada recurso a lo largo del tiempo y lo evalúa contra reglas. | https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html |  |
| T018 | AWS Config **vs** AWS Artifact | Config evalúa el cumplimiento de TUS recursos; Artifact entrega los reportes de cumplimiento de AWS (SOC, PCI) y sus acuerdos. | https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html |  |
| T019 | Amazon Inspector **vs** Amazon GuardDuty | Inspector busca vulnerabilidades de software y exposición de red en EC2, imágenes de contenedores y Lambda; GuardDuty detecta amenazas analizando registros y actividad. | https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html | sí |
| T020 | Amazon GuardDuty **vs** Amazon Detective | GuardDuty detecta la actividad sospechosa; Detective ayuda a investigarla y encontrar la causa raíz. | https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html |  |
| T021 | Amazon GuardDuty **vs** Amazon Macie | GuardDuty detecta amenazas en la cuenta; Macie descubre datos sensibles (por ejemplo, datos personales) guardados en S3. | https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html | sí |
| T022 | AWS Security Hub **vs** Amazon GuardDuty | Security Hub concentra hallazgos de varios servicios y revisa la postura contra estándares; GuardDuty es una de las fuentes que genera hallazgos. | https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html |  |
| T023 | AWS Shield Standard **vs** AWS Shield Advanced | Standard protege contra DDoS comunes sin costo extra y de forma automática; Advanced es de pago y agrega protección ampliada y acceso al equipo de respuesta. | https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html |  |
| T024 | AWS Shield **vs** AWS WAF | Shield mitiga ataques DDoS; WAF filtra peticiones web con reglas (inyección SQL, XSS, IPs, tasa). | https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html |  |
| T025 | AWS WAF **vs** AWS Firewall Manager | WAF define las reglas; Firewall Manager las administra de forma central en todas las cuentas de la organización. | https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html |  |
| T026 | Grupo de seguridad **vs** ACL de red | El grupo de seguridad actúa a nivel de instancia, solo permite y es stateful; la ACL de red actúa a nivel de subred, permite y niega, y es stateless. | https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html |  |
| T027 | AWS KMS **vs** AWS CloudHSM | KMS es un servicio administrado de claves sobre HSM compartidos; CloudHSM te da HSM dedicados que controlas tú. | https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html |  |
| T028 | AWS KMS **vs** AWS Certificate Manager | KMS administra claves de cifrado; ACM emite y renueva certificados SSL/TLS. | https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html |  |
| T029 | AWS Secrets Manager **vs** Parameter Store de Systems Manager | Secrets Manager guarda secretos y los rota automáticamente; Parameter Store guarda parámetros de configuración y valores cifrados. | https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html |  |
| T030 | Usuario de IAM **vs** Rol de IAM | El usuario tiene credenciales de largo plazo; el rol se asume y entrega credenciales temporales. | https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html |  |
| T031 | AWS IAM **vs** AWS IAM Identity Center | IAM administra identidades y permisos dentro de una cuenta; Identity Center da inicio de sesión único a la fuerza laboral en varias cuentas y aplicaciones. | https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html |  |
| T032 | AWS IAM Identity Center **vs** Amazon Cognito | Identity Center es para empleados; Cognito es para los usuarios finales de tus aplicaciones web y móviles. | https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html |  |
| T033 | Política administrada por AWS **vs** Política administrada por el cliente | La administrada por AWS la crea y actualiza AWS; la del cliente la escribes tú para ajustarla al mínimo privilegio. | https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html |  |
| T034 | Política de IAM **vs** Política de control de servicios (SCP) | La política de IAM otorga permisos; la SCP solo fija el máximo permitido en las cuentas de la organización y nunca otorga nada. | https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html |  |
| T035 | Usuario raíz **vs** Usuario administrador de IAM | Algunas tareas solo las hace el usuario raíz (cerrar la cuenta, cambiar ciertas configuraciones de la cuenta); para lo diario se usa una identidad con permisos de administrador. | https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html |  |
| T036 | Claves de acceso **vs** Contraseña | Las claves de acceso son para acceso programático (CLI, SDK, API); la contraseña es para entrar a la consola. | https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html |  |
| T037 | Cifrado en tránsito **vs** Cifrado en reposo | En tránsito protege los datos mientras viajan por la red (TLS); en reposo protege los datos almacenados (por ejemplo, con claves de KMS). | https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html |  |
| T038 | AWS Trust & Safety **vs** AWS Support | Trust & Safety recibe reportes de abuso de recursos de AWS (spam, ataques, contenido ilegal); Support atiende problemas técnicos y de cuenta propios. | https://repost.aws/knowledge-center/report-aws-abuse |  |

## D3 · Tecnología y servicios en la nube (52 pares)

| Id | Par | Diferencia | Fuente oficial | Com. |
|---|---|---|---|---|
| T039 | Región **vs** Zona de disponibilidad | Una región es un área geográfica separada; una AZ es una o más instalaciones aisladas dentro de una región. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html |  |
| T040 | Zona de disponibilidad **vs** Ubicación periférica | Las AZ alojan tus cargas; las ubicaciones periféricas (edge) sirven contenido cerca del usuario con CloudFront y Route 53. | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html |  |
| T041 | Amazon CloudFront **vs** AWS Global Accelerator | CloudFront es una CDN que guarda contenido en caché en el borde y también acelera contenido dinámico; Global Accelerator da IP estáticas anycast y lleva el tráfico TCP o UDP por la red de AWS, útil para tráfico que no es HTTP. | https://aws.amazon.com/global-accelerator/faqs/ |  |
| T042 | Amazon Route 53 **vs** Amazon CloudFront | Route 53 es DNS (registro de dominios, enrutamiento y chequeos de salud); CloudFront entrega el contenido. | https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html |  |
| T043 | AWS Direct Connect **vs** AWS Site-to-Site VPN | Direct Connect es una conexión física privada y dedicada; Site-to-Site VPN es un túnel IPsec cifrado sobre internet. | https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html |  |
| T044 | AWS Site-to-Site VPN **vs** AWS Client VPN | Site-to-Site conecta una red completa (oficina o centro de datos) con la VPC; Client VPN conecta a personas desde su dispositivo. | https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html |  |
| T045 | AWS Transit Gateway **vs** Emparejamiento de VPC | Transit Gateway es un concentrador que une muchas VPC y redes locales; el emparejamiento une dos VPC y no es transitivo. | https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html |  |
| T046 | Puerta de enlace de internet **vs** Puerta de enlace NAT | La de internet permite tráfico de entrada y salida en subredes públicas; la NAT deja salir a las subredes privadas sin permitir conexiones entrantes. | https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html |  |
| T047 | AWS PrivateLink **vs** Emparejamiento de VPC | PrivateLink expone un servicio específico de forma privada, sin internet; el emparejamiento conecta redes completas. | https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html |  |
| T048 | Elastic Load Balancing **vs** Amazon EC2 Auto Scaling | El balanceador reparte el tráfico entre destinos sanos; Auto Scaling agrega o quita instancias. | https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html |  |
| T049 | Instancia optimizada para computación **vs** Instancia optimizada para almacenamiento | Las de computación son para cargas que exigen CPU; las de almacenamiento, para mucho acceso secuencial de lectura y escritura a datos locales. | https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html |  |
| T050 | Amazon ECS **vs** Amazon EKS | ECS es el orquestador de contenedores propio de AWS; EKS es Kubernetes administrado. | https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html |  |
| T051 | Amazon ECS o EKS **vs** AWS Fargate | ECS y EKS orquestan contenedores; Fargate es el motor sin servidor donde corren, sin administrar instancias. | https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html |  |
| T052 | AWS Lambda **vs** AWS Fargate | Lambda ejecuta funciones por evento con un máximo de 15 minutos; Fargate corre contenedores sin servidor, también de larga duración. | https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html |  |
| T053 | Amazon EC2 **vs** Amazon Lightsail | EC2 da control total y muchas opciones; Lightsail empaqueta servidor, almacenamiento y red a precio mensual predecible. | https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html |  |
| T054 | AWS Elastic Beanstalk **vs** AWS CloudFormation | Beanstalk despliega una aplicación a partir del código y administra la plataforma; CloudFormation crea cualquier infraestructura a partir de plantillas (IaC). | https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html |  |
| T055 | AWS Outposts **vs** AWS Storage Gateway | Outposts instala infraestructura de AWS en tu centro de datos para correr cargas localmente; Storage Gateway da acceso local en caché a almacenamiento en la nube. | https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html |  |
| T056 | Base de datos en EC2 **vs** Amazon RDS | En EC2 administras motor, parches y respaldos; en RDS AWS se encarga de esas tareas. | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html |  |
| T057 | Amazon RDS **vs** Amazon Aurora | RDS administra varios motores relacionales; Aurora es el motor de AWS compatible con MySQL y PostgreSQL. | https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html |  |
| T058 | Amazon RDS **vs** Amazon DynamoDB | RDS es relacional con SQL; DynamoDB es NoSQL de clave-valor, sin servidor. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html |  |
| T059 | Amazon DocumentDB **vs** Amazon Neptune | DocumentDB guarda documentos JSON y es compatible con MongoDB; Neptune es una base de datos de grafos. | https://docs.aws.amazon.com/neptune/latest/userguide/intro.html |  |
| T060 | Amazon ElastiCache **vs** Amazon RDS | ElastiCache es caché en memoria para latencia muy baja; RDS es la base relacional persistente. | https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html |  |
| T061 | Amazon RDS **vs** Amazon Redshift | RDS atiende transacciones (OLTP); Redshift es un almacén de datos para análisis (OLAP). | https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html |  |
| T062 | AWS DMS **vs** AWS SCT | DMS mueve los datos; SCT convierte el esquema cuando el motor de origen y el de destino son distintos. | https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html |  |
| T063 | AWS Application Migration Service (hoy AWS Transform MGN) **vs** AWS DMS | Application Migration Service migra servidores completos (físicos, virtuales o de otra nube) replicándolos a AWS; DMS migra bases de datos. | https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html |  |
| T064 | Amazon EBS **vs** Almacén de instancias | EBS es almacenamiento en bloques persistente; el almacén de instancias es temporal y se pierde al detener o terminar la instancia. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html |  |
| T065 | Amazon EBS **vs** Amazon EFS | EBS es un disco en bloques para una instancia dentro de una AZ; EFS es un sistema de archivos NFS compartido por muchas instancias. | https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html | sí |
| T066 | Amazon EFS **vs** Amazon FSx | EFS es NFS nativo para Linux; FSx ofrece sistemas de archivos de terceros administrados (Windows File Server, Lustre, NetApp ONTAP, OpenZFS). | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html |  |
| T067 | Amazon S3 **vs** Amazon EBS | S3 es almacenamiento de objetos accesible por API; EBS es almacenamiento en bloques conectado a una instancia. | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html | sí |
| T068 | S3 Standard-IA **vs** S3 One Zone-IA | Standard-IA guarda en varias AZ; One Zone-IA guarda en una sola AZ, cuesta menos y se pierde si esa AZ se destruye. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html |  |
| T069 | S3 Glacier Instant Retrieval **vs** S3 Glacier Flexible Retrieval y Deep Archive | Instant Retrieval devuelve en milisegundos; Flexible tarda de minutos a horas y Deep Archive, horas. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html |  |
| T070 | S3 Intelligent-Tiering **vs** Política de ciclo de vida | Intelligent-Tiering mueve objetos solo según su patrón de acceso; el ciclo de vida aplica reglas fijas que tú defines (por ejemplo, por antigüedad). | https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html |  |
| T071 | AWS Backup **vs** AWS Elastic Disaster Recovery | Backup centraliza y automatiza respaldos con políticas; Elastic Disaster Recovery replica servidores continuamente para recuperarlos en minutos. | https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html |  |
| T072 | Amazon Athena **vs** Amazon Redshift | Athena consulta con SQL los datos que ya están en S3, sin servidor; Redshift carga los datos en un almacén para análisis recurrente. | https://docs.aws.amazon.com/athena/latest/ug/what-is.html |  |
| T073 | AWS Glue **vs** Amazon EMR | Glue es integración de datos y ETL sin servidor, con catálogo; EMR corre clústeres administrados de big data (Spark, Hadoop). | https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html |  |
| T074 | Amazon Kinesis **vs** Amazon SQS | Kinesis recibe y procesa flujos de datos en tiempo real; SQS es una cola de mensajes para desacoplar componentes. | https://docs.aws.amazon.com/streams/latest/dev/introduction.html |  |
| T075 | Amazon Quick Sight **vs** Amazon Athena | Quick Sight arma tableros e inteligencia de negocios; Athena ejecuta las consultas SQL. | https://docs.aws.amazon.com/quicksight/latest/user/welcome.html |  |
| T076 | Amazon SageMaker AI **vs** Servicios de IA preentrenados (Rekognition, Comprehend, etc.) | SageMaker AI sirve para crear, entrenar y desplegar tus propios modelos; los servicios de IA se consumen por API sin entrenar nada. | https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html |  |
| T077 | Amazon Lex **vs** Amazon Polly | Lex crea interfaces conversacionales (chatbots); Polly convierte texto en voz. | https://docs.aws.amazon.com/polly/latest/dg/what-is.html |  |
| T078 | Amazon Transcribe **vs** Amazon Translate | Transcribe convierte voz en texto; Translate traduce texto entre idiomas. | https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html |  |
| T079 | Amazon Comprehend **vs** Amazon Textract | Comprehend analiza el significado de un texto (entidades, sentimiento); Textract extrae texto y datos de documentos escaneados. | https://docs.aws.amazon.com/textract/latest/dg/what-is.html |  |
| T080 | Amazon Rekognition **vs** Amazon Textract | Rekognition analiza imágenes y video (rostros, objetos); Textract lee documentos. | https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html |  |
| T081 | Amazon SNS **vs** Amazon SQS | SNS empuja un mensaje a muchos suscriptores (pub/sub); en SQS los consumidores sacan los mensajes de una cola. | https://docs.aws.amazon.com/sns/latest/dg/welcome.html |  |
| T082 | Amazon SNS **vs** Amazon SES | SNS manda notificaciones (SMS, correo, push) y hace fan-out; SES es un servicio de correo para enviar y recibir email a escala. | https://docs.aws.amazon.com/ses/latest/dg/Welcome.html |  |
| T083 | Amazon EventBridge **vs** Amazon SNS | EventBridge enruta eventos de servicios de AWS, SaaS y apps con reglas; SNS distribuye mensajes de un tema a sus suscriptores. | https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html |  |
| T084 | AWS Step Functions **vs** Amazon SQS | Step Functions orquesta un flujo de pasos con estado; SQS solo guarda mensajes en una cola. | https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html |  |
| T085 | Amazon Connect **vs** Amazon SES | Connect es un centro de contacto en la nube; SES es correo electrónico. | https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html |  |
| T086 | Amazon WorkSpaces **vs** Amazon AppStream 2.0 | WorkSpaces entrega escritorios virtuales completos; AppStream 2.0 transmite aplicaciones sueltas al navegador. | https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html |  |
| T087 | AWS Amplify **vs** AWS Elastic Beanstalk | Amplify crea y hospeda frontends web y móviles full-stack; Beanstalk despliega aplicaciones y servicios de backend. | https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html |  |
| T088 | AWS CodePipeline **vs** AWS CodeBuild | CodePipeline orquesta la entrega continua de principio a fin; CodeBuild compila y ejecuta pruebas. | https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html |  |
| T089 | AWS X-Ray **vs** Amazon CloudWatch | X-Ray sigue una petición a través de los servicios de una aplicación (trazas); CloudWatch mide y alerta sobre métricas y logs. | https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html |  |
| T090 | Consola de administración **vs** Acceso programático (CLI, SDK, API) e IaC | La consola sirve para operaciones únicas a mano; CLI, SDK e IaC sirven para procesos repetibles y automatizados. | https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html |  |

## D4 · Facturación, precios y soporte (20 pares)

| Id | Par | Diferencia | Fuente oficial | Com. |
|---|---|---|---|---|
| T091 | Instancias bajo demanda **vs** Instancias de spot | Bajo demanda se paga por segundo sin compromiso y no se interrumpe; spot usa capacidad sobrante con gran descuento, pero AWS puede recuperarla. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html |  |
| T092 | Instancias reservadas **vs** Savings Plans | Las RI comprometen una configuración de instancia; Savings Plans compromete un gasto por hora y se aplica con más flexibilidad (Compute Savings Plans cubre también Fargate y Lambda). | https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html |  |
| T093 | RI estándar **vs** RI convertible | La estándar da más descuento pero cambia poco; la convertible permite cambiar a otra familia o tipo a cambio de menos descuento. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html |  |
| T094 | Hosts dedicados **vs** Instancias dedicadas | El host dedicado te da el servidor físico completo con visibilidad de sockets y núcleos (útil para BYOL); la instancia dedicada aísla el hardware sin darte control del host. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html |  |
| T095 | Reserva de capacidad **vs** Instancia reservada | La reserva de capacidad asegura capacidad en una AZ, sin descuento por sí sola; la RI da descuento en la factura. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html |  |
| T096 | Descuento de RI en una cuenta **vs** Descuento de RI en Organizations | Con facturación unificada, el descuento de una RI puede aplicarse a instancias de otras cuentas de la misma organización. | https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html |  |
| T097 | Transferencia de datos de entrada **vs** Transferencia de datos de salida | La entrada desde internet no se cobra; la salida sí. Dentro de una región, pasar datos entre zonas de disponibilidad se cobra en los dos sentidos. | https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html |  |
| T098 | AWS Budgets **vs** AWS Cost Explorer | Budgets avisa cuando el gasto real o pronosticado pasa un umbral; Cost Explorer sirve para ver y analizar el gasto. | https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html |  |
| T099 | AWS Cost Explorer **vs** Informe de costo y uso (CUR) | Cost Explorer es visual e interactivo; el CUR es el detalle más granular, exportado a S3. | https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html |  |
| T100 | Calculadora de precios de AWS **vs** AWS Cost Explorer | La calculadora estima antes de construir; Cost Explorer analiza lo que ya gastaste. | https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html |  |
| T101 | Etiquetas de asignación generadas por AWS **vs** Etiquetas definidas por el usuario | AWS genera unas (por ejemplo, createdBy) y tú defines las otras; las dos se activan en la consola de facturación para aparecer en los reportes. | https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html |  |
| T102 | AWS Organizations **vs** AWS Control Tower | Organizations agrupa cuentas, unifica la facturación y aplica SCP; Control Tower arma encima una zona de aterrizaje con controles preconfigurados. | https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html |  |
| T103 | AWS Trusted Advisor **vs** AWS Compute Optimizer | Trusted Advisor revisa buenas prácticas en varias categorías (costo, seguridad, tolerancia a fallas, rendimiento, límites); Compute Optimizer recomienda tamaños de cómputo con base en el uso. | https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html |  |
| T104 | AWS Trusted Advisor **vs** Herramienta de AWS Well-Architected | Trusted Advisor revisa tu cuenta de forma automática; la herramienta Well-Architected es una revisión guiada de una carga contra los pilares. | https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html |  |
| T105 | AWS Health Dashboard **vs** AWS Trusted Advisor | Health informa eventos de AWS que afectan tus recursos (incidentes, mantenimientos); Trusted Advisor da recomendaciones. | https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html |  |
| T106 | Trusted Advisor en Basic **vs** Trusted Advisor completo | Con el soporte Basic solo hay revisiones centrales; el conjunto completo requiere un plan de pago. | https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html |  |
| T107 | Planes de soporte de la guía (Developer, Business, Enterprise On-Ramp, Enterprise) **vs** Planes vigentes (Business Support+, Enterprise, Unified Operations) | La guía del examen todavía menciona los planes anteriores; AWS descontinúa Developer, Business y Enterprise On-Ramp el 1-ene-2027. | https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html | sí |
| T108 | AWS Marketplace **vs** AWS Partner Network | Marketplace es el catálogo para comprar software de terceros; la APN es el programa de socios (ISV, integradores). | https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html |  |
| T109 | AWS Service Catalog **vs** AWS Marketplace | Service Catalog es el catálogo interno de productos aprobados por tu organización; Marketplace vende software de terceros. | https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html |  |
| T110 | AWS Knowledge Center **vs** AWS re:Post | Knowledge Center reúne artículos de AWS con respuestas a preguntas frecuentes; re:Post es la comunidad de preguntas y respuestas. | https://repost.aws/knowledge-center |  |
## Equivalencias Azure ↔ AWS para lo que ya se explicó en el AZ-900

Para quien viene del AZ-900, el riesgo es suponer que un servicio de AWS funciona igual que su «gemelo» de Azure. La columna «¿Equivale?» usa tres valores:

- **Sí**: mismo papel y la diferencia no cambia la respuesta de una pregunta de nivel Foundational.
- **Parecido**: mismo propósito general con una diferencia que sí puede cambiar la respuesta.
- **No hay**: no existe un equivalente directo.

Fuentes de Microsoft, todas bajo https://learn.microsoft.com/en-us/azure/architecture/aws-professional/ y consultadas el 24-sep-2026:

- M1: `accounts` (actualizada el 22-jun-2026)
- M2: `regions-zones` (14-ago-2026)
- M3: `resources` (7-ene-2025)
- M4: `services` (8-may-2026)
- M5: `security-identity` (29-jun-2026)
- M6: `compute`
- M7: `networking`
- M8: `storage`

Las fuentes de AWS son las mismas de la tabla de pares.

### Infraestructura global

| Azure (AZ-900) | AWS | ¿Equivale? | Diferencia que importa | Fuente |
|---|---|---|---|---|
| Región | Región | Sí | En AWS cada región está diseñada para estar aislada de las demás. | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html |
| Pares de regiones | — | No hay | Azure empareja algunas regiones y lo usa, por ejemplo, para GRS. AWS no documenta regiones emparejadas: describe cada región como aislada de las demás, así que la segunda región y su replicación las decides tú. | M2; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html |
| Zonas de disponibilidad | Zonas de disponibilidad | Parecido | En Azure no todas las regiones tienen zonas. En AWS toda región tiene varias AZ, y cada AZ es uno o más centros de datos. | M2; https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html |
| — | Ubicaciones periféricas (edge) | No hay en el AZ-900 | Concepto nuevo para quien viene del AZ-900; en AWS son parte explícita del temario (D3.2). | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html |

### Organización, gobernanza y costos

| Azure (AZ-900) | AWS | ¿Equivale? | Diferencia que importa | Fuente |
|---|---|---|---|---|
| Suscripción | Cuenta de AWS | Sí, con matices | Microsoft las llama equivalentes: límite de facturación, de recursos y de cuotas. En AWS las identidades (IAM) viven dentro de cada cuenta; en Azure viven en el tenant de Entra, por encima de las suscripciones. | M1 |
| Grupos de administración | Unidades organizativas (OU) de AWS Organizations | Sí, con matices | Microsoft las llama equivalentes. AWS tiene además una cuenta de administración dedicada; Azure centraliza en el tenant. | M1, M4 |
| Grupo de recursos | AWS Resource Groups y etiquetas; pilas de CloudFormation | Parecido | En Azure todo recurso pertenece a un solo grupo, y borrar el grupo borra sus recursos. En AWS el grupo es opcional y borrarlo no toca los recursos. | M3 |
| Jerarquía grupo de administración > suscripción > grupo de recursos > recurso | Raíz de la organización > OU > cuenta > recurso | Parecido | Falta el nivel obligatorio de grupo de recursos. | M1 |
| Azure Policy | SCP (políticas de control de servicios) | Solo se parecen | La SCP limita el máximo de permisos de los usuarios y roles de las cuentas miembro y nunca otorga nada; no aplica a la cuenta de administración. Azure Policy evalúa y corrige la configuración de los recursos. Microsoft mapea Azure Policy con **AWS Config**, no con SCP. | M1, M4 |
| Bloqueos de recursos (locks) | — | No hay | Ninguna fuente consultada lo mapea. Conclusión propia: en AWS el efecto se logra negando acciones con políticas o con protecciones de cada servicio. Verificar antes de publicarlo. | — |
| Etiquetas | Etiquetas y etiquetas de asignación de costos | Parecido | En AWS las etiquetas distinguen mayúsculas y minúsculas y no se heredan de forma nativa; para verlas en los reportes de costos hay que activarlas. | M3; https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html |
| Microsoft Cost Management | AWS Billing and Cost Management: Cost Explorer, Budgets, CUR | Sí | En AWS son herramientas separadas; el examen pregunta cuál usar para qué. | M4 |
| Calculadora de precios | Calculadora de precios de AWS | Sí | — | https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html |
| Azure Advisor | AWS Trusted Advisor | Sí | Mismas categorías de revisión. Ojo: Microsoft también mapea la parte de costos de Advisor con AWS Compute Optimizer. En AWS, la cantidad de revisiones de Trusted Advisor depende del plan de soporte. | M4, M6; https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html |
| Azure Service Health | Panel de AWS Health | Parecido | Microsoft mapea el panel de AWS Health con **Resource Health**. El panel de AWS muestra la disponibilidad de los servicios y los eventos que afectan a tus recursos y cuentas. | M4; https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html |
| Azure Monitor (Log Analytics, alertas, Application Insights) | Amazon CloudWatch y AWS X-Ray | Parecido | Microsoft: «In AWS, you typically use both X-Ray and CloudWatch». Application Insights se parece más a X-Ray. | M4 |
| Registro de actividad (activity log) | AWS CloudTrail | Parecido | Los dos registran quién hizo qué en el plano de administración. | M4 |
| Plantillas ARM y Bicep | AWS CloudFormation | Sí | — | M3, M4 |
| Azure portal, CLI y PowerShell | Consola de administración, AWS CLI y SDK | Sí | **AWS CloudShell está fuera del alcance del CLF-C02**, aunque Azure Cloud Shell sí estaba en el AZ-900. | M3; `02-services.md` |
| Azure Arc | AWS Systems Manager para recursos fuera de AWS | Parecido | Arc extiende políticas, monitoreo y RBAC de Azure a otros entornos; Microsoft lo compara con esa parte de Systems Manager. | M6 |
| Azure Well-Architected Review | Herramienta de AWS Well-Architected | Parecido | Microsoft enumera cinco pilares; AWS tiene seis, porque agrega **sostenibilidad**. | M4; https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html |

### Identidad y seguridad

| Azure (AZ-900) | AWS | ¿Equivale? | Diferencia que importa | Fuente |
|---|---|---|---|---|
| Microsoft Entra ID | AWS IAM Identity Center + AWS IAM | Parecido | Entra ID reúne en un servicio lo que AWS separa: Identity Center (inicio de sesión único de la fuerza laboral) e IAM (identidades y permisos dentro de cada cuenta). | M4, M5 |
| Azure RBAC | Políticas de IAM | Parecido | **Trampa de vocabulario:** un «rol» de Azure RBAC es un conjunto de permisos que se asigna; un rol de IAM es una identidad que se asume y entrega credenciales temporales. | M4; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html |
| Entra Domain Services | AWS Directory Service | Sí | — | M4, M5 |
| Identidades externas (Entra External ID) | Amazon Cognito | Parecido | Cognito es para los usuarios finales de tus apps. Microsoft también mapea parte de External ID con IAM Identity Center para colaboración entre organizaciones. | M4, M5 |
| MFA | MFA | Sí | En AWS la protección del usuario raíz con MFA es tema explícito del examen (D2.3). | M4 |
| Microsoft Defender for Cloud | Amazon Inspector | Parecido | Microsoft lo mapea con Inspector (evaluación automática de vulnerabilidades). La postura contra estándares la cubre Security Hub CSPM; eso es conclusión propia, no aparece en el mapeo. | M4 |
| Azure Key Vault | AWS KMS + AWS CloudHSM (+ ACM para certificados) | Parecido | Key Vault guarda claves, secretos y certificados. En AWS son servicios distintos: KMS usa HSM compartidos y CloudHSM es dedicado. | M4 |
| Azure DDoS Protection | AWS Shield | Sí | En AWS, Shield Standard viene incluido sin costo extra. | M4, M7 |
| Azure Web Application Firewall | AWS WAF | Sí | — | M4, M7 |
| Portal de confianza de servicios de Microsoft | AWS Artifact | Sí | — | M4 |
| Modelo de responsabilidad compartida | Modelo de responsabilidad compartida | Sí | AWS lo formula como seguridad «de» la nube (AWS) contra seguridad «en» la nube (cliente). | https://aws.amazon.com/compliance/shared-responsibility-model/ |

### Cómputo, redes y almacenamiento

| Azure (AZ-900) | AWS | ¿Equivale? | Diferencia que importa | Fuente |
|---|---|---|---|---|
| Nube pública, privada e híbrida | Modelos de implementación: nube, híbrido, en las instalaciones | Parecido | Cambian los nombres: AWS llama «cloud» al despliegue todo en la nube y «on-premises» a la nube privada. | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/types-of-cloud-computing.html; guía D3.1.6 |
| Máquinas virtuales | Amazon EC2 | Sí | Los tamaños de VM de Azure y los tipos de instancia de EC2 tienen categorías parecidas. | M6 |
| Conjuntos de escalado de VM | Amazon EC2 Auto Scaling / AWS Auto Scaling | Sí | — | M6 |
| Azure Virtual Desktop | Amazon WorkSpaces y Amazon AppStream 2.0 | Parecido | AWS separa escritorios completos (WorkSpaces) de aplicaciones sueltas (AppStream 2.0, hoy WorkSpaces Applications). | M4 |
| Azure Functions | AWS Lambda | Sí | — | M6 |
| Azure App Service | AWS Elastic Beanstalk | Sí | Microsoft también compara App Service con Lightsail y Amplify para ciertos casos. | M4, M6 |
| AKS / Container Instances | Amazon EKS / AWS Fargate | Sí / Parecido | Fargate es el motor sin servidor para tareas de ECS y pods de EKS; no es un servicio de contenedores suelto como ACI. | M6 |
| Red virtual, subredes, emparejamiento | Amazon VPC, subredes, emparejamiento de VPC | Sí | — | M7 |
| Grupos de seguridad de red (NSG) | Grupos de seguridad (y ACL de red) | Parecido | AWS tiene dos capas: grupo de seguridad (instancia, stateful) y ACL de red (subred, stateless). | M7; https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html |
| Azure DNS | Amazon Route 53 | Parecido | Route 53 también registra dominios y hace enrutamiento por salud; Microsoft lo mapea a Azure DNS **y** a Traffic Manager. | M7 |
| VPN Gateway | AWS Site-to-Site VPN | Sí | — | M7 |
| ExpressRoute | AWS Direct Connect | Sí | — | M7 |
| Punto de conexión privado | Puntos de conexión de VPC (AWS PrivateLink) | Sí | — | M7 |
| Blob Storage | Amazon S3 | Sí | — | M8 |
| Niveles hot, cool, cold y archive | Clases de almacenamiento de S3 | Parecido | S3 tiene más clases y cada objeto lleva la suya. Microsoft mapea S3 Standard-IA con cool, S3 Glacier con cold y Deep Archive con archive; el mapeo con cold solo aplica a Glacier Instant Retrieval, porque Flexible Retrieval tarda de minutos a horas. | M8; https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html |
| Redundancia LRS, ZRS, GRS | Clase de almacenamiento de S3 y replicación | No hay uno a uno | En S3 la redundancia viene con la clase: Standard e IA guardan en varias AZ; One Zone-IA, en una. Copiar a otra región es una replicación que se configura aparte. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html |
| Discos administrados | Amazon EBS | Sí | — | M6, M8 |
| Azure Files | Amazon EFS / Amazon FSx for Windows File Server | Parecido | EFS es NFS; para SMB con Active Directory el equivalente es FSx for Windows File Server. | M8 |
| Azure File Sync | AWS Storage Gateway (S3 File Gateway) | Parecido | Los dos dan acceso local en caché a archivos respaldados en la nube. | M8 |
| Azure Data Box | AWS Snowball Edge | Parecido, pero fuera del CLF | Snowball no aparece en las listas del CLF-C02 y sus modelos Edge están en mantenimiento. | M8; `02-services.md` |
| Azure Migrate | AWS Application Discovery Service | Parecido | Microsoft mapea Azure Migrate con Application Discovery Service. En el temario de AWS la migración se reparte además entre Migration Hub, Application Migration Service, DMS y SCT. Application Discovery Service y Migration Hub están en mantenimiento desde 2025. | M4; `02-services.md` |
