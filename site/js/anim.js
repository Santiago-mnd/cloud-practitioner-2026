document.documentElement.classList.add("js");

const revelables = document.querySelectorAll("[data-revelar]");

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches && "IntersectionObserver" in window) {
  const observador = new IntersectionObserver((entradas) => {
    for (const entrada of entradas) {
      if (!entrada.isIntersecting) continue;
      entrada.target.classList.add("visible");
      observador.unobserve(entrada.target);
    }
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });

  revelables.forEach((el) => observador.observe(el));
} else {
  revelables.forEach((el) => el.classList.add("visible"));
}
