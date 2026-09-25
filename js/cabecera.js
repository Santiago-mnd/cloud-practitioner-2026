// La cabecera gana una línea y una sombra apenas la página deja de estar arriba,
// y publica su altura real para que las anclas no caigan debajo de ella.
const cabecera = document.querySelector(".cabecera");

if (cabecera) {
  const medir = () => {
    document.documentElement.style.setProperty("--cabecera", cabecera.offsetHeight + "px");
  };
  const pintar = () => cabecera.classList.toggle("elevada", window.scrollY > 4);

  medir();
  pintar();
  window.addEventListener("scroll", pintar, { passive: true });
  window.addEventListener("resize", medir, { passive: true });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(medir);
}
