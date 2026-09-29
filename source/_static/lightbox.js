/* Visor de imágenes de la documentación (D16, 2026-09-29).
   Toda figura del contenido se abre a tamaño completo al pulsarla. Esc o clic fuera cierra;
   un clic sobre la imagen ampliada alterna entre "ajustar a la ventana" y "tamaño real". */
(function () {
  'use strict';
  function build() {
    var box = document.createElement('div');
    box.className = 'gf-lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'Imagen ampliada');
    box.hidden = true;
    box.innerHTML =
      '<button type="button" class="gf-lightbox__close" aria-label="Cerrar">&#10005;</button>' +
      '<figure class="gf-lightbox__figure"><img alt=""><figcaption></figcaption></figure>' +
      '<p class="gf-lightbox__hint">Clic en la imagen: tamaño real · Esc: cerrar</p>';
    document.body.appendChild(box);
    var img = box.querySelector('img');
    var cap = box.querySelector('figcaption');
    var last = null;

    function close() {
      box.hidden = true;
      box.classList.remove('is-real-size');
      document.body.classList.remove('gf-lightbox-open');
      if (last) { last.focus(); last = null; }
    }
    function open(src, alt, caption, origin) {
      last = origin;
      img.src = src;
      img.alt = alt || '';
      cap.textContent = caption || '';
      cap.hidden = !caption;
      box.classList.remove('is-real-size');
      box.hidden = false;
      document.body.classList.add('gf-lightbox-open');
      box.querySelector('.gf-lightbox__close').focus();
    }
    box.addEventListener('click', function (e) {
      if (e.target === img) { box.classList.toggle('is-real-size'); return; }
      if (e.target.closest('.gf-lightbox__close') || e.target === box || e.target.closest('.gf-lightbox__hint')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!box.hidden && e.key === 'Escape') close();
    });
    return open;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var images = document.querySelectorAll('article figure img, article .figure img, article img.align-center');
    if (!images.length) return;
    var open = build();
    function captionText(fig) {
      var cap = fig ? fig.querySelector('figcaption, .caption') : null;
      if (!cap) return '';
      var clone = cap.cloneNode(true);
      clone.querySelectorAll('.headerlink').forEach(function (a) { a.remove(); });
      return clone.textContent.trim();
    }
    images.forEach(function (im) {
      /* Sphinx envuelve en un enlace a la imagen completa las figuras con :width:; el visor
         sustituye ese enlace. */
      var link = im.closest('a.image-reference');
      var full = link ? link.getAttribute('href') : (im.currentSrc || im.src);
      var target = link || im;
      im.classList.add('gf-zoomable');
      target.setAttribute('role', 'button');
      if (!link) im.setAttribute('tabindex', '0');
      var fig = im.closest('figure, .figure');
      var trigger = function (e) { if (e) e.preventDefault(); open(full, im.alt, captionText(fig), target); };
      target.addEventListener('click', trigger);
      target.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { trigger(e); } });
    });
  });
})();
