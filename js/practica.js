// Práctica: diagnóstico, repaso espaciado, simulacro y estudio por tema.
// Todo el avance vive en el navegador de quien estudia. No hay servidor ni cuentas.

const CLAVE = "az900:practica:avance";
const INTERVALOS = [0, 10 * 60e3, 8 * 3600e3, 24 * 3600e3, 72 * 3600e3];
const PESO_CAJA = [0, 0.25, 0.5, 0.8, 1];
const CUPO_SIMULACRO = { 1: 8, 2: 12, 3: 10 };

// Enlace de una pregunta a la diferencia que la explica, cuando existe.
const DIFERENCIA_DE_TEMA = {
  tipos: "frontera-iaas-paas",
  resp: "paas-so-microsoft",
  nube: "nube-privada",
  precio: "opex-vs-governance",
  benef: "agilidad-vs-elasticidad",
  geo: "zone-set-pair",
  jer: "tenant-vs-suscripcion",
  comp: "scale-sets-vs-aks",
  red: "que-conecta-con-que",
  stor: "cold-vs-archive",
  mover: "files-vs-blob",
  ident: "acceso-condicional-vs-rbac",
  costo: "estimar-analizar-recomendar",
  gob: "locks-management-group",
  admin: "cloud-shell-vs-arc",
  monitor: "advisor-no-es-todo"
};

const panel = document.getElementById("panel");
const resumenAvance = document.getElementById("resumen-avance");

let avance = cargar();
let sesion = null;

function cargar() {
  const vacio = { items: {}, historial: [], actualizado: 0 };
  try {
    const crudo = localStorage.getItem(CLAVE);
    if (!crudo) return vacio;
    return Object.assign(vacio, JSON.parse(crudo));
  } catch (e) {
    return vacio;
  }
}

function guardar() {
  avance.actualizado = Date.now();
  try {
    localStorage.setItem(CLAVE, JSON.stringify(avance));
  } catch (e) {
    // sin almacenamiento la práctica funciona, pero no recuerda entre visitas
  }
}

const estado = (id) => avance.items[id] || { caja: 0, ok: 0, ko: 0, visto: 0, toca: 0 };
const dominioDe = (p) => TEMAS[p.tp].d;
const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

function barajar(lista) {
  const a = lista.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function registrar(p, correcta) {
  const it = estado(p.id);
  if (correcta) {
    it.ok++;
    it.caja = Math.min(it.caja + 1, 4);
    it.toca = Date.now() + INTERVALOS[it.caja];
  } else {
    it.ko++;
    it.caja = 0;
    it.toca = Date.now() + 2 * 60e3;
  }
  it.visto = Date.now();
  avance.items[p.id] = it;
  guardar();
}

function aciertosDominio(d) {
  const qs = PREGUNTAS.filter((p) => dominioDe(p) === d && avance.items[p.id]);
  const ok = qs.reduce((s, p) => s + (estado(p.id).ok > 0 && estado(p.id).caja > 0 ? 1 : 0), 0);
  const intentos = qs.reduce((s, p) => s + estado(p.id).ok + estado(p.id).ko, 0);
  const buenos = qs.reduce((s, p) => s + estado(p.id).ok, 0);
  return {
    vistas: qs.length,
    total: PREGUNTAS.filter((p) => dominioDe(p) === d).length,
    pct: intentos ? Math.round((buenos / intentos) * 100) : null,
    dominadas: ok
  };
}

// ----- selección de preguntas por modo -----

function rondaDiagnostico(n = 20) {
  const cupo = { 1: 6, 2: 8, 3: 6 };
  let lista = [];
  for (const d of [1, 2, 3]) {
    lista = lista.concat(barajar(PREGUNTAS.filter((p) => dominioDe(p) === d)).slice(0, cupo[d]));
  }
  return barajar(lista).slice(0, n);
}

function rondaRepaso(n = 15) {
  const ahora = Date.now();
  const vistas = PREGUNTAS
    .filter((p) => avance.items[p.id] && estado(p.id).caja < 4 && estado(p.id).toca <= ahora)
    .sort((a, b) => estado(a.id).caja - estado(b.id).caja || estado(a.id).toca - estado(b.id).toca);
  const nuevas = barajar(PREGUNTAS.filter((p) => !avance.items[p.id]));
  let lista = vistas.slice(0, Math.ceil(n * 0.6));
  lista = lista.concat(nuevas.slice(0, n - lista.length));
  if (lista.length < n) {
    const resto = PREGUNTAS.filter((p) => !lista.includes(p))
      .sort((a, b) => estado(a.id).caja - estado(b.id).caja);
    lista = lista.concat(resto.slice(0, n - lista.length));
  }
  return barajar(lista);
}

function rondaSimulacro() {
  let lista = [];
  for (const d of [1, 2, 3]) {
    lista = lista.concat(barajar(PREGUNTAS.filter((p) => dominioDe(p) === d)).slice(0, CUPO_SIMULACRO[d]));
  }
  return barajar(lista);
}

// ----- sesión -----

function iniciar(tipo, lista, titulo) {
  sesion = {
    tipo,
    titulo,
    cola: lista.map((p) => ({ p, orden: barajar(p.o.map((_, i) => i)) })),
    i: 0,
    respuestas: [],
    seleccion: new Set(),
    revisada: false,
    reintentos: new Set(),
    inicio: Date.now()
  };
  pintar();
}

function cerrar() {
  if (!sesion || sesion.cerrada) return;
  sesion.cerrada = true;
  const unicas = new Map();
  sesion.respuestas.forEach((r) => {
    if (!unicas.has(r.p.id)) unicas.set(r.p.id, r.correcta);
  });
  const porDominio = {};
  sesion.respuestas.forEach((r) => {
    const d = dominioDe(r.p);
    porDominio[d] = porDominio[d] || { ok: 0, n: 0 };
    porDominio[d].n++;
    if (r.correcta) porDominio[d].ok++;
  });
  const total = unicas.size;
  const bien = [...unicas.values()].filter(Boolean).length;
  avance.historial = (avance.historial || []).concat({
    fecha: new Date().toISOString(),
    tipo: sesion.tipo,
    completa: sesion.i >= sesion.cola.length,
    titulo: sesion.titulo,
    total,
    bien,
    pct: total ? Math.round((bien / total) * 100) : 0,
    minutos: Math.round((Date.now() - sesion.inicio) / 60000),
    fallos: [...unicas.entries()].filter(([, ok]) => !ok).map(([id]) => id),
    dominios: porDominio
  }).slice(-60);
  guardar();
}

function responder(noSe = false) {
  if (sesion.revisada) return siguiente();
  const actual = sesion.cola[sesion.i];
  const p = actual.p;
  const sel = [...sesion.seleccion];
  const correcta = !noSe && sel.length === p.a.length && sel.every((x) => p.a.includes(x));
  registrar(p, correcta);
  sesion.respuestas.push({ p, sel, correcta });

  if (sesion.tipo === "simulacro") {
    sesion.seleccion = new Set();
    sesion.i++;
    return pintar();
  }

  sesion.revisada = true;
  if (!correcta && !sesion.reintentos.has(p.id)) {
    sesion.reintentos.add(p.id);
    const pos = Math.min(sesion.i + 4, sesion.cola.length);
    sesion.cola.splice(pos, 0, { p, orden: barajar(p.o.map((_, i) => i)) });
  }
  pintar();
}

function siguiente() {
  sesion.i++;
  sesion.seleccion = new Set();
  sesion.revisada = false;
  pintar();
}

function salir() {
  if (sesion && sesion.respuestas.length) cerrar();
  sesion = null;
  pintar();
}

// ----- pintado -----

function pintar() {
  if (!sesion) return pintarInicio();
  if (sesion.i >= sesion.cola.length) return pintarResumen();
  pintarPregunta();
}

function pintarAvance() {
  if (!resumenAvance) return;
  const vistas = Object.keys(avance.items).length;
  if (vistas === 0) {
    resumenAvance.innerHTML = `<p class="prosa">Sin avance todavía. El diagnóstico son 20 preguntas de los tres dominios y toma unos 10 minutos.</p>`;
    return;
  }
  const ultimo = (avance.historial || []).filter((h) => h.tipo === "simulacro" && h.completa).slice(-1)[0];
  resumenAvance.innerHTML = `
    <div class="tarjeta">
      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; margin-bottom: 22px; flex-wrap: wrap">
        <h2 style="font-size: 21px">Cómo vas</h2>
        <span class="meta">${vistas} de ${PREGUNTAS.length} preguntas vistas${ultimo ? ` · último simulacro ${ultimo.pct}%` : ""}</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 18px">
        ${[1, 2, 3].map((d) => {
          const a = aciertosDominio(d);
          const pct = a.pct === null ? 0 : a.pct;
          return `<div>
            <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 16px; color: var(--ink-soft); flex-wrap: wrap">
              <span>${DOMINIOS[d].nombre}</span>
              <span>${a.pct === null ? "sin datos" : `<strong style="font-weight: 600">${a.pct}%</strong> de aciertos`} <span class="meta">· ${a.vistas} de ${a.total} vistas</span></span>
            </div>
            <div class="barra-avance"><i class="${pct < 70 ? "baja" : ""}" style="width: ${pct}%"></i></div>
          </div>`;
        }).join("")}
      </div>
    </div>`;
}

function pintarInicio() {
  pintarAvance();
  const pendientes = PREGUNTAS.filter((p) => avance.items[p.id] && estado(p.id).caja < 4 && estado(p.id).toca <= Date.now()).length;
  const empezado = Object.keys(avance.items).length > 0;
  const temas = Object.entries(TEMAS).map(([k, t]) => {
    const qs = PREGUNTAS.filter((p) => p.tp === k);
    const vistas = qs.filter((p) => avance.items[p.id]).length;
    return `<button class="chip" data-tema="${k}">${esc(t.nombre)} <span class="meta">${vistas}/${qs.length}</span></button>`;
  }).join("");

  panel.innerHTML = `
    <div class="modos-practica">
      <button class="accion" data-modo="${empezado ? "repaso" : "diagnostico"}">
        <b>${empezado ? "Repaso" : "Diagnóstico"}</b>
        <span>${empezado
          ? `15 preguntas: primero lo que fallaste${pendientes ? `, y hoy tocan ${pendientes}` : ""}.`
          : "20 preguntas de los tres dominios para saber dónde estás parado. Unos 10 minutos."}</span>
      </button>
      <button class="accion" data-modo="simulacro">
        <b>Simulacro</b>
        <span>30 preguntas con la proporción del examen y cronómetro. Unos 35 minutos.</span>
      </button>
      ${empezado ? `<button class="accion" data-modo="diagnostico"><b>Diagnóstico</b><span>20 preguntas de los tres dominios, para volver a medir.</span></button>` : ""}
    </div>

    <div class="por-tema">
      <h2 style="font-size: 21px">O practica un tema suelto</h2>
      <div class="chips">${temas}</div>
    </div>`;

  panel.querySelectorAll("[data-modo]").forEach((b) => b.addEventListener("click", () => {
    const m = b.dataset.modo;
    if (m === "diagnostico") iniciar("diagnostico", rondaDiagnostico(), "Diagnóstico");
    if (m === "repaso") iniciar("repaso", rondaRepaso(), "Repaso");
    if (m === "simulacro") iniciar("simulacro", rondaSimulacro(), "Simulacro");
  }));
  panel.querySelectorAll("[data-tema]").forEach((b) => b.addEventListener("click", () => {
    const k = b.dataset.tema;
    iniciar("tema", barajar(PREGUNTAS.filter((p) => p.tp === k)), TEMAS[k].nombre);
  }));
}

function pintarPregunta() {
  const actual = sesion.cola[sesion.i];
  const p = actual.p;
  const multi = p.a.length > 1;
  const examen = sesion.tipo === "simulacro";
  const letras = ["A", "B", "C", "D", "E"];

  panel.innerHTML = `
    <div class="tarjeta">
      <div class="cabeza-pregunta">
        <span class="meta">${esc(DOMINIOS[dominioDe(p)].nombre)} · ${esc(TEMAS[p.tp].nombre)}</span>
        <span class="meta">${examen ? `<span id="reloj">00:00</span> · ` : ""}${sesion.i + 1} de ${sesion.cola.length}</span>
      </div>
      <h2 style="font-size: 23px; font-weight: 600; line-height: 1.35; margin-top: 14px">${esc(p.q)}</h2>
      ${multi ? `<p class="meta" style="margin-top: 10px" id="aviso-multi">Elige ${p.a.length} respuestas.</p>` : ""}
      <ul class="opciones">
        ${actual.orden.map((oi, pos) => `<li><button class="opcion" data-oi="${oi}" aria-pressed="${sesion.seleccion.has(oi)}"><span class="letra">${letras[pos]}</span><span>${esc(p.o[oi])}</span></button></li>`).join("")}
      </ul>
      <div id="retro"></div>
      <div class="acciones-pregunta">
        <button class="cta" id="comprobar" ${sesion.seleccion.size < (examen ? 1 : p.a.length) ? "disabled" : ""}>${examen ? "Siguiente" : "Comprobar"}</button>
        ${examen ? "" : `<button class="cta secundaria" id="nose">No sé</button>`}
        <button class="cta secundaria" id="salir">Salir</button>
      </div>
    </div>`;

  if (examen) tictac();
  panel.querySelectorAll(".opcion").forEach((b) => b.addEventListener("click", () => elegir(Number(b.dataset.oi))));
  document.getElementById("comprobar").addEventListener("click", () => responder(false));
  const nose = document.getElementById("nose");
  if (nose) nose.addEventListener("click", () => { sesion.seleccion = new Set(); responder(true); });
  document.getElementById("salir").addEventListener("click", salir);

  if (sesion.revisada) pintarRetro();
}

function elegir(oi) {
  if (sesion.revisada) return;
  const p = sesion.cola[sesion.i].p;
  if (p.a.length > 1) {
    sesion.seleccion.has(oi) ? sesion.seleccion.delete(oi) : sesion.seleccion.add(oi);
  } else {
    sesion.seleccion = new Set([oi]);
  }
  panel.querySelectorAll(".opcion").forEach((b) => b.setAttribute("aria-pressed", sesion.seleccion.has(Number(b.dataset.oi))));
  const faltan = p.a.length - sesion.seleccion.size;
  document.getElementById("comprobar").disabled = faltan > 0;
}

function pintarRetro() {
  const r = sesion.respuestas[sesion.respuestas.length - 1];
  const p = r.p;
  panel.querySelectorAll(".opcion").forEach((b) => {
    const oi = Number(b.dataset.oi);
    b.disabled = true;
    if (p.a.includes(oi)) {
      b.classList.add("correcta");
      b.insertAdjacentHTML("beforeend", '<span class="sr">respuesta correcta</span>');
    } else if (r.sel.includes(oi)) {
      b.classList.add("incorrecta");
      b.insertAdjacentHTML("beforeend", '<span class="sr">tu respuesta, incorrecta</span>');
    }
  });
  const dif = DIFERENCIA_DE_TEMA[p.tp];
  document.getElementById("retro").innerHTML = `
    <div class="retro ${r.correcta ? "bien" : "mal"}">
      <h3>${r.correcta ? "Correcto" : "No es esa"}</h3>
      ${r.correcta ? "" : `<p class="densa"><strong style="font-weight: 600">Respuesta:</strong> ${p.a.map((i) => esc(p.o[i])).join(" · ")}</p>`}
      <p class="densa">${esc(p.e)}</p>
      <p><strong class="pista">${esc(p.c)}</strong></p>
      ${!r.correcta && dif ? `<p class="meta"><a href="/diferencias#${dif}">Ver la diferencia que explica esto →</a></p>` : ""}
      ${!r.correcta ? `<p class="meta">Vuelve a aparecer en unas preguntas más.</p>` : ""}
    </div>`;
  const btn = document.getElementById("comprobar");
  btn.textContent = sesion.i + 1 >= sesion.cola.length ? "Ver resultado" : "Siguiente";
  btn.disabled = false;
  const nose = document.getElementById("nose");
  if (nose) nose.remove();
  btn.focus();
}

function pintarResumen() {
  cerrar();
  const h = avance.historial[avance.historial.length - 1];
  const examen = sesion.tipo === "simulacro";
  const vistos = new Set();
  const falladas = sesion.respuestas.filter((r) => {
    if (r.correcta || vistos.has(r.p.id)) return false;
    vistos.add(r.p.id);
    return true;
  });

  panel.innerHTML = `
    <div class="tarjeta">
      <p class="meta">${esc(sesion.titulo)} · ${h.minutos} min</p>
      <p class="resultado">${h.pct}%</p>
      <p class="prosa">${h.bien} de ${h.total} al primer intento.${examen
        ? h.pct >= 80 ? " Con ese margen, el examen real queda holgado." : h.pct >= 70 ? " Alcanza, pero con poco margen: revisa lo de abajo." : " Todavía no. Repasa lo de abajo y vuelve a medir."
        : falladas.length ? " Lo que fallaste regresa en el próximo repaso." : " Estas preguntas ya no regresan pronto."}</p>

      ${examen ? `<table class="mapa" style="margin-top: 22px">
        <caption class="sr">Aciertos por dominio</caption>
        <tbody>${[1, 2, 3].map((d) => {
          const x = h.dominios[d] || { ok: 0, n: 0 };
          return `<tr><th scope="row">${DOMINIOS[d].nombre}</th><td>${x.ok} de ${x.n}${x.n ? ` · ${Math.round((x.ok / x.n) * 100)}%` : ""}</td></tr>`;
        }).join("")}</tbody>
      </table>` : ""}

      ${falladas.length ? `<div class="repaso-lista">
        <h3>Para repasar</h3>
        ${falladas.map((r) => {
          const dif = DIFERENCIA_DE_TEMA[r.p.tp];
          return `<div class="repaso-item">
            <p style="font-weight: 600">${esc(r.p.q)}</p>
            ${r.sel.length ? `<p class="meta">Tu respuesta: ${r.sel.map((i) => esc(r.p.o[i])).join(" · ")}</p>` : ""}
            <p class="densa"><strong style="font-weight: 600">Correcta:</strong> ${r.p.a.map((i) => esc(r.p.o[i])).join(" · ")}</p>
            <p class="densa">${esc(r.p.e)}</p>
            <p><strong class="pista">${esc(r.p.c)}</strong></p>
            ${dif ? `<p class="meta"><a href="/diferencias#${dif}">Ver la diferencia que explica esto →</a></p>` : ""}
          </div>`;
        }).join("")}
      </div>` : ""}

      <div class="acciones-pregunta">
        <button class="cta" id="otra">${examen ? "Otro simulacro" : "Otra ronda"}</button>
        <button class="cta secundaria" id="inicio">Volver al inicio</button>
      </div>
    </div>`;

  document.getElementById("otra").addEventListener("click", () => {
    if (examen) iniciar("simulacro", rondaSimulacro(), "Simulacro");
    else iniciar("repaso", rondaRepaso(), "Repaso");
  });
  document.getElementById("inicio").addEventListener("click", () => { sesion = null; pintar(); });
  pintarAvance();
}

function tictac() {
  const el = document.getElementById("reloj");
  if (!el || !sesion) return;
  const s = Math.floor((Date.now() - sesion.inicio) / 1000);
  el.textContent = `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
}
setInterval(tictac, 1000);

document.addEventListener("keydown", (e) => {
  if (!sesion || sesion.i >= sesion.cola.length) return;
  if (e.target.tagName === "INPUT") return;
  // con el foco en una opción, Enter la marca: enviar aquí dejaría la respuesta a medias
  if (e.key === "Enter" && e.target.closest && e.target.closest(".opcion")) return;
  const n = Number(e.key);
  if (n >= 1 && n <= 5 && !sesion.revisada) {
    const actual = sesion.cola[sesion.i];
    if (actual.orden[n - 1] !== undefined) {
      e.preventDefault();
      elegir(actual.orden[n - 1]);
    }
  }
  if (e.key === "Enter") {
    const btn = document.getElementById("comprobar");
    if (btn && !btn.disabled && document.activeElement !== btn) {
      e.preventDefault();
      btn.click();
    }
  }
});

pintar();
