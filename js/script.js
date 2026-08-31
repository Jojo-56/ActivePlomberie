// =========================================================
// Active Plomberie 74 — script principal
// =========================================================
document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');
  var overlay = document.querySelector('.nav-overlay');

  function closeNav() {
    if (navLinks) navLinks.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    document.querySelectorAll('.has-dropdown.open').forEach(function (li) {
      li.classList.remove('open');
    });
  }

  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      if (overlay) overlay.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }
  if (overlay) overlay.addEventListener('click', closeNav);

  // Dropdown "Nos services" au clic en mobile
  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 780) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // Ferme le menu mobile si on clique un lien simple
  document.querySelectorAll('.nav-links a:not(.has-dropdown > a)').forEach(function (link) {
    link.addEventListener('click', closeNav);
  });

  /* ---------- Carrousel réalisations ---------- */
  var track = document.querySelector('.gallery-track');
  var prevBtn = document.querySelector('.gallery-nav .prev');
  var nextBtn = document.querySelector('.gallery-nav .next');
  if (track && prevBtn && nextBtn) {
    var scrollAmount = function () {
      var card = track.querySelector('.gallery-pair');
      return card ? card.getBoundingClientRect().width + 16 : 300;
    };
    prevBtn.addEventListener('click', function () {
      track.scrollBy({ left: -scrollAmount(), behavior: 'smooth' });
    });
    nextBtn.addEventListener('click', function () {
      track.scrollBy({ left: scrollAmount(), behavior: 'smooth' });
    });
  }

  /* ---------- Formulaire de contact ---------- */
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;
      var fields = form.querySelectorAll('[required]');

      fields.forEach(function (field) {
        var wrap = field.closest('.field');
        var value = field.value.trim();
        var ok = value.length > 0;

        if (ok && field.type === 'email') {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
        }
        if (ok && field.type === 'tel') {
          ok = value.replace(/[^0-9]/g, '').length >= 9;
        }

        if (wrap) wrap.classList.toggle('error', !ok);
        if (!ok) valid = false;
      });

      if (!valid) return;

      // Pas de backend connecté : on affiche une confirmation et on prépare
      // un mailto de secours. Voir le commentaire dans le HTML du formulaire
      // pour brancher un vrai service d'envoi (Formspree, Netlify Forms...).
      var success = document.querySelector('.form-success');
      if (success) {
        success.classList.add('show');
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
    });
  }

  /* ---------- Année automatique dans le footer ---------- */
  document.querySelectorAll('.js-year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});
