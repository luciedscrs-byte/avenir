# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-25 · **117 offres** · dont 36 en alternance
- **Extractions disponibles** : 51, du 2026-09-22 au 2026-11-25

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 45 |
| Provence-Alpes-Côte d'Azur | 12 |
| Auvergne-Rhône-Alpes | 12 |
| Occitanie | 9 |
| Hauts-de-France | 7 |
| Normandie | 6 |
| Outre-mer | 4 |
| Pays de la Loire | 4 |
| Nouvelle-Aquitaine | 4 |
| Bretagne | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 20 |
| 92 | 8 |
| 69 | 6 |
| 93 | 6 |
| 13 | 5 |
| 94 | 4 |
| 34 | 3 |
| 83 | 3 |
| 974 | 3 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **9** sur 117 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 55 |
| CDD | 50 |
| Intérim | 11 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 26 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 55 | 14 | 2344 € | 1350 – 6250 € | 28128 € |
| Alternance | 36 | 4 | 1250 € | 1144 – 1600 € | 15000 € |
| CDD | 14 | 8 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 11 | 5 | 2200 € | 1875 – 3417 € | 26400 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 117 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Canva | 11 | 16 |
| Adobe (Photoshop, Illustrator, InDesign…) | 11 | 13 |
| Anglais | 9 | 11 |
| LinkedIn | 9 | 10 |
| Emailing / newsletter | 8 | 14 |
| Pack Office | 8 | 12 |
| IA (ChatGPT, IA générative…) | 8 | 9 |
| Excel | 7 | 12 |
| SEO | 7 | 10 |
| PowerPoint | 7 | 8 |
| CRM | 5 | 8 |
| Instagram | 4 | 9 |
| Facebook | 4 | 7 |
| Word | 4 | 4 |
| TikTok | 3 | 5 |
| YouTube | 2 | 2 |
| Google Analytics / GA4 | 2 | 2 |
| Google Ads | 2 | 2 |
| HubSpot | 2 | 2 |
| WordPress | 2 | 2 |
| Meta Ads / Facebook Ads | 1 | 1 |
| Mailchimp, Brevo, Sendinblue, Klaviyo | 1 | 1 |
| Power BI / Looker Studio | 1 | 1 |
| Semrush / Ahrefs | 1 | 1 |

Suivis mais cités dans aucune annonce : Figma, SEA, Salesforce, Shopify, Prestashop, SQL, Python, Google Tag Manager, Notion / Trello / Asana, Zapier.

## Compétences renseignées par France Travail

Seules 18 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 21 |
| Marketing des réseaux sociaux | 3 |
| Concevoir des supports de communication et d'image | 3 |
| Elaborer une stratégie de marketing digital | 3 |
| Utiliser les outils numériques | 3 |
| Développer l'image et la notoriété de la structure | 2 |
| Elaborer un plan marketing, une stratégie de marque et de communication | 2 |
| Mener une campagne d'e-mailing | 2 |
| Optimiser le référencement naturel (SEO) des sites web | 2 |
| Gestion de campagnes publicitaires | 2 |

## Qui publie

| Entreprise | Offres |
|---|---|
| EFC | 23 |
| ISCOD | 11 |
| SOLANO | 2 |
| SUPPLAY SIEGE | 2 |
| AUREIS FORMATION | 2 |
| COMPAGNIE DES ALPES | 2 |
| Forums Talents Handicap | 2 |
| Tetranergy Business School Réunion | 2 |
| BEAUTIFULSMILE | 1 |
| MCDONALD'S | 1 |

30 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 117 (20 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 30 offres sur 117 (26 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 29 % des offres : leur poids fausse le « volume » du marché.
- 36 offres sur 117 (31 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2344 € brut par mois, 14 offres seulement) est 4 % en dessous du repère d'insertion (2433 €).
- Seules 18 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 32 intitulés sur 117 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
