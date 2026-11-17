# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-17 · **119 offres** · dont 42 en alternance
- **Extractions disponibles** : 43, du 2026-09-22 au 2026-11-17

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 37 |
| Provence-Alpes-Côte d'Azur | 16 |
| Auvergne-Rhône-Alpes | 13 |
| Nouvelle-Aquitaine | 8 |
| Occitanie | 7 |
| Hauts-de-France | 7 |
| Outre-mer | 6 |
| Centre-Val de Loire | 5 |
| Normandie | 5 |
| Bourgogne-Franche-Comté | 5 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 14 |
| 92 | 6 |
| 13 | 5 |
| 93 | 5 |
| 94 | 5 |
| 06 | 4 |
| 974 | 4 |
| 69 | 4 |
| 66 | 3 |

Puy-de-Dôme (63) : **1** offre(s). Mentionnent le télétravail dans le texte : **7** sur 119 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 58 |
| CDD | 53 |
| Intérim | 8 |

## Salaires affichés (brut)

Seules 20 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 58 | 12 | 2161 € | 1350 – 3542 € | 25932 € |
| Alternance | 42 | 4 | 1250 € | 1144 – 1867 € | 15000 € |
| CDD | 11 | 5 | 2500 € | 2292 – 3500 € | 30000 € |
| Intérim | 8 | 3 | 1972 € | 1875 – 2524 € | 23664 € |

## Outils cités dans les annonces

Texte lu pour 119 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Anglais | 15 | 15 |
| Emailing / newsletter | 13 | 14 |
| Adobe (Photoshop, Illustrator, InDesign…) | 12 | 15 |
| LinkedIn | 10 | 12 |
| Pack Office | 9 | 13 |
| SEO | 9 | 10 |
| Canva | 8 | 9 |
| Excel | 7 | 9 |
| CRM | 7 | 8 |
| IA (ChatGPT, IA générative…) | 6 | 6 |
| PowerPoint | 5 | 5 |
| Instagram | 4 | 8 |
| Facebook | 4 | 6 |
| Word | 4 | 4 |
| TikTok | 3 | 5 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| YouTube | 1 | 1 |
| Meta Ads / Facebook Ads | 1 | 1 |
| HubSpot | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| WordPress | 1 | 1 |
| Shopify | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |
| Semrush / Ahrefs | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, SEA, Salesforce, Prestashop, SQL, Python, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 19 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 22 |
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
| EFC | 23 |
| ISCOD | 11 |
| COMPAGNIE DES ALPES | 3 |
| TalenX | 3 |
| SYNERGIE | 2 |
| AUREIS FORMATION | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| SAINT MAIXENT DISTRIBUTION | 2 |
| FEDE DEPART ASS LOC ADMR | 1 |

26 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 119 (19 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 26 offres sur 119 (22 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 29 % des offres : leur poids fausse le « volume » du marché.
- 42 offres sur 119 (35 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2161 € brut par mois, 12 offres seulement) est 11 % en dessous du repère d'insertion (2433 €).
- Seules 19 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 28 intitulés sur 119 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
