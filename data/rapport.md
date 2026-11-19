# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-19 · **119 offres** · dont 41 en alternance
- **Extractions disponibles** : 45, du 2026-09-22 au 2026-11-19

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 40 |
| Provence-Alpes-Côte d'Azur | 14 |
| Auvergne-Rhône-Alpes | 13 |
| Occitanie | 9 |
| Hauts-de-France | 7 |
| Outre-mer | 6 |
| Nouvelle-Aquitaine | 6 |
| Normandie | 6 |
| Pays de la Loire | 4 |
| Grand Est | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 18 |
| 93 | 6 |
| 92 | 5 |
| 13 | 4 |
| 69 | 4 |
| 94 | 4 |
| 974 | 4 |
| 83 | 4 |
| 06 | 3 |

Puy-de-Dôme (63) : **1** offre(s). Mentionnent le télétravail dans le texte : **8** sur 119 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 56 |
| CDD | 52 |
| Intérim | 10 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 22 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 56 | 12 | 2083 € | 1350 – 3542 € | 24996 € |
| Alternance | 41 | 5 | 1325 € | 1144 – 1867 € | 15900 € |
| CDD | 11 | 6 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 10 | 3 | 1972 € | 1875 – 2524 € | 23664 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 119 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Pack Office | 11 | 14 |
| Anglais | 11 | 11 |
| Emailing / newsletter | 10 | 11 |
| Excel | 9 | 12 |
| Canva | 9 | 11 |
| Adobe (Photoshop, Illustrator, InDesign…) | 9 | 11 |
| LinkedIn | 9 | 9 |
| PowerPoint | 7 | 8 |
| SEO | 7 | 8 |
| IA (ChatGPT, IA générative…) | 7 | 7 |
| CRM | 6 | 8 |
| Instagram | 5 | 8 |
| Word | 5 | 6 |
| Facebook | 5 | 6 |
| TikTok | 4 | 5 |
| YouTube | 2 | 2 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| Meta Ads / Facebook Ads | 1 | 1 |
| HubSpot | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| WordPress | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |
| Semrush / Ahrefs | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, SEA, Salesforce, Shopify, Prestashop, SQL, Python, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 19 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 22 |
| Concevoir des supports de communication et d'image | 2 |
| Elaborer une stratégie de marketing digital | 2 |
| Elaborer un plan marketing, une stratégie de marque et de communication | 2 |
| Développer l'image et la notoriété de la structure | 2 |
| Analyser les performances de l'équipe et proposer des améliorations | 2 |
| PERMIS + VEHICULE OBLIGATOIRE | 1 |
| Analyse concurrentielle | 1 |
| Analyse des besoins des clients | 1 |
| Gestion de campagnes publicitaires | 1 |

## Qui publie

| Entreprise | Offres |
|---|---|
| EFC | 23 |
| ISCOD | 12 |
| TalenX | 3 |
| SYNERGIE | 2 |
| SUPPLAY SIEGE | 2 |
| AUREIS FORMATION | 2 |
| COMPAGNIE DES ALPES | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| LEBRUN SA | 1 |

26 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 119 (19 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 26 offres sur 119 (22 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 29 % des offres : leur poids fausse le « volume » du marché.
- 41 offres sur 119 (34 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2083 € brut par mois, 12 offres seulement) est 14 % en dessous du repère d'insertion (2433 €).
- Seules 19 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 33 intitulés sur 119 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
