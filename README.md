# Site — Active Plomberie 74

Site vitrine statique (HTML/CSS/JS, sans dépendance externe) pour un plombier chauffagiste à Thyez (Haute-Savoie).

## Mettre le site en ligne

C'est un site 100% statique : il suffit d'héberger l'ensemble de ce dossier tel quel.

- **Le plus simple** : glisser-déposer ce dossier sur [Netlify Drop](https://app.netlify.com/drop), ou le déployer sur Vercel, GitHub Pages, OVH, o2switch, etc.
- Aucune base de données, aucun serveur applicatif requis.
- Pensez à mettre à jour `BIZ["domain"]` dans `build.py` (ou directement `_data.json`) avec le vrai nom de domaine avant de régénérer `sitemap.xml` / `robots.txt` / les balises `canonical`.

## Structure

```
index.html                 Page d'accueil
nos-services.html           Page listant les 4 services
depannage-plomberie.html    Détail service
chauffage.html              Détail service
chauffe-eau.html            Détail service
salle-de-bain.html          Détail service
realisations.html           Galerie de réalisations
avis-clients.html           Avis clients + note Google
a-propos.html                Page à propos
zones-intervention.html     Communes desservies
contact.html                 Formulaire de contact
mentions-legales.html       Mentions légales (à compléter)
css/style.css                Feuille de style unique
js/script.js                  Menu mobile, carrousel, formulaire, FAQ
images/                       Logo, icônes et illustrations (SVG maison, aucune photo externe)
robots.txt, sitemap.xml       SEO technique
```

## À compléter avant mise en ligne définitive

1. **Formulaire de contact** (`contact.html`) : le formulaire valide les champs et affiche une confirmation côté navigateur, mais n'est relié à aucun service d'envoi. Branchez un service comme [Formspree](https://formspree.io), Netlify Forms, ou un script serveur, puis mettez à jour l'attribut `action` du `<form id="contact-form">`. En attendant, le téléphone et l'e-mail (cliquables partout sur le site) restent le moyen de contact fonctionnel.
2. **Mentions légales** (`mentions-legales.html`) : le numéro de SIRET, l'hébergeur et le nom du directeur de la publication sont en placeholders `[à compléter]` — à remplir avec les vraies informations de l'entreprise.
3. **Réalisations et avis** : les vignettes "avant/après" sont des illustrations représentatives (icônes stylisées), pas des photos de chantiers réels — à remplacer par de vraies photos dès que possible. Les 3 avis clients affichés sont ceux fournis dans la maquette d'origine ; ne pas en ajouter d'inventés, mais les remplacer par de vrais avis Google au fil du temps.
4. **Domaine réel** : remplacer `active-plomberie74.fr` par le nom de domaine définitif partout où il apparaît (`build.py`, balises `canonical`/Open Graph, schema.org, sitemap).
5. **Photos** : aucun accès réseau vers des banques d'images n'était disponible pour générer ce site ; le rendu s'appuie donc sur des icônes et illustrations vectorielles maison plutôt que des photos. Vous pouvez glisser de vraies photos dans `images/` et les référencer à la place des illustrations (`hero-illustration.svg`, `van-illustration.svg`, icônes de la galerie réalisations) pour un rendu encore plus convaincant.

## Régénérer le site après une modification de contenu (optionnel)

Le site a été généré avec un petit script Python pour garder toutes les pages cohérentes (même en-tête, même pied de page, mêmes coordonnées partout). Ce n'est pas nécessaire pour héberger le site, mais pratique pour le faire évoluer :

```bash
python3 build.py        # régénère _data.json (coordonnées, services, avis, communes...)
python3 pages.py        # régénère toutes les pages HTML à partir de _data.json
```

Modifiez les informations (téléphone, adresse, services, avis, communes desservies...) dans `build.py`, ou directement dans `_data.json`, puis relancez `python3 pages.py`.

## SEO déjà en place

- Données structurées schema.org (`LocalBusiness`/`Plumber`, `Service`, `FAQPage`) sur les pages concernées.
- Balises meta title/description uniques par page, Open Graph, canonical.
- `sitemap.xml` et `robots.txt`.
- Site responsive (mobile-first), maillage interne entre les pages, un bouton d'appel fixe sur mobile.
"# ActivePlomberie" 
