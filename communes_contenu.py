# -*- coding: utf-8 -*-
"""Contenu propre à chaque commune desservie (pages plombier-<commune>.html).

Chaque commune a un texte réellement différent (SEO local : Google pénalise
les pages villes identiques où seul le nom change). Distances et temps de
trajet depuis Thyez = ordres de grandeur par la route. "interventions" =
types de chantiers réellement confiés à Active Plomberie 74 dans la commune
(repris des devis acceptés dans Alya, sans aucune donnée client) ; laisser
vide plutôt que d'inventer.
"""

COMMUNES_CONTENU = {
    "Thyez": {
        "cp": "74300", "km": 0, "min": 0,
        "intro": "Thyez, c'est chez nous : l'atelier d'Active Plomberie 74 est installé rue des Sorbiers, dans la zone économique des Lacs. Quand vous appelez depuis Thyez, l'artisan est souvent à quelques minutes de chez vous, ce qui permet d'intervenir vite sur une fuite, un chauffe-eau en panne ou un WC bouché, et de passer faire un relevé avant devis sans frais de déplacement importants.",
        "contexte": "La commune mêle lotissements pavillonnaires, petits collectifs et un tissu d'entreprises et d'ateliers autour de la zone des Lacs. Côté particuliers, les demandes les plus courantes concernent le remplacement de chauffe-eau, la rénovation de salles de bain des années 1980-1990 et les fuites sur des installations anciennes. Côté professionnels, nous intervenons sur les sanitaires, les arrivées d'eau et l'eau chaude des locaux.",
        "interventions": ["Travaux de plomberie pour un centre de formation", "Remplacement de douche et pose de cumulus 200 litres chez des particuliers (devis en cours)"],
        "voisines": ["Cluses", "Marnaz", "Marignier", "Scionzier", "Vougy"],
        "faq": [
            ("En combien de temps pouvez-vous venir à Thyez ?", "Nous sommes basés à Thyez : pour une urgence (fuite, dégât des eaux), l'intervention peut souvent avoir lieu dans la journée, selon le planning."),
            ("Faites-vous des devis pour les entreprises de la zone des Lacs ?", "Oui. Active Plomberie 74 travaille aussi pour les professionnels : sanitaires, arrivées d'eau, eau chaude, entretien des installations."),
        ],
    },
    "Cluses": {
        "cp": "74300", "km": 6, "min": 10,
        "intro": "Cluses, berceau du décolletage et principale ville de la moyenne vallée de l'Arve, est à une dizaine de minutes de notre atelier de Thyez. Active Plomberie 74 y intervient pour les particuliers comme pour les commerces et entreprises : dépannage de plomberie, remplacement de chauffe-eau, entretien du chauffage et rénovation complète de salles de bain.",
        "contexte": "Le parc immobilier de Cluses compte beaucoup d'immeubles des années 1960 à 1980 et de copropriétés, où l'on rencontre des colonnes et canalisations vieillissantes, des robinets d'arrêt grippés et des salles de bain à moderniser. Dans les maisons des hauteurs, ce sont plutôt les chauffe-eau et les circuits de chauffage qui demandent de l'attention. Pour les professionnels, nous traitons aussi les demandes de traitement de l'eau et de mise aux normes.",
        "interventions": ["Pose d'un filtre à charbon avec cartouche pour un professionnel", "Recherche et réparation d'une fuite sur radiateur en résidence (devis en cours)"],
        "voisines": ["Thyez", "Scionzier", "Marnaz", "Magland"],
        "faq": [
            ("Intervenez-vous dans les copropriétés de Cluses ?", "Oui, nous intervenons dans les appartements comme dans les parties communes, en lien avec le syndic si nécessaire (fuite sur colonne, remplacement de vanne, dégât des eaux)."),
            ("Quel délai pour un chauffe-eau en panne à Cluses ?", "Cluses est à environ 10 minutes de l'atelier : nous nous organisons pour rétablir l'eau chaude au plus vite, et proposons un devis de remplacement adapté au logement."),
        ],
    },
    "Scionzier": {
        "cp": "74950", "km": 8, "min": 12,
        "intro": "À Scionzier, à l'entrée de la vallée du Reposoir, Active Plomberie 74 intervient en une douzaine de minutes depuis Thyez. Maisons individuelles, logements collectifs ou ateliers de décolletage : nous prenons en charge la plomberie, le chauffage et l'eau chaude, du petit dépannage à la rénovation de salle de bain.",
        "contexte": "Commune à la fois résidentielle et industrielle, Scionzier compte de nombreux pavillons construits entre les années 1970 et 2000. Les chauffe-eau électriques arrivés en fin de vie, les mitigeurs qui fuient et les baignoires à remplacer par une douche plus accessible font partie des demandes les plus fréquentes. Dans les secteurs plus en hauteur, les hivers rigoureux rendent utile une vérification des canalisations exposées au gel.",
        "interventions": [],
        "voisines": ["Cluses", "Marnaz", "Thyez", "Le Reposoir"],
        "faq": [
            ("Remplacez-vous les baignoires par des douches à Scionzier ?", "Oui, c'est une demande fréquente : dépose de la baignoire, pose d'un receveur extra-plat ou d'une douche à l'italienne, paroi et robinetterie, avec un devis détaillé."),
            ("Comment éviter le gel des canalisations en hiver ?", "Isoler les tuyaux situés dans les garages, caves ou vides sanitaires, et purger les robinets extérieurs avant les premières gelées. Nous pouvons vérifier les points sensibles."),
        ],
    },
    "Marnaz": {
        "cp": "74460", "km": 4, "min": 8,
        "intro": "Marnaz, voisine immédiate de Thyez et de Scionzier, fait partie des communes où Active Plomberie 74 intervient le plus rapidement : moins de dix minutes de trajet. Nous y réalisons des dépannages, des remplacements de chauffe-eau, des travaux de chauffage et des modifications de réseaux d'eau dans les maisons comme dans les appartements.",
        "contexte": "Majoritairement résidentielle, Marnaz associe pavillons et petits immeubles. Beaucoup de logements ont des installations d'origine qu'il faut adapter : nourrice de distribution à reprendre, arrivée d'eau à déplacer lors d'une rénovation de cuisine ou de salle de bain, ballon d'eau chaude à remplacer par un modèle plus économe. Nous conseillons sur les solutions les plus adaptées au budget et à la configuration du logement.",
        "interventions": ["Modification d'une nourrice de distribution d'eau chez un particulier"],
        "voisines": ["Thyez", "Scionzier", "Cluses", "Marignier"],
        "faq": [
            ("Pouvez-vous modifier la distribution d'eau de ma maison à Marnaz ?", "Oui : reprise ou remplacement de nourrice, ajout d'un réducteur de pression, déplacement d'arrivées d'eau, en cuivre, PER ou multicouche."),
            ("Le devis est-il payant ?", "Non, le devis est gratuit et sans engagement. À Marnaz, nous pouvons généralement passer rapidement pour voir l'installation."),
        ],
    },
    "Marignier": {
        "cp": "74970", "km": 5, "min": 8,
        "intro": "Marignier, au confluent du Giffre et de l'Arve, est à moins de dix minutes de notre atelier. Active Plomberie 74 y intervient pour les fuites, les chauffe-eau, le chauffage et la rénovation de salles de bain, auprès des particuliers et des professionnels.",
        "contexte": "Entre centre-bourg, hameaux et lotissements récents, l'habitat de Marignier est varié. Dans les maisons anciennes, nous remplaçons souvent des canalisations en acier galvanisé ou en plomb par du multicouche, et modernisons des salles de bain d'origine : baignoire acrylique à changer, douche à créer, WC suspendu. Les logements plus récents nous sollicitent surtout pour l'entretien du chauffage et le remplacement de ballons d'eau chaude.",
        "interventions": ["Remplacement d'une baignoire acrylique (devis en cours)"],
        "voisines": ["Thyez", "Vougy", "Bonneville", "Saint-Jeoire"],
        "faq": [
            ("Remplacez-vous les vieilles canalisations à Marignier ?", "Oui, nous remplaçons les tuyaux galvanisés ou en plomb par du multicouche ou du PER, ce qui supprime les fuites récurrentes et améliore la qualité de l'eau."),
            ("Intervenez-vous dans les hameaux autour de Marignier ?", "Oui, toute la commune est desservie, ainsi que la vallée du Giffre jusqu'à Taninges et Samoëns."),
        ],
    },
    "Vougy": {
        "cp": "74130", "km": 7, "min": 10,
        "intro": "Petite commune située entre Marignier et Bonneville, Vougy est à une dizaine de minutes de Thyez. Active Plomberie 74 y intervient pour tous les travaux de plomberie et de chauffage : dépannage, remplacement de chauffe-eau, installation de radiateurs, rénovation de salle de bain.",
        "contexte": "À Vougy, l'habitat est surtout composé de maisons individuelles, souvent avec sous-sol ou garage où se trouvent le chauffe-eau et la chaufferie. Ce sont précisément ces pièces non chauffées qui posent problème en hiver : canalisations exposées au froid, groupes de sécurité qui fuient, ballons entartrés. Nous proposons un diagnostic de l'installation et, si besoin, un remplacement par un chauffe-eau adapté à la taille du foyer.",
        "interventions": [],
        "voisines": ["Marignier", "Bonneville", "Thyez", "Ayse"],
        "faq": [
            ("Mon groupe de sécurité fuit, est-ce grave ?", "Un léger écoulement pendant la chauffe est normal ; une fuite permanente ne l'est pas. Nous le remplaçons rapidement pour éviter une surconsommation d'eau et protéger le ballon."),
            ("Installez-vous des chauffe-eau thermodynamiques à Vougy ?", "Oui. Dans une maison avec garage ou sous-sol, c'est souvent une bonne solution pour réduire la facture d'électricité ; nous vérifions la faisabilité lors du devis."),
        ],
    },
    "Bonneville": {
        "cp": "74130", "km": 10, "min": 15,
        "intro": "Sous-préfecture de la Haute-Savoie, Bonneville est à environ quinze minutes de notre atelier de Thyez. C'est l'une des communes où Active Plomberie 74 réalise le plus de chantiers : rénovation de salles de bain, remplacement de canalisations, eau chaude sanitaire et dépannages.",
        "contexte": "Le centre de Bonneville compte de nombreux immeubles anciens avec caves, où les canalisations en acier galvanisé arrivent en fin de vie : fuites, perte de pression, eau colorée. Nous les remplaçons par du multicouche. Dans les appartements comme dans les maisons, la transformation d'une baignoire en douche est aussi très demandée, avec receveur extra-plat, coffrage et paroi sur mesure.",
        "interventions": [
            "Remplacement d'une conduite en acier galvanisé par du multicouche en cave",
            "Dépose d'une baignoire et installation d'un receveur de douche avec coffrage",
            "Remplacement d'un receveur de douche",
            "Remplacement des équipements d'eau chaude sanitaire",
            "Dépose et pose de robinetterie",
        ],
        "voisines": ["Vougy", "Marignier", "Saint-Pierre-en-Faucigny", "Ayse", "La Roche-sur-Foron"],
        "faq": [
            ("Faites-vous la rénovation complète de salle de bain à Bonneville ?", "Oui : dépose, plomberie, receveur ou baignoire, meuble vasque, WC, robinetterie. Nous avons réalisé plusieurs transformations de baignoire en douche à Bonneville."),
            ("Mes tuyaux en cave fuient, que faire ?", "Coupez l'eau au compteur et appelez-nous. Dans les immeubles anciens de Bonneville, le remplacement des conduites galvanisées par du multicouche règle durablement le problème."),
        ],
    },
    "Saint-Pierre-en-Faucigny": {
        "cp": "74800", "km": 17, "min": 20,
        "intro": "Saint-Pierre-en-Faucigny, entre Bonneville et La Roche-sur-Foron, est à une vingtaine de minutes de Thyez. Active Plomberie 74 y intervient pour les particuliers et pour les entreprises de la commune : installation sanitaire, eau chaude, chauffage, dépannage.",
        "contexte": "La commune combine quartiers résidentiels en plein développement et zones d'activités. Dans les maisons récentes, les demandes portent surtout sur l'équipement des salles de bain (colonne de douche, meuble vasque, WC suspendu) et l'entretien du chauffage. Pour les professionnels, nous réalisons des raccordements, des branchements d'eau pour les ateliers et l'entretien des installations sanitaires.",
        "interventions": ["Installation d'une colonne de douche pour un professionnel", "Branchement d'eau pour un atelier de décolletage (devis en cours)"],
        "voisines": ["Bonneville", "La Roche-sur-Foron", "Amancy", "Arenthon"],
        "faq": [
            ("Travaillez-vous pour les entreprises de Saint-Pierre-en-Faucigny ?", "Oui, nous réalisons des branchements, des sanitaires et de l'eau chaude pour les locaux professionnels et ateliers."),
            ("Quel est le délai d'intervention ?", "Comptez environ 20 minutes de trajet depuis Thyez ; les rendez-vous sont planifiés rapidement, en priorité pour les urgences."),
        ],
    },
    "La Roche-sur-Foron": {
        "cp": "74800", "km": 23, "min": 25,
        "intro": "Cité médiévale au cœur du Faucigny, La Roche-sur-Foron est à environ 25 minutes de Thyez. Active Plomberie 74 y intervient pour les travaux de plomberie et de chauffage des particuliers et des professionnels, avec un devis gratuit établi après visite.",
        "contexte": "Le centre historique et ses immeubles anciens demandent un savoir-faire particulier : passages de canalisations contraints, colonnes vétustes, salles de bain exiguës à optimiser. Autour, les quartiers pavillonnaires plus récents nous sollicitent pour le remplacement de chauffe-eau, l'installation de radiateurs ou le passage à un chauffage plus économe. Nous adaptons chaque solution aux contraintes du bâti.",
        "interventions": [],
        "voisines": ["Saint-Pierre-en-Faucigny", "Bonneville", "Amancy", "Saint-Laurent"],
        "faq": [
            ("Intervenez-vous dans le centre ancien de La Roche-sur-Foron ?", "Oui, nous avons l'habitude des immeubles anciens : remplacement de colonnes, création de salle de bain dans un petit espace, reprise de canalisations."),
            ("Le déplacement jusqu'à La Roche-sur-Foron est-il facturé ?", "Un forfait de déplacement est indiqué clairement sur le devis, qui reste gratuit et sans engagement."),
        ],
    },
    "Sallanches": {
        "cp": "74700", "km": 22, "min": 20,
        "intro": "Face au Mont-Blanc, Sallanches est à une vingtaine de minutes de notre atelier par la vallée de l'Arve. Active Plomberie 74 y intervient pour la plomberie, le chauffage, l'eau chaude et la rénovation de salles de bain, dans les résidences principales comme dans les logements de location.",
        "contexte": "À Sallanches, les hivers froids sollicitent fortement les installations de chauffage et d'eau chaude. Nous intervenons sur des chaudières et circuits de radiateurs à entretenir ou à moderniser, des ballons à remplacer et des canalisations à protéger du gel. Les appartements des années 1970-1980 du centre sont aussi nombreux à faire rénover leur salle de bain.",
        "interventions": [],
        "voisines": ["Passy", "Domancy", "Magland", "Combloux"],
        "faq": [
            ("Entretenez-vous les installations de chauffage à Sallanches ?", "Oui : désembouage, purge et équilibrage des radiateurs, remplacement de vannes et de circulateurs, conseils pour réduire la consommation."),
            ("Pouvez-vous intervenir sur un logement de location ?", "Oui, pour les propriétaires bailleurs comme pour les locataires, avec un devis clair à transmettre à l'agence si besoin."),
        ],
    },
    "Annemasse": {
        "cp": "74100", "km": 35, "min": 30,
        "intro": "Agglomération frontalière de Genève, Annemasse est à une trentaine de minutes de Thyez par l'autoroute. Active Plomberie 74 y réalise surtout des chantiers planifiés : rénovation de salle de bain, remplacement de chauffe-eau, travaux de chauffage et mises aux normes.",
        "contexte": "L'habitat d'Annemasse est majoritairement collectif : copropriétés, résidences récentes et immeubles plus anciens du centre. Les salles de bain compactes, les chauffe-eau placés en placard et les colonnes communes imposent des solutions sur mesure. Nous prenons le temps d'une visite pour proposer un devis précis, avec un planning qui limite la gêne pour les occupants.",
        "interventions": [],
        "voisines": ["Ambilly", "Gaillard", "Ville-la-Grand", "Étrembières"],
        "faq": [
            ("Intervenez-vous à Annemasse pour des petits dépannages ?", "Nous privilégions à Annemasse les chantiers planifiés (rénovation, remplacement d'équipements). Pour une urgence, appelez-nous : nous vous dirons tout de suite si nous pouvons venir."),
            ("Rénovez-vous les petites salles de bain d'appartement ?", "Oui : douche à la place de la baignoire, meuble vasque compact, WC suspendu, tout est pensé pour gagner de la place."),
        ],
    },
    "Taninges": {
        "cp": "74440", "km": 15, "min": 20,
        "intro": "Dans la vallée du Giffre, sur la route du Praz de Lys, Taninges est à une vingtaine de minutes de Thyez. Active Plomberie 74 y intervient régulièrement, en particulier pour des professionnels : réseaux d'eau, compteurs, eau chaude, relevage et sanitaires.",
        "contexte": "Taninges associe centre-bourg ancien, hameaux de montagne et activités touristiques. Les bâtiments anciens ont souvent des compteurs et canalisations en cave à reprendre, et l'altitude impose de protéger les installations du gel. Nous réalisons aussi des installations spécifiques comme les pompes de relevage, les fontaines d'eau ou la ventilation des locaux.",
        "interventions": [
            "Déplacement de deux compteurs d'eau hors de la cave et ajout d'un troisième compteur",
            "Installation d'une mini-pompe de relevage et réparation de sertissage inox",
            "Pose de deux fontaines d'eau",
            "Remplacement du groupe de sécurité d'un ballon d'eau chaude",
            "Pose d'une aération ventilée",
        ],
        "voisines": ["Mieussy", "Marignier", "Saint-Jeoire", "Samoëns"],
        "faq": [
            ("Pouvez-vous déplacer des compteurs d'eau à Taninges ?", "Oui, nous avons déjà réalisé ce type de travaux à Taninges : déplacement hors cave, création de nouveaux compteurs divisionnaires, reprise des réseaux."),
            ("Installez-vous des pompes de relevage ?", "Oui, pour évacuer les eaux usées d'une pièce située sous le niveau du réseau (sous-sol, cave aménagée, sanitaires ajoutés)."),
        ],
    },
    "Samoëns": {
        "cp": "74340", "km": 27, "min": 30,
        "intro": "Station-village du Grand Massif, Samoëns est à une demi-heure de Thyez par la vallée du Giffre. Active Plomberie 74 y intervient pour les chalets, appartements et résidences secondaires : eau chaude, chauffage, plomberie et rénovation de salles de bain.",
        "contexte": "À Samoëns, beaucoup de logements sont occupés par intermittence : ballons d'eau chaude à remplacer, installations à mettre hors gel ou à remettre en service, fuites découvertes à l'arrivée des vacances. Nous planifions les travaux hors saison quand c'est possible et intervenons sur les chalets comme sur les résidences de tourisme.",
        "interventions": ["Dépose et repose de ballons d'eau chaude chez un particulier"],
        "voisines": ["Morillon", "Verchaix", "Taninges", "Sixt-Fer-à-Cheval"],
        "faq": [
            ("Remplacez-vous les ballons d'eau chaude des chalets à Samoëns ?", "Oui, dépose de l'ancien ballon, pose et raccordement du nouveau, avec vérification du groupe de sécurité."),
            ("Pouvez-vous intervenir en l'absence du propriétaire ?", "Oui, sur rendez-vous avec remise des clés ou accès par l'agence ; nous envoyons un compte rendu et des photos après l'intervention."),
        ],
    },
    "La Clusaz": {
        "cp": "74220", "km": 45, "min": 50,
        "intro": "Station de ski des Aravis, La Clusaz est plus éloignée de Thyez, mais Active Plomberie 74 y réalise des chantiers planifiés, notamment pour des hébergements touristiques : installation de chauffe-eau, équipement de salles de bain, rénovations.",
        "contexte": "Chalets, résidences de tourisme et logements saisonniers constituent l'essentiel de l'habitat de La Clusaz. Les besoins en eau chaude y sont importants en haute saison, et les travaux doivent souvent être réalisés entre deux saisons. Nous intervenons sur devis, pour des chantiers organisés à l'avance : production d'eau chaude, sanitaires, baignoires et douches.",
        "interventions": ["Déplacement et installation de deux chauffe-eau électriques pour un hébergement", "Installation d'une baignoire acrylique et de ses accessoires"],
        "voisines": ["Le Grand-Bornand", "Saint-Jean-de-Sixt", "Thônes", "Les Villards-sur-Thônes"],
        "faq": [
            ("Intervenez-vous pour les résidences de tourisme à La Clusaz ?", "Oui, nous réalisons des chantiers planifiés pour les hébergements : eau chaude, salles de bain, remplacement d'équipements entre deux saisons."),
            ("Faites-vous du dépannage d'urgence à La Clusaz ?", "La distance ne permet pas toujours une intervention immédiate ; nous privilégions les travaux planifiés. Appelez-nous pour en discuter."),
        ],
    },
}

# Conseil de l'artisan propre à chaque commune + une question fréquente
# supplémentaire (contenu unique, ajouté après le contrôle "avant/après" :
# les pages restaient sous l'objectif de longueur).
CONSEILS = {
    "Thyez": ("Avant de rénover une salle de bain à Thyez, vérifiez l'état des arrivées d'eau et des évacuations cachées derrière le carrelage : dans les maisons des années 1980, remplacer les tuyaux en même temps que les sanitaires coûte bien moins cher que de rouvrir les murs quelques années plus tard. Nous faisons ce diagnostic lors de la visite de devis, gratuitement.",
              ("Pouvez-vous passer voir l'installation avant de chiffrer ?", "Oui. À Thyez, la visite est rapide à organiser : nous regardons l'existant, prenons les mesures et vous remettons un devis détaillé.")),
    "Marnaz": ("Si la pression de l'eau est trop forte chez vous (robinets qui cognent, chasse d'eau qui fuit, flexibles qui lâchent), un réducteur de pression installé après le compteur protège toute l'installation. C'est une petite intervention, souvent réalisée en moins d'une heure, qui évite bien des fuites dans les maisons de Marnaz.",
               ("Mes robinets font du bruit quand je les ferme, pourquoi ?", "C'est souvent un coup de bélier dû à une pression trop élevée. Un réducteur de pression ou un anti-bélier règle le problème.")),
    "Marignier": ("Dans une maison ancienne de Marignier, une eau légèrement colorée au premier tirage ou une baisse de débit sont souvent les signes de canalisations galvanisées qui s'entartrent et rouillent de l'intérieur. Plutôt que de réparer fuite après fuite, il est plus économique de remplacer le tronçon principal en une seule fois.",
                  ("Combien de temps dure un remplacement de canalisations ?", "Pour une maison, comptez généralement une à trois journées selon l'accessibilité ; l'eau n'est coupée que pendant les raccordements.")),
    "Cluses": ("En appartement à Cluses, repérez l'emplacement du robinet d'arrêt de votre logement et vérifiez qu'il se ferme bien : en cas de fuite, c'est lui qui limite les dégâts chez vous et chez vos voisins du dessous. S'il est grippé, nous pouvons le remplacer lors d'une intervention courte.",
               ("Qui paie la réparation d'une fuite en copropriété ?", "Cela dépend de l'endroit de la fuite : partie privative ou colonne commune. Nous identifions l'origine et rédigeons un constat utile pour le syndic et l'assurance.")),
    "Scionzier": ("Pour une douche plus accessible à Scionzier, un receveur extra-plat posé à la place de la baignoire est souvent la solution la plus simple : moins de travaux qu'une douche à l'italienne maçonnée, une installation en quelques jours et un sol plus facile à entretenir.",
                  ("Faut-il refaire tout le carrelage pour changer une baignoire ?", "Pas forcément : un receveur aux bonnes dimensions et des panneaux muraux permettent souvent de limiter les travaux au seul coin douche.")),
    "Vougy": ("Un chauffe-eau électrique dure en moyenne 10 à 15 ans. Si le vôtre approche de cet âge et chauffe moins bien, anticiper son remplacement évite de se retrouver sans eau chaude un matin d'hiver. À Vougy, où il est souvent installé au garage, pensez aussi à vérifier le groupe de sécurité une fois par mois.",
              ("Quelle capacité de chauffe-eau choisir ?", "En règle générale : 100 litres pour 1 à 2 personnes, 150 à 200 litres pour 3 à 4 personnes, 250 à 300 litres au-delà.")),
    "Bonneville": ("Avant de transformer une baignoire en douche dans un immeuble ancien de Bonneville, il faut vérifier la pente et le diamètre de l'évacuation : c'est elle qui détermine si un receveur extra-plat est possible ou s'il faut surélever légèrement. Nous contrôlons ce point lors de la visite pour éviter les mauvaises surprises.",
                   ("Combien de temps pour transformer une baignoire en douche ?", "Généralement deux à quatre jours selon les finitions : dépose, reprise de l'évacuation, pose du receveur, de la paroi et de la robinetterie.")),
    "Taninges": ("À Taninges, les caves et sous-sols non chauffés exposent les compteurs et canalisations au gel. Isoler les tuyaux, installer un robinet de purge et, si besoin, déplacer le compteur dans un endroit protégé évite les ruptures de canalisations pendant les hivers rigoureux de la vallée du Giffre.",
                 ("Mon compteur d'eau a gelé, que faire ?", "Coupez l'eau, ne chauffez jamais à la flamme et appelez-nous : nous remplaçons les éléments abîmés et protégeons l'installation contre le gel.")),
    "Saint-Pierre-en-Faucigny": ("Pour une maison neuve ou récente à Saint-Pierre-en-Faucigny, choisir une robinetterie thermostatique pour la douche est un vrai confort : la température reste stable même si quelqu'un tire de l'eau ailleurs, et l'on évite les brûlures pour les enfants.",
                                 ("Posez-vous des colonnes de douche thermostatiques ?", "Oui, nous fournissons et posons colonnes de douche, mitigeurs thermostatiques et robinetterie, en adaptant les raccordements existants.")),
    "Sallanches": ("Avant l'hiver à Sallanches, un désembouage du circuit de chauffage et une purge des radiateurs améliorent nettement le confort : les boues accumulées dans les vieux circuits réduisent la chaleur et font travailler la chaudière pour rien. Une intervention tous les quelques années suffit.",
                   ("Mes radiateurs chauffent en haut mais pas en bas, pourquoi ?", "C'est souvent le signe de boues dans le circuit. Un désembouage rend la chaleur uniforme et réduit la consommation.")),
    "La Roche-sur-Foron": ("Dans les logements anciens de La Roche-sur-Foron, créer une salle d'eau dans un petit espace est tout à fait possible : WC suspendu, douche d'angle et meuble vasque compact permettent de gagner une place précieuse. Le point clé reste l'évacuation, que nous étudions avant tout chiffrage.",
                           ("Peut-on installer un WC suspendu dans un appartement ancien ?", "Oui, dans la plupart des cas, grâce à un bâti-support adapté ; nous vérifions la solidité de la cloison et le passage de l'évacuation.")),
    "Samoëns": ("Pour une résidence secondaire à Samoëns, la mise hors gel avant une longue absence est indispensable : coupure de l'eau, vidange des canalisations exposées et du chauffe-eau si le logement n'est pas chauffé. Nous pouvons réaliser la mise hors gel et la remise en service pour vous.",
                ("Proposez-vous la mise hors gel des chalets ?", "Oui, vidange et protection de l'installation avant votre départ, puis remise en eau et vérification à votre retour.")),
    "Annemasse": ("En appartement à Annemasse, remplacer un vieux chauffe-eau en placard par un modèle plat ou vertical plus compact libère souvent de la place. Si le logement est équipé d'une production collective, nous intervenons plutôt sur la robinetterie, les sanitaires et les réseaux privatifs.",
                  ("Existe-t-il des chauffe-eau pour les petits placards ?", "Oui, des modèles plats ou compacts de 50 à 100 litres s'installent dans des espaces réduits, y compris au-dessus d'un WC.")),
    "La Clusaz": ("Pour un hébergement touristique à La Clusaz, dimensionner la production d'eau chaude sur les pics de haute saison est essentiel : plusieurs ballons en parallèle ou un ballon de plus grande capacité évitent les douches froides quand toutes les chambres sont occupées.",
                  ("Planifiez-vous les travaux entre deux saisons ?", "Oui, nous organisons les chantiers au printemps ou à l'automne pour ne pas gêner l'exploitation.")),
}

# ── Corrections et repères vérifiés (sources : Wikipédia et l-itineraire.com,
# consultés le 24/09/2026). km/min = trajet routier depuis Thyez (l-itineraire ;
# La Roche-sur-Foron, Samoëns et La Clusaz = estimations, affichées "environ") ; None =
# commune limitrophe de Thyez (quelques minutes). Chantiers : uniquement les
# devis ACCEPTÉS (les devis encore en attente ne sont jamais affichés).
_MAJ = {
    "Thyez": dict(interventions=["Travaux de plomberie pour un centre de formation"],
                  reperes="6 344 habitants (2022), dans l'agglomération de Cluses ; église Saint-Théodule des XIIe-XIIIe siècles et sommet boisé du Mont Orchez.",
                  wiki="Thyez"),
    "Marnaz": dict(km=None, voisines=["Thyez", "Scionzier", "Vougy", "Mont-Saxonnex", "Le Reposoir"],
                   reperes="5 920 habitants (2022), au pied de la chaîne du Bargy et bordée au nord par l'Arve ; tradition du décolletage et de la poterie.",
                   wiki="Marnaz"),
    "Marignier": dict(km=None, interventions=[], voisines=["Thyez", "Vougy", "Ayze", "Saint-Jeoire", "Mieussy"],
                      reperes="6 432 habitants (2022), au confluent de l'Arve et du Giffre, dominée par le Môle (1 863 m) ; gare desservie par le Léman Express depuis 2019.",
                      wiki="Marignier"),
    "Cluses": dict(km=7.6, min=11, interventions=["Pose d'un filtre à charbon avec cartouche pour un professionnel"],
                   voisines=["Thyez", "Scionzier", "Marignier", "Magland"],
                   reperes="17 366 habitants (2022), « capitale du décolletage » héritée de l'horlogerie implantée en 1720 ; Pont Vieux de 1674, à l'entrée de la plus grande cluse des Alpes.",
                   wiki="Cluses"),
    "Scionzier": dict(km=None, reperes="9 074 habitants (2022), entre basse et haute vallée de l'Arve ; château de la Croix du XVIe siècle, classé monument historique.",
                      intro="À Scionzier, commune voisine de Thyez et porte de la vallée du Reposoir, Active Plomberie 74 intervient en quelques minutes. Maisons individuelles, logements collectifs ou ateliers de décolletage : nous prenons en charge la plomberie, le chauffage et l'eau chaude, du petit dépannage à la rénovation de salle de bain.",
                      wiki="Scionzier"),
    "Vougy": dict(km=None, voisines=["Cluses", "Bonneville", "Marignier", "Thyez", "Mont-Saxonnex"],
                  intro="Petite commune de la vallée de l'Arve située entre Cluses et Bonneville, Vougy est voisine de Thyez. Active Plomberie 74 y intervient pour tous les travaux de plomberie et de chauffage : dépannage, remplacement de chauffe-eau, installation de radiateurs, rénovation de salle de bain.",
                  reperes="1 622 habitants (2022), étirée entre l'Arve et les premières pentes du Mont-Saxonnex.",
                  wiki="Vougy_(Haute-Savoie)"),
    "Bonneville": dict(km=17, min=19, voisines=["Vougy", "Ayze", "Marignier", "Saint-Pierre-en-Faucigny", "La Roche-sur-Foron"],
                       intro="Sous-préfecture de la Haute-Savoie, Bonneville est à une vingtaine de minutes de notre atelier de Thyez. C'est l'une des communes où Active Plomberie 74 réalise le plus de chantiers : rénovation de salles de bain, remplacement de canalisations, eau chaude sanitaire et dépannages.",
                       reperes="13 320 habitants (2022), au confluent de l'Arve et du Borne, au pied du Môle et de la pointe d'Andey ; château des sires de Faucigny du XIIIe siècle.",
                       wiki="Bonneville_(Haute-Savoie)"),
    "Saint-Pierre-en-Faucigny": dict(km=21, min=21, interventions=["Installation d'une colonne de douche pour un professionnel"],
                                     voisines=["Bonneville", "Amancy", "Arenthon", "Saint-Laurent", "Le Petit-Bornand-les-Glières"],
                                     reperes="7 848 habitants (2022), commune née en 1965 de la fusion de Passeirier, Saint-Maurice-de-Rumilly et Saint-Pierre-de-Rumilly.",
                                     wiki="Saint-Pierre-en-Faucigny"),
    "Taninges": dict(km=19, min=25,
                     intro="Dans la vallée du Giffre, sur la route du Praz de Lys, Taninges est à environ 25 minutes de Thyez. Active Plomberie 74 y intervient régulièrement, en particulier pour des professionnels : réseaux d'eau, compteurs, eau chaude, relevage et sanitaires.",
                     reperes="3 501 habitants (2022), titre de ville accordé en 1835 ; premier carillon de Haute-Savoie, une quarantaine de cloches dans l'église Saint-Jean-Baptiste.",
                     wiki="Taninges"),
    "Sallanches": dict(km=25, min=30, voisines=["Passy", "Domancy", "Saint-Gervais-les-Bains", "Cordon", "Megève"],
                       intro="Face au Mont-Blanc, Sallanches est à une trentaine de minutes de notre atelier par la vallée de l'Arve. Active Plomberie 74 y intervient pour la plomberie, le chauffage, l'eau chaude et la rénovation de salles de bain, dans les résidences principales comme dans les logements de location.",
                       reperes="17 041 habitants (2022), reconstruite en plan en damier après l'incendie de 1840, dans un large bassin glaciaire entre Aravis et Mont-Blanc.",
                       wiki="Sallanches"),
    "La Roche-sur-Foron": dict(km=26, min=25,
                               reperes="11 239 habitants (2022), deuxième ville de France éclairée à l'électricité (1885) ; tour des comtes de Genève du XIIIe siècle et gare au pont tournant historique.",
                               wiki="La_Roche-sur-Foron"),
    "Annemasse": dict(km=39, min=34, voisines=["Ambilly", "Gaillard", "Ville-la-Grand", "Étrembières", "Cranves-Sales", "Vétraz-Monthoux"],
                      reperes="37 595 habitants (2022), à 2 km du canton de Genève, à l'entrée de la vallée de l'Arve.",
                      wiki="Annemasse"),
    "Samoëns": dict(km=30, min=35,
                    reperes="2 193 habitants (2022), chef-lieu à 703 m ; village des anciens tailleurs de pierre, relié au domaine skiable du Grand Massif (265 km de pistes).",
                    wiki="Samo%C3%ABns"),
    "La Clusaz": dict(km=50, min=55, voisines=["Le Grand-Bornand", "Saint-Jean-de-Sixt", "Thônes", "Manigod", "Les Villards-sur-Thônes"],
                      reperes="1 663 habitants (2022), station de ski des Aravis depuis 1909, au cœur du pays du reblochon.",
                      wiki="La_Clusaz"),
}
for _c, _v in _MAJ.items():
    COMMUNES_CONTENU[_c].update(_v)
