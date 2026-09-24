# -*- coding: utf-8 -*-
"""Génère toutes les pages HTML. Exécuter: python3 pages.py"""
from build_pages import *  # noqa

# =================================================================
# INDEX
# =================================================================
def page_index():
    services_cards = ""
    for s in SERVICES:
        services_cards += """<div class="service-card">
          <span class="icon-wrap">{icon}</span>
          <h3>{title}</h3>
          <p>{short}</p>
          <a class="more" href="{slug}.html">En savoir plus {arrow}</a>
        </div>""".format(icon=icon(s["icon"]), title=s["title"], short=s["short"], slug=s["slug"], arrow=icon("icon-arrow.svg"))

    gallery_pairs = ""
    for r in REALISATIONS:
        if r.get("before_after"):
            gallery_pairs += photo_card_before_after(r["photo"], r["title"], r["city"])
        else:
            gallery_pairs += photo_card_single(r["photo"], r["title"], r["city"])

    testi_cards = ""
    for i, t in enumerate(TESTIMONIALS[:3]):
        testi_cards += """<div class="testi-card">
          {stars}
          <p>&laquo;&nbsp;{text}&nbsp;&raquo;</p>
          <div class="testi-who">
            <span class="avatar" style="background:{color}">{initials}</span>
            <div>
              <strong>{name}</strong>
              <span>{google} Avis Google</span>
            </div>
          </div>
        </div>""".format(stars=stars(), text=t["text"], color=AVATAR_COLORS[i % 3], initials=t["initials"],
                          name=t["name"], google=icon("icon-google-blue.svg", "icon"))

    main = """
    <section class="hero">
      <div class="container">
        <div>
          <span class="eyebrow">Votre confort, notre expertise.</span>
          <h1>Plombier chauffagiste &agrave; {city} en Haute-Savoie</h1>
          <p class="lead">D&eacute;pannage, installations et r&eacute;novations de plomberie et chauffage dans toute la Haute-Savoie.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="{phone_href}">{phone_icon} Appeler maintenant</a>
            <a class="btn btn-outline" href="{devis_href}">{devis_label}</a>
          </div>
          <div class="trust-row">
            <span class="item"><span class="icon-wrap">{doc}</span> Devis gratuit<br>et sans engagement</span>
            <span class="item"><span class="icon-wrap">{badge}</span> Artisan local<br>&agrave; votre service</span>
            <span class="item">{stars}<br><strong>{rating}/5</strong> sur Google &middot; {reviews} avis</span>
          </div>
        </div>
        <div class="hero-media">
          <div class="frame"><img class="lightbox-img" src="images/photos/hero-bain-luxe.jpg" alt="Douche italienne r&eacute;nov&eacute;e par Active Plomberie, ambiance gris anthracite" style="width:100%; height:100%; object-fit:cover; display:block;"></div>
          <div class="hero-badges">
            <div class="hero-badge">
              <span class="icon-wrap">{pin}</span>
              <div><span class="num">{radius}</span><br><span class="label">autour de {city}<br>et alentours</span></div>
            </div>
            <div class="hero-badge">
              {google}
              <div><span class="num">{rating}/5</span><br><span class="label">sur Google &middot; {reviews} avis clients</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head center">
          <span class="eyebrow">Nos services</span>
          <h2>Des solutions pour tous vos besoins en plomberie et chauffage.</h2>
        </div>
        <div class="services-grid">{services_cards}</div>
        <div class="services-cta"><a class="btn btn-outline" href="nos-services.html">Voir tous nos services {arrow}</a></div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="gallery-head">
          <div class="section-head" style="margin-bottom:0;">
            <span class="eyebrow">R&eacute;alisations</span>
            <h2>Des chantiers r&eacute;alis&eacute;s avec soin et exigence.</h2>
            <p>Quelques exemples repr&eacute;sentatifs de nos interventions r&eacute;centes en Haute-Savoie.</p>
          </div>
        </div>
        <div class="gallery-nav">
          <button class="prev" aria-label="Pr&eacute;c&eacute;dent">{arrow}</button>
          <button class="next" aria-label="Suivant">{arrow}</button>
        </div>
        <div class="gallery">
          <div class="gallery-track">{gallery_pairs}</div>
        </div>
        <div class="services-cta"><a class="btn btn-outline" href="realisations.html">Voir toutes nos r&eacute;alisations {arrow}</a></div>
      </div>
    </section>

    <section>
      <div class="container about-grid">
        <div class="about-media">
          <div class="photo-frame"><img class="lightbox-img" src="images/photos/artisan-vehicule.jpg" alt="Le plombier d'Active Plomberie 74 devant son v&eacute;hicule de service" loading="lazy"></div>
          <div class="about-badge">
            {stars_sm}
            <div><strong>{rating}/5</strong><br><span>{reviews} avis Google</span></div>
          </div>
        </div>
        <div>
          <span class="eyebrow">&Agrave; propos</span>
          <h2 style="font-size:clamp(1.6rem,3vw,2.2rem); font-weight:800; color:var(--navy); margin:10px 0 16px;">Un artisan passionn&eacute; &agrave; votre service.</h2>
          <p style="color:var(--muted);">Install&eacute; &agrave; {city}, j'interviens dans tout le 74 pour vos travaux de plomberie, chauffage et r&eacute;novation de salle de bain. Mon objectif&nbsp;: vous offrir un travail soign&eacute;, des conseils personnalis&eacute;s et un service r&eacute;actif.</p>
          <ul class="about-list">
            <li>{check} Plus de 10 ans d'exp&eacute;rience</li>
            <li>{check} Travail soign&eacute; et durable</li>
            <li>{check} Mat&eacute;riaux de qualit&eacute;</li>
            <li>{check} Respect des d&eacute;lais et des lieux</li>
          </ul>
          <a class="btn btn-primary" href="a-propos.html">En savoir plus sur moi</a>
          <div class="info-cards">
            <div class="info-card"><span class="icon-wrap">{doc}</span><div><strong>Devis gratuit</strong><span>R&eacute;ponse sous 24h</span></div></div>
            <div class="info-card"><span class="icon-wrap">{shield}</span><div><strong>Garantie d&eacute;cennale</strong><span>Et assurance professionnelle</span></div></div>
            <div class="info-card"><span class="icon-wrap">{badge}</span><div><strong>Conseils personnalis&eacute;s</strong><span>Des solutions adapt&eacute;es &agrave; vos besoins</span></div></div>
          </div>
          <div class="zone-mini">
            <span class="icon-wrap">{pin}</span>
            <div><strong>Zone d'intervention</strong><span>{city} et alentours dans un rayon de {radius}</span></div>
            <a href="zones-intervention.html">Voir toutes les communes &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="testi-head">
          <div class="section-head" style="margin-bottom:0;">
            <span class="eyebrow">Ils nous font confiance</span>
            <h2>Avis clients</h2>
          </div>
          <a class="btn btn-outline" href="avis-clients.html">Voir tous les avis Google</a>
        </div>
        <div class="testi-grid">{testi_cards}</div>
      </div>
    </section>
    """.format(devis_href="simulateur-devis.html" if SIMULATEUR_PUBLIC else "contact.html", devis_label="Estimer mon devis en ligne" if SIMULATEUR_PUBLIC else "Demander un devis", 
        city=BIZ["city"], phone_href=BIZ["phone_href"], phone_icon=icon("icon-phone-white.svg"),
        clock=icon("icon-clock.svg"), doc=icon("icon-doc.svg"), badge=icon("icon-badge.svg"),
        stars=stars(), rating=BIZ["rating"], reviews=BIZ["reviews"], pin=icon("icon-pin.svg"),
        radius=BIZ["radius"], services_cards=services_cards, arrow=icon("icon-arrow.svg"),
        gallery_pairs=gallery_pairs, stars_sm=stars(), check=icon("icon-check-green.svg"),
        shield=icon("icon-shield.svg"), testi_cards=testi_cards,
        google=icon("icon-google-blue.svg", "icon"),
    )

    main += build_cta_banner()

    page = wrap_page(
        title="Plombier chauffagiste à {} | {}".format(BIZ["city"], BIZ["legal"]),
        description="Plombier chauffagiste à Thyez : dépannage, installation et rénovation en plomberie, chauffage et salle de bain. Devis gratuit et sans engagement.",
        path="", main_html=main, active="accueil",
    )
    return page

# =================================================================
# NOS SERVICES (page listant les 4 services)
# =================================================================
def page_nos_services():
    cards = ""
    for s in SERVICES:
        items_html = "".join('<li>{check} {t}</li>'.format(check=icon("icon-check-green.svg"), t=t) for t, d in s["items"])
        cards += """<div class="service-card" style="padding:32px 26px;">
          <span class="icon-wrap" style="width:60px;height:60px;"><img src="images/{icon}" class="icon" style="width:28px;height:28px;" alt=""></span>
          <h3 style="font-size:1.25rem;">{title}</h3>
          <p>{short}</p>
          <ul style="display:grid; gap:8px; margin:14px 0 18px; font-size:.88rem; color:var(--text); font-weight:600;">{items}</ul>
          <a class="btn btn-outline btn-sm" href="{slug}.html">D&eacute;couvrir {arrow}</a>
        </div>""".format(icon=s["icon"], title=s["title"], short=s["short"], items=items_html, slug=s["slug"], arrow=icon("icon-arrow.svg"))

    main = build_page_header(
        "Nos services", "Plomberie, chauffage, chauffe-eau, salle de bain : découvrez l'ensemble de nos prestations à Thyez et dans toute la Haute-Savoie.",
        [("Accueil", "index.html"), ("Nos services", None)]
    ) + """
    <section>
      <div class="container">
        <div class="services-grid services-grid-2col">{cards}</div>
      </div>
    </section>
    """.format(cards=cards) + build_cta_banner()

    return wrap_page(
        title="Nos services de plomberie et chauffage | Active Plomberie 74",
        description="Découvrez tous nos services : dépannage plomberie, chauffage, chauffe-eau et rénovation de salle de bain à Thyez et en Haute-Savoie.",
        path="nos-services.html", main_html=main, active="services",
    )

# =================================================================
# PAGE DE SERVICE (détail)
# =================================================================
SERVICE_PHOTOS = {
    "depannage-plomberie": ("reparation-robinet.jpg", "Intervention de d&eacute;pannage plomberie par Active Plomberie 74"),
    "chauffage": ("distribution-cuivre.jpg", "Installation de distribution de chauffage par Active Plomberie 74"),
    "chauffe-eau": ("chauffe-eau-installation.jpg", "Installation d'un chauffe-eau par Active Plomberie 74"),
    "salle-de-bain": ("bain-double-vasque-1.jpg", "R&eacute;novation de salle de bain par Active Plomberie 74"),
}

def page_service(s):
    items_html = ""
    for t, d in s["items"]:
        items_html += """<li><span class="icon-wrap">{check}</span><div><strong>{t}</strong><span>{d}</span></div></li>""".format(
            check=icon("icon-check.svg"), t=t, d=d)

    faq_html = ""
    faq_schema_items = []
    for q, a in s["faq"]:
        faq_html += """<details class="faq-item">
          <summary>{q} {chev}</summary>
          <div class="faq-body">{a}</div>
        </details>""".format(q=q, chev=icon("icon-chevron.svg"), a=a)
        faq_schema_items.append({
            "@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    sidebar_links = ""
    for s2 in SERVICES:
        cls = ' class="active"' if s2["slug"] == s["slug"] else ""
        sidebar_links += '<a{cls} href="{slug}.html">{title} {chev}</a>'.format(
            cls=cls, slug=s2["slug"], title=s2["title"], chev=icon("icon-arrow.svg"))

    main = build_page_header(
        s["title"], s["hero_lead"],
        [("Accueil", "index.html"), ("Nos services", "nos-services.html"), (s["title"], None)]
    ) + """
    <section>
      <div class="container detail-grid">
        <div>
          <span class="eyebrow">Ce que nous proposons</span>
          <h2 style="font-size:1.7rem; font-weight:800; color:var(--navy); margin:10px 0 4px;">{title}</h2>
          <p style="color:var(--muted); margin-top:10px;">{lead}</p>
          <div class="service-photo"><img class="lightbox-img" src="images/photos/{photo}" alt="{photo_alt}" loading="lazy"></div>
          <ul class="detail-list">{items}</ul>

          <span class="eyebrow">Questions fr&eacute;quentes</span>
          <h2 style="font-size:1.4rem; font-weight:800; color:var(--navy); margin:10px 0 20px;">Tout savoir sur nos prestations</h2>
          <div class="faq">{faq}</div>
        </div>
        <aside class="sidebar-card">
          <h4>Nos services</h4>
          <div class="services-mini">{sidebar_links}</div>
          <div class="call-box">
            <p>Besoin d'un devis ou d'une intervention ?</p>
            <a href="{phone_href}">{phone}</a>
            <a class="btn btn-outline-light btn-block" href="contact.html">Demander un devis gratuit</a>{simulateur_btn}
          </div>
        </aside>
      </div>
    </section>
    """.format(simulateur_btn='\n            <a class="btn btn-primary btn-block" href="simulateur-devis.html" style="margin-top:10px;">Estimer mon devis en ligne</a>' if SIMULATEUR_PUBLIC else "", title=s["title"], lead=s["hero_lead"], items=items_html, faq=faq_html,
               photo=SERVICE_PHOTOS[s["slug"]][0], photo_alt=SERVICE_PHOTOS[s["slug"]][1],
               sidebar_links=sidebar_links, phone_href=BIZ["phone_href"], phone=BIZ["phone_display"])
    main += build_cta_banner()

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema_items}
    service_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": s["title"], "name": s["title"], "description": s["short"],
        "provider": {"@type": "Plumber", "name": BIZ["legal"]},
        "areaServed": "Haute-Savoie",
    }

    return wrap_page(
        title="{} à {} | {}".format(s["title"], BIZ["city"], BIZ["legal"]),
        description=s["short"] + " Devis gratuit en Haute-Savoie.",
        path=s["slug"] + ".html", main_html=main, active="services", active_service=s["slug"],
        extra_schema=faq_schema,
    ).replace("</script>\n", "</script>\n  <script type=\"application/ld+json\">" + json.dumps(service_schema, ensure_ascii=False) + "</script>\n", 1)

# =================================================================
# RÉALISATIONS
# =================================================================
def page_realisations():
    cards = ""
    for r in REALISATIONS_GALERIE:
        cards += photo_card_single(r["photo"], r["title"], "Active Plomberie 74")

    main = build_page_header(
        "Nos réalisations", "Un aperçu de nos chantiers récents en plomberie, chauffage et rénovation de salle de bain en Haute-Savoie — toutes les photos ci-dessous sont issues de nos interventions réelles.",
        [("Accueil", "index.html"), ("Réalisations", None)]
    ) + """
    <section>
      <div class="container">
        <div class="realisation-feature">
          <figure>
            <img class="lightbox-img" src="images/photos/avant-apres-salle-de-bain.webp" alt="R&eacute;novation de salle de bain, avant et apr&egrave;s" loading="lazy">
          </figure>
          <div class="cap-body">
            <div>
              <h3>R&eacute;novation compl&egrave;te de salle de bain</h3>
              <p>D'une salle de bain vétuste &agrave; un espace moderne enti&egrave;rement r&eacute;nov&eacute; &mdash; d&eacute;molition, plomberie, faïence et finitions.</p>
            </div>
            <a class="btn btn-primary" href="salle-de-bain.html">Voir le service {arrow}</a>
          </div>
        </div>
        <div class="services-grid" style="grid-template-columns:repeat(3,1fr); gap:20px;">{cards}</div>
      </div>
    </section>
    """.format(cards=cards, arrow=icon("icon-arrow-white.svg")) + build_cta_banner()

    return wrap_page(
        title="Nos réalisations | Active Plomberie 74",
        description="Découvrez un aperçu de nos réalisations en plomberie, chauffage et rénovation de salle de bain à Thyez et en Haute-Savoie.",
        path="realisations.html", main_html=main, active="realisations",
    )

# =================================================================
# AVIS CLIENTS
# =================================================================
def page_avis():
    cards = ""
    for i, t in enumerate(TESTIMONIALS):
        cards += """<div class="testi-card">
          {stars}
          <p>&laquo;&nbsp;{text}&nbsp;&raquo;</p>
          <div class="testi-who">
            <span class="avatar" style="background:{color}">{initials}</span>
            <div><strong>{name}</strong><span>{google} Avis Google</span></div>
          </div>
        </div>""".format(stars=stars(), text=t["text"], color=AVATAR_COLORS[i % 3],
                          initials=t["initials"], name=t["name"], google=icon("icon-google-blue.svg", "icon"))

    main = build_page_header(
        "Avis clients", "La satisfaction de nos clients est notre priorité. Découvrez leurs retours d'expérience.",
        [("Accueil", "index.html"), ("Avis clients", None)]
    ) + """
    <section>
      <div class="container">
        <div class="map-frame" style="max-width:420px; margin:0 auto 50px;">
          <span class="icon-wrap">{google}</span>
          {stars}
          <h3 style="font-size:2rem; font-weight:800; color:var(--navy); margin:10px 0 4px;">{rating}/5</h3>
          <p style="color:var(--muted);">Bas&eacute; sur {reviews} avis Google</p>
          <a class="btn btn-primary" style="margin-top:16px;" href="https://www.google.com/maps/search/?api=1&query={query}" target="_blank" rel="noopener">Voir les avis sur Google</a>
        </div>
        <div class="testi-grid">{cards}</div>
      </div>
    </section>
    """.format(google=icon("icon-google-blue.svg"), stars=stars(), rating=BIZ["rating"], reviews=BIZ["reviews"],
               query=(BIZ["legal"] + " " + BIZ["address_zip"]).replace(" ", "+"), cards=cards) + build_cta_banner()

    return wrap_page(
        title="Avis clients | Active Plomberie 74",
        description="Découvrez les avis de nos clients sur nos interventions de plomberie, chauffage et rénovation en Haute-Savoie.",
        path="avis-clients.html", main_html=main, active="avis",
    )

# =================================================================
# À PROPOS
# =================================================================
def page_apropos():
    stats = [("10+", "ans d'exp&eacute;rience"), (BIZ["reviews"], "avis clients"),
              (BIZ["rating"] + "/5", "note Google"), (BIZ["radius"], "zone d'intervention")]
    stats_html = "".join(
        '<div class="badge-tech"><strong style="font-size:1.4rem; color:var(--primary);">{n}</strong><span>{l}</span></div>'.format(n=n, l=l)
        for n, l in stats
    )
    main = build_page_header(
        "À propos", "Artisan plombier chauffagiste indépendant, installé à Thyez et au service de la Haute-Savoie depuis plus de 10 ans.",
        [("Accueil", "index.html"), ("À propos", None)]
    ) + """
    <section>
      <div class="container about-grid">
        <div class="about-media">
          <div class="photo-frame"><img class="lightbox-img" src="images/photos/artisan-vehicule.jpg" alt="Le plombier d'Active Plomberie 74 devant son v&eacute;hicule de service" loading="lazy"></div>
          <div class="about-badge">{stars}<div><strong>{rating}/5</strong><br><span>{reviews} avis Google</span></div></div>
        </div>
        <div>
          <span class="eyebrow">Mon histoire</span>
          <h2 style="font-size:clamp(1.6rem,3vw,2.2rem); font-weight:800; color:var(--navy); margin:10px 0 16px;">Un artisan de confiance, proche de chez vous.</h2>
          <p style="color:var(--muted);">Install&eacute; &agrave; {city}, je mets mon exp&eacute;rience au service des particuliers et professionnels de Haute-Savoie pour tous leurs travaux de plomberie, chauffage et r&eacute;novation de salle de bain. Chaque intervention est r&eacute;alis&eacute;e avec le m&ecirc;me soin, du simple d&eacute;pannage au chantier de r&eacute;novation compl&egrave;te.</p>
          <p style="color:var(--muted); margin-top:12px;">Mon objectif&nbsp;: un travail propre, durable, et une relation de confiance avec chacun de mes clients &mdash; d'o&ugrave; une note de {rating}/5 sur {reviews} avis Google.</p>
          <p style="color:var(--muted); margin-top:12px;">Pour des devis clairs et rapides, je travaille avec <a href="https://alyapro.com/artisans/active-plomberie-74">Alya Pro, le logiciel de devis et de facturation des artisans</a>&nbsp;: retrouvez aussi ma fiche dans <a href="https://alyapro.com/artisans">l'annuaire des artisans Alya Pro</a>.</p>
          <ul class="about-list">
            <li>{check} Plus de 10 ans d'exp&eacute;rience</li>
            <li>{check} Travail soign&eacute; et durable</li>
            <li>{check} Mat&eacute;riaux de qualit&eacute;</li>
            <li>{check} Respect des d&eacute;lais et des lieux</li>
            <li>{check} Garantie d&eacute;cennale et assurance professionnelle</li>
          </ul>
          <a class="btn btn-primary" href="contact.html">Demander un devis gratuit</a>
        </div>
      </div>
    </section>
    <section class="section-alt">
      <div class="container">
        <div class="badges-tech">{stats}</div>
      </div>
    </section>
    """.format(stars=stars(), rating=BIZ["rating"], reviews=BIZ["reviews"], city=BIZ["city"],
               check=icon("icon-check-green.svg"), stats=stats_html) + build_cta_banner()

    return wrap_page(
        title="À propos | Active Plomberie 74 – Plombier chauffagiste à Thyez",
        description="Découvrez le parcours d'Active Plomberie 74, artisan plombier chauffagiste indépendant installé à Thyez, au service de la Haute-Savoie.",
        path="a-propos.html", main_html=main, active="apropos",
    )

# =================================================================
# PAGE PAR COMMUNE (SEO local)
# =================================================================
def page_commune(commune):
    slug = commune_slug(commune)

    services_cards = ""
    for s in SERVICES:
        services_cards += """<div class="service-card">
          <span class="icon-wrap">{icon}</span>
          <h3>{title}</h3>
          <p>{short}</p>
          <a class="more" href="{slug}.html">En savoir plus {arrow}</a>
        </div>""".format(icon=icon(s["icon"]), title=s["title"], short=s["short"], slug=s["slug"], arrow=icon("icon-arrow.svg"))

    nearby = [c for c in COMMUNES if c != commune]
    chips = "".join('<a class="zone-chip" href="plombier-{s}.html">{pin} {c}</a>'.format(
        s=commune_slug(c), pin=icon("icon-pin.svg"), c=c) for c in nearby)

    main = build_page_header(
        "Plombier chauffagiste à " + commune,
        "Active Plomberie 74 intervient à {commune} pour vos travaux de plomberie, chauffage et rénovation de salle de bain.".format(commune=commune),
        [("Accueil", "index.html"), ("Zones d'intervention", "zones-intervention.html"), (commune, None)]
    ) + """
    <section>
      <div class="container">
        <div class="section-head center">
          <span class="eyebrow">Nos services &agrave; {commune}</span>
          <h2>Plomberie et chauffage, tous vos besoins couverts.</h2>
        </div>
        <div class="services-grid">{services_cards}</div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container about-grid">
        <div class="about-media">
          <div class="photo-frame"><img class="lightbox-img" src="images/photos/artisan-vehicule.jpg" alt="Le plombier d'Active Plomberie 74, artisan &agrave; {commune}" loading="lazy"></div>
          <div class="about-badge">{stars}<div><strong>{rating}/5</strong><br><span>{reviews} avis Google</span></div></div>
        </div>
        <div>
          <span class="eyebrow">Active Plomberie 74 &agrave; {commune}</span>
          <h2 style="font-size:clamp(1.6rem,3vw,2.2rem); font-weight:800; color:var(--navy); margin:10px 0 16px;">Un artisan de proximit&eacute;, &agrave; votre &eacute;coute.</h2>
          <p style="color:var(--muted);">Bas&eacute; &agrave; {city}, j'interviens r&eacute;guli&egrave;rement &agrave; {commune} pour des travaux de plomberie, de chauffage et de r&eacute;novation de salle de bain, aupr&egrave;s des particuliers comme des professionnels.</p>
          <ul class="about-list">
            <li>{check} Plus de 10 ans d'exp&eacute;rience</li>
            <li>{check} Travail soign&eacute; et durable</li>
            <li>{check} Devis gratuit et sans engagement</li>
            <li>{check} Garantie d&eacute;cennale et assurance professionnelle</li>
          </ul>
          <a class="btn btn-primary" href="contact.html">Demander un devis gratuit</a>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <span class="eyebrow">Zones voisines</span>
        <h2 style="font-size:1.4rem; font-weight:800; color:var(--navy); margin:10px 0 20px;">Nous intervenons aussi pr&egrave;s de {commune}</h2>
        <div class="zone-grid">{chips}</div>
      </div>
    </section>
    """.format(commune=commune, city=BIZ["city"], services_cards=services_cards, arrow=icon("icon-arrow.svg"),
               stars=stars(), rating=BIZ["rating"], reviews=BIZ["reviews"],
               check=icon("icon-check-green.svg"), chips=chips)
    main += build_cta_banner()

    service_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": "Plomberie et chauffage",
        "name": "Plombier chauffagiste à " + commune,
        "provider": {"@type": "Plumber", "name": BIZ["legal"]},
        "areaServed": {"@type": "City", "name": commune},
    }

    return wrap_page(
        title="Plombier chauffagiste à {} | {}".format(commune, BIZ["legal"]),
        description="Active Plomberie 74, votre plombier chauffagiste à {}. Dépannage, installation et rénovation en plomberie et chauffage. Devis gratuit.".format(commune),
        path="plombier-{}.html".format(slug), main_html=main, active="zones",
        extra_schema=service_schema,
    )

# =================================================================
# ZONES D'INTERVENTION
# =================================================================
def page_zones():
    chips = "".join('<a class="zone-chip" href="plombier-{slug}.html">{pin} {c}</a>'.format(slug=commune_slug(c), pin=icon("icon-pin.svg"), c=c) for c in COMMUNES)
    main = build_page_header(
        "Zones d'intervention", "Active Plomberie 74 intervient à {city} et dans un rayon de {radius} autour, en Haute-Savoie.".format(city=BIZ["city"], radius=BIZ["radius"]),
        [("Accueil", "index.html"), ("Zones d'intervention", None)]
    ) + """
    <section>
      <div class="container">
        <div class="detail-grid zone-detail-grid">
          <div>
            <span class="eyebrow">Communes desservies</span>
            <h2 style="font-size:1.5rem; font-weight:800; color:var(--navy); margin:10px 0 20px;">Nos secteurs d'intervention</h2>
            <div class="zone-grid">{chips}</div>
            <p style="color:var(--muted); font-size:.9rem; margin-top:18px;">Et les communes voisines dans un rayon de {radius} autour de {city}. Vous n'&ecirc;tes pas s&ucirc;r d'&ecirc;tre dans notre zone&nbsp;? <a href="contact.html" style="color:var(--primary); font-weight:700;">Contactez-nous</a>, nous vous r&eacute;pondrons rapidement.</p>
          </div>
          <div class="map-frame">
            <span class="icon-wrap">{pin}</span>
            <h3 style="font-weight:800; color:var(--navy); margin-bottom:6px;">Rayon de {radius}</h3>
            <p>autour de {city}, {zip}</p>
            <a class="btn btn-primary" style="margin-top:16px;" href="{phone_href}">{phone_icon} V&eacute;rifier mon secteur</a>
          </div>
        </div>
      </div>
    </section>
    """.format(chips=chips, radius=BIZ["radius"], city=BIZ["city"], pin=icon("icon-pin.svg", "icon"),
               zip=BIZ["address_zip"], phone_href=BIZ["phone_href"], phone_icon=icon("icon-phone-white.svg")) + build_cta_banner()

    return wrap_page(
        title="Zones d'intervention | Active Plomberie 74",
        description="Active Plomberie 74 intervient à Thyez, Cluses, Scionzier, Marignier, Bonneville, Sallanches et dans toute la Haute-Savoie.",
        path="zones-intervention.html", main_html=main, active="zones",
    )

# =================================================================
# CONTACT
# =================================================================
def page_contact():
    main = build_page_header(
        "Contact", "Une question ou un projet ? Contactez-nous par téléphone, e-mail ou via le formulaire ci-dessous.",
        [("Accueil", "index.html"), ("Contact", None)]
    ) + """
    <section>
      <div class="container contact-grid">
        <div>
          <div class="form-success"><span class="icon">{check}</span><span>Merci&nbsp;! Votre message a bien &eacute;t&eacute; pr&eacute;par&eacute;. Pour une r&eacute;ponse imm&eacute;diate, appelez-nous directement au {phone}.</span></div>
          <div class="form-card">
            <!--
              Ce formulaire est fonctionnel c&ocirc;t&eacute; navigateur (validation, message de confirmation)
              mais n'est reli&eacute; &agrave; aucun service d'envoi. Pour recevoir r&eacute;ellement les messages,
              branchez un service comme Formspree, Netlify Forms, ou un script serveur, puis mettez &agrave;
              jour l'attribut action/method ci-dessous.
            -->
            <form id="contact-form" action="#" method="post">
              <div class="form-row">
                <div class="field"><label for="nom">Nom complet *</label><input type="text" id="nom" name="nom" required></div>
                <div class="field"><label for="tel">T&eacute;l&eacute;phone *</label><input type="tel" id="tel" name="tel" required><span class="error-msg">Num&eacute;ro invalide</span></div>
              </div>
              <div class="field"><label for="email">E-mail *</label><input type="email" id="email" name="email" required><span class="error-msg">E-mail invalide</span></div>
              <div class="field">
                <label for="sujet">Type de demande</label>
                <select id="sujet" name="sujet">
                  <option>D&eacute;pannage</option>
                  <option>Devis chauffage</option>
                  <option>Devis chauffe-eau</option>
                  <option>Devis salle de bain</option>
                  <option>Autre demande</option>
                </select>
              </div>
              <div class="field"><label for="message">Votre message *</label><textarea id="message" name="message" required></textarea></div>
              <button type="submit" class="btn btn-primary btn-block">Envoyer ma demande</button>
              <p class="form-note">En envoyant ce formulaire, vous acceptez d'&ecirc;tre recontact&eacute; par Active Plomberie 74.</p>
            </form>
          </div>
        </div>
        <div>
          <div class="contact-cards">
            <div class="contact-card"><span class="icon-wrap">{phone_icon}</span><div><strong>T&eacute;l&eacute;phone</strong><a href="{phone_href}">{phone}</a></div></div>
            <div class="contact-card"><span class="icon-wrap">{mail_icon}</span><div><strong>E-mail</strong><a href="mailto:{email}">{email}</a></div></div>
            <div class="contact-card"><span class="icon-wrap">{pin_icon}</span><div><strong>Adresse</strong><span>{addr}, {zip}</span></div></div>
          </div>
          <div class="sidebar-card" style="position:static;">
            <h4>Horaires d'intervention</h4>
            <table class="hours-table">
              <tr><td>Lundi &ndash; Vendredi</td><td>7h &ndash; 20h</td></tr>
              <tr><td>Samedi</td><td>8h &ndash; 18h</td></tr>
              <tr><td>Dimanche &amp; f&eacute;ri&eacute;s</td><td>Ferm&eacute;</td></tr>
            </table>
          </div>
        </div>
      </div>
    </section>
    """.format(check=icon("icon-check.svg"), phone=BIZ["phone_display"], phone_icon=icon("icon-phone.svg"),
               phone_href=BIZ["phone_href"], mail_icon=icon("icon-mail.svg"), email=BIZ["email"],
               pin_icon=icon("icon-pin.svg"), addr=BIZ["address_line"], zip=BIZ["address_zip"])

    return wrap_page(
        title="Contact – Devis gratuit | Active Plomberie 74",
        description="Contactez Active Plomberie 74 par téléphone, e-mail ou via notre formulaire pour toute demande de devis ou d'intervention.",
        path="contact.html", main_html=main, active="contact",
    )

# =================================================================
# SIMULATEUR DE DEVIS (estimation calculée par Alya, voir js/simulateur.js)
# =================================================================
SIMULATEUR_API = "https://alyapro.com/api/site-simulateur"
SIMULATEUR_CLE = "active-plomberie-74"

def page_simulateur():
    types = [
        ("depannage", "Dépannage / fuite", "icon-droplet.svg"),
        ("chauffe-eau", "Chauffe-eau", "icon-water-heater.svg"),
        ("chauffage", "Chauffage", "icon-radiator.svg"),
        ("salle-de-bain", "Salle de bain", "icon-bathtub.svg"),
        ("sanitaires", "WC, lavabo, douche", "icon-tools.svg"),
        ("autre", "Autre projet", "icon-doc.svg"),
    ]
    types_html = ""
    for slug, label, ic in types:
        types_html += ('<button type="button" class="sim-type" data-type="' + slug + '" data-label="' + html.escape(label) +
                       '" aria-pressed="false"><span class="icon-wrap">' + icon(ic) + '</span>' + html.escape(label) + '</button>')

    main = build_page_header(
        "Simulateur de devis en ligne",
        "Estimez gratuitement le prix de vos travaux de plomberie et chauffage en 2 minutes, puis demandez votre devis précis à l'artisan.",
        [("Accueil", "index.html"), ("Simulateur de devis", None)]
    ) + """
    <section>
      <div class="container sim-grid">
        <div id="simulateur" class="sim-card" data-api=\"""" + SIMULATEUR_API + """\" data-cle=\"""" + SIMULATEUR_CLE + """\">
          <div class="sim-steps" aria-hidden="true"><span class="on"></span><span></span><span></span></div>

          <!-- Étape 1 : description des travaux -->
          <div class="sim-step" data-step="form">
            <h2>Quels travaux souhaitez-vous réaliser&nbsp;?</h2>
            <p class="sim-sub">Aucune coordonnée demandée à cette étape. Estimation gratuite et sans engagement.</p>
            <form id="sim-form" novalidate>
              <div class="sim-types" role="group" aria-label="Type de travaux">""" + types_html + """</div>
              <div class="sim-details" hidden>
                <div class="sim-fields" id="sim-questions"></div>
                <div class="sim-fields">
                  <div class="field"><label for="sim-logement">Type de logement</label>
                    <select id="sim-logement"><option value="">— Choisir —</option><option>Maison</option><option>Appartement</option><option>Local professionnel</option></select></div>
                  <div class="field"><label for="sim-age">Âge du logement</label>
                    <select id="sim-age"><option value="">— Choisir —</option><option>Plus de 2 ans</option><option>Moins de 2 ans (neuf)</option></select></div>
                  <div class="field full"><label for="sim-cp">Code postal du chantier</label>
                    <input type="text" id="sim-cp" inputmode="numeric" maxlength="5" placeholder="74300" autocomplete="postal-code"></div>
                  <div class="field full"><label for="sim-description">Décrivez vos travaux *</label>
                    <textarea id="sim-description" maxlength="2000" required></textarea>
                    <p class="sim-hint">Plus votre description est précise (dimensions, équipement actuel, accès…), plus l'estimation sera juste.</p></div>
                </div>
                <div class="sim-error" id="sim-error-1" role="alert"></div>
                <button type="submit" class="btn btn-primary btn-block">Calculer mon estimation</button>
              </div>
            </form>
          </div>

          <!-- Étape 2a : calcul en cours -->
          <div class="sim-step sim-loading" data-step="loading" hidden aria-live="polite">
            <div class="sim-spinner"></div>
            <strong>Calcul de votre estimation…</strong>
            <p id="sim-loading-msg">Analyse de votre demande…</p>
            <div class="sim-progress"><span></span></div>
            <p style="font-size:.8rem; margin-top:14px;">Cela prend généralement 20 à 40 secondes.</p>
          </div>

          <!-- Étape 2b : résultat -->
          <div class="sim-step" data-step="result" hidden>
            <h2 id="sim-result-title">Votre estimation</h2>
            <p class="sim-sub">Fourchette de prix indicative pour vos travaux, fournitures et main d'œuvre comprises.</p>
            <div class="sim-result-box" aria-live="polite">
              <small>Estimation indicative</small>
              <span class="sim-range" id="sim-range"></span>
              <span class="sim-ttc">TTC, fournitures et pose comprises</span>
            </div>
            <div id="sim-postes-wrap">
              <p style="font-weight:700; color:var(--navy); margin-bottom:10px;">Ce que comprend cette estimation&nbsp;:</p>
              <ul class="sim-postes" id="sim-postes"></ul>
            </div>
            <div class="sim-disclaimer">
              """ + icon("icon-shield.svg") + """
              <div><strong>Prix estimatif, non contractuel.</strong> Cette fourchette est calculée automatiquement à partir de votre description.
              Le prix définitif sera établi et validé par Active Plomberie 74 dans un devis gratuit, après examen de vos photos et, si besoin, une visite sur place.</div>
            </div>
            <p style="font-weight:700; color:var(--navy); margin-bottom:4px;">Vous souhaitez un devis précis&nbsp;?</p>
            <p class="sim-sub" style="margin-bottom:14px;">Laissez vos coordonnées, Active Plomberie 74 vous recontacte. Vous pourrez aussi joindre des photos (facultatif).</p>
            <div class="sim-actions">
              <button type="button" class="btn btn-primary" id="sim-affiner">Recevoir mon devis précis</button>
              <button type="button" class="btn btn-outline" id="sim-modifier">Modifier ma demande</button>
            </div>
          </div>

          <!-- Étape 3 : photos + coordonnées -->
          <div class="sim-step" data-step="contact" hidden>
            <h2>Recevoir mon devis précis</h2>
            <p class="sim-sub">Indiquez vos coordonnées&nbsp;: Active Plomberie 74 vous recontacte pour établir et valider votre devis. Les photos sont facultatives, mais elles aident l'artisan à être plus précis.</p>
            <form id="sim-contact" novalidate>
              <div class="form-row">
                <div class="field"><label for="sim-c-nom">Nom complet *</label><input type="text" id="sim-c-nom" autocomplete="name" required></div>
                <div class="field"><label for="sim-c-tel">Téléphone *</label><input type="tel" id="sim-c-tel" autocomplete="tel" required></div>
              </div>
              <div class="field"><label for="sim-c-email">E-mail <span style="font-weight:400; color:var(--muted);">(pour recevoir le récapitulatif)</span></label><input type="email" id="sim-c-email" autocomplete="email"></div>
              <div class="form-row">
                <div class="field"><label for="sim-c-cp">Code postal</label><input type="text" id="sim-c-cp" inputmode="numeric" maxlength="5" autocomplete="postal-code"></div>
                <div class="field"><label for="sim-c-ville">Ville</label><input type="text" id="sim-c-ville" autocomplete="address-level2"></div>
              </div>
              <div class="field"><label for="sim-c-message">Précisions (disponibilités, accès…)</label><textarea id="sim-c-message" maxlength="1500" style="min-height:80px;"></textarea></div>
              <div class="sim-drop" tabindex="0" role="button" aria-label="Ajouter des photos">
                """ + icon("icon-doc.svg") + """
                <strong>Ajouter des photos <span style="font-weight:400; color:var(--muted);">(facultatif)</span></strong>
                <span>Jusqu'à 3 photos (vue d'ensemble, équipement actuel…) &middot; JPEG ou PNG &middot; depuis votre téléphone ou ordinateur</span>
                <input type="file" id="sim-photos" accept="image/*" multiple>
              </div>
              <div class="sim-thumbs"></div>
              <div class="sim-hp" aria-hidden="true"><label for="sim-c-website">Site web</label><input type="text" id="sim-c-website" tabindex="-1" autocomplete="off"></div>
              <label class="sim-check"><input type="checkbox" id="sim-c-ok"> <span>J'accepte d'être recontacté par Active Plomberie 74 au sujet de ma demande. Mes informations et photos sont transmises uniquement à l'artisan pour établir mon devis.</span></label>
              <div class="sim-error" id="sim-error-3" role="alert"></div>
              <div class="sim-actions">
                <button type="submit" class="btn btn-primary" id="sim-envoyer">Envoyer à l'artisan</button>
                <button type="button" class="btn btn-outline" id="sim-retour">Retour</button>
              </div>
            </form>
          </div>

          <!-- Confirmation -->
          <div class="sim-step sim-done" data-step="done" hidden>
            <span class="icon-wrap">""" + icon("icon-check-green.svg") + """</span>
            <h2>Demande envoyée&nbsp;!</h2>
            <p>Merci, Active Plomberie 74 a bien reçu votre demande. Vous serez recontacté rapidement pour valider votre devis.</p>
            <p>Pour une urgence, appelez directement le <a href=\"""" + BIZ["phone_href"] + """\"><strong>""" + BIZ["phone_display"] + """</strong></a>.</p>
          </div>
          <p class="sim-powered">Estimation calculée avec Alya, le logiciel de devis de votre artisan.</p>
        </div>

        <aside class="sim-aside">
          <div class="sim-how">
            <h3>Comment ça marche&nbsp;?</h3>
            <ol>
              <li><div><strong>Décrivez vos travaux</strong>Type d'intervention, équipement, dimensions&hellip;</div></li>
              <li><div><strong>Obtenez une fourchette de prix</strong>Estimation instantanée basée sur les tarifs de l'artisan.</div></li>
              <li><div><strong>Demandez votre devis précis</strong>Laissez vos coordonnées (et des photos si vous le souhaitez)&nbsp;: l'artisan valide votre devis, gratuitement.</div></li>
            </ol>
          </div>
          <div class="sim-callbox">
            <p>Une urgence ou une question&nbsp;? Appelez directement&nbsp;:</p>
            <a class="tel" href=\"""" + BIZ["phone_href"] + """\">""" + BIZ["phone_display"] + """</a>
            <small>Devis gratuit et sans engagement</small>
          </div>
        </aside>
      </div>
    </section>
    <script src="js/simulateur.js" defer></script>
    """

    return wrap_page(
        title="Simulateur de devis plomberie en ligne | Active Plomberie 74",
        description="Estimez gratuitement le prix de vos travaux de plomberie, chauffe-eau, chauffage ou salle de bain en Haute-Savoie, puis envoyez vos photos pour un devis précis.",
        path="simulateur-devis.html", main_html=main, active="services", active_service="simulateur",
        extra_head='\n  <link rel="stylesheet" href="css/simulateur.css">',
        robots="index, follow" if SIMULATEUR_PUBLIC else "noindex, nofollow",
    )

# =================================================================
# MENTIONS LÉGALES
# =================================================================
def page_mentions():
    main = build_page_header(
        "Mentions légales", "Informations légales relatives au site et à l'entreprise Active Plomberie 74.",
        [("Accueil", "index.html"), ("Mentions légales", None)]
    ) + """
    <section>
      <div class="container legal-body">
        <h2>&Eacute;diteur</h2>
        <p><strong>CHRONOSHARP</strong> &mdash; SAS, soci&eacute;t&eacute; par actions simplifi&eacute;e au capital de 800&nbsp;&euro;<br>
        SIREN&nbsp;: 889 637 856<br>
        SIRET&nbsp;: 889 637 856 00036<br>
        Si&egrave;ge social&nbsp;: 7 rue Foy, 29200 Brest<br>
        Contact&nbsp;: jordan.cornec@chrono-sharp.com<br>
        Directeur de la publication&nbsp;: Jordan Cornec</p>

        <h2>H&eacute;bergement</h2>
        <p><strong>Vercel Inc.</strong><br>
        340 S Lemon Ave #4133, Walnut, CA 91789, &Eacute;tats-Unis<br>
        <a href="https://vercel.com" target="_blank" rel="noopener">vercel.com</a></p>

        <h2>Propri&eacute;t&eacute; intellectuelle</h2>
        <p>L'ensemble des contenus du site (textes, images, logo, interface) est la propri&eacute;t&eacute; exclusive de CHRONOSHARP et est prot&eacute;g&eacute; par les lois fran&ccedil;aises et internationales relatives au droit d'auteur. Toute reproduction, m&ecirc;me partielle, est interdite sans autorisation pr&eacute;alable.</p>
      </div>
    </section>
    """

    return wrap_page(
        title="Mentions légales | Active Plomberie 74",
        description="Mentions légales du site Active Plomberie 74.",
        path="mentions-legales.html", main_html=main, active="", include_topbar=True,
    )

# =================================================================
# BUILD ALL
# =================================================================
def build_all():
    print("Génération des pages...")
    write_page("index.html", page_index())
    write_page("nos-services.html", page_nos_services())
    for s in SERVICES:
        write_page(s["slug"] + ".html", page_service(s))
    write_page("realisations.html", page_realisations())
    write_page("avis-clients.html", page_avis())
    write_page("a-propos.html", page_apropos())
    write_page("zones-intervention.html", page_zones())
    for c in COMMUNES:
        write_page("plombier-{}.html".format(commune_slug(c)), page_commune(c))
    write_page("simulateur-devis.html", page_simulateur())
    write_page("contact.html", page_contact())
    write_page("mentions-legales.html", page_mentions())

    # robots.txt
    robots = "User-agent: *\nAllow: /\nSitemap: {domain}/sitemap.xml\n".format(domain=BIZ["domain"])
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # sitemap.xml
    pages = ["index.html", "nos-services.html"] + [s["slug"] + ".html" for s in SERVICES] + \
        ["realisations.html", "avis-clients.html", "a-propos.html", "zones-intervention.html"] + \
        ["plombier-{}.html".format(commune_slug(c)) for c in COMMUNES] + \
        (["simulateur-devis.html"] if SIMULATEUR_PUBLIC else []) + ["contact.html", "mentions-legales.html"]
    urls = ""
    for p in pages:
        loc = BIZ["domain"] + "/" + p
        priority = "1.0" if p == "index.html" else "0.7"
        urls += "  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{prio}</priority></url>\n".format(loc=loc, prio=priority)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'.format(urls=urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    print("Terminé.")

if __name__ == "__main__":
    build_all()
