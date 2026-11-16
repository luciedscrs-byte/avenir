# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-16 · **117 offres** · dont 39 en alternance
- **Extractions disponibles** : 42, du 2026-09-22 au 2026-11-16

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 35 |
| Provence-Alpes-Côte d'Azur | 16 |
| Auvergne-Rhône-Alpes | 12 |
| Nouvelle-Aquitaine | 9 |
| Occitanie | 7 |
| Hauts-de-France | 7 |
| Outre-mer | 6 |
| Centre-Val de Loire | 5 |
| Bourgogne-Franche-Comté | 5 |
| Grand Est | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 13 |
| 92 | 7 |
| 13 | 6 |
| 94 | 6 |
| 06 | 4 |
| 974 | 4 |
| 93 | 3 |
| 66 | 3 |
| 33 | 3 |

Puy-de-Dôme (63) : **1** offre(s). Mentionnent le télétravail dans le texte : **7** sur 117 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 57 |
| CDD | 51 |
| Intérim | 9 |

## Salaires affichés (brut)

Seules 18 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 57 | 10 | 2242 € | 1667 – 3542 € | 26904 € |
| Alternance | 39 | 3 | 1325 € | 1174 – 1867 € | 15900 € |
| CDD | 12 | 4 | 2792 € | 2292 – 3500 € | 33504 € |
| Intérim | 9 | 4 | 2123 € | 1875 – 2524 € | 25476 € |

## Outils cités dans les annonces

Texte lu pour 117 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Anglais | 14 | 14 |
| Emailing / newsletter | 13 | 14 |
| Adobe (Photoshop, Illustrator, InDesign…) | 11 | 14 |
| LinkedIn | 10 | 12 |
| SEO | 10 | 11 |
| Pack Office | 7 | 11 |
| Canva | 7 | 7 |
| IA (ChatGPT, IA générative…) | 7 | 7 |
| CRM | 6 | 7 |
| Excel | 5 | 8 |
| Instagram | 4 | 8 |
| Facebook | 4 | 6 |
| PowerPoint | 4 | 4 |
| TikTok | 3 | 5 |
| Word | 3 | 3 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| YouTube | 1 | 1 |
| SEA | 1 | 1 |
| Meta Ads / Facebook Ads | 1 | 1 |
| HubSpot | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| WordPress | 1 | 1 |
| Shopify | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |
| Semrush / Ahrefs | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, Salesforce, Prestashop, SQL, Python, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 18 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 20 |
| Analyser les performances de l'équipe et proposer des améliorations | 3 |
| Concevoir des supports de communication et d'image | 2 |
| Elaborer une stratégie de marketing digital | 2 |
| Elaborer un plan marketing, une stratégie de marque et de communication | 2 |
| Développer l'image et la notoriété de la structure | 2 |
| Analyse concurrentielle | 1 |
| Analyse des besoins des clients | 1 |
| Gestion de campagnes publicitaires | 1 |
| Utiliser les outils numériques | 1 |

## Qui publie

| Entreprise | Offres |
|---|---|
| EFC | 23 |
| ISCOD | 9 |
| COMPAGNIE DES ALPES | 3 |
| TalenX | 3 |
| SYNERGIE | 2 |
| AUREIS FORMATION | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| SAINT MAIXENT DISTRIBUTION | 2 |
| TOURIST DEVELOPMENT CORPORATION | 1 |

27 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 117 (20 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 27 offres sur 117 (23 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 27 % des offres : leur poids fausse le « volume » du marché.
- 39 offres sur 117 (33 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2242 € brut par mois, 10 offres seulement) est 8 % en dessous du repère d'insertion (2433 €).
- Seules 18 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 27 intitulés sur 117 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
