# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-27 · **113 offres** · dont 35 en alternance
- **Extractions disponibles** : 53, du 2026-09-22 au 2026-11-27

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 42 |
| Auvergne-Rhône-Alpes | 13 |
| Provence-Alpes-Côte d'Azur | 11 |
| Occitanie | 10 |
| Hauts-de-France | 6 |
| Normandie | 6 |
| Outre-mer | 5 |
| Pays de la Loire | 4 |
| Grand Est | 3 |
| Nouvelle-Aquitaine | 3 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 18 |
| 69 | 7 |
| 92 | 7 |
| 93 | 7 |
| 974 | 4 |
| 13 | 4 |
| 34 | 3 |
| 94 | 3 |
| 83 | 3 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **7** sur 113 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 52 |
| CDD | 49 |
| Intérim | 11 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 27 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 52 | 14 | 2550 € | 1350 – 6250 € | 30600 € |
| Alternance | 35 | 3 | 1325 € | 1144 – 1600 € | 15900 € |
| CDD | 14 | 8 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 11 | 5 | 2200 € | 1875 – 3417 € | 26400 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 113 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Canva | 11 | 17 |
| Adobe (Photoshop, Illustrator, InDesign…) | 10 | 12 |
| Anglais | 9 | 10 |
| Pack Office | 8 | 11 |
| LinkedIn | 8 | 10 |
| Emailing / newsletter | 7 | 13 |
| IA (ChatGPT, IA générative…) | 7 | 8 |
| Excel | 6 | 10 |
| SEO | 6 | 9 |
| PowerPoint | 6 | 7 |
| Instagram | 5 | 9 |
| CRM | 5 | 8 |
| Facebook | 5 | 7 |
| TikTok | 4 | 4 |
| Word | 3 | 3 |
| WordPress | 3 | 3 |
| YouTube | 2 | 2 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| HubSpot | 2 | 2 |
| Meta Ads / Facebook Ads | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, SEA, Salesforce, Shopify, Prestashop, SQL, Python, Semrush / Ahrefs, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 20 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 23 |
| Concevoir des supports de communication et d'image | 4 |
| Utiliser les outils numériques | 4 |
| Développer l'image et la notoriété de la structure | 3 |
| Marketing des réseaux sociaux | 3 |
| Elaborer une stratégie de marketing digital | 3 |
| Analyser les performances de l'équipe et proposer des améliorations | 3 |
| Participer aux phases créatives d'un projet marketing | 2 |
| Elaborer un plan marketing, une stratégie de marque et de communication | 2 |
| Mener une campagne d'e-mailing | 2 |

## Qui publie

| Entreprise | Offres |
|---|---|
| EFC | 23 |
| ISCOD | 12 |
| SOLANO | 2 |
| SUPPLAY SIEGE | 2 |
| AUREIS FORMATION | 2 |
| COMPAGNIE DES ALPES | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| SM2C | 1 |
| VIGNAL SYSTEMS | 1 |

26 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 113 (20 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 26 offres sur 113 (23 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 31 % des offres : leur poids fausse le « volume » du marché.
- 35 offres sur 113 (31 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2550 € brut par mois, 14 offres seulement) est 5 % au-dessus du repère d'insertion (2433 €).
- Seules 20 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 31 intitulés sur 113 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
