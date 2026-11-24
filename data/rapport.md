# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-24 · **124 offres** · dont 39 en alternance
- **Extractions disponibles** : 50, du 2026-09-22 au 2026-11-24

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 47 |
| Provence-Alpes-Côte d'Azur | 14 |
| Auvergne-Rhône-Alpes | 13 |
| Occitanie | 11 |
| Hauts-de-France | 7 |
| Nouvelle-Aquitaine | 5 |
| Normandie | 5 |
| Outre-mer | 4 |
| Grand Est | 4 |
| Bretagne | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 21 |
| 92 | 8 |
| 69 | 6 |
| 93 | 6 |
| 13 | 5 |
| 94 | 4 |
| 83 | 4 |
| 31 | 3 |
| 33 | 3 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **11** sur 124 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 57 |
| CDD | 54 |
| Intérim | 12 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 27 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 57 | 16 | 2521 € | 1350 – 6250 € | 30252 € |
| Alternance | 39 | 4 | 1250 € | 1144 – 1600 € | 15000 € |
| CDD | 15 | 8 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 12 | 5 | 2200 € | 1875 – 3417 € | 26400 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 124 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Adobe (Photoshop, Illustrator, InDesign…) | 13 | 16 |
| Canva | 12 | 16 |
| Emailing / newsletter | 11 | 16 |
| Anglais | 11 | 11 |
| LinkedIn | 10 | 11 |
| IA (ChatGPT, IA générative…) | 10 | 11 |
| Excel | 9 | 15 |
| Pack Office | 8 | 11 |
| SEO | 7 | 10 |
| PowerPoint | 7 | 9 |
| CRM | 6 | 9 |
| Word | 6 | 7 |
| Instagram | 4 | 8 |
| Facebook | 4 | 6 |
| TikTok | 3 | 5 |
| YouTube | 2 | 2 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| HubSpot | 2 | 2 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 2 | 2 |
| WordPress | 2 | 2 |
| Meta Ads / Facebook Ads | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |
| Semrush / Ahrefs | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, SEA, Salesforce, Shopify, Prestashop, SQL, Python, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 19 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 22 |
| Analyser les performances de l'équipe et proposer des améliorations | 4 |
| Marketing des réseaux sociaux | 3 |
| Concevoir des supports de communication et d'image | 3 |
| Développer l'image et la notoriété de la structure | 3 |
| Utiliser les outils numériques | 3 |
| Elaborer une stratégie de marketing digital | 3 |
| Gestion de campagnes publicitaires | 2 |
| Planification de campagnes publicitaires | 2 |
| Assurer le suivi des chiffres de vente et réaliser le reporting associé | 2 |

## Qui publie

| Entreprise | Offres |
|---|---|
| EFC | 23 |
| ISCOD | 13 |
| SOLANO | 2 |
| SUPPLAY SIEGE | 2 |
| AUREIS FORMATION | 2 |
| COMPAGNIE DES ALPES | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| BEAUTIFULSMILE | 1 |
| MCDONALD'S | 1 |

28 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 124 (19 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 28 offres sur 124 (23 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 29 % des offres : leur poids fausse le « volume » du marché.
- 39 offres sur 124 (31 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2521 € brut par mois, 16 offres seulement) est 4 % au-dessus du repère d'insertion (2433 €).
- Seules 19 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 34 intitulés sur 124 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
