#!/usr/bin/env python3
"""Genera diferencias.html a partir de la lista de diferencias clave.

Cada entrada es un dict:
  dominio    1, 2 o 3 (dominios del examen)
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
    1: "Conceptos de nube",
    2: "Arquitectura y servicios",
    3: "Administración y gobernanza",
}


ETIQUETAS = {
    "sql-database-paas": "SQL Database es PaaS",
    "infraestructura-iaas": "La infraestructura es IaaS",
    "frontera-iaas-paas": "¿Quién parcha el SO?",
    "paas-vs-saas": "PaaS o SaaS",
    "modelo-vs-tipo": "Modelo o tipo de servicio",
    "opex-vs-governance": "OpEx o governance",
    "confiabilidad-vs-disponibilidad": "Confiabilidad o disponibilidad",
    "agilidad-vs-elasticidad": "Agilidad o elasticidad",
    "geografia-vs-desastres": "Geografía o desastres",
    "nube-publica": "Nube pública",
    "nube-privada": "Nube privada",
    "paas-so-microsoft": "El SO en PaaS",
    "scale-sets-vs-aks": "Scale Sets, AKS o set",
    "zona-de-una-vm": "La zona de una VM",
    "zone-set-pair": "Zone, set y pair",
    "cold-vs-archive": "Cold o Archive",
    "archive-restricciones": "Dónde cabe Archive",
    "files-vs-blob": "Files o Blob",
    "que-conecta-con-que": "Qué conecta con qué",
    "capas-vs-zero-trust": "Capas o Zero Trust",
    "acceso-condicional-vs-rbac": "Acceso condicional o RBAC",
    "sso-vs-mfa": "SSO o MFA",
    "entra-no-hace-dns": "Entra ID no hace DNS",
    "locks-management-group": "Locks y management groups",
    "lock-vs-rbac": "Lock o RBAC",
    "tenant-vs-suscripcion": "Tenant o suscripción",
    "un-solo-resource-group": "Un solo resource group",
    "advisor-no-es-todo": "Advisor y su familia",
    "cloud-shell-vs-arc": "Cloud Shell o Arc",
    "budget-avisa": "El budget solo avisa",
    "estimar-analizar-recomendar": "Estimar, analizar, recomendar",
    "cost-management-no-tco": "Cost Management y el TCO",
    "ingress-egress": "Entrada y salida de datos",
    "tags-para-costos": "Tags para costos",
}

DIFERENCIAS = [
  # ---------- Dominio 1 ----------
  dict(dominio=1, tema="Tipos de servicio", id="sql-database-paas",
       titulo="Azure SQL Database siempre es PaaS",
       pista="«Administrada» o «Azure SQL Database» = PaaS. «Dentro de una VM» = IaaS.",
       confusion="El nombre suena a servidor de base de datos, y quien ha administrado SQL Server lo asocia con una máquina que alguien mantiene.",
       regla="Es un motor de base de datos administrado: Microsoft opera el servidor, el sistema operativo, los parches y los respaldos. Solo se aportan tablas, consultas y datos. SQL Server instalado dentro de una máquina virtual sí es IaaS. Cosmos DB va en la misma bolsa que Azure SQL."),
  dict(dominio=1, tema="Tipos de servicio", id="infraestructura-iaas",
       titulo="La infraestructura es IaaS, aunque nadie instale cables",
       pista="VM, VNet y disco = IaaS. App Service, Azure SQL y Functions = PaaS.",
       confusion="Como una red virtual se crea con unos clics y no hay hardware de por medio, parece una plataforma administrada.",
       regla="Las máquinas virtuales, las redes virtuales, los discos y los balanceadores son la capa de infraestructura: el cliente los diseña y los administra. PaaS empieza un piso más arriba, cuando la plataforma ya está lista para recibir código o datos."),
  dict(dominio=1, tema="Tipos de servicio", id="frontera-iaas-paas",
       titulo="La frontera entre IaaS y PaaS es el sistema operativo",
       pista="La pregunta que decide: ¿quién parcha el sistema operativo?",
       confusion="En los dos modelos se construye algo encima, así que «construir» no distingue nada.",
       regla="Si el cliente instala y parcha el sistema operativo, es IaaS, y eso incluye a los Scale Sets. Si Microsoft lo parcha, es PaaS."),
  dict(dominio=1, tema="Tipos de servicio", id="paas-vs-saas",
       titulo="PaaS y SaaS se separan por quién escribe la aplicación",
       pista="Si alguien escribe código o diseña tablas, ya no es SaaS.",
       confusion="Los dos evitan administrar servidores, así que suenan intercambiables.",
       regla="PaaS es una herramienta para construir encima: el código y las tablas son del cliente. SaaS es un producto terminado que solo se usa, como Microsoft 365, Teams, Outlook o Power BI."),
  dict(dominio=1, tema="Tipos de servicio", id="modelo-vs-tipo",
       titulo="Modelo de implementación y tipo de servicio son ejes distintos",
       pista="On-premises conectado con Azure = nube híbrida, aunque el escenario hable de VMs.",
       confusion="Un escenario menciona máquinas virtuales y la respuesta parece ser IaaS, aunque la pregunta sea sobre dónde vive la solución.",
       regla="El modelo responde dónde: pública, privada, híbrida o multinube. El tipo de servicio responde cuánto administra el cliente: IaaS, PaaS o SaaS. Son independientes entre sí."),
  dict(dominio=1, tema="Beneficios", id="opex-vs-governance",
       titulo="Pagar por uso es OpEx; governance es otra cosa",
       pista="Sin inversión inicial = OpEx. Reglas y estándares = governance.",
       confusion="La palabra control aparece en las dos ideas, y quien decide el gasto también parece estar gobernando.",
       regla="CapEx es la inversión inicial en infraestructura. OpEx es pagar conforme se usa, y la nube es OpEx por naturaleza. Governance son reglas y cumplimiento sobre lo que puede existir: Policy, locks, tags y RBAC."),
  dict(dominio=1, tema="Beneficios", id="confiabilidad-vs-disponibilidad",
       titulo="Confiabilidad es recuperarse; alta disponibilidad es no caerse",
       pista="Recuperarse de fallas = confiabilidad.",
       confusion="Distribuir una aplicación en varias regiones suena directamente a disponibilidad.",
       regla="La confiabilidad es la capacidad de recuperarse de una falla y seguir operando. La alta disponibilidad es mantenerse en línea el mayor tiempo posible, y se mide con el SLA. La agilidad es desplegar rápido, y la previsibilidad es que el costo y el rendimiento sean esperables."),
  dict(dominio=1, tema="Beneficios", id="agilidad-vs-elasticidad",
       titulo="Agilidad es desplegar rápido; elasticidad es ajustarse solo",
       pista="Rápido de implementar = agilidad. Según la demanda = elasticidad.",
       confusion="Las dos suenan a rapidez y a nube moderna.",
       regla="La agilidad es la rapidez para crear o cambiar recursos nuevos. La elasticidad es que lo ya desplegado crezca y se reduzca según la demanda."),
  dict(dominio=1, tema="Beneficios", id="geografia-vs-desastres",
       titulo="Distribución geográfica y recuperación ante desastres no son lo mismo",
       pista="Cerca de los usuarios = distribución geográfica. Restaurar tras un desastre = recuperación ante desastres.",
       confusion="Las dos hablan de tener la solución en varios lugares del mundo.",
       regla="La distribución geográfica busca estar cerca de los usuarios para dar mejor rendimiento. La recuperación ante desastres busca restaurar el servicio después de una catástrofe, con respaldos y conmutación a otra región. GRS es redundancia de almacenamiento, no distribución."),
  dict(dominio=1, tema="Modelos de nube", id="nube-publica",
       titulo="La nube pública no incluye hardware propio del cliente",
       pista="Si el hardware es de la organización, no es pública.",
       confusion="El escenario menciona servidores y centros de datos, y eso se asocia con infraestructura propia.",
       regla="La nube pública es del proveedor y está disponible para cualquiera. Hardware propio o de uso exclusivo describe una nube privada."),
  dict(dominio=1, tema="Modelos de nube", id="nube-privada",
       titulo="En la nube privada alguien compró el hardware",
       pista="Privada: se compra y se controla. Pública: se renta y se escala rápido.",
       confusion="Como se contrata y se usa de forma parecida a la pública, se le atribuyen sus ventajas: aprovisionamiento rápido y pago por uso.",
       regla="Una nube privada es infraestructura de uso exclusivo de una organización, en su propio centro de datos o hospedada por un tercero. Alguien adquirió ese hardware, y la organización mantiene el control de los recursos y de la seguridad."),
  dict(dominio=1, tema="Responsabilidad compartida", id="paas-so-microsoft",
       titulo="En PaaS el sistema operativo es de Microsoft",
       pista="Los datos y las identidades nunca dejan de ser del cliente.",
       confusion="Como en PaaS el cliente conserva bastante control sobre su aplicación, parece que también conserva el sistema operativo.",
       regla="En PaaS el proveedor cubre lo físico y además el sistema operativo. Los datos, las cuentas, los accesos y los dispositivos son siempre responsabilidad del cliente, en los tres modelos."),

  # ---------- Dominio 2 ----------
  dict(dominio=2, tema="Cómputo", id="scale-sets-vs-aks",
       titulo="Scale Sets escalan máquinas; AKS orquesta contenedores",
       pista="Máquinas idénticas que escalan = Scale Set. Contenedores orquestados = AKS.",
       confusion="Los dos crecen solos y reponen lo que se cae, así que la diferencia parece de tamaño y no de naturaleza.",
       regla="Cada uno resuelve un problema distinto, aunque los tres suenen a que nada se caiga.",
       tabla=[("Que varias máquinas no caigan juntas", "Availability set"),
              ("Agregar y quitar máquinas idénticas según la carga", "Virtual Machine Scale Set"),
              ("Coordinar muchos contenedores", "Azure Kubernetes Service")]),
  dict(dominio=2, tema="Cómputo", id="zona-de-una-vm",
       titulo="La availability zone de una máquina virtual se fija al crearla",
       pista="El portal hace casi todo, pero no mueve de zona una VM existente.",
       confusion="El portal permite cambiar casi cualquier propiedad, así que la zona parece una más.",
       regla="La zona se elige al crear la máquina. Para cambiarla hay que recrearla o migrarla."),
  dict(dominio=2, tema="Regiones", id="zone-set-pair",
       titulo="Zone, set y region pair protegen de cosas distintas",
       pista="Rack = set. Centro de datos = zone. Región = pair.",
       confusion="Las tres suenan a alta disponibilidad, y en el examen aparecen juntas como opciones.",
       regla="La alta disponibilidad es el concepto y se pacta en el SLA; lo demás son formas concretas de repartir el riesgo.",
       tabla=[("Falla un rack o hay un reinicio por mantenimiento", "Availability set"),
              ("Cae un centro de datos completo", "Availability zone"),
              ("Cae la región entera", "Region pair")]),
  dict(dominio=2, tema="Storage", id="cold-vs-archive",
       titulo="Cold sigue en línea; Archive no",
       pista="Si la pregunta dice que puede tardar horas, es Archive.",
       confusion="Los dos guardan datos que casi nunca se consultan, los dos son baratos y los dos suenan igual de fríos.",
       regla="Hot, Cool y Cold están en línea: se leen en milisegundos. Archive está fuera de línea y hay que rehidratarlo a un tier en línea antes de leerlo, lo que puede tardar hasta 15 horas según la prioridad que se elija. Entre más frío el tier, más barato guardar y más caro leer. Cada uno tiene un mínimo de permanencia, y salirse antes genera un cargo prorrateado.",
       tabla=[("Datos en uso, se leen y escriben seguido", "Hot · sin mínimo"),
              ("Poco frecuentes, pero disponibles al instante", "Cool · 30 días"),
              ("Raros, y aun así se necesitan rápido", "Cold · 90 días"),
              ("Casi nunca, y se puede esperar horas", "Archive · 180 días")]),
  dict(dominio=2, tema="Storage", id="archive-restricciones",
       titulo="Archive no sirve para todo ni se activa en cualquier cuenta",
       pista="Archive: por blob, nunca por defecto, y solo en LRS, GRS o RA-GRS.",
       confusion="Si Archive es el más barato, parece razonable ponerlo como valor por defecto de la cuenta y olvidarse.",
       regla="El tier por defecto de una storage account solo puede ser Hot, Cool o Cold; Archive se asigna blob por blob. Además, Archive solo está disponible en cuentas con redundancia LRS, GRS o RA-GRS, no en ZRS ni GZRS, y los tiers de acceso aplican únicamente a block blobs."),
  dict(dominio=2, tema="Storage", id="files-vs-blob",
       titulo="Azure Files se monta; Blob se consume por URL",
       pista="Carpeta compartida o unidad montada = Azure Files.",
       confusion="Los dos guardan archivos, así que cualquiera parece servir.",
       regla="Azure Files entrega recursos compartidos que se montan como unidad de red con SMB o NFS. Blob guarda objetos no estructurados y se consume por HTTP o REST. Los niveles Hot, Cool, Cold y Archive son exclusivos de Blob."),
  dict(dominio=2, tema="Redes", id="que-conecta-con-que",
       titulo="Cada conexión tiene su servicio",
       pista="Red con red = peering. Servicio con red = endpoint. Oficina con Azure = VPN o ExpressRoute.",
       confusion="Peering, service endpoint, private endpoint, VPN y ExpressRoute se describen todos como conectar, y las opciones aparecen mezcladas.",
       regla="La pregunta útil es qué dos cosas se están uniendo.",
       tabla=[("Dos redes virtuales entre sí", "VNet peering"),
              ("Un servicio de Azure con una red virtual", "Service endpoint o private endpoint"),
              ("Una oficina con Azure, cifrado por internet", "VPN Gateway"),
              ("Una oficina con Azure, línea privada dedicada", "ExpressRoute")]),
  dict(dominio=2, tema="Identidad y seguridad", id="capas-vs-zero-trust",
       titulo="Defense-in-depth son capas; Zero Trust es una filosofía",
       pista="Capas = defense-in-depth. Nunca confiar y siempre verificar = Zero Trust.",
       confusion="Las dos describen seguridad seria y aparecen juntas en las opciones.",
       regla="Defense-in-depth organiza la protección en capas (física, identidad, perímetro, red, cómputo, aplicación y datos) con los datos al centro. Zero Trust son tres principios: verificar explícitamente, dar el mínimo privilegio y asumir que ya hubo una brecha."),
  dict(dominio=2, tema="Identidad y seguridad", id="acceso-condicional-vs-rbac",
       titulo="El acceso condicional decide cómo se entra; RBAC, qué se puede hacer",
       pista="«Solo desde…» o «únicamente cuando…» = acceso condicional.",
       confusion="Restringir el acceso a ciertas aplicaciones suena a permisos, y los permisos suenan a RBAC.",
       regla="El acceso condicional evalúa señales del inicio de sesión (usuario, ubicación, dispositivo, aplicación cliente y riesgo) y decide si deja pasar, pide MFA o bloquea. Son políticas que alguien configura, no un comportamiento automático. RBAC define qué puede hacer una identidad con los recursos una vez dentro."),
  dict(dominio=2, tema="Identidad y seguridad", id="sso-vs-mfa",
       titulo="SSO es una sesión para muchas apps; MFA es una prueba adicional",
       pista="Una sola vez = SSO. Prueba adicional = MFA.",
       confusion="Las dos mejoran el inicio de sesión y suelen configurarse juntas.",
       regla="El inicio de sesión único permite autenticarse una vez y entrar a varias aplicaciones. La autenticación multifactor exige dos o más factores de categorías distintas: algo que se sabe, algo que se tiene y algo que se es. Dos contraseñas no son MFA."),
  dict(dominio=2, tema="Identidad y seguridad", id="entra-no-hace-dns",
       titulo="Microsoft Entra ID no resuelve nombres de dominio",
       pista="Entra = personas. DNS = nombres y direcciones.",
       confusion="Entra ID aparece como el servicio central de identidad, así que parece cubrir todo lo que suene a red.",
       regla="Entra ID administra identidades: autenticación, inicio de sesión único, MFA, acceso condicional e identidades externas. La resolución de nombres a direcciones IP es Azure DNS, otro servicio."),

  # ---------- Dominio 3 ----------
  dict(dominio=3, tema="Jerarquía", id="locks-management-group",
       titulo="Los resource locks no existen en management groups",
       pista="Management group = reglas, no candados.",
       confusion="Como todo lo demás se hereda hacia abajo desde el management group, parece el lugar natural para poner un candado.",
       regla="Los locks se aplican en suscripción, resource group o recurso, y desde ahí se heredan. Un management group agrupa suscripciones: ahí van Azure Policy y RBAC."),
  dict(dominio=3, tema="Jerarquía", id="lock-vs-rbac",
       titulo="Un lock aplica a todos; RBAC aplica a alguien",
       pista="Si la pregunta nombra a una persona o a un equipo, es RBAC.",
       confusion="Ambos impiden que se borre algo, así que cualquiera de los dos parece resolver la pregunta.",
       regla="El lock protege el recurso frente a cualquiera, incluido un Owner. RBAC define qué puede hacer una persona o un grupo en un ámbito determinado."),
  dict(dominio=3, tema="Jerarquía", id="tenant-vs-suscripcion",
       titulo="Las cuentas de usuario viven en el tenant, no en la suscripción",
       pista="Tenant = personas. Suscripción = factura. Resource group = contenedor.",
       confusion="La suscripción se siente como la cuenta de Azure, así que ahí parecerían vivir los usuarios.",
       regla="Dentro de una suscripción se crean resource groups y recursos. Los management groups están por encima. Los usuarios y grupos viven en el tenant de Microsoft Entra ID, que es un eje aparte en el que la suscripción confía."),
  dict(dominio=3, tema="Jerarquía", id="un-solo-resource-group",
       titulo="Un recurso vive en un solo resource group",
       pista="Muchas tags, un solo resource group.",
       confusion="Como un recurso puede tener varias etiquetas y aparecer en varios reportes, parece que puede pertenecer a varios grupos.",
       regla="Cada recurso pertenece a exactamente un resource group. Se puede mover, pero nunca está en dos a la vez. Para agrupar por otro criterio se usan tags."),
  dict(dominio=3, tema="Herramientas", id="advisor-no-es-todo",
       titulo="Azure Advisor no es la respuesta a todo lo que suene a consejo",
       pista="Recomendación = Advisor. Caída de Azure = Service Health. Aplicación lenta = Application Insights.",
       confusion="Advisor aparece como la herramienta que revisa y sugiere, y eso encaja con casi cualquier pregunta de operación.",
       regla="Seis herramientas distintas se reparten el trabajo que suele atribuirse a una sola.",
       tabla=[("Recomendaciones sobre los recursos propios", "Azure Advisor"),
              ("Fallas y mantenimiento de la plataforma", "Azure Service Health"),
              ("Si un recurso concreto está afectado por Azure", "Resource Health"),
              ("Rendimiento y errores de una aplicación", "Application Insights"),
              ("Métricas, logs y alertas", "Azure Monitor"),
              ("Postura de seguridad y amenazas", "Microsoft Defender for Cloud")]),
  dict(dominio=3, tema="Herramientas", id="cloud-shell-vs-arc",
       titulo="Cloud Shell es una terminal; Azure Arc conecta lo que está fuera",
       pista="Administrar algo que está fuera de Azure, desde Azure = Arc.",
       confusion="Cloud Shell parece la herramienta general para administrar cualquier cosa desde Azure.",
       regla="Cloud Shell es una terminal en el navegador, con la CLI y PowerShell listas y la sesión ya iniciada. Azure Arc incorpora a Azure servidores y servicios que viven fuera, en un centro de datos propio o en otra nube, para aplicarles Policy, RBAC y monitoreo."),
  dict(dominio=3, tema="Costos", id="budget-avisa",
       titulo="Un presupuesto avisa; por sí solo no apaga nada",
       pista="Budget = semáforo, no llave de paso.",
       confusion="Si se configura un límite de gasto, parece lógico que al llegar al tope Azure detenga los recursos.",
       regla="Los budgets de Cost Management envían alertas al alcanzar los porcentajes definidos. Los recursos siguen corriendo y el gasto sigue creciendo, salvo que alguien automatice una acción aparte."),
  dict(dominio=3, tema="Costos", id="estimar-analizar-recomendar",
       titulo="Estimar, analizar y recomendar son tres herramientas distintas",
       pista="Antes de crear = calculator. Lo que ya corre = Cost Management. Consejo = Advisor.",
       confusion="Las tres hablan de dinero y todas viven en el portal.",
       regla="Lo que separa a las tres es el momento en el que se usan.",
       tabla=[("Calcular el costo de algo que aún no existe", "Pricing calculator"),
              ("Analizar el gasto real, con presupuestos y alertas", "Cost Management"),
              ("Recibir sugerencias para gastar menos", "Azure Advisor")]),
  dict(dominio=3, tema="Costos", id="cost-management-no-tco",
       titulo="Cost Management no calcula el costo total de propiedad",
       pista="Estimar lo que no existe = pricing calculator.",
       confusion="Suena a la herramienta de dinero por excelencia, así que parece que también proyecta escenarios.",
       regla="El TCO, o Total Cost of Ownership, es todo lo que cuesta sostener algo: hardware, energía, espacio, licencias y personal. Cost Management solo trabaja con gasto real y su pronóstico. El TCO calculator, además, ya no forma parte del temario vigente."),
  dict(dominio=3, tema="Costos", id="ingress-egress",
       titulo="Entrar datos no se cobra; sacarlos sí",
       pista="Como el estacionamiento: se paga al salir.",
       confusion="Como la nube cobra por casi todo, se asume que el tráfico se cobra en ambos sentidos.",
       regla="El tráfico de entrada a Azure normalmente no tiene costo. El de salida, hacia internet o hacia otra región, sí se cobra. Lo que se queda dentro de la misma región suele ser gratuito."),
  dict(dominio=3, tema="Costos", id="tags-para-costos",
       titulo="Los costos por área se reportan con tags",
       pista="Costos por departamento o proyecto = tags.",
       confusion="Reorganizar los recursos en grupos por departamento parece la forma natural de separar gastos.",
       regla="Las tags son pares nombre-valor que permiten filtrar y reportar costos sin mover nada de lugar. No se heredan del resource group, salvo que una Policy lo imponga."),
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
for num in (1, 2, 3):
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
reparto = ", ".join(str(len([d for d in DIFERENCIAS if d["dominio"] == k])) for k in (1, 2, 3))

doc = f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Las {total} diferencias clave del AZ-900 · Cuaderno AZ-900</title>
<meta name="description" content="Las {total} diferencias clave del examen Microsoft AZ-900: dónde se confunden, qué pasa en realidad y la frase que decide la respuesta.">
<link rel="canonical" href="https://az900.sintitulo.dev/diferencias">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cuaderno AZ-900">
<meta property="og:locale" content="es_MX">
<meta property="og:url" content="https://az900.sintitulo.dev/diferencias">
<meta property="og:title" content="Las 34 diferencias clave del AZ-900">
<meta property="og:description" content="Dónde se confunde cada par de conceptos del examen AZ-900, qué pasa en realidad y la frase que decide la respuesta.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Las 34 diferencias clave del AZ-900">
<meta name="twitter:description" content="Dónde se confunde cada par de conceptos del examen AZ-900, qué pasa en realidad y la frase que decide la respuesta.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#fbf9f2">
<meta property="og:image" content="https://az900.sintitulo.dev/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Cuaderno AZ-900: ¿un lock o un permiso? ¿Cold o Archive? ¿PaaS o SaaS?">
<meta name="twitter:image" content="https://az900.sintitulo.dev/og.png">
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
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1a6b52" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H18a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H5.5A1.5 1.5 0 0 1 4 18.5z"></path><path d="M4 16.5h15"></path><path d="M8 3v17"></path></svg>
      Cuaderno AZ&#8209;900
    </a>
    <nav class="menu" aria-label="Secciones">
      <a class="nav-cta" href="/practica">Practicar</a>
      <a href="/diferencias" aria-current="page">Diferencias</a>
      <a href="/metodo">Método</a>
      <a href="/examen"><span class="largo">Día del examen</span><span class="corto">Examen</span></a>
    </nav>
  </div>
</header>

<main id="contenido" tabindex="-1" class="limite pad" style="padding-top: 64px">

  <div class="encabezado-diferencias">
    <h1>Las {total} diferencias del AZ&#8209;900</h1>
    <p class="subtitulo">¿Un lock o un permiso? ¿Cold o Archive? Resueltas una por una.</p>
    <p class="prosa" style="margin-top: 20px">La respuesta equivocada convence hasta que alguien explica por qué falla. De cada una: la pista que decide la respuesta, dónde se confunde y qué pasa en realidad. Se leen en unos veinte minutos; en la vista de pistas, en cinco.</p>
    <div class="controles">
      <button type="button" class="cta secundaria" id="alternar-pistas" aria-pressed="false">Solo pistas</button>
      <span class="meta" id="estado-dominadas" role="status"></span>
      <span class="meta">Marca las que ya dominas y desaparecen de la hoja de pistas.</span>
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
        <p class="densa">Son {total} porque salieron de preparar el examen: los errores que se cometieron al estudiar y los puntos donde el material oficial queda ambiguo. Ninguna reproduce preguntas del examen ni del Practice Assessment de Microsoft.</p>
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
      <p class="sello">Contenido verificado contra la guía oficial de Microsoft en septiembre de 2026, con los <em>skills measured</em> del 20 de julio de 2026. Si el temario cambia, esta fecha se queda atrás: compruébalo en learn.microsoft.com.</p>
      <p class="sello">Sin cuentas, sin correo y sin cookies. La analítica de visitas es agregada: cuenta páginas vistas, país y navegador, sin perfiles ni seguimiento entre sitios. Tu avance de estudio nunca sale de tu navegador.</p>
      <p class="sello">El primero de una serie de recursos libres que irán apareciendo en sintitulo.dev.</p>
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
print(f"diferencias.html: {total} diferencias en 3 dominios ({reparto})")
