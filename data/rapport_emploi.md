# Le marché de « Assistant / Assistante marketing » (ROME M1620) — CDI / CDD seulement

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière ; seulement les vrais CDI et CDD (sans alternance, stage, intérim ni annonce de formation), à partir du 07/10/2026
- **Date d'extraction** : 2026-11-22 · **41 offres**
- **Extractions disponibles** : 47, du 2026-10-07 au 2026-11-22

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 12 |
| Provence-Alpes-Côte d'Azur | 7 |
| Auvergne-Rhône-Alpes | 5 |
| Hauts-de-France | 5 |
| Nouvelle-Aquitaine | 3 |
| Pays de la Loire | 2 |
| Occitanie | 2 |
| Grand Est | 2 |
| Bretagne | 1 |
| Bourgogne-Franche-Comté | 1 |

| Département | Offres |
|---|---|
| 75 | 4 |
| 69 | 3 |
| 92 | 3 |
| 13 | 2 |
| 93 | 2 |
| 94 | 2 |
| 67 | 2 |
| 33 | 2 |
| 83 | 2 |
| 59 | 2 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **6** sur 41 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 30 |
| CDD | 11 |

## Salaires affichés (brut)

Seules 46 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 30 | 13 | 2500 € | 1900 – 3542 € | 30000 € |
| CDD | 11 | 6 | 2292 € | 1867 – 3500 € | 27504 € |

## Outils cités dans les annonces

Texte lu pour 41 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Adobe (Photoshop, Illustrator, InDesign…) | 7 | 8 |
| Canva | 6 | 8 |
| Emailing / newsletter | 6 | 7 |
| Anglais | 6 | 7 |
| IA (ChatGPT, IA générative…) | 6 | 6 |
| Pack Office | 5 | 7 |
| PowerPoint | 4 | 6 |
| LinkedIn | 4 | 4 |
| Excel | 3 | 5 |
| CRM | 3 | 3 |
| SEO | 2 | 2 |
| Google Ads | 2 | 2 |
| HubSpot | 2 | 2 |
| WordPress | 2 | 2 |
| Word | 1 | 1 |
| Instagram | 1 | 1 |
| TikTok | 1 | 1 |
| Google Analytics / GA4 | 1 | 1 |
| Meta Ads / Facebook Ads | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, Facebook, YouTube, SEA, Salesforce, Shopify, Prestashop, SQL, Python, Semrush / Ahrefs, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 41 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 16 |
| Elaborer une stratégie de marketing digital | 3 |
| Analyse concurrentielle | 2 |
| Marketing des réseaux sociaux | 2 |
| Utiliser les outils numériques | 2 |
| Concevoir des supports de communication et d'image | 2 |
| Développer l'image et la notoriété de la structure | 2 |
| Analyser les performances de l'équipe et proposer des améliorations | 2 |
| Planification de campagnes publicitaires | 1 |
| Analyser le retour sur investissement des campagnes publicitaires | 1 |

## Qui publie

| Entreprise | Offres |
|---|---|
| TalenX | 3 |
| SENTEO | 1 |
| LEBRUN SA | 1 |
| MANPOWER | 1 |
| FEDE DEPART ASS LOC ADMR | 1 |
| TOURIST DEVELOPMENT CORPORATION | 1 |
| ANDROS | 1 |
| ITINOVA | 1 |
| KAROIL | 1 |
| K-TEX | 1 |

12 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 12 offres sur 41 (29 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Aucun employeur ne domine : le plus présent, TalenX, publie 3 offres sur 41.
- Le salaire médian affiché en CDI (2500 € brut par mois, 13 offres seulement) est 3 % au-dessus du repère d'insertion (2433 €).
- Seules 41 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 20 intitulés sur 41 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
