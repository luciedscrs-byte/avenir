# Le marché de « Assistant / Assistante marketing » (ROME M1620) — CDI / CDD seulement

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière ; seulement les vrais CDI et CDD (sans alternance, stage, intérim ni annonce de formation), à partir du 07/10/2026
- **Date d'extraction** : 2026-11-18 · **40 offres**
- **Extractions disponibles** : 43, du 2026-10-07 au 2026-11-18

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 13 |
| Provence-Alpes-Côte d'Azur | 7 |
| Nouvelle-Aquitaine | 4 |
| Pays de la Loire | 3 |
| Hauts-de-France | 3 |
| Auvergne-Rhône-Alpes | 3 |
| Occitanie | 2 |
| Outre-mer | 2 |
| Bourgogne-Franche-Comté | 2 |
| Grand Est | 1 |

| Département | Offres |
|---|---|
| 75 | 5 |
| 13 | 2 |
| 93 | 2 |
| 94 | 2 |
| 72 | 2 |
| 33 | 2 |
| 92 | 2 |
| 06 | 2 |
| 44 | 1 |
| 05 | 1 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **4** sur 40 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 30 |
| CDD | 10 |

## Salaires affichés (brut)

Seules 40 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 30 | 10 | 2270 € | 2000 – 3542 € | 27240 € |
| CDD | 10 | 6 | 2292 € | 1867 – 3500 € | 27504 € |

## Outils cités dans les annonces

Texte lu pour 40 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Anglais | 8 | 8 |
| Adobe (Photoshop, Illustrator, InDesign…) | 7 | 8 |
| Emailing / newsletter | 6 | 6 |
| Pack Office | 5 | 7 |
| Canva | 4 | 4 |
| IA (ChatGPT, IA générative…) | 4 | 4 |
| Excel | 3 | 4 |
| PowerPoint | 3 | 3 |
| CRM | 3 | 3 |
| LinkedIn | 2 | 2 |
| SEO | 2 | 2 |
| Google Ads | 2 | 2 |
| Word | 1 | 1 |
| Google Analytics / GA4 | 1 | 1 |
| Meta Ads / Facebook Ads | 1 | 1 |
| HubSpot | 1 | 1 |
| WordPress | 1 | 1 |
| Shopify | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, Instagram, Facebook, TikTok, YouTube, SEA, Salesforce, Mailchimp, Brevo, Sendinblue, Klaviyo, Prestashop, SQL, Python, Semrush / Ahrefs, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 40 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 15 |
| Analyser les performances de l'équipe et proposer des améliorations | 3 |
| Concevoir des supports de communication et d'image | 2 |
| Elaborer une stratégie de marketing digital | 2 |
| Elaborer un plan marketing, une stratégie de marque et de communication | 2 |
| Développer l'image et la notoriété de la structure | 2 |
| PERMIS + VEHICULE OBLIGATOIRE | 1 |
| Analyse concurrentielle | 1 |
| Analyse des besoins des clients | 1 |
| Gestion de campagnes publicitaires | 1 |

## Qui publie

| Entreprise | Offres |
|---|---|
| TalenX | 3 |
| MANPOWER | 1 |
| FEDE DEPART ASS LOC ADMR | 1 |
| TOURIST DEVELOPMENT CORPORATION | 1 |
| ANDROS | 1 |
| ITINOVA | 1 |
| KAROIL | 1 |
| SOCOMEC | 1 |
| LACO | 1 |
| LUCHE TRADITION VOLAILLES | 1 |

13 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 13 offres sur 40 (32 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Aucun employeur ne domine : le plus présent, TalenX, publie 3 offres sur 40.
- Le salaire médian affiché en CDI (2270 € brut par mois, 10 offres seulement) est 7 % en dessous du repère d'insertion (2433 €).
- Seules 40 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 22 intitulés sur 40 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
