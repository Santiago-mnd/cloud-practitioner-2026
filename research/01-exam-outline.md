# Temario oficial del CLF-C02, punto por punto

Copiado de la guía oficial del examen **AWS Certified Cloud Practitioner (CLF-C02)** sin resumir ni reordenar. Cada punto va en español, como lo publica la versión es_es de la guía, y debajo en inglés, como lo publica la versión en_us.

- Fuente en español: https://docs.aws.amazon.com/es_es/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html (páginas `cloud-practitioner-02-domain1` a `-domain4`, versión Markdown)
- Fuente en inglés: https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html
- PDF usado para cotejar: `cloud-practitioner-02.pdf` en las dos rutas (español: 33 páginas, generado el 24-sep-2026; inglés: 32 páginas, generado el 23-sep-2026)
- Fecha de consulta: **24-sep-2026**

## Cómo leer los ids

- `D1.2.3` = dominio 1, enunciado de tarea 1.2, punto 3.
- Dentro de cada tarea, los puntos siguen el orden de la guía: primero los de **conocimiento** `[C]` («Conocimientos de» / *Knowledge of*) y luego los de **habilidad** `[H]` («Habilidades para» / *Skills in*).
- Los «por ejemplo» son parte del texto oficial: AWS los usa para ilustrar, no para cerrar la lista.

## Notas de la propia guía que acotan el alcance

> En esta guía, no se proporciona una lista completa del contenido del examen. Sin embargo, hay contexto adicional disponible de cada enunciado de tareas como ayuda en la preparación para el examen.

> *This exam guide includes weightings, content domains, and task statements for the exam. This guide does not provide a comprehensive list of the content on the exam. However, additional context for each task statement is available to help you prepare for the exam.*

Fuera del alcance del candidato, según la guía: codificación, diseño de la arquitectura de nube, solución de problemas, implementación, y pruebas de carga y de rendimiento.

## Verificación de la copia

- Las versiones en español y en inglés tienen el mismo número de puntos en cada tarea; se emparejaron por posición y se revisaron a ojo.
- Los 331 renglones de lista de las páginas Markdown (temario, tecnologías y conceptos, servicios dentro y fuera del alcance) aparecen en el PDF del mismo idioma, en los dos idiomas. Diferencias de traducción que conviene conocer están al final de este archivo.

## D1 · Conceptos de la nube (24%)

*Content Domain 1: Cloud Concepts.* Domain 1 covers Cloud Concepts and represents 24% of the scored content on the exam.

### D1.1 · Definir los beneficios de la nube de AWS.

*1.1: Define the benefits of the AWS Cloud.*

- **D1.1.1** `[C]` Propuesta de valor de la nube de AWS  
  *Value proposition of the AWS Cloud*
- **D1.1.2** `[H]` Comprender los beneficios de la infraestructura global (por ejemplo, velocidad de implementación, alcance global).  
  *Understanding the benefits of global infrastructure (for example, speed of deployment, global reach)*
- **D1.1.3** `[H]` Comprender las ventajas de la alta disponibilidad, la elasticidad y la agilidad.  
  *Understanding the advantages of high availability, elasticity, and agility*

### D1.2 · Identificar los principios de diseño de la nube de AWS.

*1.2: Identify design principles of the AWS Cloud.*

- **D1.2.1** `[C]` Marco de AWS Well-Architected  
  *AWS Well-Architected Framework*
- **D1.2.2** `[H]` Comprender los pilares del Marco de Well-Architected (por ejemplo, la excelencia operativa, la seguridad, la fiabilidad, la eficiencia del rendimiento, la optimización de costos, la sostenibilidad).  
  *Understanding the pillars of the Well-Architected Framework (for example, operational excellence, security, reliability, performance efficiency, cost optimization, sustainability)*
- **D1.2.3** `[H]` Identificar las diferencias entre los pilares del Marco de Well-Architected.  
  *Identifying differences between the pillars of the Well-Architected Framework*

### D1.3 · Comprender los beneficios y las estrategias de la migración a la nube de AWS.

*1.3: Understand the benefits of and strategies for migration to the AWS Cloud.*

- **D1.3.1** `[C]` Estrategias de adopción de la nube  
  *Cloud adoption strategies*
- **D1.3.2** `[C]` Recursos para respaldar el proceso de migración a la nube  
  *Resources to support the cloud migration journey*
- **D1.3.3** `[H]` Comprender los componentes de AWS Cloud Adoption Framework (AWS CAF) (por ejemplo, reducción del riesgo empresarial; mejora del rendimiento del entorno, social y de gobernanza [ESG]; aumento de los ingresos; aumento de la eficiencia operativa).  
  *Understanding the components of the AWS Cloud Adoption Framework (AWS CAF) (for example, reduced business risk; improved environmental, social, and governance [ESG] performance; increased revenue; increased operational efficiency)*
- **D1.3.4** `[H]` Identificar las estrategias de migración adecuadas (por ejemplo, replicación de bases de datos).  
  *Identifying appropriate migration strategies (for example, database replication)*

### D1.4 · Comprender los conceptos de la economía de la nube.

*1.4: Understand concepts of cloud economics.*

- **D1.4.1** `[C]` Aspectos de la economía de la nube  
  *Aspects of cloud economics*
- **D1.4.2** `[C]` Ahorro de costos al migrar a la nube  
  *Cost savings of moving to the cloud*
- **D1.4.3** `[H]` Comprender el rol de los costos fijos en comparación con los costos variables.  
  *Understanding the role of fixed costs compared with variable costs*
- **D1.4.4** `[H]` Comprender los costos asociados a los entornos en las instalaciones.  
  *Understanding costs that are associated with on-premises environments*
- **D1.4.5** `[H]` Comprender las diferencias entre las estrategias de licencias (por ejemplo, el modelo Bring Your Own License [BYOL] en comparación con las licencias incluidas).  
  *Understanding the differences between licensing strategies (for example, Bring Your Own License [BYOL] model compared with included licenses)*
- **D1.4.6** `[H]` Comprender el concepto de dimensionamiento correcto.  
  *Understanding the concept of rightsizing*
- **D1.4.7** `[H]` Identificar los beneficios de la automatización.  
  *Identifying benefits of automation*
- **D1.4.8** `[H]` Comprender las economías de escala (por ejemplo, ahorro de costos).  
  *Understanding the economies of scale (for example, cost savings)*

## D2 · Seguridad y cumplimiento (30%)

*Content Domain 2: Security and Compliance.* Domain 2 covers Security and Compliance and represents 30% of the scored content on the exam.

### D2.1 · Comprender el modelo de responsabilidad compartida de AWS.

*2.1: Understand the AWS shared responsibility model.*

- **D2.1.1** `[C]` Modelo de responsabilidad compartida de AWS  
  *AWS shared responsibility model*
- **D2.1.2** `[H]` Reconocer los componentes del modelo de responsabilidad compartida de AWS.  
  *Recognizing the components of the AWS shared responsibility model*
- **D2.1.3** `[H]` Describir las responsabilidades del cliente en AWS.  
  *Describing the customer's responsibilities on AWS*
- **D2.1.4** `[H]` Describir las responsabilidades de AWS.  
  *Describing AWS responsibilities*
- **D2.1.5** `[H]` Describir las responsabilidades que comparten el cliente y AWS.  
  *Describing responsibilities that the customer and AWS share*
- **D2.1.6** `[H]` Describir cómo pueden cambiar las responsabilidades de AWS y las del cliente según el servicio utilizado (por ejemplo, Amazon RDS, AWS Lambda o Amazon EC2).  
  *Describing how AWS responsibilities and customer responsibilities can shift, depending on the service used (for example, Amazon RDS, AWS Lambda, Amazon EC2)*

### D2.2 · Comprender los conceptos de seguridad, gobernanza y cumplimiento en la nube de AWS.

*2.2: Understand AWS Cloud security, governance, and compliance concepts.*

- **D2.2.1** `[C]` Conceptos de cumplimiento y gobernanza de AWS  
  *AWS compliance and governance concepts*
- **D2.2.2** `[C]` Beneficios de la seguridad en la nube (por ejemplo, cifrado)  
  *Benefits of cloud security (for example, encryption)*
- **D2.2.3** `[C]` Dónde capturar y localizar los registros asociados a la seguridad en la nube  
  *Where to capture and locate logs that are associated with cloud security*
- **D2.2.4** `[H]` Identificar dónde encontrar la información de cumplimiento de AWS (por ejemplo, AWS Artifact).  
  *Identifying where to find AWS compliance information (for example, AWS Artifact)*
- **D2.2.5** `[H]` Comprender las necesidades de cumplimiento entre ubicaciones geográficas o industrias (por ejemplo, cumplimiento de AWS).  
  *Understanding compliance needs among geographic locations or industries (for example, AWS compliance)*
- **D2.2.6** `[H]` Describir cómo los clientes protegen los recursos en AWS (por ejemplo, Amazon Inspector, AWS Security Hub, Amazon GuardDuty, AWS Shield).  
  *Describing how customers secure resources on AWS (for example, Amazon Inspector, AWS Security Hub, Amazon GuardDuty, AWS Shield)*
- **D2.2.7** `[H]` Identificar opciones de cifrado (por ejemplo, cifrado en tránsito, cifrado en reposo).  
  *Identifying encryption options (for example, encryption in transit, encryption at rest)*
- **D2.2.8** `[H]` Reconocer los servicios que ayudan con la gobernanza y el cumplimiento (por ejemplo, la supervisión con Amazon CloudWatch; la auditoría con AWS CloudTrail y AWS Config; la generación de informes con informes de acceso).  
  *Recognizing services that aid in governance and compliance (for example, monitoring with Amazon CloudWatch; auditing with AWS CloudTrail and AWS Config; reporting with access reports)*
- **D2.2.9** `[H]` Reconocer los requisitos de cumplimiento que varían entre los servicios de AWS.  
  *Recognizing compliance requirements that vary among AWS services*

### D2.3 · Identificar las capacidades de administración de acceso a AWS.

*2.3: Identify AWS access management capabilities.*

- **D2.3.1** `[C]` Administración de identidades y accesos (por ejemplo, AWS Identity and Access Management [IAM])  
  *Identity and access management (for example, AWS Identity and Access Management [IAM])*
- **D2.3.2** `[C]` Importancia de proteger la cuenta de usuario raíz de AWS  
  *Importance of protecting the AWS root user account*
- **D2.3.3** `[C]` Principio de mínimo privilegio  
  *Principle of least privilege*
- **D2.3.4** `[C]` AWS IAM Identity Center  
  *AWS IAM Identity Center*
- **D2.3.5** `[H]` Comprender las claves de acceso, las políticas de contraseñas y el almacenamiento de credenciales (por ejemplo, AWS Secrets Manager, AWS Systems Manager).  
  *Understanding access keys, password policies, and credential storage (for example, AWS Secrets Manager, AWS Systems Manager)*
- **D2.3.6** `[H]` Identificar los métodos de autenticación en AWS (por ejemplo, autenticación multifactor [MFA], IAM Identity Center, roles de IAM entre cuentas).  
  *Identifying authentication methods in AWS (for example, multi-factor authentication [MFA], IAM Identity Center, cross-account IAM roles)*
- **D2.3.7** `[H]` Definir grupos, usuarios, políticas personalizadas y políticas administradas en cumplimiento con el principio de mínimo privilegio.  
  *Defining groups, users, custom policies, and managed policies in compliance with the principle of least privilege*
- **D2.3.8** `[H]` Identificar las tareas que solo el usuario raíz de la cuenta puede realizar.  
  *Identifying tasks that only the account root user can perform*
- **D2.3.9** `[H]` Comprender qué métodos pueden lograr la protección del usuario raíz.  
  *Understanding which methods can achieve root user protection*
- **D2.3.10** `[H]` Comprender los tipos de administración de identidad (por ejemplo, federada).  
  *Understanding the types of identity management (for example, federated)*

### D2.4 · Identifique los componentes y recursos para la seguridad.

*2.4: Identify components and resources for security.*

- **D2.4.1** `[C]` Capacidades de seguridad que proporciona AWS  
  *Security capabilities that AWS provides*
- **D2.4.2** `[C]` Documentación relacionada con la seguridad que proporciona AWS  
  *Security-related documentation that AWS provides*
- **D2.4.3** `[H]` Describir las características y los servicios de seguridad de AWS (por ejemplo, AWS WAF, AWS Firewall Manager, AWS Shield, Amazon GuardDuty).  
  *Describing AWS security features and services (for example, AWS WAF, AWS Firewall Manager, AWS Shield, Amazon GuardDuty)*
- **D2.4.4** `[H]` Comprender que los productos de seguridad de terceros están disponibles en AWS Marketplace.  
  *Understanding that third-party security products are available from AWS Marketplace*
- **D2.4.5** `[H]` Identificar dónde está disponible la información de seguridad de AWS (por ejemplo, AWS Knowledge Center, AWS Security Center, el blog de seguridad de AWS).  
  *Identifying where AWS security information is available (for example, AWS Knowledge Center, AWS Security Center, AWS Security Blog)*
- **D2.4.6** `[H]` Comprender el uso de los servicios de AWS para identificar problemas de seguridad (por ejemplo, AWS Trusted Advisor).  
  *Understanding the use of AWS services for identifying security issues (for example, AWS Trusted Advisor)*

## D3 · Tecnología y servicios en la nube (34%)

*Content Domain 3: Cloud Technology and Services.* Domain 3 covers Cloud Technology and Services and represents 34% of the scored content on the exam.

### D3.1 · Definir métodos de implementación y funcionamiento en la nube de AWS.

*3.1: Define methods of deploying and operating in the AWS Cloud.*

- **D3.1.1** `[C]` Varias formas de aprovisionamiento y operación en la nube de AWS  
  *Various ways of provisioning and operating in the AWS Cloud*
- **D3.1.2** `[C]` Varias formas de acceder a los servicios de AWS  
  *Various ways to access AWS services*
- **D3.1.3** `[C]` Tipos de modelos de implementación en la nube  
  *Types of cloud deployment models*
- **D3.1.4** `[H]` Decidir entre opciones como el acceso programático (por ejemplo, las API, los SDK, la CLI), la Consola de administración de AWS y la infraestructura como código (IaC).  
  *Deciding between options such as programmatic access (for example, APIs, SDKs, CLI), the AWS Management Console, and infrastructure as code (IaC)*
- **D3.1.5** `[H]` Evaluar los requisitos para determinar si se deben utilizar operaciones únicas o procesos repetibles.  
  *Evaluating requirements to determine whether to use one-time operations or repeatable processes*
- **D3.1.6** `[H]` Identificar modelos de implementación (por ejemplo, en la nube, híbridos, en las instalaciones).  
  *Identifying deployment models (for example, cloud, hybrid, on-premises)*

### D3.2 · Definir la infraestructura global de AWS.

*3.2: Define the AWS global infrastructure.*

- **D3.2.1** `[C]` Regiones de AWS, zonas de disponibilidad y ubicaciones periféricas  
  *AWS Regions, Availability Zones, and edge locations*
- **D3.2.2** `[C]` Alta disponibilidad  
  *High availability*
- **D3.2.3** `[C]` Uso de múltiples regiones  
  *Use of multiple Regions*
- **D3.2.4** `[C]` Beneficios de las ubicaciones periféricas  
  *Benefits of edge locations*
- **D3.2.5** `[H]` Describir las relaciones entre las regiones, las zonas de disponibilidad y las ubicaciones periféricas.  
  *Describing relationships among Regions, Availability Zones, and edge locations*
- **D3.2.6** `[H]` Describir cómo lograr una alta disponibilidad mediante el uso de varias zonas de disponibilidad.  
  *Describing how to achieve high availability by using multiple Availability Zones*
- **D3.2.7** `[H]` Reconocer que las zonas de disponibilidad no comparten puntos únicos de error.  
  *Recognizing that Availability Zones do not share single points of failure*
- **D3.2.8** `[H]` Describir cuándo utilizar varias regiones (por ejemplo, recuperación de desastres, continuidad de actividades, baja latencia para los usuarios finales, soberanía de datos).  
  *Describing when to use multiple Regions (for example, disaster recovery, business continuity, low latency for end users, data sovereignty)*

### D3.3 · Identificar los servicios de computación de AWS.

*3.3: Identify AWS compute services.*

- **D3.3.1** `[C]` Servicios de computación de AWS  
  *AWS compute services*
- **D3.3.2** `[H]` Reconocer el uso adecuado de varios tipos de instancia de Amazon EC2 (por ejemplo, optimizadas para computación, optimizadas para almacenamiento).  
  *Recognizing the appropriate use of various Amazon EC2 instance types (for example, compute optimized, storage optimized)*
- **D3.3.3** `[H]` Reconocer el uso adecuado de diversas opciones de contenedores (por ejemplo, Amazon Elastic Container Service [Amazon ECS], Amazon Elastic Kubernetes Service [Amazon EKS]).  
  *Recognizing the appropriate use of various container options (for example, Amazon Elastic Container Service [Amazon ECS], Amazon Elastic Kubernetes Service [Amazon EKS])*
- **D3.3.4** `[H]` Reconocer el uso adecuado de diversas opciones de computación sin servidor (por ejemplo, AWS Fargate, AWS Lambda).  
  *Recognizing the appropriate use of various serverless compute options (for example, AWS Fargate, AWS Lambda)*
- **D3.3.5** `[H]` Reconocer que el escalado automático proporciona elasticidad.  
  *Recognizing that auto scaling provides elasticity*
- **D3.3.6** `[H]` Identificar los propósitos de los equilibradores de carga.  
  *Identifying the purposes of load balancers*

### D3.4 · Identificar los servicios de bases de datos de AWS.

*3.4: Identify AWS database services.*

- **D3.4.1** `[C]` Servicios de bases de datos de AWS  
  *AWS database services*
- **D3.4.2** `[C]` Migración de bases de datos  
  *Database migration*
- **D3.4.3** `[H]` Decidir cuándo utilizar las bases de datos alojadas en EC2 o las bases de datos administradas por AWS.  
  *Deciding when to use EC2 hosted databases or AWS managed databases*
- **D3.4.4** `[H]` Identificar bases de datos relacionales (por ejemplo, Amazon RDS, Amazon Aurora).  
  *Identifying relational databases (for example, Amazon RDS, Amazon Aurora)*
- **D3.4.5** `[H]` Identificar bases de datos NoSQL (por ejemplo, Amazon DynamoDB)  
  *Identifying NoSQL databases (for example, Amazon DynamoDB)*
- **D3.4.6** `[H]` Identificar bases de datos basadas en memoria (por ejemplo, Amazon ElastiCache).  
  *Identifying memory-based databases (for example, Amazon ElastiCache)*
- **D3.4.7** `[H]` Identificar herramientas de migración de bases de datos (por ejemplo, AWS Database Migration Service [AWS DMS], AWS Schema Conversion Tool [AWS SCT]).  
  *Identifying database migration tools (for example, AWS Database Migration Service [AWS DMS], AWS Schema Conversion Tool [AWS SCT])*

### D3.5 · Identificar los servicios de red de AWS.

*3.5: Identify AWS network services.*

- **D3.5.1** `[C]` Servicios de red de AWS  
  *AWS network services*
- **D3.5.2** `[H]` Identificar los componentes de una VPC (por ejemplo, subredes, puertas de enlace).  
  *Identifying the components of a VPC (for example, subnets, gateways)*
- **D3.5.3** `[H]` Describir la seguridad en una VPC (por ejemplo, ACL de red, grupos de seguridad, Amazon Inspector).  
  *Understanding security in a VPC (for example, network ACLs, security groups, Amazon Inspector)*
- **D3.5.4** `[H]` Comprender el propósito de Amazon Route 53.  
  *Understanding the purpose of Amazon Route 53*
- **D3.5.5** `[H]` Identificar las opciones de conectividad de red con AWS (por ejemplo, AWS VPN, AWS Direct Connect).  
  *Identifying network connectivity options to AWS (for example, AWS VPN, AWS Direct Connect)*

### D3.6 · Identificar los servicios de almacenamiento de AWS.

*3.6: Identify AWS storage services.*

- **D3.6.1** `[C]` Servicios de almacenamiento de AWS  
  *AWS storage services*
- **D3.6.2** `[H]` Identificar los usos del almacenamiento de objetos.  
  *Identifying the uses for object storage*
- **D3.6.3** `[H]` Reconocer las diferencias en las clases de almacenamiento de Amazon S3.  
  *Recognizing the differences in Amazon S3 storage classes*
- **D3.6.4** `[H]` Identificar soluciones de almacenamiento en bloques (por ejemplo, Amazon Elastic Block Store [Amazon EBS], almacén de instancias).  
  *Identifying block storage solutions (for example, Amazon Elastic Block Store [Amazon EBS], instance store)*
- **D3.6.5** `[H]` Identificar servicios de archivos (por ejemplo, Amazon Elastic File System [Amazon EFS], Amazon FSx).  
  *Identifying file services (for example, Amazon Elastic File System [Amazon EFS], Amazon FSx)*
- **D3.6.6** `[H]` Identificar los sistemas de archivos en caché (por ejemplo, AWS Storage Gateway).  
  *Identifying cached file systems (for example, AWS Storage Gateway)*
- **D3.6.7** `[H]` Comprender los casos de uso de las políticas de ciclo de vida.  
  *Understanding use cases for lifecycle policies*
- **D3.6.8** `[H]` Describir los casos de uso de AWS Backup.  
  *Understanding use cases for AWS Backup*

### D3.7 · Identificar los servicios de inteligencia artificial y machine learning (IA/ML) y los servicios de análisis de AWS.

*3.7: Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services.*

- **D3.7.1** `[C]` Servicios de IA/ML de AWS  
  *AWS AI/ML services*
- **D3.7.2** `[C]` Servicios de análisis de AWS  
  *AWS analytics services*
- **D3.7.3** `[H]` Comprender los servicios de IA/ML y las tareas que realizan (por ejemplo, Amazon SageMaker AI, Amazon Lex).  
  *Understanding AI/ML services and the tasks that they accomplish (for example, Amazon SageMaker AI, Amazon Lex)*
- **D3.7.4** `[H]` Identificar los servicios de análisis de datos (por ejemplo, Amazon Athena, Amazon Kinesis, AWS Glue, Amazon Quick Sight).  
  *Identifying the services for data analytics (for example, Amazon Athena, Amazon Kinesis, AWS Glue, Amazon Quick Sight)*

### D3.8 · Identificar los servicios de otras categorías de servicios de AWS dentro del alcance del examen.

*3.8: Identify services from other in-scope AWS service categories.*

- **D3.8.1** `[C]` Servicios de integración de aplicaciones de Amazon EventBridge, Amazon Simple Notification Service (Amazon SNS) y Amazon Simple Queue Service (Amazon SQS)  
  *Application integration services of Amazon EventBridge, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS)*
- **D3.8.2** `[C]` Servicios de aplicaciones empresariales de Amazon Connect y Amazon Simple Email Service (Amazon SES)  
  *Business application services of Amazon Connect and Amazon Simple Email Service (Amazon SES)*
- **D3.8.3** `[C]` Servicios de habilitación de clientes (por ejemplo, AWS Support)  
  *Customer enablement services (for example, AWS Support)*
- **D3.8.4** `[C]` Servicios y capacidades de herramientas para desarrolladores (por ejemplo, AWS CodeBuild, AWS CodePipeline y AWS X-Ray)  
  *Developer tool services and capabilities (for example, AWS CodeBuild, AWS CodePipeline, and AWS X-Ray)*
- **D3.8.5** `[C]` Servicios de computación para usuarios finales de Amazon AppStream 2.0, Amazon WorkSpaces y el navegador seguro Amazon WorkSpaces  
  *End-user computing services of Amazon AppStream 2.0, Amazon WorkSpaces, and Amazon WorkSpaces Secure Browser*
- **D3.8.6** `[C]` Servicios web y móviles de frontend de AWS Amplify  
  *Frontend web and mobile services of AWS Amplify*
- **D3.8.7** `[C]` Servicios de IoT (por ejemplo, AWS IoT Core)  
  *IoT services (for example, AWS IoT Core)*
- **D3.8.8** `[H]` Elegir el servicio adecuado para entregar mensajes y enviar alertas y notificaciones.  
  *Choosing the appropriate service to deliver messages and to send alerts and notifications*
- **D3.8.9** `[H]` Elegir el servicio adecuado para satisfacer las necesidades de las aplicaciones empresariales.  
  *Choosing the appropriate service to meet business application needs*
- **D3.8.10** `[H]` Elegir la opción adecuada para la asistencia de soporte empresarial.  
  *Choosing the appropriate option for business support assistance*
- **D3.8.11** `[H]` Identificar las herramientas para desarrollar e implementar aplicaciones y solucionar problemas relacionados.  
  *Identifying the tools to develop, deploy, and troubleshoot applications*
- **D3.8.12** `[H]` Identificar los servicios que pueden presentar la salida de las máquinas virtuales (VM) en las máquinas de los usuarios finales.  
  *Identifying the services that can present the output of virtual machines (VMs) on end-user machines*
- **D3.8.13** `[H]` Identificar los servicios que pueden crear e implementar servicios móviles y de frontend.  
  *Identifying the services that can create and deploy frontend and mobile services*
- **D3.8.14** `[H]` Identificar los servicios que administran los dispositivos de IoT.  
  *Identifying the services that manage IoT devices*

## D4 · Facturación, precios y soporte (12%)

*Content Domain 4: Billing, Pricing, and Support.* Domain 4 covers Billing, Pricing, and Support and represents 12% of the scored content on the exam.

### D4.1 · Comparar los modelos de precios de AWS.

*4.1: Compare AWS pricing models.*

- **D4.1.1** `[C]` Opciones de compra de computación (por ejemplo, instancias bajo demanda, instancias reservadas, instancias de spot, AWS Savings Plans, hosts dedicados, instancias dedicadas, reservas de capacidad)  
  *Compute purchasing options (for example, On-Demand Instances, Reserved Instances, Spot Instances, AWS Savings Plans, Dedicated Hosts, Dedicated Instances, Capacity Reservations)*
- **D4.1.2** `[C]` Opciones y niveles de almacenamiento  
  *Storage options and tiers*
- **D4.1.3** `[H]` Identificar cuándo utilizar varias opciones de compra de computación.  
  *Identifying when to use various compute purchasing options*
- **D4.1.4** `[H]` Describir la flexibilidad de las instancias reservadas.  
  *Describing Reserved Instance flexibility*
- **D4.1.5** `[H]` Describir el comportamiento de las instancias reservadas en AWS Organizations.  
  *Describing Reserved Instance behavior in AWS Organizations*
- **D4.1.6** `[H]` Comprender los costos de transferencia de datos entrantes y salientes (por ejemplo, de una región de AWS a otra, dentro de la misma región).  
  *Understanding incoming data transfer costs and outgoing data transfer costs (for example, from one AWS Region to another Region, within the same Region)*
- **D4.1.7** `[H]` Comprender las opciones de precios para las distintas opciones y niveles de almacenamiento.  
  *Understanding pricing options for various storage options and tiers*

### D4.2 · Comprender los recursos para la facturación, el presupuesto y la administración de costos.

*4.2: Understand resources for billing, budget, and cost management.*

- **D4.2.1** `[C]` Soporte e información sobre facturación  
  *Billing support and information*
- **D4.2.2** `[C]` Información sobre precios de los servicios de AWS  
  *Pricing information for AWS services*
- **D4.2.3** `[C]` AWS Organizations  
  *AWS Organizations*
- **D4.2.4** `[C]` Etiquetas de asignación de costos de AWS  
  *AWS cost allocation tags*
- **D4.2.5** `[H]` Comprender los usos y las capacidades adecuados de AWS Budgets y el Explorador de costos de AWS.  
  *Understanding the appropriate uses and capabilities of AWS Budgets and AWS Cost Explorer*
- **D4.2.6** `[H]` Comprender los usos y las capacidades adecuados de la Calculadora de precios de AWS.  
  *Understanding the appropriate uses and capabilities of AWS Pricing Calculator*
- **D4.2.7** `[H]` Comprender la facturación unificada de AWS Organizations y la asignación de costos.  
  *Understanding AWS Organizations consolidated billing and allocation of costs*
- **D4.2.8** `[H]` Comprender los distintos tipos de etiquetas de asignación de costos y su relación con los informes de facturación (por ejemplo, Informe de costo y uso de AWS).  
  *Understanding various types of cost allocation tags and their relation to billing reports (for example, AWS Cost and Usage Report)*

### D4.3 · Identificar los recursos técnicos de AWS y las opciones de AWS Support.

*4.3: Identify AWS technical resources and AWS Support options.*

- **D4.3.1** `[C]` Los recursos y la documentación disponibles en los sitios web oficiales de AWS  
  *Resources and documentation available on official AWS websites*
- **D4.3.2** `[C]` Planes de AWS Support  
  *AWS Support plans*
- **D4.3.3** `[C]` Roles de la red de socios de AWS, incluidos los proveedores de software independientes y los integradores de sistemas  
  *Role of the AWS Partner Network, including independent software vendors and system integrators*
- **D4.3.4** `[C]` Centro de soporte de AWS  
  *AWS Support Center*
- **D4.3.5** `[H]` Localizar documentos técnicos, blogs y documentación de AWS en los sitios web oficiales de AWS.  
  *Locating AWS whitepapers, blogs, and documentation on official AWS websites*
- **D4.3.6** `[H]` Identificar y localizar los recursos técnicos de AWS (por ejemplo, recomendaciones de AWS, AWS Knowledge Center, AWS re:Post).  
  *Identifying and locating AWS technical resources (for example, AWS Prescriptive Guidance, AWS Knowledge Center, AWS re:Post)*
- **D4.3.7** `[H]` Identificar las opciones de AWS Support para los clientes de AWS (por ejemplo, comunidades y servicio al cliente, AWS Developer Support, AWS Business Support, AWS Enterprise On-Ramp Support, AWS Enterprise Support).  
  *Identifying AWS Support options for AWS customers (for example, customer service and communities, AWS Developer Support, AWS Business Support, AWS Enterprise On-Ramp Support, AWS Enterprise Support)*
- **D4.3.8** `[H]` Identificar el rol de AWS Trusted Advisor, el Panel de AWS Health y la API de AWS Health para ayudar a administrar y supervisar los entornos para la optimización de costos.  
  *Identifying the role of AWS Trusted Advisor, AWS Health Dashboard, and the AWS Health API to help manage and monitor environments for cost optimization*
- **D4.3.9** `[H]` Identificar el rol del equipo de confianza y seguridad de AWS para denunciar el abuso de los recursos de AWS.  
  *Identifying the role of the AWS Trust and Safety team to report abuse of AWS resources*
- **D4.3.10** `[H]` Comprender el rol de los socios de AWS (por ejemplo, AWS Marketplace, proveedores de software independientes, integradores de sistemas).  
  *Understanding the role of AWS Partners (for example, AWS Marketplace, independent software vendors, system integrators)*
- **D4.3.11** `[H]` Identificar los beneficios de ser socio de AWS (por ejemplo, formación y certificación para socios, eventos para socios, descuentos por volumen para socios).  
  *Identifying the benefits of being an AWS Partner (for example, partner training and certification, partner events, partner volume discounts)*
- **D4.3.12** `[H]` Identificar los servicios clave que ofrece AWS Marketplace (por ejemplo, administración de costos, gobernanza y derechos).  
  *Identifying the key services that AWS Marketplace offers (for example, cost management, governance and entitlement)*
- **D4.3.13** `[H]` Identificar las opciones de asistencia técnica disponibles en AWS (por ejemplo, AWS Profesional Services, arquitectos de soluciones de AWS).  
  *Identifying technical assistance options available at AWS (for example, AWS Professional Services, AWS solutions architects)*

## Total de puntos por dominio

| Dominio | Peso | Tareas | Conocimiento `[C]` | Habilidad `[H]` | Total |
|---|---:|---:|---:|---:|---:|
| D1 · Conceptos de la nube | 24% | 4 | 6 | 12 | 18 |
| D2 · Seguridad y cumplimiento | 30% | 4 | 10 | 21 | 31 |
| D3 · Tecnología y servicios en la nube | 34% | 8 | 21 | 37 | 58 |
| D4 · Facturación, precios y soporte | 12% | 3 | 10 | 18 | 28 |
| **Total** | **100%** | **19** | **47** | **88** | **135** |

Para el AZ-900 fueron 57 bullets en una sola lista. Aquí AWS separa conocimiento y habilidad, y muchos puntos de conocimiento son el paraguas de las habilidades de la misma tarea (por ejemplo, D3.3.1 «Servicios de computación de AWS» contiene D3.3.2 a D3.3.6). Para medir cobertura del banco conviene contar las habilidades; los puntos de conocimiento sirven para detectar temas que ninguna habilidad nombra, como D2.3.4 (IAM Identity Center) o D4.2.1 (soporte e información sobre facturación).

## Diferencias de traducción entre la guía en español y la original

| Punto | Español (es_es) | Inglés (en_us) | Nota |
|---|---|---|---|
| D4.3.6 | «recomendaciones de AWS» | *AWS Prescriptive Guidance* | Es el nombre de un recurso concreto; la traducción lo vuelve genérico. La lista de tecnologías y conceptos hace lo mismo. |
| D4.3.13 | «AWS Profesional Services» | *AWS Professional Services* | Errata en la guía en español. |
| D3.3.6 | «equilibradores de carga» | *load balancers* | El PDF anterior de la guía (versión 1.2, abril de 2025, con variantes para Latinoamérica y España) decía «balanceadores de carga». No se pudo confirmar cuál término usa el examen en español. |
| D1.4.6 | «dimensionamiento correcto» | *rightsizing* | La variante de España del PDF 1.2 decía «redimensionamiento». |

La guía en docs.aws.amazon.com/es_es no dice si su texto es la variante de Latinoamérica o la de España. El examen se ofrece en las dos. El PDF anterior sí traía ambas variantes: https://d1.awsstatic.com/es_ES/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf (versión 1.2, 54 páginas, consultado el 24-sep-2026). Ese PDF es anterior a los cambios de nombre de 2025 (SageMaker AI, Quick Sight, WorkSpaces Secure Browser), así que sirve para terminología y no como temario vigente.
