# Le marché de « Assistant / Assistante marketing » (ROME M1620)

- **Requête** : API France Travail — Offres d'emploi v2, codeROME=M1620, France entière
- **Date d'extraction** : 2026-11-26 · **113 offres** · dont 34 en alternance
- **Extractions disponibles** : 52, du 2026-09-22 au 2026-11-26

**Comment ce rapport est fabriqué.** Un script lit le fichier CSV daté du jour (`data/offres_M1620_<date>.csv`) et le texte des annonces, et compte : les offres par région, département et contrat ; les salaires affichés ; les outils cités ; les employeurs. Chaque chiffre vient de ces fichiers, rien n'est saisi à la main, et le rapport se régénère à chaque extraction.

## Où

| Région | Offres |
|---|---|
| Île-de-France | 41 |
| Auvergne-Rhône-Alpes | 13 |
| Provence-Alpes-Côte d'Azur | 12 |
| Occitanie | 9 |
| Hauts-de-France | 6 |
| Normandie | 6 |
| Outre-mer | 4 |
| Pays de la Loire | 4 |
| Centre-Val de Loire | 4 |
| Nouvelle-Aquitaine | 4 |

| Département | Offres |
|---|---|
| Région seule | 23 |
| 75 | 17 |
| 69 | 7 |
| 92 | 7 |
| 93 | 7 |
| 13 | 5 |
| 34 | 3 |
| 94 | 3 |
| 83 | 3 |
| 974 | 3 |

Puy-de-Dôme (63) : **0** offre(s). Mentionnent le télétravail dans le texte : **7** sur 113 annonces lues (une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).

## Contrats

| Contrat | Offres |
|---|---|
| CDI | 53 |
| CDD | 48 |
| Intérim | 11 |
| Profession libérale | 1 |

## Salaires affichés (brut)

Seules 26 % des offres affichent un salaire (les autres n'en disent rien). Annuel ÷ 12 et horaire × 35 h × 52 ÷ 12 donnent le mensuel ; le mensuel × 12 donne l'annuel. Repère du cours : 2433 € brut par mois (médiane d'insertion à un an, deck de rentrée de l'IAE). Un salaire affiché n'est pas un salaire versé.

| Groupe | Offres | Avec salaire affiché | Médiane par mois | Min – max par mois | Médiane par an |
|---|---|---|---|---|---|
| CDI | 53 | 13 | 2500 € | 1350 – 6250 € | 30000 € |
| Alternance | 34 | 3 | 1325 € | 1144 – 1600 € | 15900 € |
| CDD | 14 | 8 | 2292 € | 1867 – 3500 € | 27504 € |
| Intérim | 11 | 5 | 2200 € | 1875 – 3417 € | 26400 € |
| Profession libérale | 1 | 0 | – | – | – |

## Outils cités dans les annonces

Texte lu pour 113 annonces. Classés par nombre d'**entreprises** distinctes qui les citent (pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).

| Outil | Entreprises | Offres |
|---|---|---|
| Canva | 10 | 15 |
| Adobe (Photoshop, Illustrator, InDesign…) | 10 | 12 |
| LinkedIn | 9 | 10 |
| Anglais | 9 | 9 |
| Emailing / newsletter | 8 | 13 |
| Pack Office | 8 | 11 |
| SEO | 7 | 10 |
| IA (ChatGPT, IA générative…) | 7 | 8 |
| Excel | 6 | 10 |
| PowerPoint | 6 | 7 |
| CRM | 5 | 8 |
| Instagram | 4 | 7 |
| Facebook | 4 | 5 |
| Word | 3 | 3 |
| TikTok | 3 | 3 |
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

Seules 19 % des offres ont ce champ rempli.

| Compétence | Offres |
|---|---|
| Mettre en place des solutions d'amélioration de la performance | 22 |
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
| VIGNAL SYSTEMS | 1 |
| BEAUTIFULSMILE | 1 |

28 offres n'ont aucun nom d'employeur et ne sont pas classées.

## Ce qui étonne dans ces chiffres

- 23 annonces sur 113 (20 %) font la promotion d'une formation à distance, pas d'un emploi (publiées par EFC) ; France Travail les classe pourtant comme des offres.
- 28 offres sur 113 (25 %) n'ont aucun nom d'employeur : on ne sait pas qui recrute.
- Deux employeurs (EFC et ISCOD) publient 30 % des offres : leur poids fausse le « volume » du marché.
- 34 offres sur 113 (30 %) sont de l'alternance.
- Le salaire médian affiché en CDI (2500 € brut par mois, 13 offres seulement) est 3 % au-dessus du repère d'insertion (2433 €).
- Seules 19 % des offres renseignent des compétences dans le champ France Travail, et la plus citée (« Mettre en place des solutions d'amélioration de la performance ») est générique : les outils se lisent surtout dans le texte des annonces.
- 32 intitulés sur 113 ne contiennent pas le mot « marketing » : le code M1620 regroupe des postes proches mais pas identiques.
