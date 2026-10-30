# avenir — Veille métier : Assistant(e) marketing (ROME M1620)

Projet de cours : veille automatisée du marché de l'emploi pour mon métier ciblé,
via l'API France Travail, enrichie de données entreprises, et restituée dans un
dashboard web qui se met à jour tout seul.

## 1. Métier ciblé

**Intitulé principal :** Assistant / Assistante marketing
**Code ROME :** [M1620](https://candidat.francetravail.fr/metierscope/fiche-metier/M1620/assistant-assistante-marketing) (secteur Communication et marketing)

**Variantes rencontrées sur le marché** (comptées dans les 136 intitulés du 07/10/2026) :
- Assistant / Assistante marketing — dans 77 intitulés
- Assistant(e) commercial(e) et marketing — 14
- Assistant(e) marketing et communication — 10
- Assistant(e) chef de produit — 4

« Digital » n'apparaît que dans 2 intitulés : le marché dit « assistant marketing », pas « assistant marketing digital ». 45 intitulés parlent d'alternance.

**Pourquoi ce métier :** correspond à mon stage chez Mapache (assistante marketing et
communication) — SEO sur Shopify, segmentation client pour newsletters, gestion de
campagnes marketing, fiches produit. Le référentiel ROME confirme ce lien : le
savoir-faire *"Optimiser le référencement naturel (SEO) des sites web"* et
*"Mener une campagne d'e-mailing"* apparaissent explicitement dans la fiche M1620.

**Métier proche noté pour plus tard :** Chargé/Chargée de marketing digital (M1718,
poste cadre) — objectif d'évolution à moyen terme, pas le point d'entrée.

## 2. Questions sur ce marché

1. Combien d'offres pour ce métier sont publiées actuellement, et où (régions/départements) ?
2. Quelles compétences et quels outils reviennent le plus souvent dans les offres (SEO, CRM, Shopify, emailing...) ?
3. Quelle fourchette de salaire est proposée, et comment se compare-t-elle au salaire médian d'insertion ?
4. Quelles entreprises recrutent le plus sur ce métier, et quel est le "marché caché" (entreprises du secteur qui ne publient pas d'offre) ?

## 3. Les entreprises qui recrutent le plus cet intitulé

**Période et méthode.** 24 extractions du 7 au 30 octobre 2026, France entière, code ROME M1620 : 252 identifiants d'offres, soit **212 annonces distinctes** une fois regroupées par entreprise, titre et lieu (une annonce republiée reçoit un nouvel identifiant). **60 annonces distinctes (28 %) n'ont aucun nom d'employeur** et ne peuvent pas être classées. Les noms sont ceux déclarés dans les annonces ; une nature n'est indiquée que lorsque j'ai lu le texte de l'annonce.

| Rang | Entreprise | Annonces distinctes | Ce que disent les annonces |
|---|---|---|---|
| 1 | ISCOD | 27 | École de formation en digital learning : elle recrute des alternants pour des entreprises partenaires (27 annonces sur 27 en alternance) |
| 2 | EFC CONSULTING | 12 | Les annonces font la promotion d'une formation à distance (« En suivant la formation Assistant Marketing à distance, vous vous formerez… ») : ce ne sont pas des offres d'emploi |
| 3 | Randstad (plusieurs entités) | 7 | Agence d'intérim : elle recrute pour le compte de ses clients |
| 4 | Aureis Formation | 5 | Annonces d'alternance, toutes issues de La Bonne Alternance |
| 5 ex æquo | SCI Pro immo, Compagnie des Alpes, Herta, TalenX | 3 chacune | voir ci-dessous |

Les entreprises du 5ᵉ rang :
- **SCI Pro immo** : employeur direct, assistant(e) marketing en CDI, à La Réunion.
- **Compagnie des Alpes** : employeur direct (domaines skiables) ; « assistant marketing & commercial » en CDD et « alternant moniteur de ski et chargé marketing/communication ».
- **Herta** : employeur direct, mais les annonces lues sont des stages de 6 mois (chef de produit marketing, community manager), classés « CDI » par France Travail.
- **TalenX** : cabinet de recrutement ; l'annonce lue n'est pas du marketing (« Responsable SAV / Gestionnaire planning »).

**Lecture.** Le haut du classement mesure surtout des intermédiaires (une école, de l'intérim) et des annonces de formation : seuls trois employeurs directs apparaissent, au 5ᵉ rang, avec trois annonces chacun. Le marché direct de cet intitulé est donc une longue traîne d'entreprises qui publient une ou deux annonces. La page *Les offres* affiche le classement du jour (dernière extraction seulement, par offre), qui n'a pas la même méthode.

**Pour les trois professionnels à trouver sur LinkedIn** : privilégier les employeurs directs ci-dessus ou les entreprises de la liste du marché caché, pas les écoles, l'intérim ni les annonces de formation.

## 4. Structure du projet

- `scripts/fetch_offres.py` — extraction France Travail (canal commun) → `data/offres_M1620_<date>.csv`
- `scripts/fetch_offres_alternance.py` — extraction La Bonne Alternance (2ᵉ canal) → `data/offres_alternance_M1620_<date>.csv`
- `scripts/textes.py` — garde le texte de chaque annonce une seule fois, dans `data/textes.jsonl`
- `scripts/resumer.py` — calcule `data/resume.json` (ce que le site affiche) et `data/rapport.md` (rapport lisible)
- `scripts/entreprises.py` — le marché caché : `data/entreprises.csv` (lancé à la main, pas chaque jour)
- `data/formation.json` — ce que le descriptif public du M2 MOD nomme (outils, unités, métiers et codes ROME visés), lu le 30/10/2026, source des tableaux « formation » du site
- Le site, servi par GitHub Pages, en quatre pages qui lisent `data/resume.json` et `data/entreprises.csv` : `metier.html` (le métier tel que le marché le nomme), `index.html` (les offres), `mouvement.html` (comment le métier bouge : courbe, offres nouvelles et disparues, outils suivis, source Apec) et `entreprises.html` (le marché caché) ; `assets/commun.css` et `assets/commun.js` partagés
- `.github/workflows/veille.yml` — GitHub Actions : chaque matin, les deux extractions, le résumé, puis un commit des nouvelles données

## 5. Sources de données (légales, documentées)

- **Canal commun :** [API France Travail — Offres d'emploi v2](https://francetravail.io/data/api/offres-emploi) — compte développeur sur francetravail.io. Une requête par code ROME, le total se lit dans l'en-tête `Content-Range`.
- **2ᵉ canal :** [La Bonne Alternance](https://api.apprentissage.beta.gouv.fr) — offres d'alternance. L'API renvoie chaque offre en double ; le script dédoublonne par identifiant. Elle reprend en partie des offres France Travail (recoupement mesuré sur le site).
- **Entreprises :** [API Recherche d'entreprises (data.gouv.fr)](https://recherche-entreprises.api.gouv.fr/docs/) — gratuite, sans clé : nom, adresse du siège, activité (NAF), tranche de salariés, date de création. Elle ne fournit ni site web ni coordonnées.
- Scraping LinkedIn / APEC / Indeed : **interdit**, non utilisé dans ce projet.

## 6. Le marché caché

Les sites d'offres ne montrent que les entreprises qui publient. `scripts/entreprises.py` part des entreprises elles-mêmes :

- **Périmètre** : entreprises actives d'au moins 6 salariés, dont le siège est dans un département abritant une commune de plus de 100 000 habitants (37 départements).
- **Secteurs** (codes NAF) : e-commerce, numérique, édition et médias, événementiel, marques et commerce spécialisé, et agences (publicité, communication, études de marché, design).
- **Trois sections**, pour repérer d'un coup d'œil ce qui m'intéresse le plus : *cibles principales* ; *agences* (récoltées mais séparées) ; *villes du nord* (plus hautes que Paris, hors Île-de-France : Lille, Reims, Le Havre, Rouen, Amiens, Metz, Caen), tous types confondus.
- **Limites** : le code NAF donne le secteur de l'entreprise, pas l'existence d'un poste marketing ; seul le siège est retenu (une entreprise dont le siège est ailleurs mais qui a un établissement local n'apparaît pas) ; l'API ne donne pas le site web.

## 7. Configuration et lancement

1. Créer un compte sur https://francetravail.io et s'abonner à l'API « Offres d'emploi v2 » ; créer une clé sur api.apprentissage.beta.gouv.fr
2. Copier `.env.example` vers `.env` et renseigner les identifiants (jamais commités — voir `.gitignore`). Sur GitHub, les mêmes valeurs sont des *secrets* du dépôt (Settings → Secrets and variables → Actions).

```bash
pip install -r requirements.txt
python scripts/fetch_offres.py
python scripts/fetch_offres_alternance.py
python scripts/resumer.py
python scripts/entreprises.py      # le marché caché, à relancer de temps en temps
python3 -m http.server             # pour voir le site en local
```

## 8. RGPD

- Les dirigeants d'entreprise sont des données publiques ; un contact nominatif de salarié (e-mail, téléphone) est une donnée personnelle.
- Ce dépôt est public : `data/entreprises.csv` ne contient **que des données d'entreprises, aucun nom de personne**.
- Si un contact est cherché plus tard, ce sera pour une entreprise précise, en lien avec la **fonction** de la personne (responsable marketing, RH…), pour une **finalité claire** : une candidature. La personne garde un droit d'opposition (la CNIL admet la prospection B2B à ces conditions).
- Jamais de fichier constitué pour être revendu ; jamais de contact hors de sa fonction ; aucune donnée de ce type n'est versionnée dans ce dépôt.
