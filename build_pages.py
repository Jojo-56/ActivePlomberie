# -*- coding: utf-8 -*-
"""
Génère toutes les pages HTML du site Active Plomberie 74 à partir de _data.json.
Exécuter avec: python3 build_pages.py
"""
import os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT, "_data.json"), encoding="utf-8") as f:
    DATA = json.load(f)

BIZ = DATA["biz"]
COMMUNES = DATA["communes"]
SERVICES = DATA["services"]
TESTIMONIALS = DATA["testimonials"]
AVATAR_COLORS = DATA["avatar_colors"]
REALISATIONS = DATA["realisations"]
REALISATIONS_GALERIE = DATA["realisations_galerie"]

CURRENT_YEAR = 2026

# -----------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------
def icon(name, cls="icon"):
    return '<img src="images/{}" class="{}" alt="" loading="lazy">'.format(name, cls)

def stars(n=5):
    return '<span class="stars">' + (icon("icon-star.svg") * n) + '</span>'

def service_by_slug(slug):
    for s in SERVICES:
        if s["slug"] == slug:
            return s
    return None

# -----------------------------------------------------------------
# Cartes photos réelles (réalisations)
# -----------------------------------------------------------------
def photo_card_before_after(image, title, subtitle):
    return """<div class="gallery-pair">
      <div class="imgs imgs-single">
        <figure style="aspect-ratio:16/8;">
          <span class="tag tag-avant">Avant</span>
          <span class="tag tag-apres">Apr&egrave;s</span>
          <img class="lightbox-img" src="images/photos/{image}" alt="{title} &ndash; avant / apr&egrave;s" loading="lazy" style="object-position:center;">
        </figure>
      </div>
      <div class="cap-body"><strong>{title}</strong><span>{subtitle}</span></div>
    </div>""".format(image=image, title=title, subtitle=subtitle)

def photo_card_single(image, title, subtitle):
    return """<div class="gallery-pair">
      <div class="imgs imgs-single">
        <figure>
          <img class="lightbox-img" src="images/photos/{image}" alt="{title}" loading="lazy">
        </figure>
      </div>
      <div class="cap-body"><strong>{title}</strong><span>{subtitle}</span></div>
    </div>""".format(image=image, title=title, subtitle=subtitle)

# -----------------------------------------------------------------
# HEAD
# -----------------------------------------------------------------
def build_head(title, description, path, schema_objects=None):
    canonical = BIZ["domain"] + "/" + path
    schema_html = ""
    if schema_objects:
        for obj in schema_objects:
            schema_html += '\n  <script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"
    return """<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="fr_FR">
  <meta name="theme-color" content="#1d6fe0">
  <link rel="icon" href="images/logo.svg" type="image/svg+xml">
  <link rel="stylesheet" href="css/style.css">{schema}
""".format(title=html.escape(title), desc=html.escape(description), canonical=canonical, schema=schema_html)

# -----------------------------------------------------------------
# LocalBusiness schema (utilisé sur toutes les pages)
# -----------------------------------------------------------------
def local_business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Plumber",
        "name": BIZ["legal"],
        "image": BIZ["domain"] + "/images/logo-real-transparent.png",
        "telephone": BIZ["phone_href"].replace("tel:", ""),
        "email": BIZ["email"],
        "url": BIZ["domain"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BIZ["address_line"],
            "postalCode": "74300",
            "addressLocality": "Thyez",
            "addressCountry": "FR",
        },
        "areaServed": {"@type": "GeoCircle", "geoMidpoint": {"@type": "GeoCoordinates", "addressCountry": "FR"}},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": BIZ["rating"],
            "reviewCount": BIZ["reviews"],
        },
        "priceRange": "€€",
    }

# -----------------------------------------------------------------
# TOPBAR + HEADER + NAV
# -----------------------------------------------------------------
def build_topbar():
    return """  <div class="topbar">
    <div class="container">
      <div class="topbar-left">
        <span>{pin} {addr}, {zip}</span>
        <span>{mail} <a href="mailto:{email}">{email}</a></span>
      </div>
    </div>
  </div>
""".format(pin=icon("icon-pin.svg", "icon"), addr=BIZ["address_line"], zip=BIZ["address_zip"],
           mail=icon("icon-mail.svg", "icon"), email=BIZ["email"])

NAV_ITEMS = [
    ("index.html", "accueil", "Accueil"),
    ("realisations.html", "realisations", "Réalisations"),
    ("avis-clients.html", "avis", "Avis clients"),
    ("a-propos.html", "apropos", "À propos"),
    ("zones-intervention.html", "zones", "Zones d'intervention"),
    ("contact.html", "contact", "Contact"),
]

def build_services_dropdown(active_slug=None):
    links = ""
    for s in SERVICES:
        cls = " active" if s["slug"] == active_slug else ""
        links += '<li><a class="{cls}" href="{slug}.html">{icon}{title}</a></li>'.format(
            cls=cls.strip(), slug=s["slug"], icon=icon(s["icon"]), title=s["title"])
    links += '<li><a href="nos-services.html">{icon}Tous nos services</a></li>'.format(icon=icon("icon-arrow.svg"))
    return links

def build_header(active, active_service=None):
    nav_html = ""
    # Accueil first
    href, key, label = NAV_ITEMS[0]
    cls = "active" if active == key else ""
    nav_html += '<li><a class="{cls}" href="{href}">{label}</a></li>'.format(cls=cls, href=href, label=label)

    # Services dropdown
    services_cls = "active" if active == "services" else ""
    nav_html += """<li class="has-dropdown"><a class="{cls}" href="nos-services.html">Nos services {chev}</a>
      <ul class="dropdown">{items}</ul>
    </li>""".format(cls=services_cls, chev=icon("icon-chevron-muted.svg", "icon chev"),
                     items=build_services_dropdown(active_service))

    for href, key, label in NAV_ITEMS[1:]:
        cls = "active" if active == key else ""
        nav_html += '<li><a class="{cls}" href="{href}">{label}</a></li>'.format(cls=cls, href=href, label=label)

    return """<header class="site-header">
  <div class="nav-overlay"></div>
    <div class="container nav">
      <a href="index.html" class="brand brand-photo">
        {logo}
        <span class="brand-tagline-only"><small>Plombier &middot; Chauffagiste &middot; Thyez</small></span>
      </a>
      <ul class="nav-links">{nav}</ul>
      <div class="nav-cta">
        <div class="nav-phone">
          <a href="{phone_href}">{phone_icon} {phone}</a>
        </div>
        <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false">{menu_icon}</button>
      </div>
    </div>
  </header>
""".format(logo='<img src="images/logo-real-transparent.png" alt="Logo {name}" class="brand-logo">'.format(name=BIZ["name"]),
           name=BIZ["name"], nav=nav_html, phone_href=BIZ["phone_href"],
           phone_icon=icon("icon-phone.svg"), phone=BIZ["phone_display"],
           menu_icon=icon("icon-menu.svg"))

# -----------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------
def build_footer():
    services_links = "".join(
        '<li><a href="{slug}.html">{title}</a></li>'.format(slug=s["slug"], title=s["title"]) for s in SERVICES
    )
    communes_links = "".join(
        '<li>{c}</li>'.format(c=c) for c in COMMUNES[:6]
    )
    return """<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand brand-photo">
            <img src="images/logo-real-transparent.png" alt="Logo {name}" class="brand-logo">
          </a>
          <p>Plombier chauffagiste &agrave; {city} &mdash; Plomberie, chauffage, sanitaire. D&eacute;pannage, installation et r&eacute;novation en Haute-Savoie.</p>
          <div class="social-row">
            <a href="#" aria-label="Facebook">{fb}</a>
            <a href="#" aria-label="Instagram">{ig}</a>
            <a href="#" aria-label="Avis Google">{go}</a>
          </div>
        </div>
        <div>
          <h4>Nos services</h4>
          <ul>{services_links}</ul>
        </div>
        <div>
          <h4>Liens utiles</h4>
          <ul>
            <li><a href="a-propos.html">&Agrave; propos</a></li>
            <li><a href="realisations.html">R&eacute;alisations</a></li>
            <li><a href="avis-clients.html">Avis clients</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="mentions-legales.html">Mentions l&eacute;gales</a></li>
          </ul>
        </div>
        <div>
          <h4>Zone d'intervention</h4>
          <ul>{communes_links}<li><a href="zones-intervention.html">Toutes les communes &rarr;</a></li></ul>
        </div>
      </div>
      <div class="footer-grid" style="grid-template-columns:1fr; border:none; padding-top:0; padding-bottom:26px;">
        <ul class="foot-contact" style="display:flex; flex-wrap:wrap; gap:24px;">
          <li>{phone_icon}<a href="{phone_href}">{phone}</a></li>
          <li>{mail_icon}<a href="mailto:{email}">{email}</a></li>
          <li>{pin_icon}<span>{addr}, {zip}</span></li>
        </ul>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span class="js-year">{year}</span> {legal} &mdash; Tous droits r&eacute;serv&eacute;s.</span>
        <span><a href="mentions-legales.html">Mentions l&eacute;gales</a> &middot; Site r&eacute;alis&eacute; avec soin en Haute-Savoie</span>
      </div>
    </div>
  </footer>
  <div class="mobile-call-bar">
    <a href="{phone_href}" style="color:#fff; display:flex; align-items:center; gap:10px;">{phone_icon_white} Appeler {phone}</a>
  </div>
  <script src="js/script.js"></script>
""".format(name=BIZ["name"], city=BIZ["city"], fb=icon("icon-facebook.svg"), ig=icon("icon-instagram.svg"),
           go=icon("icon-google.svg"), services_links=services_links, communes_links=communes_links,
           phone_icon=icon("icon-phone.svg"), phone_href=BIZ["phone_href"], phone=BIZ["phone_display"],
           mail_icon=icon("icon-mail.svg"), email=BIZ["email"], pin_icon=icon("icon-pin.svg"),
           addr=BIZ["address_line"], zip=BIZ["address_zip"], year=CURRENT_YEAR, legal=BIZ["legal"],
           phone_icon_white=icon("icon-phone-white.svg"))

# -----------------------------------------------------------------
# PAGE HEADER (bannière pages intérieures)
# -----------------------------------------------------------------
def build_page_header(title, lead, crumbs):
    crumb_html = ""
    for i, (label, href) in enumerate(crumbs):
        if href:
            crumb_html += '<a href="{href}">{label}</a>'.format(href=href, label=label)
        else:
            crumb_html += '<span>{label}</span>'.format(label=label)
        if i < len(crumbs) - 1:
            crumb_html += icon("icon-chevron-muted.svg", "icon") if False else ' &rarr; '
    return """<section class="page-header">
    <div class="container">
      <div class="breadcrumb">{crumbs}</div>
      <h1>{title}</h1>
      <p>{lead}</p>
    </div>
  </section>
""".format(crumbs=crumb_html, title=title, lead=lead)

# -----------------------------------------------------------------
# CTA banner
# -----------------------------------------------------------------
def build_cta_banner():
    return """<section class="cta-banner">
    <div class="container">
      <div class="text">
        <span class="icon-wrap">{icon}</span>
        <div>
          <h3>Besoin d'un plombier ?</h3>
          <p>Appelez-moi, j'interviens &agrave; {city} et dans tout le 74.</p>
        </div>
      </div>
      <a class="btn btn-primary" href="{phone_href}">{phone_icon} {phone}</a>
    </div>
  </section>
""".format(icon=icon("icon-phone-white.svg"), city=BIZ["city"], phone_href=BIZ["phone_href"],
           phone_icon=icon("icon-phone.svg", "icon"), phone=BIZ["phone_display"])

# -----------------------------------------------------------------
# Page wrapper
# -----------------------------------------------------------------
def wrap_page(title, description, path, main_html, active, active_service=None, extra_schema=None, include_topbar=True):
    schemas = [local_business_schema()]
    if extra_schema:
        schemas.append(extra_schema)
    head = build_head(title, description, path, schemas)
    topbar = build_topbar() if include_topbar else ""
    header = build_header(active, active_service)
    footer = build_footer()
    return """<!doctype html>
<html lang="fr">
<head>
{head}</head>
<body>
{topbar}{header}
  <main>
{main}
  </main>
{footer}
</body>
</html>
""".format(head=head, topbar=topbar, header=header, main=main_html, footer=footer)

def write_page(filename, html_content):
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    print("  ->", filename)

print("Fonctions communes chargées.")
