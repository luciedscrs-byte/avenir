"""Lit les CSV France Travail datés et les textes d'annonces de data/, puis produit
data/resume.json (ce que le site affiche) et data/rapport.md (le rapport lisible)."""
import csv
import glob
import json
import re
import statistics
from collections import Counter
from datetime import datetime, timezone

CODE_ROME = "M1620"
TOP = 10
MEDIANE_INSERTION = 2433
HEURES_PAR_MOIS = 35 * 52 / 12

REGIONS = {
    "Auvergne-Rhône-Alpes": "01 03 07 15 26 38 42 43 63 69 73 74",
    "Bourgogne-Franche-Comté": "21 25 39 58 70 71 89 90",
    "Bretagne": "22 29 35 56",
    "Centre-Val de Loire": "18 28 36 37 41 45",
    "Corse": "2A 2B 20",
    "Grand Est": "08 10 51 52 54 55 57 67 68 88",
    "Hauts-de-France": "02 59 60 62 80",
    "Île-de-France": "75 77 78 91 92 93 94 95",
    "Normandie": "14 27 50 61 76",
    "Nouvelle-Aquitaine": "16 17 19 23 24 33 40 47 64 79 86 87",
    "Occitanie": "09 11 12 30 31 32 34 46 48 65 66 81 82",
    "Pays de la Loire": "44 49 53 72 85",
    "Provence-Alpes-Côte d'Azur": "04 05 06 13 83 84",
    "Outre-mer": "971 972 973 974 976",
}
REGION_DE = {d: r for r, ds in REGIONS.items() for d in ds.split()}

OUTILS = [
    ("Excel", r"(?i)\bexcel\b"),
    ("PowerPoint", r"(?i)\bpower ?point\b"),
    ("Word", r"\bWord\b"),
    ("Pack Office", r"(?i)\b(pack|suite) office\b"),
    ("Canva", r"(?i)\bcanva\b"),
    ("Adobe (Photoshop, Illustrator, InDesign…)", r"(?i)\b(adobe|photoshop|illustrator|indesign)\b"),
    ("Figma", r"(?i)\bfigma\b"),
    ("Instagram", r"(?i)\binstagram\b"),
    ("LinkedIn", r"(?i)\blinked ?in\b"),
    ("Facebook", r"(?i)\bfacebook\b"),
    ("TikTok", r"(?i)\btik ?tok\b"),
    ("YouTube", r"(?i)\byoutube\b"),
    ("SEO", r"\bSEO\b"),
    ("SEA", r"\bSEA\b"),
    ("Google Analytics / GA4", r"(?i)\bgoogle analytics\b|\bGA4\b"),
    ("Google Ads", r"(?i)\bgoogle ads\b"),
    ("Meta Ads / Facebook Ads", r"(?i)\b(meta|facebook) ads\b"),
    ("CRM", r"\bCRM\b"),
    ("HubSpot", r"(?i)\bhub ?spot\b"),
    ("Salesforce", r"(?i)\bsalesforce\b"),
    ("Emailing / newsletter", r"(?i)\be-?mailing\b|\bnewsletters?\b"),
    ("Mailchimp, Brevo, Sendinblue, Klaviyo", r"(?i)\b(mailchimp|brevo|sendinblue|klaviyo)\b"),
    ("WordPress", r"(?i)\bwordpress\b"),
    ("Shopify", r"(?i)\bshopify\b"),
    ("Prestashop", r"(?i)\bprestashop\b"),
    ("IA (ChatGPT, IA générative…)", r"\bIA\b|(?i:intelligence artificielle|chatgpt)"),
    ("Anglais", r"(?i)\b(anglais|english|bilingue)\b"),
]
OUTILS = [(nom, re.compile(motif)) for nom, motif in OUTILS]
TELETRAVAIL = re.compile(r"(?i)télétravail|teletravail|\bremote\b|travail à distance|home ?office|hybride")


def lire(chemin):
    with open(chemin, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def charger_textes():
    textes = {}
    try:
        with open("data/textes.jsonl", encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    d = json.loads(ligne)
                    textes[d["id"]] = d["description"]
    except FileNotFoundError:
        pass
    return textes


def decouper_competences(texte):
    if not texte:
        return []
    return [c.strip() for c in texte.split(" | " if " | " in texte else ", ") if c.strip()]


def departement(lieu):
    m = re.match(r"^(\d{2,3}|2[AB])\s*-", lieu or "")
    if m:
        return m.group(1)
    return "Région seule" if (lieu or "").strip() in REGIONS else "Non précisé"


def region(lieu):
    d = departement(lieu)
    return REGION_DE.get(d) or ((lieu or "").strip() if d == "Région seule" else "Non précisé")


def groupe_contrat(offre):
    if offre["alternance"] == "Oui":
        return "Alternance"
    return offre["contrat"].split(" - ")[0]


def salaire_mensuel_brut(libelle):
    """« Mensuel de 1900 à 2300 Euros » → 2100 ; annuel ÷ 12 ; horaire × 35 h × 52 ÷ 12."""
    m = re.match(r"(Mensuel|Annuel|Horaire)", libelle or "")
    nombres = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*Euros", libelle or "")]
    if not m or not nombres:
        return None
    valeur = sum(nombres) / len(nombres)
    if m.group(1) == "Annuel":
        valeur /= 12
    elif m.group(1) == "Horaire":
        valeur *= HEURES_PAR_MOIS
    return valeur if 500 <= valeur <= 15000 else None


def top(compteur, cle="nom"):
    return [{cle: k, "n": n} for k, n in compteur.most_common(TOP)]


def compter_outils(offres, textes):
    """Pour chaque outil : nombre d'offres et nombre d'entreprises distinctes qui le citent."""
    avec_texte = [o for o in offres if textes.get(o.get("id"))]
    resultat = []
    for nom, motif in OUTILS:
        citent = [o for o in avec_texte if motif.search(textes[o["id"]] + " " + o["intitule"])]
        if citent:
            resultat.append({
                "nom": nom,
                "offres": len(citent),
                "entreprises": len({o["entreprise"] for o in citent}),
            })
    resultat.sort(key=lambda x: (-x["entreprises"], -x["offres"]))
    return resultat, len(avec_texte)


def calculer_salaires(offres):
    groupes = {}
    for o in offres:
        groupes.setdefault(groupe_contrat(o), []).append(o)
    lignes = []
    for nom, os_ in sorted(groupes.items(), key=lambda x: -len(x[1])):
        valeurs = [v for v in (salaire_mensuel_brut(o["salaire"]) for o in os_) if v]
        ligne = {"nom": nom, "total": len(os_), "affichent": len(valeurs)}
        if valeurs:
            ligne.update(mediane=round(statistics.median(valeurs)), min=round(min(valeurs)), max=round(max(valeurs)))
        lignes.append(ligne)
    return lignes


def main():
    fichiers = sorted(glob.glob(f"data/offres_{CODE_ROME}_*.csv"))
    textes = charger_textes()

    serie, serie_outils = [], []
    for chemin in fichiers:
        jour = re.search(r"(\d{4}-\d{2}-\d{2})\.csv$", chemin).group(1)
        lignes = lire(chemin)
        serie.append({
            "date": jour,
            "total": len(lignes),
            "alternance": sum(1 for l in lignes if l["alternance"] == "Oui"),
        })
        if lignes and "id" in lignes[0]:
            outils, n_texte = compter_outils(lignes, textes)
            serie_outils.append({"date": jour, "avec_texte": n_texte,
                                 "outils": {o["nom"]: o["offres"] for o in outils}})

    offres = lire(fichiers[-1])
    derniere_date = serie[-1]["date"]
    total = len(offres)

    try:
        ids_lba = {l["id"] for l in lire(f"data/offres_alternance_{CODE_ROME}_{derniere_date}.csv") if l.get("id")}
    except FileNotFoundError:
        ids_lba = set()
    ids_ft = {o["id"] for o in offres if o.get("id")}
    canaux = {"lba_distinctes": len(ids_lba), "lba_deja_dans_ft": len(ids_lba & ids_ft)} if ids_lba else None

    entreprises = Counter(o["entreprise"] for o in offres if o["entreprise"] != "Non précisé")
    top2 = entreprises.most_common(2)
    competences = Counter(c for o in offres for c in decouper_competences(o["competences"]))
    avec_salaire = sum(1 for o in offres if salaire_mensuel_brut(o["salaire"]))

    depts = Counter(departement(o["lieu"]) for o in offres)
    regions = Counter(region(o["lieu"]) for o in offres)
    outils, n_texte = compter_outils(offres, textes)
    teletravail = sum(1 for o in offres if textes.get(o.get("id")) and TELETRAVAIL.search(textes[o["id"]]))

    resume = {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "metier": "Assistant / Assistante marketing",
        "code_rome": CODE_ROME,
        "requete": f"API France Travail — Offres d'emploi v2, codeROME={CODE_ROME}, France entière",
        "serie": serie,
        "serie_outils": serie_outils,
        "derniere": {
            "date": derniere_date,
            "total": total,
            "alternance": serie[-1]["alternance"],
            "part_salaire_affiche": round(100 * avec_salaire / total),
            "contrats": top(Counter(o["contrat"].split(" - ")[0] for o in offres)),
            "natures": top(Counter(o["nature_contrat"] for o in offres)),
            "departements": top(depts),
            "regions": top(regions),
            "canaux": canaux,
            "n_puy_de_dome": depts.get("63", 0),
            "teletravail": {"offres": teletravail, "sur": n_texte},
            "entreprises": top(entreprises),
            "concentration_top2": {"noms": [n for n, _ in top2], "part": round(100 * sum(n for _, n in top2) / total)},
            "competences": top(competences),
            "salaires": {"mediane_insertion": MEDIANE_INSERTION, "groupes": calculer_salaires(offres)},
            "outils": {"avec_texte": n_texte, "liste": outils},
        },
    }

    with open("data/resume.json", "w", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=2)
    with open("data/rapport.md", "w", encoding="utf-8") as f:
        f.write(rapport(resume))
    print(f"resume.json et rapport.md écrits : {len(serie)} extraction(s), dernière = {derniere_date}, {total} offres")


def rapport(r):
    x = r["derniere"]
    p = lambda n, s: f"{round(100 * n / s)} %" if s else "–"
    L = [
        f"# Le marché de « {r['metier']} » (ROME {r['code_rome']})",
        "",
        f"- **Requête** : {r['requete']}",
        f"- **Date d'extraction** : {x['date']} · **{x['total']} offres** · dont {x['alternance']} en alternance",
        f"- **Extractions disponibles** : {', '.join(s['date'] for s in r['serie'])}",
        "",
        "## Où",
        "",
        "| Région | Offres |", "|---|---|",
        *[f"| {l['nom']} | {l['n']} |" for l in x["regions"]],
        "",
        f"Puy-de-Dôme (63) : **{x['n_puy_de_dome']}** offre(s). "
        f"Mentionnent le télétravail dans le texte : **{x['teletravail']['offres']}** sur {x['teletravail']['sur']} annonces lues "
        "(une mention peut l'exclure : c'est un repère, pas un décompte d'offres qui l'autorisent).",
        "",
        "## Contrats", "",
        "| Contrat | Offres |", "|---|---|",
        *[f"| {l['nom']} | {l['n']} |" for l in x["contrats"]],
        "",
        "## Salaires affichés (brut mensuel)", "",
        f"Seules {x['part_salaire_affiche']} % des offres affichent un salaire. Annuel ÷ 12, horaire × 35 h × 52 ÷ 12. "
        f"Repère du cours : {x['salaires']['mediane_insertion']} € brut (médiane d'insertion à un an). "
        "Un salaire affiché n'est pas un salaire versé.",
        "",
        "| Groupe | Offres | Avec salaire affiché | Médiane | Min – max |", "|---|---|---|---|---|",
        *[f"| {g['nom']} | {g['total']} | {g['affichent']} | "
          + (f"{g['mediane']} € | {g['min']} – {g['max']} €" if g["affichent"] else "– | –") + " |"
          for g in x["salaires"]["groupes"]],
        "",
        "## Outils et compétences cités dans les annonces", "",
        f"Texte lu pour {x['outils']['avec_texte']} annonces. Classés par nombre d'**entreprises** distinctes qui les citent "
        "(pour ne pas laisser un employeur qui publie le même gabarit vingt fois peser sur le classement).",
        "",
        "| Outil | Entreprises | Offres |", "|---|---|---|",
        *[f"| {o['nom']} | {o['entreprises']} | {o['offres']} |" for o in x["outils"]["liste"]],
        "",
        "## Qui publie", "",
        f"Les deux premiers employeurs ({' et '.join(x['concentration_top2']['noms'])}) publient "
        f"**{x['concentration_top2']['part']} %** des offres.",
        "",
        "| Entreprise | Offres |", "|---|---|",
        *[f"| {l['nom']} | {l['n']} |" for l in x["entreprises"]],
        "",
    ]
    return "\n".join(L)


if __name__ == "__main__":
    main()
