document.documentElement.classList.add("js");

const CLAVE_DOMINADAS = "az900:diferencias:dominadas";
const CLAVE_VISTA = "az900:diferencias:vista";
const CLAVE_LEGACY = "az900-diferencias-dominadas";

const boton = document.getElementById("alternar-pistas");
const estado = document.getElementById("estado-dominadas");
const casillas = document.querySelectorAll("[data-dominada]");
const enlacesIndice = document.querySelectorAll("[data-indice]");
const gruposIndice = document.querySelectorAll("[data-indice-dominio]");
const cajaIndice = document.getElementById("indice-caja");
const total = casillas.length;

function leer(clave) {
  try {
    return JSON.parse(localStorage.getItem(clave) || "null");
  } catch (e) {
    return null;
  }
}

function escribir(clave, valor) {
  try {
    localStorage.setItem(clave, typeof valor === "string" ? valor : JSON.stringify(valor));
  } catch (e) {
    // almacenamiento bloqueado: la página funciona igual, sin memoria
  }
}

let dominadas = new Set(leer(CLAVE_DOMINADAS) || leer(CLAVE_LEGACY) || []);

function pintarEstado() {
  if (!estado) return;
  estado.textContent = dominadas.size === 0
    ? `${total} diferencias`
    : `${dominadas.size} de ${total} dominadas`;
}

function aplicarDominadas() {
  casillas.forEach((casilla) => {
    const marcada = dominadas.has(casilla.dataset.dominada);
    casilla.checked = marcada;
    casilla.closest(".diferencia").classList.toggle("dominada-si", marcada);
  });
  pintarEstado();
}

casillas.forEach((casilla) => {
  casilla.addEventListener("change", () => {
    if (casilla.checked) dominadas.add(casilla.dataset.dominada);
    else dominadas.delete(casilla.dataset.dominada);
    escribir(CLAVE_DOMINADAS, [...dominadas]);
    aplicarDominadas();
  });
});

if (boton) {
  const soloPistas = () => document.body.classList.contains("solo-pistas");
  const pintarBoton = () => {
    boton.setAttribute("aria-pressed", String(soloPistas()));
  };

  if (leer(CLAVE_VISTA) === "pistas" || localStorage.getItem(CLAVE_VISTA) === "pistas") {
    document.body.classList.add("solo-pistas");
  }

  boton.addEventListener("click", () => {
    document.body.classList.toggle("solo-pistas");
    escribir(CLAVE_VISTA, soloPistas() ? "pistas" : "todo");
    pintarBoton();
  });

  pintarBoton();
}

// el índice sigue a la lectura: resalta la diferencia actual y abre solo su dominio
if ("IntersectionObserver" in window && enlacesIndice.length) {
  const porId = new Map([...enlacesIndice].map((a) => [a.dataset.indice, a]));
  let actual = null;

  const marcar = (id) => {
    if (!id || id === actual) return;
    actual = id;
    enlacesIndice.forEach((a) => a.classList.toggle("actual", a.dataset.indice === id));
    const enlace = porId.get(id);
    const dominio = enlace && enlace.closest("[data-indice-dominio]");
    gruposIndice.forEach((g) => g.classList.toggle("abierto", g === dominio));
    if (enlace && cajaIndice && cajaIndice.open && window.innerWidth > 1000) {
      const caja = cajaIndice.getBoundingClientRect();
      const fila = enlace.getBoundingClientRect();
      if (fila.top < caja.top || fila.bottom > caja.bottom) {
        enlace.scrollIntoView({ block: "nearest" });
      }
    }
  };

  // al cargar, el primer dominio queda abierto: sin esto el índice arranca vacío
  marcar(enlacesIndice[0].dataset.indice);

  const observador = new IntersectionObserver((entradas) => {
    const visibles = entradas
      .filter((e) => e.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visibles.length) marcar(visibles[0].target.id);
  }, { rootMargin: "-10% 0px -70% 0px", threshold: 0 });

  document.querySelectorAll(".diferencia").forEach((el) => observador.observe(el));
}

// en pantallas chicas el índice arranca plegado: 33 títulos antes del contenido son tres pantallas
if (cajaIndice && window.matchMedia("(max-width: 1000px)").matches) {
  cajaIndice.open = false;
}

// las fuentes web llegan después y recorren el layout: hay que volver al ancla
if (location.hash && document.fonts && document.fonts.ready) {
  const destino = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (destino) {
    document.fonts.ready.then(() => {
      destino.scrollIntoView({ block: "start", behavior: "instant" });
    });
  }
}

aplicarDominadas();

// el scroll suave se aplica solo al hacer clic, nunca al tabular
document.addEventListener("click", (e) => {
  const enlace = e.target.closest('a[href^="#"]');
  if (!enlace) return;
  const destino = document.getElementById(decodeURIComponent(enlace.getAttribute("href").slice(1)));
  if (!destino) return;
  e.preventDefault();
  const suave = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  destino.scrollIntoView({ behavior: suave ? "smooth" : "instant", block: "start" });
  history.replaceState(null, "", enlace.getAttribute("href"));
});
