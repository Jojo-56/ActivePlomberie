/* =========================================================
   Simulateur de devis en ligne — Active Plomberie 74
   L'estimation est calculée par Alya (logiciel de devis de l'artisan)
   à partir de ses propres tarifs : POST {api} action=estimate, puis
   action=submit pour transmettre coordonnées + photos à l'artisan.
   ========================================================= */
(function () {
  'use strict';
  var root = document.getElementById('simulateur');
  if (!root) return;

  var API = root.getAttribute('data-api');
  var CLE = root.getAttribute('data-cle');
  var MAX_PHOTOS = 3;

  // Questions complémentaires par type de travaux (libellé → options).
  var QUESTIONS = {
    'depannage': [
      { id: 'probleme', label: 'Quel est le problème ?', options: ['Fuite d\'eau', 'WC bouché ou qui fuit', 'Évier / canalisation bouchée', 'Robinet ou mitigeur défectueux', 'Chasse d\'eau en panne', 'Autre'] },
      { id: 'urgence', label: 'Délai souhaité', options: ['Urgent (sous 24 h)', 'Dans la semaine', 'Pas pressé'] }
    ],
    'chauffe-eau': [
      { id: 'type', label: 'Type de chauffe-eau souhaité', options: ['Électrique', 'Thermodynamique', 'Gaz', 'Je ne sais pas / conseil'] },
      { id: 'capacite', label: 'Capacité', options: ['100 L (1-2 pers.)', '150 L (2-3 pers.)', '200 L (3-4 pers.)', '300 L (5 pers. et +)', 'Je ne sais pas'] },
      { id: 'existant', label: 'Situation', options: ['Remplacement d\'un chauffe-eau existant', 'Première installation'] }
    ],
    'chauffage': [
      { id: 'projet', label: 'Votre projet', options: ['Remplacement de chaudière', 'Réparation / dépannage', 'Ajout ou remplacement de radiateurs', 'Plancher chauffant', 'Pompe à chaleur', 'Entretien annuel'] },
      { id: 'energie', label: 'Énergie actuelle', options: ['Gaz', 'Fioul', 'Électricité', 'Bois / granulés', 'Je ne sais pas'] },
      { id: 'surface', label: 'Surface chauffée', options: ['Moins de 70 m²', '70 à 120 m²', '120 à 180 m²', 'Plus de 180 m²'] }
    ],
    'salle-de-bain': [
      { id: 'projet', label: 'Votre projet', options: ['Rénovation complète', 'Remplacer la baignoire par une douche', 'Douche à l\'italienne', 'Changer le meuble vasque / les sanitaires'] },
      { id: 'surface', label: 'Surface de la pièce', options: ['Moins de 4 m²', '4 à 6 m²', '6 à 8 m²', 'Plus de 8 m²'] },
      { id: 'gamme', label: 'Gamme de finition', options: ['Économique', 'Standard', 'Haut de gamme'] }
    ],
    'sanitaires': [
      { id: 'equipement', label: 'Équipement à installer ou remplacer', options: ['WC suspendu', 'WC classique (au sol)', 'Lavabo / meuble vasque', 'Receveur et paroi de douche', 'Robinetterie / mitigeur', 'Évier de cuisine'] },
      { id: 'quantite', label: 'Quantité', options: ['1', '2', '3 ou plus'] }
    ],
    'autre': []
  };

  var PLACEHOLDERS = {
    'depannage': 'Ex. : fuite sous l\'évier de la cuisine depuis ce matin, le tuyau goutte au niveau du raccord.',
    'chauffe-eau': 'Ex. : chauffe-eau électrique de 200 L de 15 ans à remplacer, installé dans le garage.',
    'chauffage': 'Ex. : chaudière gaz de 20 ans à remplacer, maison de 110 m² avec 8 radiateurs.',
    'salle-de-bain': 'Ex. : remplacer la baignoire par une douche à l\'italienne de 120 x 90, avec nouveau meuble vasque.',
    'sanitaires': 'Ex. : remplacer un WC classique par un WC suspendu avec bâti-support.',
    'autre': 'Décrivez vos travaux le plus précisément possible.'
  };

  var state = { type: null, typeLabel: '', demandeId: null, jeton: null, photos: [] };

  function $(sel) { return root.querySelector(sel); }
  function $all(sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }

  function showStep(name) {
    $all('.sim-step').forEach(function (el) { el.hidden = el.getAttribute('data-step') !== name; });
    var idx = { form: 1, loading: 2, result: 2, contact: 3, done: 3 }[name] || 1;
    $all('.sim-steps span').forEach(function (s, i) { s.classList.toggle('on', i < idx); });
    var top = root.getBoundingClientRect().top + window.pageYOffset - 100;
    if (window.pageYOffset > top) window.scrollTo({ top: top, behavior: 'smooth' });
  }

  function showError(el, msg) {
    el.textContent = msg || '';
    el.classList.toggle('show', !!msg);
  }

  function euros(n) {
    return Math.round(n).toLocaleString('fr-FR') + ' €';
  }

  function post(payload) {
    payload.cle = CLE;
    return fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (data) {
        if (!r.ok) throw new Error(data.error || 'Une erreur est survenue. Réessayez ou appelez-nous.');
        return data;
      });
    });
  }

  /* ---------- Étape 1 : type de travaux + questions ---------- */
  var details = $('.sim-details');
  var qWrap = $('#sim-questions');
  var descInput = $('#sim-description');

  $all('.sim-type').forEach(function (btn) {
    btn.addEventListener('click', function () {
      $all('.sim-type').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      state.type = btn.getAttribute('data-type');
      state.typeLabel = btn.getAttribute('data-label');
      renderQuestions();
      details.hidden = false;
      descInput.placeholder = PLACEHOLDERS[state.type] || PLACEHOLDERS.autre;
    });
  });

  function renderQuestions() {
    qWrap.innerHTML = '';
    (QUESTIONS[state.type] || []).forEach(function (q) {
      var f = document.createElement('div');
      f.className = 'field';
      var id = 'sim-q-' + q.id;
      var html = '<label for="' + id + '">' + q.label + '</label><select id="' + id + '" data-q="' + q.label.replace(/"/g, '&quot;') + '"><option value="">— Choisir —</option>';
      q.options.forEach(function (o) { html += '<option>' + o.replace(/</g, '&lt;') + '</option>'; });
      f.innerHTML = html + '</select>';
      qWrap.appendChild(f);
    });
  }

  var loadingTimer = null;
  function startLoading() {
    var msgs = [
      'Analyse de votre demande…',
      'Sélection des fournitures adaptées…',
      'Calcul de la main d\'œuvre…',
      'Application des tarifs de l\'artisan…',
      'Finalisation de votre estimation…'
    ];
    var i = 0, pct = 6;
    var txt = $('#sim-loading-msg'), bar = $('.sim-progress span');
    txt.textContent = msgs[0];
    bar.style.width = pct + '%';
    clearInterval(loadingTimer);
    loadingTimer = setInterval(function () {
      i = Math.min(i + 1, msgs.length - 1);
      txt.textContent = msgs[i];
      pct = Math.min(pct + (95 - pct) * 0.18, 95);
      bar.style.width = pct + '%';
    }, 4500);
  }
  function stopLoading() { clearInterval(loadingTimer); }

  $('#sim-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var err = $('#sim-error-1');
    if (!state.type) return showError(err, 'Choisissez d\'abord le type de travaux.');
    var description = descInput.value.trim();
    if (description.length < 10) { descInput.focus(); return showError(err, 'Décrivez vos travaux en quelques mots (10 caractères minimum).'); }
    showError(err, '');

    var reponses = {};
    $all('#sim-questions select').forEach(function (s) { if (s.value) reponses[s.getAttribute('data-q')] = s.value; });
    var logement = $('#sim-logement').value, age = $('#sim-age').value, cp = $('#sim-cp').value.trim();
    if (logement) reponses['Logement'] = logement;
    if (age) reponses['Âge du logement'] = age;
    if (cp) reponses['Code postal du chantier'] = cp;
    if (cp) $('#sim-c-cp').value = cp;

    showStep('loading');
    startLoading();
    post({ action: 'estimate', typeTravaux: state.type, description: description, reponses: reponses })
      .then(function (data) {
        stopLoading();
        state.demandeId = data.demandeId;
        state.jeton = data.jeton;
        $('#sim-range').textContent = euros(data.min) + ' – ' + euros(data.max);
        $('#sim-result-title').textContent = data.titre || state.typeLabel;
        var ul = $('#sim-postes');
        ul.innerHTML = '';
        (data.postes || []).forEach(function (p) {
          var li = document.createElement('li');
          li.innerHTML = '<img src="images/icon-check-green.svg" class="icon" alt="">';
          li.appendChild(document.createTextNode(p));
          ul.appendChild(li);
        });
        $('#sim-postes-wrap').hidden = !(data.postes && data.postes.length);
        $('#sim-affiner').hidden = !state.demandeId;
        showStep('result');
      })
      .catch(function (e2) {
        stopLoading();
        showStep('form');
        showError(err, e2.message);
      });
  });

  $('#sim-modifier').addEventListener('click', function () { showStep('form'); });
  $('#sim-affiner').addEventListener('click', function () { showStep('contact'); });
  $('#sim-retour').addEventListener('click', function () { showStep('result'); });

  /* ---------- Étape 3 : photos ---------- */
  var drop = $('.sim-drop');
  var fileInput = $('#sim-photos');
  var thumbs = $('.sim-thumbs');

  drop.addEventListener('click', function (e) { if (e.target !== fileInput) fileInput.click(); });
  drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fileInput.click(); } });
  ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('drag'); }); });
  ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('drag'); }); });
  drop.addEventListener('drop', function (e) { addFiles(e.dataTransfer.files); });
  fileInput.addEventListener('change', function () { addFiles(fileInput.files); fileInput.value = ''; });

  // Redimensionne chaque photo (1400 px max, JPEG) avant envoi : une photo de
  // smartphone fait souvent 4-8 Mo, inutile pour que l'artisan juge le chantier.
  function resize(file) {
    return new Promise(function (resolve, reject) {
      var url = URL.createObjectURL(file);
      var img = new Image();
      img.onload = function () {
        var max = 1400, w = img.naturalWidth, h = img.naturalHeight;
        var ratio = Math.min(1, max / Math.max(w, h));
        var c = document.createElement('canvas');
        c.width = Math.round(w * ratio); c.height = Math.round(h * ratio);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        URL.revokeObjectURL(url);
        resolve(c.toDataURL('image/jpeg', 0.72));
      };
      img.onerror = function () { URL.revokeObjectURL(url); reject(new Error('Format de photo non pris en charge.')); };
      img.src = url;
    });
  }

  function addFiles(list) {
    var err = $('#sim-error-3');
    showError(err, '');
    var files = Array.prototype.slice.call(list || []).filter(function (f) { return /^image\//.test(f.type) || /\.(jpe?g|png|webp|heic)$/i.test(f.name); });
    var place = MAX_PHOTOS - state.photos.length;
    if (files.length > place) showError(err, 'Maximum ' + MAX_PHOTOS + ' photos.');
    files.slice(0, Math.max(0, place)).forEach(function (f) {
      resize(f).then(function (dataUrl) {
        if (state.photos.length >= MAX_PHOTOS) return;
        state.photos.push(dataUrl);
        renderThumbs();
      }).catch(function (e) { showError(err, e.message + ' Utilisez une photo JPEG ou PNG.'); });
    });
  }

  function renderThumbs() {
    thumbs.innerHTML = '';
    state.photos.forEach(function (p, i) {
      var d = document.createElement('div');
      d.className = 'sim-thumb';
      d.innerHTML = '<img alt="Photo ' + (i + 1) + '"><button type="button" aria-label="Retirer la photo">×</button>';
      d.querySelector('img').src = p;
      d.querySelector('button').addEventListener('click', function () { state.photos.splice(i, 1); renderThumbs(); });
      thumbs.appendChild(d);
    });
    drop.style.display = state.photos.length >= MAX_PHOTOS ? 'none' : '';
  }

  /* ---------- Étape 3 : envoi ---------- */
  $('#sim-contact').addEventListener('submit', function (e) {
    e.preventDefault();
    var err = $('#sim-error-3');
    var nom = $('#sim-c-nom').value.trim();
    var tel = $('#sim-c-tel').value.trim();
    var email = $('#sim-c-email').value.trim();
    if (!nom) return showError(err, 'Merci d\'indiquer votre nom.');
    if (tel.replace(/\D/g, '').length < 9) return showError(err, 'Merci d\'indiquer un numéro de téléphone valide.');
    if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return showError(err, 'Adresse e-mail invalide.');
    if (!$('#sim-c-ok').checked) return showError(err, 'Merci d\'accepter d\'être recontacté par Active Plomberie 74.');
    showError(err, '');

    var btn = $('#sim-envoyer');
    btn.disabled = true;
    btn.textContent = 'Envoi en cours…';
    post({
      action: 'submit',
      demandeId: state.demandeId,
      jeton: state.jeton,
      nom: nom,
      telephone: tel,
      email: email,
      codePostal: $('#sim-c-cp').value.trim(),
      ville: $('#sim-c-ville').value.trim(),
      message: $('#sim-c-message').value.trim(),
      consentement: true,
      photos: state.photos,
      website: $('#sim-c-website').value
    }).then(function () {
      showStep('done');
    }).catch(function (e2) {
      showError(err, e2.message);
    }).then(function () {
      btn.disabled = false;
      btn.textContent = 'Envoyer à l\'artisan';
    });
  });
})();
