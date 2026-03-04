(function () {
    function switchLang(targetLang) {
        const path = window.location.pathname;

        // Espera rutas tipo /docs/<lang>/<version>/...
        // Ej: /docs/en/17.0/conceptual-model/structural-logic.html
        const m = path.match(/^\/docs\/(en|es|it)\/(.*)$/);
        if (!m) {
            // fallback: si no encaja, manda al home del idioma
            window.location.pathname = `/docs/${targetLang}/`;
            return;
        }

        const rest = m[2]; // todo lo que va después del idioma
        window.location.pathname = `/docs/${targetLang}/${rest}`;
    }

    document.addEventListener("click", (ev) => {
        const a = ev.target.closest("a[data-lang]");
        if (!a) return;
        ev.preventDefault();
        switchLang(a.getAttribute("data-lang"));
    });
})();