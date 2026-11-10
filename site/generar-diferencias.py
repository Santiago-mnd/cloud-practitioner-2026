#!/usr/bin/env python3
"""Genera diferencias.html a partir de la lista de diferencias clave.

Cada entrada es un dict:
  dominio    1 a 4 (dominios del examen)
  tema       etiqueta fina dentro del dominio
  id         ancla estable; practica.html enlaza aquí desde una pregunta fallada
  titulo     la distinción, en una línea
  pista      la frase que decide la respuesta en el examen
  confusion  por qué la respuesta equivocada se siente correcta
  regla      qué pasa en realidad
  tabla      opcional, lista de (situación, respuesta) para los mapas de servicios
"""
import html
import pathlib

DOMINIOS = {
    1: "Conceptos de la nube",
    2: "Seguridad y cumplimiento",
    3: "Tecnología y servicios en la nube",
    4: "Facturación, precios y soporte",
}


ETIQUETAS = {
    "agility-vs-elasticity": "Agilidad o elasticidad",
    "economies-of-scale": "Escala o gasto variable",
    "well-architected-pillars": "Los seis pilares",
    "caf-perspectives": "CAF: perspectivas y resultados",
    "seven-rs": "Las siete R",
    "byol-vs-license-included": "BYOL o licencia incluida",
    "rightsizing-vs-autoscaling": "Rightsizing o Auto Scaling",
    "security-of-vs-in": "De la nube o en la nube",
    "responsibility-by-service": "Responsabilidad por servicio",
    "shared-controls": "Controles compartidos",
    "cloudwatch-cloudtrail-config": "CloudWatch, CloudTrail, Config",
    "artifact-vs-config": "Artifact o Config",
    "threat-detection-family": "Cinco servicios de seguridad",
    "shield-waf-firewall-manager": "Shield, WAF, Firewall Manager",
    "keys-certificates-secrets": "Claves, certificados, secretos",
    "encryption-transit-vs-rest": "En tránsito o en reposo",
    "iam-user-vs-role": "Usuario o rol",
    "iam-identity-center-cognito": "IAM, Identity Center, Cognito",
    "iam-policy-vs-scp": "Política de IAM o SCP",
    "root-user": "El usuario raíz",
    "deployment-models": "Modelos de implementación",
    "console-vs-iac": "Consola o código",
    "region-az-edge": "Región, AZ y periferia",
    "ec2-instance-families": "Familias de instancia",
    "compute-options": "ECS, EKS, Fargate, Lambda",
    "elb-vs-auto-scaling": "Balanceador o Auto Scaling",
    "database-options": "Qué base de datos",
    "dms-vs-sct": "DMS o SCT",
    "security-group-vs-nacl": "Grupo de seguridad o ACL",
    "connectivity-options": "Conectar redes",
    "edge-services": "CloudFront, Accelerator, Route 53",
    "storage-types": "Bloque, archivo u objeto",
    "s3-storage-classes": "Clases de S3",
    "analytics-services": "Servicios de análisis",
    "ai-services": "Servicios de IA",
    "messaging-services": "SNS, SQS, EventBridge",
    "other-services": "Escritorios, IoT, código",
    "purchase-options": "Opciones de compra",
    "savings-plans-vs-ri": "Savings Plans o RI",
    "data-transfer": "Entrada y salida de datos",
    "cost-tools": "Herramientas de costos",
    "cost-allocation-tags": "Etiquetas de costos",
    "organizations-vs-control-tower": "Organizations o Control Tower",
    "support-plans": "Planes de soporte",
    "where-to-go": "A quién acudir",
}

DIFERENCIAS = [
  # ---------- Dominio 1 ----------
  dict(dominio=1, tema="Beneficios", id="agility-vs-elasticity",
       titulo="Agilidad es lanzar rápido; elasticidad es ajustarse a la demanda",
       pista="Algo nuevo disponible en minutos = agilidad. Crecer y encogerse según la carga = elasticidad.",
       confusion="Las dos suenan a rapidez; además, pueden aparecer juntas en un escenario de lanzamiento.",
       regla="AWS enumera seis ventajas de la nube. «Aumentar la velocidad y la agilidad» habla de tener recursos nuevos en minutos para experimentar más. «Dejar de adivinar la capacidad» habla de subirla o bajarla según la demanda real, que es la elasticidad. La alta disponibilidad responde a otra pregunta: que el servicio siga en línea aunque falle una parte."),
  dict(dominio=1, tema="Economía de la nube", id="economies-of-scale",
       titulo="Economías de escala y gasto variable abaratan por caminos distintos",
       pista="Pagar solo lo que se consume = gasto variable. Precio más bajo porque AWS suma el uso de muchos clientes = economías de escala.",
       confusion="Ambas pueden significar «sale más barato», así que parecen la misma ventaja.",
       regla="Cambiar gasto fijo por variable significa no invertir por adelantado en centros de datos y servidores, y pagar solo cuando se consume. Las economías de escala vienen de que AWS suma el uso de cientos de miles de clientes. Con ese volumen cobra un precio por uso más bajo del que lograría una empresa por su cuenta."),
  dict(dominio=1, tema="Well-Architected", id="well-architected-pillars",
       titulo="Los seis pilares de Well-Architected se distinguen por la pregunta que responden",
       pista="Funcionar bien y de forma constante = fiabilidad. Usar el recurso adecuado conforme cambia la demanda = eficiencia del rendimiento. Energía o impacto ambiental = sostenibilidad.",
       confusion="Varios pilares suenan a «que todo funcione bien». Apagar recursos que sobran ahorra dinero y energía a la vez, así que costos y sostenibilidad también se cruzan.",
       regla="La herramienta AWS Well-Architected mide una carga de trabajo contra las buenas prácticas del marco y da recomendaciones para mejorarla.",
       tabla=[("Organizar al equipo, operar la carga y mejorarla con el tiempo", "Excelencia operativa"),
              ("Proteger datos, sistemas y activos", "Seguridad"),
              ("Que la carga haga su función de forma correcta y constante", "Fiabilidad"),
              ("Usar los recursos con eficiencia conforme cambian la demanda y la tecnología", "Eficiencia del rendimiento"),
              ("Entregar valor de negocio al menor precio", "Optimización de costos"),
              ("Reducir el impacto ambiental, sobre todo el consumo de energía", "Sostenibilidad")]),
  dict(dominio=1, tema="Adopción de la nube", id="caf-perspectives",
       titulo="El AWS CAF tiene seis perspectivas y cuatro resultados de negocio",
       pista="Negocio, personas, gobernanza, plataforma, seguridad y operaciones = perspectivas. Menos riesgo, mejor ESG, más ingresos y más eficiencia = resultados.",
       confusion="Las dos listas se parecen, y «gobernanza» aparece como perspectiva y también dentro del ESG.",
       regla="El marco de adopción de la nube de AWS (AWS CAF) agrupa en seis perspectivas las capacidades que una organización necesita para adoptar la nube; cada perspectiva tiene sus propios responsables. Los resultados son lo que la transformación entrega al negocio: menor riesgo, mejor desempeño ambiental, social y de gobernanza (ESG), más ingresos y más eficiencia operativa."),
  dict(dominio=1, tema="Migración", id="seven-rs",
       titulo="Las siete estrategias de migración se distinguen por lo que le pasa a la aplicación",
       pista="Sin cambios = rehost. Con ajustes = replatform. Rediseño nativo = refactor. Otro producto = repurchase.",
       confusion="Rehost, relocate y replatform suenan igual: mover la aplicación a la nube.",
       regla="Para migraciones grandes, AWS recomienda rehost, replatform o relocate, y dejar el rediseño para después de migrar, porque refactor es la estrategia más compleja.",
       tabla=[("Moverla tal cual, sin cambios (lift and shift)", "Rehost"),
              ("Moverla con algunos ajustes para aprovechar la nube (lift, tinker and shift)", "Replatform"),
              ("Rediseñarla con capacidades nativas de la nube", "Refactor"),
              ("Cambiarla por otro producto, a menudo software como servicio o SaaS (drop and shop)", "Repurchase"),
              ("Pasar muchos servidores a la versión en la nube de la misma plataforma, sin comprar hardware ni reescribir", "Relocate"),
              ("Dejarla donde está por ahora", "Retain"),
              ("Apagarla porque ya no aporta valor", "Retire")]),
  dict(dominio=1, tema="Economía de la nube", id="byol-vs-license-included",
       titulo="Con BYOL se reusa la licencia propia; con licencia incluida, AWS la cobra",
       pista="Ya tiene licencias y quiere reusarlas = BYOL.",
       confusion="En ambos casos el software termina funcionando en AWS, así que la diferencia parece solo contable.",
       regla="Con licencia incluida, el precio del servicio ya trae la licencia del software; por ejemplo, Oracle Database Standard Edition 2 en Amazon RDS, que también admite BYOL. Con BYOL (Bring Your Own License), la empresa usa licencias que ya compró. Algunas licencias se cuentan por socket o por núcleo físico, y los hosts dedicados permiten usarlas."),
  dict(dominio=1, tema="Economía de la nube", id="rightsizing-vs-autoscaling",
       titulo="Rightsizing cambia el tamaño; Auto Scaling cambia la cantidad",
       pista="Instancias sobradas todo el tiempo = rightsizing. Carga que sube y baja = Auto Scaling.",
       confusion="Ambos ajustan la capacidad al uso para no pagar de más.",
       regla="El dimensionamiento correcto (rightsizing) elige el tipo y el tamaño de instancia que corresponden al uso real, al menor costo. Es una revisión continua. AWS Compute Optimizer da recomendaciones de este tipo. El escalado automático agrega o quita instancias según la demanda, sin cambiarles el tamaño."),

  # ---------- Dominio 2 ----------
  dict(dominio=2, tema="Responsabilidad compartida", id="security-of-vs-in",
       titulo="AWS protege la nube; el cliente protege lo que pone en ella",
       pista="Instalaciones, hardware, red y virtualización = AWS. Datos, identidades, configuración y sistema operativo invitado = cliente.",
       confusion="«Seguridad de la nube» y «seguridad en la nube» se leen casi igual.",
       regla="AWS responde por la seguridad de la nube: la infraestructura de hardware, software, red e instalaciones con la que opera todos sus servicios. El cliente responde por la seguridad en la nube: sus datos, sus accesos, su configuración y, según el servicio, el sistema operativo y las aplicaciones."),
  dict(dominio=2, tema="Responsabilidad compartida", id="responsibility-by-service",
       titulo="Lo que le toca al cliente cambia con cada servicio",
       pista="EC2 = el cliente parcha el sistema operativo. S3 o DynamoDB = AWS opera hasta la plataforma.",
       confusion="El modelo se aprende como una línea fija, pero esa línea cambia según el servicio.",
       regla="Mientras más abstracto es el servicio, más capas opera AWS. Los datos, las opciones de cifrado y los permisos de AWS Identity and Access Management (IAM) siempre quedan del lado del cliente.",
       tabla=[("Amazon EC2", "Cliente: sistema operativo invitado con sus parches, aplicaciones y grupo de seguridad"),
              ("Amazon RDS", "AWS: parches, respaldos y recuperación ante fallas. Cliente: datos, usuarios y acceso de red"),
              ("AWS Lambda", "AWS: servidores, sistema operativo, capacidad y escalado. Cliente: código, datos y permisos"),
              ("Amazon S3 y DynamoDB", "AWS: infraestructura, sistema operativo y plataforma. Cliente: datos, opciones de cifrado y permisos")]),
  dict(dominio=2, tema="Responsabilidad compartida", id="shared-controls",
       titulo="En un control compartido, cada parte cubre su propia capa",
       pista="Parches, configuración y capacitación = compartidos. Físicos y ambientales = heredados de AWS.",
       confusion="«Compartido» suena a que AWS y el cliente hacen juntos la misma tarea.",
       regla="Un control heredado lo cumple AWS por completo y el cliente lo recibe tal cual, como los controles físicos y ambientales. En un control compartido, cada parte lo implementa en su capa: AWS parcha su infraestructura y el cliente parcha su sistema operativo invitado y sus aplicaciones; AWS capacita a su personal y el cliente al suyo. Los controles específicos del cliente, como separar datos en zonas de seguridad, son solo suyos."),
  dict(dominio=2, tema="Monitoreo y auditoría", id="cloudwatch-cloudtrail-config",
       titulo="CloudWatch, CloudTrail y Config responden tres preguntas distintas",
       pista="¿Cómo se comporta? = CloudWatch. ¿Quién hizo qué? = CloudTrail. ¿Cómo está configurado y si cumple? = Config.",
       confusion="Los tres registran algo, y la guía los pone juntos en la misma habilidad de gobernanza y cumplimiento.",
       regla="Un cambio de configuración deja rastro en los dos últimos: CloudTrail guarda quién hizo la llamada y Config, si está grabando ese tipo de recurso, guarda cómo quedó.",
       tabla=[("Métricas, registros y alarmas de recursos y aplicaciones", "Amazon CloudWatch"),
              ("Quién hizo cada acción en la cuenta, y cuándo", "AWS CloudTrail"),
              ("Historial de configuración de los recursos y su evaluación contra reglas", "AWS Config")]),
  dict(dominio=2, tema="Cumplimiento", id="artifact-vs-config",
       titulo="Artifact entrega los reportes de AWS; Config evalúa tus recursos",
       pista="Descargar el reporte SOC o PCI de AWS = Artifact.",
       confusion="Los dos aparecen cuando el enunciado dice «cumplimiento».",
       regla="AWS Artifact es el portal para descargar los documentos de cumplimiento de AWS, como los reportes SOC y PCI y las certificaciones ISO. Ahí también se aceptan acuerdos con AWS. Sirve para mostrarle a un auditor lo que AWS cumple de su lado. AWS Config revisa si los recursos del cliente cumplen las reglas que el cliente define."),
  dict(dominio=2, tema="Protección", id="threat-detection-family",
       titulo="Cinco servicios de seguridad, cinco preguntas distintas",
       pista="Vulnerabilidades = Inspector. Actividad sospechosa = GuardDuty. Causa raíz = Detective. Datos sensibles en S3 = Macie. Todo junto = Security Hub.",
       confusion="Todos buscan problemas de seguridad, y sus nombres no dicen qué buscan.",
       regla="Inspector revisa el software instalado. GuardDuty analiza registros de actividad de la cuenta, de la red y de DNS.",
       tabla=[("Vulnerabilidades de software y exposición de red en EC2, imágenes de contenedores y Lambda", "Amazon Inspector"),
              ("Actividad sospechosa o maliciosa en la cuenta", "Amazon GuardDuty"),
              ("Investigar un hallazgo hasta su causa raíz", "Amazon Detective"),
              ("Datos sensibles, como datos personales, guardados en S3", "Amazon Macie"),
              ("Reunir hallazgos de varios servicios y revisar la postura contra estándares", "AWS Security Hub")]),
  dict(dominio=2, tema="Protección", id="shield-waf-firewall-manager",
       titulo="Shield frena DDoS, WAF filtra peticiones web y Firewall Manager administra las reglas",
       pista="Denegación de servicio = Shield. Inyección SQL o XSS = WAF. Reglas en todas las cuentas = Firewall Manager.",
       confusion="Los tres se presentan como protección del perímetro, y WAF y Shield suelen ir juntos.",
       regla="AWS Shield Standard protege contra los ataques de denegación de servicio distribuido (DDoS) más comunes, sin costo adicional y sin configurarlo. Shield Advanced es de pago y agrega protección y ayuda especializada. AWS WAF filtra peticiones HTTP y HTTPS con reglas, por ejemplo contra inyección SQL y secuencias de comandos entre sitios (XSS). AWS Firewall Manager administra esas reglas de forma central en las cuentas de AWS Organizations."),
  dict(dominio=2, tema="Cifrado y secretos", id="keys-certificates-secrets",
       titulo="Claves, HSM dedicados, certificados y secretos viven en servicios separados",
       pista="Claves de cifrado = KMS. HSM dedicado = CloudHSM. Certificados TLS = ACM. Contraseñas que rotan = Secrets Manager.",
       confusion="Todo suena a guardar algo secreto.",
       regla="Otros servicios de AWS, como S3 y EBS, se integran con KMS para cifrar sus datos con claves de KMS.",
       tabla=[("Crear y controlar claves de cifrado administradas", "AWS Key Management Service (KMS)"),
              ("Un módulo de seguridad de hardware (HSM) dedicado que controla el cliente", "AWS CloudHSM"),
              ("Emitir y renovar certificados SSL/TLS", "AWS Certificate Manager"),
              ("Guardar credenciales y rotarlas de forma automática", "AWS Secrets Manager")]),
  dict(dominio=2, tema="Cifrado y secretos", id="encryption-transit-vs-rest",
       titulo="El cifrado en tránsito protege el viaje; el cifrado en reposo protege lo guardado",
       pista="TLS o HTTPS = en tránsito. Datos guardados en S3, EBS o RDS = en reposo.",
       confusion="Ambas formas se llaman cifrado y muchos servicios ofrecen las dos.",
       regla="El cifrado en tránsito protege los datos mientras viajan entre sistemas, con protocolos de cifrado como TLS. El cifrado en reposo protege los datos almacenados; en AWS se puede hacer con claves de AWS KMS."),
  dict(dominio=2, tema="Identidad y acceso", id="iam-user-vs-role",
       titulo="Un usuario de IAM tiene credenciales fijas; un rol se asume",
       pista="Credenciales temporales o acceso entre cuentas = rol.",
       confusion="Los dos reciben políticas de permisos, así que parecen dos formas de lo mismo.",
       regla="Un usuario de IAM es una identidad con credenciales de largo plazo: contraseña para la consola o claves de acceso para la línea de comandos (CLI) y los kits de desarrollo (SDK). Un rol no tiene credenciales de largo plazo; quien lo asume recibe credenciales temporales. Se usa para dar permisos a servicios, a otras cuentas o a identidades federadas."),
  dict(dominio=2, tema="Identidad y acceso", id="iam-identity-center-cognito",
       titulo="IAM, IAM Identity Center y Cognito atienden a gente distinta",
       pista="Empleados en varias cuentas = Identity Center. Usuarios de tu app = Cognito.",
       confusion="Los tres autentican usuarios.",
       regla="IAM Identity Center antes se llamaba AWS Single Sign-On, y ese nombre sigue apareciendo en material de estudio.",
       tabla=[("Identidades y permisos dentro de una cuenta de AWS", "AWS IAM"),
              ("Inicio de sesión único de los empleados en varias cuentas y aplicaciones", "AWS IAM Identity Center"),
              ("Registro e inicio de sesión de los usuarios de tus apps web y móviles", "Amazon Cognito")]),
  dict(dominio=2, tema="Identidad y acceso", id="iam-policy-vs-scp",
       titulo="Una SCP pone el techo; una política de IAM da el permiso",
       pista="Limitar lo que pueden hacer los usuarios y roles de las cuentas miembro = SCP.",
       confusion="Las dos se escriben en JSON y hablan de permitir y negar acciones.",
       regla="Las políticas de control de servicios (SCP) de AWS Organizations fijan el máximo de permisos para los usuarios y roles de las cuentas miembro, incluido su usuario raíz. Por sí mismas no otorgan nada. No afectan a la cuenta de administración. Para hacer una acción, una política de IAM tiene que permitirla y las SCP de cada nivel sobre la cuenta también: basta un nivel que no la permita para bloquearla."),
  dict(dominio=2, tema="Identidad y acceso", id="root-user",
       titulo="El usuario raíz se guarda para unas cuantas tareas",
       pista="En una cuenta independiente, cambiar el correo o la contraseña raíz, o cerrar la cuenta = usuario raíz.",
       confusion="Como el usuario raíz puede hacer todo, parece la identidad natural para administrar.",
       regla="AWS recomienda no usar el usuario raíz en el día a día, protegerlo con autenticación multifactor (MFA) y reservarlo para lo que lo exige. Eso incluye devolverle permisos a un administrador de IAM que se quitó los suyos. En una cuenta que no pertenece a AWS Organizations, también incluye cambiar el correo, la contraseña y las claves de acceso del usuario raíz, y cerrar la cuenta."),

  # ---------- Dominio 3 ----------
  dict(dominio=3, tema="Implementación", id="deployment-models",
       titulo="Para AWS, la nube privada se llama «en las instalaciones»",
       pista="Todo en AWS = en la nube. AWS y centro de datos propio conectados = híbrido. Todo en centro propio = en las instalaciones.",
       confusion="Quien estudió otros temarios busca «pública, privada e híbrida» y no encuentra esos nombres en las opciones.",
       regla="La guía del CLF-C02 nombra tres modelos de implementación: en la nube, híbrido y en las instalaciones (on-premises). En la nube, la aplicación corre por completo ahí. El híbrido conecta recursos de la nube con los que siguen fuera de ella. En las instalaciones, que AWS a veces llama nube privada, la infraestructura está en el centro de datos propio."),
  dict(dominio=3, tema="Implementación", id="console-vs-iac",
       titulo="La consola sirve para una vez; lo que se repite va en código",
       pista="Operación única = consola. Proceso repetible o automatizado = CLI, SDK o infraestructura como código.",
       confusion="Todo se puede hacer desde la consola, así que parece la respuesta segura.",
       regla="La consola de administración sirve para tareas puntuales mediante una interfaz visual. La CLI, los SDK y las API, que son las interfaces que usan los programas, permiten automatizar. Con infraestructura como código, como AWS CloudFormation, el entorno se describe en plantillas y se crea igual cada vez."),
  dict(dominio=3, tema="Infraestructura global", id="region-az-edge",
       titulo="Región, zona de disponibilidad y ubicación periférica son tres niveles distintos",
       pista="Falla un centro de datos = varias AZ. Desastre regional, latencia o soberanía de datos = varias regiones. Contenido cerca del usuario = ubicación periférica.",
       confusion="Las tres son lugares de AWS, y un escenario de alta disponibilidad parece pedir más regiones.",
       regla="Una región es una ubicación física con varias zonas de disponibilidad (AZ), aislada de las demás regiones. Cada AZ comprende uno o más centros de datos con energía, red y conectividad redundantes; las AZ no comparten puntos únicos de falla. Las ubicaciones periféricas acercan el contenido al usuario con Amazon CloudFront."),
  dict(dominio=3, tema="Cómputo", id="ec2-instance-families",
       titulo="La familia de instancia se elige por el recurso que más usa la carga",
       pista="CPU intensiva = optimizada para cómputo. Datos grandes en memoria = optimizada para memoria. Mucha lectura y escritura local = optimizada para almacenamiento.",
       confusion="Todas son máquinas virtuales de EC2, y las letras de cada familia no dicen nada a primera vista.",
       regla="EC2 agrupa sus tipos de instancia en familias según el recurso que optimizan.",
       tabla=[("Balance entre cómputo, memoria y red", "Uso general"),
              ("Lotes, transcodificación, servidores web de alto rendimiento, cómputo de alto rendimiento (HPC)", "Optimizada para cómputo"),
              ("Conjuntos de datos grandes procesados en memoria", "Optimizada para memoria"),
              ("Lectura y escritura secuencial intensa sobre datos locales muy grandes", "Optimizada para almacenamiento"),
              ("Aceleradores de hardware, como GPU", "Computación acelerada")]),
  dict(dominio=3, tema="Cómputo", id="compute-options",
       titulo="ECS, EKS, Fargate y Lambda resuelven capas distintas",
       pista="Kubernetes = EKS. Contenedores sin administrar servidores = Fargate. Código que corre por evento, hasta 15 minutos = Lambda.",
       confusion="Los cuatro corren código sin que el cliente toque hardware, y Fargate funciona con ECS y con EKS.",
       regla="ECS y EKS orquestan contenedores: ECS es el orquestador de AWS y EKS es Kubernetes administrado. Fargate es el motor sin servidor donde corren esos contenedores, sin administrar instancias de EC2. Lambda ejecuta funciones en respuesta a eventos, con un máximo de 15 minutos por ejecución."),
  dict(dominio=3, tema="Cómputo", id="elb-vs-auto-scaling",
       titulo="El balanceador reparte el tráfico; Auto Scaling decide cuántas instancias hay",
       pista="Repartir peticiones entre instancias sanas = Elastic Load Balancing. Agregar o quitar instancias = Auto Scaling.",
       confusion="En los diagramas de arquitectura aparecen juntos, así que parecen un solo servicio.",
       regla="Elastic Load Balancing reparte el tráfico entrante entre varios destinos y deja de enviarlo a los que no están sanos. Amazon EC2 Auto Scaling mantiene el número de instancias y lo ajusta según la demanda; eso es lo que da elasticidad."),
  dict(dominio=3, tema="Bases de datos", id="database-options",
       titulo="Cada modelo de datos tiene su base de datos administrada",
       pista="Relacional = RDS o Aurora. NoSQL sin servidor = DynamoDB. Caché en memoria = ElastiCache. Almacén de datos para análisis = Redshift.",
       confusion="Todas guardan datos, y todas las administra AWS.",
       regla="Primero se decide el modelo de datos. Después, si conviene que AWS administre la base o instalarla en EC2 para controlar el motor y el sistema operativo.",
       tabla=[("Relacional administrada, con varios motores", "Amazon RDS"),
              ("Relacional de AWS, compatible con MySQL y PostgreSQL", "Amazon Aurora"),
              ("NoSQL de clave-valor y de documentos, sin servidor", "Amazon DynamoDB"),
              ("Documentos, compatible con MongoDB", "Amazon DocumentDB"),
              ("Grafos", "Amazon Neptune"),
              ("Caché en memoria", "Amazon ElastiCache"),
              ("Almacén de datos para análisis", "Amazon Redshift"),
              ("Control total del motor y del sistema operativo", "Base de datos instalada en EC2")]),
  dict(dominio=3, tema="Bases de datos", id="dms-vs-sct",
       titulo="DMS mueve los datos; SCT convierte el esquema",
       pista="Motor de origen distinto al de destino = SCT para el esquema y DMS para los datos.",
       confusion="Las dos herramientas aparecen en cualquier migración de base de datos.",
       regla="AWS Database Migration Service copia los datos de una base a otra: puede hacer una migración única o replicar los cambios en curso para mantener sincronizados el origen y el destino. AWS Schema Conversion Tool convierte el esquema y el código de la base cuando el motor cambia, por ejemplo de Oracle a Aurora PostgreSQL."),
  dict(dominio=3, tema="Redes", id="security-group-vs-nacl",
       titulo="El grupo de seguridad cuida la instancia; la ACL de red cuida la subred",
       pista="Regla de denegar o nivel de subred = ACL de red. Solo permitir, a nivel de instancia = grupo de seguridad.",
       confusion="Los dos filtran tráfico con reglas de puertos y direcciones dentro de una red virtual de AWS (VPC).",
       regla="El grupo de seguridad se asocia a las instancias, solo admite reglas de permitir y tiene estado: si una conexión entra permitida, su respuesta sale sin otra regla. La lista de control de acceso (ACL) de red se asocia a la subred, admite reglas de permitir y de denegar, y no tiene estado: la entrada y la salida se permiten por separado."),
  dict(dominio=3, tema="Redes", id="connectivity-options",
       titulo="Para conectar redes con AWS, el servicio depende de qué se conecta",
       pista="Enlace físico dedicado = Direct Connect. Túnel cifrado por internet = Site-to-Site VPN. Personas desde su equipo = Client VPN.",
       confusion="Los cuatro conectan algo con una VPC.",
       regla="Direct Connect evita pasar por internet. Site-to-Site VPN sí viaja por internet, dentro de un túnel IPsec cifrado.",
       tabla=[("Conexión física dedicada y privada desde el centro de datos", "AWS Direct Connect"),
              ("Túnel IPsec cifrado sobre internet entre una red y la VPC", "AWS Site-to-Site VPN"),
              ("Acceso de personas desde su propio dispositivo", "AWS Client VPN"),
              ("Un concentrador que une muchas VPC y redes locales", "AWS Transit Gateway")]),
  dict(dominio=3, tema="Redes", id="edge-services",
       titulo="CloudFront entrega contenido web, Global Accelerator acelera TCP y UDP, y Route 53 resuelve nombres",
       pista="Contenido web en caché cerca del usuario = CloudFront. IP estáticas o tráfico que no es HTTP = Global Accelerator. DNS = Route 53.",
       confusion="Los tres usan la red global de AWS y mejoran lo que percibe el usuario.",
       regla="Amazon CloudFront es una red de entrega de contenido que guarda copias en las ubicaciones periféricas y también acelera contenido dinámico. AWS Global Accelerator da direcciones IP estáticas. Recibe los paquetes TCP o UDP en la ubicación periférica y los lleva a la región por la red de AWS. Amazon Route 53 es el servicio de DNS, el sistema que traduce nombres de dominio en direcciones: registra dominios, enruta el tráfico y revisa la salud de los destinos."),
  dict(dominio=3, tema="Almacenamiento", id="storage-types",
       titulo="Bloque, archivo u objeto: la primera pregunta del almacenamiento",
       pista="Disco de una instancia = EBS. Carpeta compartida entre instancias Linux = EFS; entre instancias Windows = FSx for Windows File Server. Objetos por API = S3.",
       confusion="S3, EBS y EFS guardan datos y los tres tienen una S en el nombre.",
       regla="AWS Backup y Elastic Disaster Recovery se dedican a respaldos y recuperación. Storage Gateway también sirve para respaldar y archivar desde las instalaciones.",
       tabla=[("Disco en bloques persistente para una instancia", "Amazon EBS"),
              ("Disco en bloques temporal, que se pierde al detener o terminar la instancia", "Almacén de instancias"),
              ("Sistema de archivos compartido por muchas instancias, con el protocolo NFS", "Amazon EFS"),
              ("Sistemas de archivos de terceros: Windows File Server, Lustre, NetApp ONTAP, OpenZFS", "Amazon FSx"),
              ("Objetos accesibles por API", "Amazon S3"),
              ("Acceso local, en caché, a almacenamiento en la nube", "AWS Storage Gateway"),
              ("Respaldos centralizados con políticas", "AWS Backup"),
              ("Replicación continua para recuperar servidores tras un desastre", "AWS Elastic Disaster Recovery")]),
  dict(dominio=3, tema="Almacenamiento", id="s3-storage-classes",
       titulo="La clase de S3 se elige por la frecuencia de acceso y por cuánto se puede esperar",
       pista="Acceso impredecible = Intelligent-Tiering. Dato que se puede recrear = One Zone-IA. Puede esperar horas = Glacier Flexible Retrieval o Deep Archive.",
       confusion="Todas las clases guardan el mismo objeto; cambian el precio, las zonas de disponibilidad y el tiempo para recuperarlo.",
       regla="Las políticas de ciclo de vida mueven objetos de una clase a otra con reglas fijas, por ejemplo por antigüedad. Intelligent-Tiering los mueve solo entre sus propios niveles de acceso, dentro de la misma clase, según el acceso real.",
       tabla=[("Acceso frecuente", "S3 Standard"),
              ("Patrón de acceso desconocido o cambiante", "S3 Intelligent-Tiering"),
              ("Acceso poco frecuente, dato que no se puede recrear", "S3 Standard-IA"),
              ("Acceso poco frecuente, dato recreable; una sola AZ", "S3 One Zone-IA"),
              ("Archivo que se lee en milisegundos", "S3 Glacier Instant Retrieval"),
              ("Archivo que se recupera en minutos u horas", "S3 Glacier Flexible Retrieval"),
              ("Archivo que se consulta menos de una vez al año; recuperación en horas", "S3 Glacier Deep Archive")]),
  dict(dominio=3, tema="Análisis", id="analytics-services",
       titulo="Consultar, transformar, procesar, transmitir y visualizar son servicios distintos",
       pista="SQL sobre datos en S3 = Athena. ETL sin servidor = Glue. Datos en tiempo real = Kinesis. Tableros = Quick Sight.",
       confusion="Todos trabajan con datos para análisis, y en una arquitectura real se usan encadenados.",
       regla="Por ejemplo, Kinesis puede recibir los datos, Glue transformarlos, Athena consultarlos y Quick Sight mostrarlos en un tablero.",
       tabla=[("Consultas SQL directas sobre datos en S3, sin servidor", "Amazon Athena"),
              ("Integración de datos y ETL (extraer, transformar y cargar), sin servidor", "AWS Glue"),
              ("Clústeres de big data con Spark o Hadoop", "Amazon EMR"),
              ("Flujos de datos en tiempo real", "Amazon Kinesis"),
              ("Almacén de datos para análisis recurrente", "Amazon Redshift"),
              ("Tableros e inteligencia de negocios", "Amazon Quick Sight")]),
  dict(dominio=3, tema="IA y machine learning", id="ai-services",
       titulo="Los servicios de IA se reconocen por lo que reciben y lo que devuelven",
       pista="Voz a texto = Transcribe. Texto a voz = Polly. Chatbot = Lex. Entrenar un modelo propio = SageMaker AI.",
       confusion="Los nombres no dicen qué hacen, y varios trabajan con texto.",
       regla="Salvo SageMaker AI, estos servicios traen modelos ya entrenados y se usan por API sin saber de machine learning. Algunos, como Comprehend, también permiten entrenar modelos propios.",
       tabla=[("Crear, entrenar y desplegar modelos propios", "Amazon SageMaker AI"),
              ("Chatbots e interfaces conversacionales", "Amazon Lex"),
              ("Texto a voz", "Amazon Polly"),
              ("Voz a texto", "Amazon Transcribe"),
              ("Traducir texto entre idiomas", "Amazon Translate"),
              ("Encontrar entidades, sentimiento y frases clave en un texto", "Amazon Comprehend"),
              ("Extraer texto y datos de documentos escaneados", "Amazon Textract"),
              ("Analizar imágenes y video", "Amazon Rekognition")]),
  dict(dominio=3, tema="Integración de aplicaciones", id="messaging-services",
       titulo="SNS empuja, SQS espera y EventBridge enruta",
       pista="Un mensaje a muchos suscriptores = SNS. Cola que desacopla = SQS. Eventos con reglas = EventBridge. Correo electrónico = SES.",
       confusion="Todos mueven mensajes entre partes de una aplicación.",
       regla="SNS entrega el mensaje a sus suscriptores en cuanto llega. En SQS el mensaje espera en la cola hasta que un consumidor lo pide.",
       tabla=[("Enviar un mensaje a muchos suscriptores", "Amazon SNS"),
              ("Cola de mensajes que desacopla componentes", "Amazon SQS"),
              ("Bus de eventos que enruta con reglas", "Amazon EventBridge"),
              ("Orquestar los pasos de un flujo de trabajo", "AWS Step Functions"),
              ("Enviar y recibir correo electrónico", "Amazon SES"),
              ("Centro de contacto en la nube (hoy se llama Amazon Connect Customer)", "Amazon Connect")]),
  dict(dominio=3, tema="Otras categorías", id="other-services",
       titulo="Escritorios, frontends, IoT y herramientas de desarrollo tienen su propio servicio",
       pista="Escritorio virtual completo = WorkSpaces. Aplicaciones transmitidas, sin escritorio persistente = AppStream 2.0. Seguir una petición entre servicios = X-Ray.",
       confusion="Son servicios que se usan poco al estudiar y sus nombres se parecen entre sí.",
       regla="AppStream 2.0 hoy se llama WorkSpaces Applications, pero la guía del examen usa el nombre anterior.",
       tabla=[("Escritorios virtuales completos", "Amazon WorkSpaces"),
              ("Transmitir aplicaciones sueltas (hoy se llama WorkSpaces Applications)", "Amazon AppStream 2.0"),
              ("Acceso seguro desde el navegador a sitios internos", "Navegador seguro Amazon WorkSpaces"),
              ("Crear y hospedar frontends web y móviles", "AWS Amplify"),
              ("Conectar y administrar dispositivos IoT", "AWS IoT Core"),
              ("Compilar código y correr pruebas", "AWS CodeBuild"),
              ("Entrega continua de principio a fin", "AWS CodePipeline"),
              ("Trazar peticiones entre servicios", "AWS X-Ray")]),

  # ---------- Dominio 4 ----------
  dict(dominio=4, tema="Precios", id="purchase-options",
       titulo="La opción de compra de EC2 depende del compromiso y de la tolerancia a interrupciones",
       pista="Puede interrumpirse = spot. Uso estable por 1 o 3 años = Savings Plans o instancias reservadas. Licencia por socket o núcleo = host dedicado.",
       confusion="Varias opciones ofrecen descuentos y varias hablan de «reservar».",
       regla="Las reservas de capacidad aseguran capacidad pero, por sí solas, se cobran a precio bajo demanda; el descuento llega al combinarlas con Savings Plans o instancias reservadas regionales.",
       tabla=[("Sin compromiso, pago por uso", "Instancias bajo demanda"),
              ("Capacidad sobrante con gran descuento, que AWS puede recuperar", "Instancias de spot"),
              ("Compromiso de gasto por hora a 1 o 3 años; el de cómputo es flexible entre familias, regiones y servicios", "Savings Plans"),
              ("Compromiso con una configuración de instancia a 1 o 3 años", "Instancias reservadas"),
              ("Servidor físico completo, con visibilidad de sockets y núcleos", "Hosts dedicados"),
              ("Hardware aislado para la cuenta, sin control del servidor", "Instancias dedicadas"),
              ("Asegurar capacidad en una AZ", "Reservas de capacidad")]),
  dict(dominio=4, tema="Precios", id="savings-plans-vs-ri",
       titulo="Savings Plans compromete dinero; una instancia reservada compromete una configuración",
       pista="Descuento que también cubre Fargate y Lambda = Compute Savings Plans.",
       confusion="Los dos dan descuento a cambio de un compromiso de uno o tres años.",
       regla="Con Savings Plans, el cliente se compromete a gastar una cantidad por hora. Compute Savings Plans aplica sin importar familia, tamaño, sistema operativo, tenencia o región; también cubre Fargate y Lambda. Una instancia reservada compromete una configuración: la estándar da más descuento y la convertible permite cambiarla por otra. En AWS Organizations, los descuentos se comparten entre las cuentas de la facturación unificada, salvo que se desactive."),
  dict(dominio=4, tema="Precios", id="data-transfer",
       titulo="Meter datos a AWS desde internet no cuesta; sacarlos sí",
       pista="Salida a internet = se cobra. Entrada = en general sin costo.",
       confusion="Parece lógico que mover datos cueste lo mismo en las dos direcciones.",
       regla="La transferencia desde internet hacia AWS no se cobra. La salida hacia internet sí; mientras más se transfiere, menos cuesta cada GB. Dentro de una región, algunos servicios no cobran el tráfico, pero pasar datos entre zonas de disponibilidad se cobra en los dos sentidos. Pasar datos a otra región también genera cargos."),
  dict(dominio=4, tema="Costos", id="cost-tools",
       titulo="Estimar, analizar, avisar y detallar: una herramienta de costos para cada verbo",
       pista="Antes de construir = Calculadora de precios. Gasto pasado y pronóstico = Cost Explorer. Aviso al pasar un umbral = Budgets. Detalle máximo = CUR.",
       confusion="Las cuatro hablan de costos y viven juntas en la consola de facturación.",
       regla="AWS Budgets avisa cuando el gasto real o pronosticado pasa un umbral. Con acciones de presupuesto, también puede aplicar una política de IAM o una SCP, o detener instancias de EC2 o RDS. Esas acciones corren solas o después de una aprobación.",
       tabla=[("Estimar el costo antes de construir", "Calculadora de precios de AWS"),
              ("Ver y analizar el gasto, con pronóstico", "AWS Cost Explorer"),
              ("Recibir una alerta cuando el gasto real o pronosticado pasa un umbral", "AWS Budgets"),
              ("El detalle más completo de costo y uso, entregado en S3", "Informe de costo y uso (CUR)"),
              ("Recomendaciones de tamaño de cómputo según el uso", "AWS Compute Optimizer")]),
  dict(dominio=4, tema="Costos", id="cost-allocation-tags",
       titulo="Una etiqueta no aparece en los reportes de costos hasta activarla",
       pista="Costos por proyecto o por área = etiquetas de asignación de costos, activadas.",
       confusion="Se etiqueta el recurso y se espera verlo de inmediato en el reporte de costos.",
       regla="Hay etiquetas generadas por AWS, como createdBy, y etiquetas definidas por el usuario. Las dos se activan en la consola de Billing and Cost Management; solo entonces AWS las usa para organizar los costos en el reporte de asignación."),
  dict(dominio=4, tema="Cuentas", id="organizations-vs-control-tower",
       titulo="Organizations agrupa las cuentas; Control Tower arma la zona de aterrizaje",
       pista="Facturación unificada y SCP = Organizations. Entorno de varias cuentas listo, con controles = Control Tower.",
       confusion="Los dos administran varias cuentas.",
       regla="AWS Organizations agrupa cuentas en unidades organizativas, unifica la facturación y aplica SCP. AWS Control Tower se apoya en Organizations para montar una zona de aterrizaje con controles ya configurados."),
  dict(dominio=4, tema="Soporte", id="support-plans",
       titulo="Los planes de soporte del examen se distinguen por el TAM y el tiempo de respuesta",
       pista="TAM designado = Enterprise. Grupo de TAM = Enterprise On-Ramp. Teléfono 24/7 = desde Business. Solo web en horario laboral = Developer.",
       confusion="Los planes de pago comparten casi todo, y «Enterprise On-Ramp» suena a una versión menor de Business.",
       regla="La guía del CLF-C02 nombra Developer, Business, Enterprise On-Ramp y Enterprise; el examen sigue esa guía. AWS descontinúa Developer, Business y Enterprise On-Ramp el 1 de enero de 2027; hoy ofrece Business Support+, Enterprise Support y Unified Operations. Basic, sin costo, incluye servicio al cliente, las revisiones centrales de Trusted Advisor y AWS Health.",
       tabla=[("Experimentar o probar; web en horario laboral", "Developer"),
              ("Mínimo recomendado para producción; teléfono, web y chat 24/7; todas las revisiones de Trusted Advisor", "Business"),
              ("Cargas críticas; un grupo de gerentes técnicos de cuenta (TAM); menos de 30 minutos si cae un sistema crítico", "Enterprise On-Ramp"),
              ("Cargas críticas; TAM designado; menos de 15 minutos si cae un sistema crítico", "Enterprise")]),
  dict(dominio=4, tema="Soporte", id="where-to-go",
       titulo="Cada necesidad tiene a quién acudir en AWS",
       pista="Reportar abuso desde recursos de AWS = Trust & Safety. Consultoría de AWS = Professional Services. Software de terceros = Marketplace.",
       confusion="Varias opciones suenan a «pedirle ayuda a AWS».",
       regla="Trust & Safety atiende el abuso que sale de recursos de AWS. Un problema técnico de tu propia cuenta va con AWS Support.",
       tabla=[("Reportar spam, ataques o contenido ilegal que sale de recursos de AWS", "Equipo de confianza y seguridad (Trust & Safety)"),
              ("Consultoría del propio equipo de AWS", "AWS Professional Services"),
              ("Integradores y proveedores de software externos", "Socios de la AWS Partner Network (APN)"),
              ("Comprar software de terceros", "AWS Marketplace"),
              ("Revisiones automáticas de buenas prácticas en la cuenta", "AWS Trusted Advisor"),
              ("Eventos de AWS que afectan tus recursos", "Panel de AWS Health"),
              ("Artículos de AWS con respuestas a preguntas frecuentes", "AWS Knowledge Center"),
              ("Preguntas y respuestas de la comunidad", "AWS re:Post")]),
]


def esc(t):
    return html.escape(t, quote=True)


def tarjeta(d, numero):
    filas = ""
    if d.get("tabla"):
        cuerpo_tabla = "\n".join(
            f'              <tr><th scope="row">{esc(a)}</th><td>{esc(b)}</td></tr>'
            for a, b in d["tabla"])
        filas = f"""
            <table class="mapa">
              <caption class="sr">Qué servicio responde a cada situación</caption>
              <tbody>
{cuerpo_tabla}
              </tbody>
            </table>"""
    return f"""        <article class="diferencia" id="{d['id']}" data-dif="{d['id']}">
          <div class="dif-cabeza">
            <span class="numero">{numero:02d}</span>
            <div class="dif-titular">
              <h3><a href="#{d['id']}">{esc(d['titulo'])}</a></h3>
              <p><strong class="pista">{esc(d['pista'])}</strong></p>
            </div>
            <label class="dominada">
              <input type="checkbox" data-dominada="{d['id']}" aria-label="Marcar como dominada: {esc(d['titulo'])}">
              <span>Dominada</span>
            </label>
          </div>
          <div class="dif-cuerpo">
            <p class="confusion"><span class="rotulo">Dónde se confunde:</span> {esc(d['confusion'])}</p>
            <p class="regla">{esc(d['regla'])}</p>{filas}
            <p class="tema-pie">{esc(d['tema'])}</p>
          </div>
        </article>"""


def bloque_dominio(num, items, inicio):
    cuerpo = "\n".join(tarjeta(d, inicio + i) for i, d in enumerate(items))
    rango = f"{inicio:02d}–{inicio + len(items) - 1:02d}"
    return f"""      <section class="dominio" id="dominio-{num}" data-dominio="{num}">
        <h2>{esc(DOMINIOS[num])} <span class="conteo">{rango}</span></h2>
        <div class="lista-diferencias">
{cuerpo}
        </div>
      </section>"""


bloques, indice, n = [], [], 1
for num in (1, 2, 3, 4):
    items = [d for d in DIFERENCIAS if d["dominio"] == num]
    bloques.append(bloque_dominio(num, items, n))
    enlaces = "\n".join(
        f'              <li><a href="#{d["id"]}" data-indice="{d["id"]}"><span class="indice-num">{n + i:02d}</span> {esc(ETIQUETAS[d["id"]])}</a></li>'
        for i, d in enumerate(items))
    rango = f"{n:02d}–{n + len(items) - 1:02d}"
    indice.append(f"""          <li class="indice-dominio" data-indice-dominio="{num}">
            <a class="indice-dominio-titulo" href="#dominio-{num}">{esc(DOMINIOS[num])} <span class="indice-rango">{rango}</span></a>
            <ul>
{enlaces}
            </ul>
          </li>""")
    n += len(items)

total = len(DIFERENCIAS)
salto = chr(10)
reparto = ", ".join(str(len([d for d in DIFERENCIAS if d["dominio"] == k])) for k in (1, 2, 3, 4))

SITE_URL = "https://cloud-practitioner.sintitulo.dev"

doc = f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Las {total} diferencias clave del CLF-C02 · Cuaderno Cloud Practitioner</title>
<meta name="description" content="Las {total} diferencias clave del examen AWS Certified Cloud Practitioner (CLF-C02): dónde se confunden los servicios, qué pasa en realidad y qué frase decide la respuesta.">
<link rel="canonical" href="{SITE_URL}/diferencias">
<link rel="alternate" hreflang="es-MX" href="{SITE_URL}/diferencias">
<link rel="alternate" hreflang="en-US" href="{SITE_URL}/en/differences">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/diferencias">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cuaderno Cloud Practitioner">
<meta property="og:locale" content="es_MX">
<meta property="og:url" content="{SITE_URL}/diferencias">
<meta property="og:title" content="Las {total} diferencias clave del CLF-C02">
<meta property="og:description" content="Cada par de servicios y conceptos del CLF-C02 tiene una confusión frecuente; aquí encuentras la frase que decide la respuesta y la explicación.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Las {total} diferencias clave del CLF-C02">
<meta name="twitter:description" content="Cada par de servicios y conceptos del CLF-C02 tiene una confusión frecuente; aquí encuentras la frase que decide la respuesta y la explicación.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#fbf9f2">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Cuaderno Cloud Practitioner: ¿CloudTrail o CloudWatch? ¿Shield o WAF? ¿EBS o EFS?">
<meta name="twitter:image" content="{SITE_URL}/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Work+Sans:wght@400;600;700&display=swap">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>

<header class="cabecera">
  <div class="limite pad barra">
    <a class="marca-sitio" href="/">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF9900" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H18a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H5.5A1.5 1.5 0 0 1 4 18.5z"></path><path d="M4 16.5h15"></path><path d="M8 3v17"></path></svg>
      Cuaderno Cloud Practitioner
    </a>
    <nav class="menu" aria-label="Secciones">
      <a class="nav-cta" href="/practica">Practicar</a>
      <a href="/diferencias" aria-current="page">Diferencias</a>
      <a href="/metodo">Método</a>
      <a href="/examen"><span class="largo">Día del examen</span><span class="corto">Examen</span></a>
      <a class="idioma" href="/en/differences" hreflang="en" lang="en"><span class="largo">English</span><span class="corto">EN</span></a>
    </nav>
  </div>
</header>

<main id="contenido" tabindex="-1" class="limite pad" style="padding-top: 64px">

  <div class="encabezado-diferencias">
    <h1>Las {total} diferencias del CLF&#8209;C02</h1>
    <p class="subtitulo">¿CloudTrail o CloudWatch? ¿Shield o WAF? Una frase para distinguir cada par.</p>
    <p class="prosa" style="margin-top: 20px">Una opción equivocada puede sonar convincente porque nombra un servicio real. Cada diferencia te muestra la pista que decide la respuesta, dónde surge la confusión y qué pasa en realidad; puedes leerlas en unos 25 minutos o repasar solo las pistas en siete.</p>
    <div class="controles">
      <button type="button" class="cta secundaria" id="alternar-pistas" aria-pressed="false">Solo pistas</button>
      <span class="meta" id="estado-dominadas" role="status"></span>
      <span class="meta">Marca las que dominas para quitarlas de la hoja de pistas.</span>
    </div>
  </div>

  <div class="marco-diferencias">
    <nav class="indice-lateral" aria-label="Índice de diferencias">
      <details class="indice-caja" id="indice-caja" open>
        <summary>Índice · {total} diferencias</summary>
        <ul>
{salto.join(indice)}
        </ul>
      </details>
    </nav>

    <div class="columna-diferencias">
{salto.join(bloques)}
    </div>
  </div>

</main>

<footer class="pie-sitio">
  <div class="limite pad">
    <div class="pie-rejilla">
      <div class="pie-columna">
        <p class="densa">Estas {total} diferencias salen de cruzar la guía oficial del examen, la documentación de cada servicio y lo que reporta quien ya lo presentó. Ninguna reproduce preguntas del examen ni preguntas de práctica oficiales de AWS.</p>
        <p class="nota">practicarlas <span aria-hidden="true">→</span></p>
      </div>
      <nav class="pie-columna pie-menu" aria-label="Secciones del sitio">
        <h2>El cuaderno</h2>
        <a href="/practica">Práctica</a>
        <a href="/diferencias">Diferencias</a>
        <a href="/metodo">Método</a>
        <a href="/examen"><span class="largo">Día del </span>examen</a>
      </nav>
      <div class="pie-columna pie-menu">
        <h2>Quién lo hizo</h2>
        <a href="https://www.santiagos.mx/es/inicio">Santiago García Arellano</a>
        <a href="https://github.com/Santiago-mnd">GitHub</a>
        <a href="https://www.linkedin.com/in/santiago-garcia-arellano/">LinkedIn</a>
        <a href="https://github.com/sponsors/Santiago-mnd">Apoyar el proyecto</a>
      </div>
    </div>
    <div class="pie-letra-chica">
      <p class="sello"><strong>Aviso.</strong> Cuaderno Cloud Practitioner es un proyecto personal y gratuito; no está afiliado a Amazon Web Services ni tiene su patrocinio o aval. AWS, Amazon Web Services y AWS Certified Cloud Practitioner son marcas de Amazon.com, Inc. o sus filiales. Este material te ayuda a estudiar, pero no garantiza que apruebes. Las preguntas de práctica son propias del sitio; ninguna proviene del examen real. Preparé parte del contenido con ayuda de IA y lo revisé contra la documentación oficial; si encuentras un error, avísame en <a href="https://github.com/Santiago-mnd">GitHub</a>.</p>
      <p class="sello">Verifiqué el contenido en septiembre de 2026 contra la guía oficial del CLF-C02 y la documentación de AWS. Si cambia el temario, comprueba la información actual en docs.aws.amazon.com.</p>
      <p class="sello">No necesitas cuenta ni correo; el sitio tampoco usa cookies. La analítica reúne páginas vistas, país y navegador, sin crear perfiles ni seguirte entre sitios. Tu avance de estudio se queda en tu navegador.</p>
      <p class="sello">Este es el segundo recurso libre de sintitulo.dev; habrá más.</p>
    </div>
  </div>
</footer>

<script src="js/cabecera.js" defer></script>
<script src="js/diferencias.js" defer></script>
<script>
  window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
</script>
<script defer src="https://va.vercel-scripts.com/v1/script.js" data-sdkn="@vercel/analytics" data-sdkv="1"></script>
</body>
</html>
"""

pathlib.Path("diferencias.html").write_text(doc, encoding="utf-8")
print(f"diferencias.html: {total} diferencias en 4 dominios ({reparto})")
