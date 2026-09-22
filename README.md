# avenir — Veille métier : Assistant(e) marketing (ROME M1620)

Projet de cours : veille automatisée du marché de l'emploi pour mon métier ciblé,
via l'API France Travail, enrichie de données entreprises, et restituée dans un
dashboard web qui se met à jour tout seul.

## 1. Métier ciblé

**Intitulé principal :** Assistant / Assistante marketing
**Code ROME :** [M1620](https://candidat.francetravail.fr/metierscope/fiche-metier/M1620/assistant-assistante-marketing) (secteur Communication et marketing)

**Variantes rencontrées sur le marché :**
- Assistant marketing et communication
- Assistant marketing digital
- Assistant chef de produit marketing

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

## 3. Structure du projet

- `scripts/` — scripts Python de collecte des données
- `data/` — données collectées (CSV datés), versionnées dans Git = historique du marché
- `index.html` — le dashboard web (à la racine, pour GitHub Pages)
- `.github/workflows/` — automatisation GitHub Actions (collecte planifiée quotidienne)

## 4. Sources de données (légales, documentées)

- **Canal principal :** [API France Travail — Offres d'emploi v2](https://francetravail.io/data/api/offres-emploi) — nécessite un compte développeur sur francetravail.io
- **Entreprises :** [API Recherche d'Entreprises (data.gouv.fr)](https://recherche-entreprises.api.gouv.fr/docs/) — gratuite, sans clé, données légales (SIRET, activité, effectif, dirigeants publics)
- Scraping LinkedIn / APEC / Indeed : **interdit**, non utilisé dans ce projet

## 5. Configuration

1. Créer un compte sur https://francetravail.io et s'abonner à l'API "Offres d'emploi v2"
2. Copier `.env.example` vers `.env` et renseigner les identifiants obtenus (jamais commités — voir `.gitignore`)

## 6. Installation

```bash
pip install -r requirements.txt
python scripts/fetch_offres.py
```

## RGPD

Les données entreprises utilisées (nom, activité, dirigeants) sont publiques. Aucune
donnée personnelle de salarié (email, téléphone nominatif) n'est collectée ou stockée.
