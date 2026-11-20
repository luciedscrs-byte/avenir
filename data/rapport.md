# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-20 · **123 offres** · dont 41 en alternance
- **Extractions disponibles** : 46, du 2026-09-22 au 2026-11-20

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 43 |
| Provence-Alpes-Côte d'Azur | 15 |
| Auvergne-Rhône-Alpes | 12 |
| Hauts-de-France | 8 |
| Occitanie | 8 |
| Outre-mer | 6 |
| Nouvelle-Aquitaine | 6 |
| Normandie | 6 |
| Pays de la Loire | 4 |
| Grand Est | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 19 |
| 92 | 7 |
| 93 | 6 |
| 13 | 5 |
| 69 | 4 |
| 94 | 4 |
| 974 | 4 |
| 83 | 4 |
| 06 | 3 |

Puy-de-Dôme (63) : **1** offre(s). Mentionnent le télétravail dans le texte : **9** sur 123 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 58 |
| CDD | 53 |
| Intérim | 11 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 22 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 58 | 13 | 2083 € | 1350 – 3542 € | 24996 € |
| Alternance | 41 | 4 | 1250 € | 1144 – 1600 € | 15000 € |
| CDD | 12 | 6 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 11 | 4 | 2362 € | 1875 – 3417 € | 28344 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 123 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Adobe (Photoshop, Illustrator, InDesign…) | 11 | 13 |
| Anglais | 11 | 12 |
| Pack Office | 10 | 14 |
| Canva | 10 | 12 |
| Emailing / newsletter | 10 | 12 |
| LinkedIn | 10 | 10 |
| Excel | 8 | 12 |
| IA (ChatGPT, IA générative…) | 8 | 8 |
| SEO | 7 | 8 |
| CRM | 6 | 8 |
| PowerPoint | 6 | 7 |
| Instagram | 5 | 8 |
| Facebook | 5 | 6 |
| Word | 4 | 5 |
| TikTok | 4 | 5 |
| YouTube | 2 | 2 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| WordPress | 2 | 2 |
| Meta Ads / Facebook Ads | 1 | 1 |
| HubSpot | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
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
| SUPPLAY SIEGE | 2 |
| AUREIS FORMATION | 2 |
| COMPAGNIE DES ALPES | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| SOLANO | 1 |
| SENTEO | 1 |

27 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 123 (19 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 27 offres sur 123 (22 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 28 % des offres : leur poids fausse le « volume » du marché.
- 41 offres sur 123 (33 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2083 € brut par mois, 13 offres seulement) est 14 % en dessous du repère d'insertion (2433 €).
- Seules 19 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 35 intitulés sur 123 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
