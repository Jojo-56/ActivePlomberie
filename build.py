# -*- coding: utf-8 -*-
"""
Générateur statique du site Active Plomberie 74.
Exécuter avec: python3 build.py
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------
# Données de l'entreprise
# ---------------------------------------------------------------
BIZ = {
    "name": "Active Plomberie",
    "legal": "Active Plomberie 74",
    "phone_display": "06 04 67 09 43",
    "phone_href": "tel:+33604670943",
    "email": "activeplomberie74@gmail.com",
    "address_line": "320 rue des Sorbiers",
    "address_zip": "74300 Thyez",
    "city": "Thyez",
    "radius": "40 km",
    "rating": "4.9",
    "reviews": "50",
    "domain": "https://www.active-plomberie74.fr",
}

COMMUNES = ["Thyez", "Cluses", "Scionzier", "Marignier", "Bonneville", "Sallanches",
            "La Roche-sur-Foron", "Annemasse", "Marnaz", "Vougy"]

SERVICES = [
    {
        "slug": "depannage-plomberie", "icon": "icon-droplet.svg",
        "title": "Dépannage plomberie",
        "short": "Fuite d'eau, canalisation bouchée, chasse d'eau.",
        "hero_lead": "Fuite d'eau, canalisation bouchée, WC en panne... nos plombiers interviennent à Thyez et dans toute la Haute-Savoie.",
        "items": [
            ("Recherche et réparation de fuite", "Détection précise et réparation sans dégât inutile."),
            ("Débouchage de canalisation", "Évier, douche, WC : intervention efficace et soignée."),
            ("Réparation de robinetterie", "Mitigeurs, joints, chasses d'eau qui fuient."),
            ("Dépannage WC et chasse d'eau", "Remise en état ou remplacement le jour même si besoin."),
        ],
        "faq": [
            ("Intervenez-vous le week-end ?",
             "Je suis disponible du lundi au samedi. Contactez-moi directement pour vérifier mes disponibilités selon votre demande."),
            ("Quel est le délai d'intervention moyen ?",
             "Cela dépend de votre secteur et de la nature de la demande. Contactez-moi directement au 06 04 67 09 43 pour connaître le délai avant de me déplacer."),
            ("Le devis est-il vraiment gratuit et sans engagement ?",
             "Oui, chaque devis est établi gratuitement et sans engagement de votre part, avant le début des travaux."),
        ],
    },
    {
        "slug": "chauffage", "icon": "icon-radiator.svg",
        "title": "Chauffage",
        "short": "Installation, entretien et dépannage de vos systèmes de chauffage.",
        "hero_lead": "De l'installation d'une nouvelle chaudière à l'entretien annuel, nous assurons le bon fonctionnement de votre système de chauffage toute l'année.",
        "items": [
            ("Installation de chaudière", "Chaudière gaz, électrique ou à condensation, conseils adaptés à votre logement."),
            ("Entretien annuel", "Contrôle et nettoyage pour un chauffage performant et sécurisé."),
            ("Dépannage panne de chauffage", "Diagnostic précis en cas de panne, même en hiver."),
            ("Remplacement de radiateurs", "Radiateurs eau chaude, sèche-serviettes, équilibrage du réseau."),
        ],
        "faq": [
            ("L'entretien annuel de chaudière est-il obligatoire ?",
             "Oui, l'entretien annuel est une obligation légale pour la plupart des chaudières. Il garantit aussi votre sécurité et réduit votre consommation."),
            ("Quels types de chauffage installez-vous ?",
             "Nous installons et entretenons les chaudières gaz, électriques et à condensation, ainsi que les radiateurs eau chaude et sèche-serviettes."),
            ("Que faire en cas de panne de chauffage en hiver ?",
             "Contactez-nous directement au 06 04 67 09 43 pour un diagnostic et une remise en route."),
        ],
    },
    {
        "slug": "chauffe-eau", "icon": "icon-water-heater.svg",
        "title": "Chauffe-eau",
        "short": "Installation, remplacement et entretien de chauffe-eau électrique ou thermodynamique.",
        "hero_lead": "Plus d'eau chaude ou chauffe-eau vieillissant ? Nous installons, remplaçons et entretenons tous types de chauffe-eau.",
        "items": [
            ("Chauffe-eau électrique", "Installation et remplacement, tous volumes, toutes marques."),
            ("Chauffe-eau thermodynamique", "Solution économique et écologique, éligible aux aides."),
            ("Détartrage et entretien", "Pour prolonger la durée de vie de votre appareil."),
            ("Dépannage panne d'eau chaude", "Diagnostic précis en cas de panne ou de fuite."),
        ],
        "faq": [
            ("Quelle est la durée de vie moyenne d'un chauffe-eau ?",
             "En moyenne 10 à 15 ans, selon l'entretien et la qualité de l'eau. Un détartrage régulier prolonge sa durée de vie."),
            ("Chauffe-eau électrique ou thermodynamique, lequel choisir ?",
             "Le thermodynamique consomme moins d'électricité et convient bien en remplacement, mais nécessite un local suffisamment ventilé. Nous vous conseillons selon votre logement."),
        ],
    },
    {
        "slug": "salle-de-bain", "icon": "icon-bathtub.svg",
        "title": "Salle de bain",
        "short": "Rénovation complète de salle de bain, sanitaires et robinetterie.",
        "hero_lead": "De la conception à la pose, nous accompagnons votre projet de rénovation de salle de bain, clé en main.",
        "items": [
            ("Conception et devis personnalisé", "Un projet adapté à votre espace et à votre budget."),
            ("Douche à l'italienne", "Création sur-mesure, étanchéité garantie."),
            ("Remplacement baignoire ou douche", "Dépose de l'ancien équipement et pose du nouveau."),
            ("Robinetterie et sanitaires", "Vasques, WC, meubles et accessoires."),
        ],
        "faq": [
            ("Combien de temps dure une rénovation de salle de bain ?",
             "Comptez en moyenne 1 à 2 semaines pour une rénovation complète, selon l'ampleur des travaux. Un planning précis vous est communiqué avec le devis."),
            ("Proposez-vous un accompagnement pour le choix des matériaux ?",
             "Oui, nous vous conseillons sur le choix des matériaux et équipements en fonction de votre budget et de vos goûts."),
        ],
    },
]

# Avis clients authentiques, repris de la fiche Google "Active Plomberie 74"
# (https://www.google.com/maps/search/Active+Plomberie+74+Thyez), 4,9/5 sur 50 avis.
TESTIMONIALS = [
    {"name": "Anne J.", "initials": "AJ",
     "text": "J'ai fait appel à ce plombier et je suis très satisfaite de son intervention. Il a été disponible très rapidement, est arrivé à l'heure, et a tout de suite trouvé la cause du problème. Le travail a été fait proprement et efficacement. Je recommande sans hésiter !"},
    {"name": "Véronique P.", "initials": "VP",
     "text": "J'ai fait appel à ce plombier pour intervenir sur mes toilettes et j'en suis vraiment ravie. Il a été très professionnel, rapide et le travail est impeccable. Je recommande vivement !"},
    {"name": "Lionel T.", "initials": "LT",
     "text": "Intervention rapide, bon travail et très sympa, je referais appel à lui si nécessaire, je recommande fortement. Merci."},
    {"name": "Evelyne J.", "initials": "EJ",
     "text": "Professionnel réactif et disponible rapidement. Efficace, agréable et cordial. Nous recommandons vivement."},
    {"name": "Frédéric B.", "initials": "FB",
     "text": "Un professionnel sérieux, ponctuel et soigné. Nous avons fait appel à ses services à plusieurs reprises et il a toujours su réaliser les travaux demandés rapidement et pour un coût raisonnable."},
    {"name": "Céline", "initials": "C",
     "text": "Ravie ! Personne professionnelle et qui donne de bons conseils ! À l'écoute du client et rapide pour intervenir. Je recommande."},
    {"name": "Cécile F.", "initials": "CF",
     "text": "Très réactive, bonne communication, très efficace, je recommande à 100 %."},
    {"name": "Lucie B.", "initials": "LB",
     "text": "Efficacité, rapidité et explications claires ! Je recommande Active Plomberie sans hésiter."},
]

AVATAR_COLORS = ["#1d6fe0", "#0f4fb0", "#3f8cff"]

REALISATIONS = [
    {"title": "Rénovation salle de bain complète", "city": "Haute-Savoie", "icon": "icon-bathtub.svg",
     "photo": "avant-apres-salle-de-bain.webp", "before_after": True},
    {"title": "Remplacement chauffe-eau", "city": "Haute-Savoie", "icon": "icon-water-heater.svg",
     "photo": "chauffe-eau-installation.jpg", "before_after": False},
    {"title": "Installation de chaudière", "city": "Haute-Savoie", "icon": "icon-radiator.svg",
     "photo": "chaudiere-installation.jpg", "before_after": False},
    {"title": "Dépannage fuite d'eau", "city": "Haute-Savoie", "icon": "icon-droplet.svg",
     "photo": "reparation-robinet.jpg", "before_after": False},
]

REALISATIONS_GALERIE = [
    {"title": "Double vasque", "photo": "bain-double-vasque-1.jpg"},
    {"title": "Douche à l'italienne, finitions dorées", "photo": "douche-luxe-dore.jpg"},
    {"title": "Douche vitrée, faïence grise", "photo": "douche-finie-1.webp"},
    {"title": "Rénovation salle d'eau complète", "photo": "bain-baignoire-1.jpg"},
    {"title": "Douche à l'italienne", "photo": "douche-finie-2.webp"},
    {"title": "Faïence bleu nuit", "photo": "douche-bleue.jpg"},
    {"title": "WC suspendu, finitions soignées", "photo": "toilette-finie.jpg"},
    {"title": "Distribution chauffage en cuivre", "photo": "distribution-cuivre.jpg"},
]

print("Données chargées. Voir build_pages.py pour la génération HTML.")

with open(os.path.join(ROOT, "_data.json"), "w", encoding="utf-8") as f:
    json.dump({"biz": BIZ, "communes": COMMUNES, "services": SERVICES,
               "testimonials": TESTIMONIALS, "avatar_colors": AVATAR_COLORS,
               "realisations": REALISATIONS, "realisations_galerie": REALISATIONS_GALERIE},
              f, ensure_ascii=False, indent=2)
