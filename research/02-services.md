# Servicios, tecnologías y conceptos del CLF-C02

Listas oficiales de la guía del examen, completas y en el orden de AWS. Cuando el nombre en español difiere del original, el inglés va entre paréntesis.

- Dentro del alcance: https://docs.aws.amazon.com/es_es/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html
- Fuera del alcance: https://docs.aws.amazon.com/es_es/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html
- Tecnologías y conceptos: https://docs.aws.amazon.com/es_es/aws-certification/latest/cloud-practitioner-02/clf-technologies-concepts.html
- Originales en inglés: las mismas rutas sin `es_es/`.
- Fecha de consulta: **24-sep-2026**. Los conteos coinciden entre español e inglés en cada categoría.

AWS aclara en las tres listas que **no son exhaustivas y están sujetas a cambios**. La de tecnologías agrega que el orden no indica peso ni importancia.

## Dentro del alcance: 111 servicios y características en 19 categorías

| Categoría | Servicios | # |
|---|---|---:|
| Análisis (*Analytics*) | Amazon Athena · Amazon EMR · AWS Glue · Amazon Kinesis · Amazon OpenSearch Service · Amazon Quick Sight · Amazon Redshift | 7 |
| Integración de aplicaciones (*Application Integration*) | Amazon EventBridge · Amazon Simple Notification Service (Amazon SNS) · Amazon Simple Queue Service (Amazon SQS) · AWS Step Functions | 4 |
| Aplicaciones empresariales (*Business Applications*) | Amazon Connect · Amazon Simple Email Service (Amazon SES) | 2 |
| Administración financiera en la nube (*Cloud Financial Management*) | AWS Budgets · Informes de costo y uso de AWS (*AWS Cost and Usage Reports*) · Explorador de costos de AWS (*AWS Cost Explorer*) · AWS Marketplace | 4 |
| Computación (*Compute*) | AWS Batch · Amazon EC2 · AWS Elastic Beanstalk · Amazon Lightsail · AWS Outposts | 5 |
| Contenedores (*Containers*) | Amazon Elastic Container Registry (Amazon ECR) · Amazon Elastic Container Service (Amazon ECS) · Amazon Elastic Kubernetes Service (Amazon EKS) | 3 |
| Habilitación del cliente (*Customer Enablement*) | AWS Support | 1 |
| Base de datos (*Database*) | Amazon Aurora · Amazon DocumentDB · Amazon DynamoDB · Amazon ElastiCache · Amazon Neptune · Amazon RDS | 6 |
| Herramientas para desarrolladores (*Developer Tools*) | AWS CLI · AWS CodeBuild · AWS CodePipeline · AWS X-Ray | 4 |
| Computación para usuarios finales (*End User Computing*) | Amazon AppStream 2.0 · Amazon WorkSpaces · Navegador seguro Amazon WorkSpaces (*Amazon WorkSpaces Secure Browser*) | 3 |
| Frontend web y móvil (*Frontend Web and Mobile*) | AWS Amplify | 1 |
| Internet de las cosas (IoT) (*Internet of Things (IoT)*) | AWS IoT Core | 1 |
| Machine learning (*Machine Learning*) | Amazon Comprehend · Amazon Lex (*Amazon Lex*) · Amazon Polly · Amazon Q · Amazon Rekognition · Amazon SageMaker AI · Amazon Textract · Amazon Transcribe (*Amazon Transcribe*) · Amazon Translate | 9 |
| Administración y gobernanza (*Management and Governance*) | AWS Auto Scaling · AWS CloudFormation · AWS CloudTrail · Amazon CloudWatch · AWS Compute Optimizer · AWS Config · AWS Control Tower · Panel de AWS Health (*AWS Health Dashboard*) · AWS License Manager · Consola de administración de AWS (*AWS Management Console*) · AWS Organizations · AWS Service Catalog · Service Quotas · AWS Systems Manager · AWS Trusted Advisor · Herramienta de AWS Well-Architected (*AWS Well-Architected Tool*) | 16 |
| Migración y transferencia (*Migration and Transfer*) | AWS Application Discovery Service · AWS Application Migration Service · AWS Database Migration Service (AWS DMS) · Migration Evaluator · AWS Migration Hub · Herramienta de conversión de esquemas de AWS (AWS SCT) (*AWS Schema Conversion Tool (AWS SCT)*) | 6 |
| Redes y entrega de contenido (*Networking and Content Delivery*) | Amazon API Gateway · Amazon CloudFront · AWS Direct Connect · AWS Global Accelerator · AWS PrivateLink · Amazon Route 53 · AWS Transit Gateway · Amazon VPC · AWS VPN · AWS Site-to-Site VPN · AWS Client VPN | 11 |
| Seguridad, identidad y cumplimiento (*Security, Identity, and Compliance*) | AWS Artifact · AWS Certificate Manager (ACM) · AWS CloudHSM · Amazon Cognito · Amazon Detective · AWS Directory Service · AWS Firewall Manager · Amazon GuardDuty · AWS Identity and Access Management (IAM) · AWS IAM Identity Center · Amazon Inspector · AWS Key Management Service (AWS KMS) · Amazon Macie · AWS Resource Access Manager (AWS RAM) · AWS Secrets Manager · AWS Security Hub · AWS Shield · AWS WAF | 18 |
| Sin servidor (*Serverless*) | AWS Fargate · AWS Lambda | 2 |
| Almacenamiento (*Storage*) | AWS Backup · Amazon Elastic Block Store (Amazon EBS) · Amazon Elastic File System (Amazon EFS) · AWS Elastic Disaster Recovery · Amazon FSx · Amazon S3 · Amazon S3 Glacier · AWS Storage Gateway | 8 |

## Fuera del alcance: 56 servicios y características en 19 categorías

| Categoría | Servicios | # |
|---|---|---:|
| Análisis (*Analytics*) | Amazon AppFlow · AWS Clean Rooms · AWS Data Exchange · Amazon DataZone · Amazon Managed Streaming para Apache Kafka (Amazon MSK) (*Amazon Managed Streaming for Apache Kafka (Amazon MSK)*) | 5 |
| Integración de aplicaciones (*Application Integration*) | AWS AppFabric · Amazon Simple Workflow Service | 2 |
| Aplicaciones empresariales (*Business Applications*) | Amazon WorkDocs | 1 |
| Computación (*Compute*) | AWS Copilot · AWS Wavelength | 2 |
| Administración de costos (*Cost Management*) | AWS Application Cost Profiler · Amazon DevPay | 2 |
| Habilitación del cliente (*Customer Enablement*) | AWS Activate · AWS IQ · AWS Managed Services (AMS) | 3 |
| Administración financiera en la nube (*Cloud Financial Management*) | AWS Billing Conductor | 1 |
| Base de datos (*Database*) | Amazon Keyspaces (para Apache Cassandra) (*Amazon Keyspaces (for Apache Cassandra)*) · Amazon MemoryDB para Redis (*Amazon MemoryDB for Redis OSS*) · AWS AppConfig | 3 |
| Herramientas para desarrolladores (*Developer Tools*) | AWS Application Composer · AWS CodeArtifact · AWS CodeDeploy · Amazon CodeGuru · AWS CloudShell · AWS Device Farm | 6 |
| Tecnología de juegos (*Game Tech*) | Amazon GameLift · Amazon Lumberyard | 2 |
| Internet de las cosas (IoT) (*Internet of Things (IoT)*) | AWS IoT Device Defender · AWS IoT Greengrass · Amazon Monitron | 3 |
| Machine learning (*Machine Learning*) | Amazon Fraud Detector · Amazon Lookout for Metrics · AWS Panorama · Amazon Personalize | 4 |
| Administración y gobernanza (*Management and Governance*) | AWS Chatbot · Amazon Data Lifecycle Manager · Amazon Elastic Transcoder · AWS Launch Wizard | 4 |
| Servicios multimedia (*Media Services*) | Software y dispositivos de AWS Elemental (*AWS Elemental Appliances and Software*) · AWS Elemental MediaConnect · AWS Elemental MediaConvert · AWS Elemental MediaLive · AWS Elemental MediaPackage · AWS Elemental MediaStore · AWS Elemental MediaTailor · Amazon Interactive Video Service (Amazon IVS) | 8 |
| Migración y transferencia (*Migration and Transfer*) | AWS Migration Hub Refactor Spaces · AWS Transfer Family | 2 |
| Redes y entrega de contenido (*Networking and Content Delivery*) | AWS Cloud Map · Analizador de acceso a la red de AWS (*AWS Network Access Analyzer*) · AWS Ground Station · Amazon VPC Lattice | 4 |
| Seguridad, identidad y cumplimiento (*Security, Identity, and Compliance*) | Amazon Cloud Directory · AWS Network Firewall | 2 |
| Robótica (*Robotics*) | AWS RoboMaker | 1 |
| Almacenamiento (*Storage*) | Amazon FSx para Lustre (*Amazon FSx for Lustre*) | 1 |

## Tecnologías y conceptos: 29 elementos

> La siguiente lista contiene las tecnologías y los conceptos que pueden aparecer en el examen. Esta lista no es exhaustiva y está sujeta a cambios. El orden y la ubicación de los elementos de esta lista no indican su ponderación ni importancia relativos en el examen.

1. API (*APIs*)
2. Beneficios de migrar a la nube de AWS (*Benefits of migrating to the AWS Cloud*)
3. AWS Cloud Adoption Framework (AWS CAF)
4. Conformidad de AWS (*AWS Compliance*)
5. Computación (*Compute*)
6. Administración de costos (*Cost management*)
7. Bases de datos (*Databases*)
8. Tipos de instancias de Amazon EC2 (por ejemplo, instancias reservadas, instancias bajo demanda, instancias de spot) (*Amazon EC2 instance types (for example, Reserved Instances, On-Demand Instances, Spot Instances)*)
9. Infraestructura global de AWS (por ejemplo, regiones de AWS, zonas de disponibilidad) (*AWS global infrastructure (for example, AWS Regions, Availability Zones)*)
10. Infraestructura como código (IaC) (*Infrastructure as code (IaC)*)
11. AWS Knowledge Center
12. Machine learning (*Machine learning*)
13. Administración y gobernanza (*Management and governance*)
14. Migración y transferencia de datos (*Migration and data transfer*)
15. Servicios de red (*Network services*)
16. Red de socios de AWS (APN) (*AWS Partner Network (APN)*)
17. Recomendaciones de AWS (*AWS Prescriptive Guidance*)
18. Calculadora de precios de AWS (*AWS Pricing Calculator*)
19. AWS Professional Services
20. AWS re:Post
21. AWS SDK (*AWS SDKs*)
22. Seguridad (*Security*)
23. Blog de seguridad de AWS (*AWS Security Blog*)
24. Modelo de responsabilidad compartida de AWS (*AWS shared responsibility model*)
25. Arquitectos de soluciones de AWS (*AWS solutions architects*)
26. Almacenamiento (*Storage*)
27. Centro de soporte de AWS (*AWS Support Center*)
28. Planes de AWS Support (*AWS Support plans*)
29. Marco de AWS Well-Architected (*AWS Well-Architected Framework*)

## Notas verificadas: lo que cambió después de la guía

La guía no dice fecha de revisión. Su contenido ya usa nombres de 2025 (Amazon SageMaker AI, Amazon Quick Sight, navegador seguro Amazon WorkSpaces), pero varios servicios de la lista cambiaron de nombre o dejaron de aceptar clientes nuevos. El examen sigue la guía; el sitio tendría que enseñar el nombre de la guía y aclarar el estado actual.

La política oficial para estos casos: un servicio nuevo necesita 3 meses de disponibilidad general antes de aparecer en un examen, AWS reemplaza las preguntas afectadas por un cambio, y si una pregunta parece afectada hay que elegir la mejor respuesta disponible. Fuente: https://aws.amazon.com/certification/faqs/ (consultado 24-sep-2026).

| En la guía | Qué cambió | Fuente (consultada 24-sep-2026) |
|---|---|---|
| Planes de AWS Support: Developer, Business, Enterprise On-Ramp, Enterprise (D4.3.7) | Developer y Business se descontinúan el 1-ene-2027 y se reemplazan por Business Support+. Enterprise On-Ramp también termina el 1-ene-2027; sus clientes pasan a Enterprise Support durante 2026. Los planes que AWS compara hoy son Basic, Business Support+, Enterprise Support y Unified Operations. | https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html · https://aws.amazon.com/premiumsupport/plans/ |
| AWS Migration Hub | En mantenimiento: no acepta clientes nuevos desde el 7-nov-2025. AWS recomienda AWS Transform. | https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html |
| AWS Application Discovery Service | En mantenimiento (anunciado el 7-oct-2025; sin clientes nuevos desde el 7-nov-2025). | https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html · https://aws.amazon.com/about-aws/whats-new/2025/10/aws-service-availability/ |
| Amazon S3 Glacier | El servicio original de bóvedas (Amazon Glacier, «S3 Glacier Direct») pasó a mantenimiento. Las clases de almacenamiento S3 Glacier (Instant Retrieval, Flexible Retrieval, Deep Archive) siguen vigentes. | https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html · https://aws.amazon.com/about-aws/whats-new/2025/10/aws-service-availability/ |
| Amazon AppStream 2.0 | Se llama Amazon WorkSpaces Applications; la documentación conserva la ruta `appstream2`. | https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html |
| AWS Application Migration Service | La documentación lo presenta como AWS Transform MGN. | https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html |
| Amazon Connect | Se llama Amazon Connect Customer; «Amazon Connect» ahora nombra un conjunto de soluciones de IA. | https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html |
| AWS Security Hub | La documentación de ese servicio ahora se titula AWS Security Hub CSPM. | https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html |
| Amazon Q | Amazon Q Business está en mantenimiento (anuncio del 30-jun-2026) y los plugins de IDE de Amazon Q Developer están en sunset. | https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html · https://docs.aws.amazon.com/general/latest/gr/sunset_services.html |

Cambios que tocan una característica y no el servicio completo, y que el examen de nivel Foundational difícilmente pregunta: CloudTrail Lake, AWS WAF Classic, Amazon Cognito Sync, AWS Directory Service Simple AD, Systems Manager Incident Manager y Change Manager, Amazon S3 Object Lambda. Están en las mismas dos tablas de ciclo de vida.

## Mencionados en el temario pero ausentes de la lista de servicios

El temario los nombra como ejemplo, pero no aparecen en la lista de servicios dentro del alcance:

- Elastic Load Balancing (D3.3.6 habla de «equilibradores de carga»).
- Savings Plans, instancias dedicadas, hosts dedicados y reservas de capacidad (D4.1.1); son opciones de compra de EC2.
- Amazon EC2 Auto Scaling (D3.3.5); la lista incluye AWS Auto Scaling.
- Almacén de instancias (D3.6.4); es una característica de EC2.
- Informes de acceso de IAM (D2.2.8).
- API de AWS Health (D4.3.8); la lista incluye el Panel de AWS Health.
- Equipo de confianza y seguridad de AWS (D4.3.9).
- AWS Security Center (D2.4.5).
- AWS Knowledge Center, AWS re:Post, AWS Prescriptive Guidance, Calculadora de precios de AWS y el blog de seguridad de AWS aparecen en la lista de tecnologías y conceptos, no en la de servicios.

## Frecuentes en material de estudio viejo y ausentes de las dos listas

Revisado con búsqueda de texto sobre las listas oficiales en inglés el 24-sep-2026:

- AWS Snowball y la familia Snow: no están en ninguna lista. Además, Snowball Edge Compute Optimized y Storage Optimized están en mantenimiento desde octubre de 2025 (https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html).
- AWS DataSync, AWS Local Zones, Amazon Bedrock, AWS Audit Manager, IAM Access Analyzer y Amazon Security Lake: no están en ninguna lista.
- AWS CloudShell y AWS CodeDeploy: están explícitamente **fuera** del alcance.

Que no estén en la lista no garantiza que no aparezcan, porque la lista no es exhaustiva. Para el banco, conviene no escribir preguntas cuyo eje sea uno de estos servicios.
