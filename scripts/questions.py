"""Questions supplémentaires posées au marché, pour les trois postes visés : data/questions.json,
lu par la page « Le métier ». Tout est recalculé à partir des fichiers datés et du texte des annonces.

Une offre est comptée une fois (dernière version connue de son identifiant) ; seules les offres de vrais
CDI et CDD sont gardées. Assistant marketing = offres du code M1620 dont le titre contient « assistant … marketing »."""
import csv
import glob
import json
import re
import statistics
from collections import Counter
from datetime import datetime, timezone

import resumer

ASSISTANT = re.compile(r"(?i)assistant\S*\s+(?:\S+\s+)?marketing")
POSTES = [
    ("responsable-ecommerce", "Responsable e-commerce"),
    ("responsable-marketing", "Responsable marketing"),
    ("assistant-marketing", "Assistant marketing"),
]
CHAMPS_APPOINT = ["experience", "statut", "secteur", "naf", "effectif_etab"]
IDF = {"75", "77", "78", "91", "92", "93", "94", "95"}


def lire_fichiers(motif):
    offres, dates = {}, []
    for chemin in sorted(glob.glob(motif)):
        rows = resumer.lire(chemin)
        if rows and "id" not in rows[0]:
            continue
        dates.append(re.search(r"(\d{4}-\d{2}-\d{2})\.csv$", chemin).group(1))
        for r in rows:
            offres[r["id"]] = r
    return offres, dates


def charger_postes(textes):
    appoint = {}
    for chemin in glob.glob("data/enrichissement_M1620_*.csv"):
        for r in resumer.lire(chemin):
            appoint[r["id"]] = r
    garder = resumer.emploi_seulement(textes)
    postes = {}
    for cle, libelle in POSTES:
        if cle == "assistant-marketing":
            brut, dates = lire_fichiers("data/offres_M1620_*.csv")
            offres = [dict(r) for r in brut.values() if garder(r) and ASSISTANT.search(r["intitule"])]
        else:
            brut, dates = lire_fichiers(f"data/offres_{cle}_*.csv")
            offres = [dict(r) for r in brut.values()]
        for r in offres:
            for champ in CHAMPS_APPOINT:
                if not r.get(champ):
                    r[champ] = appoint.get(r["id"], {}).get(champ, "")
        postes[cle] = {"libelle": libelle, "offres": offres, "depuis": dates[0] if dates else None, "jours": len(dates)}
    return postes


def pct(n, total):
    return round(100 * n / total) if total else 0


def mediane(valeurs):
    return round(statistics.median(valeurs)) if valeurs else None


# ---- 1. Outils : ce qui change quand on monte d'assistant à responsable
def question_outils(postes, textes):
    def part(offres, motif):
        return sum(1 for o in offres if motif.search(textes.get(o["id"], "") + " " + o["intitule"]))
    a, rm, re_ = (postes[k]["offres"] for k in ("assistant-marketing", "responsable-marketing", "responsable-ecommerce"))
    lignes = []
    for nom, motif in resumer.OUTILS:
        na, nr, ne = part(a, motif), part(rm, motif), part(re_, motif)
        if max(na, nr) < 2:
            continue
        lignes.append({"nom": nom, "assistant": pct(na, len(a)), "responsable_marketing": pct(nr, len(rm)),
                       "responsable_ecommerce": pct(ne, len(re_)), "ecart": pct(nr, len(rm)) - pct(na, len(a))})
    lignes.sort(key=lambda x: -x["ecart"])
    return {"n_assistant": len(a), "n_responsable_marketing": len(rm), "n_responsable_ecommerce": len(re_), "outils": lignes}


# ---- 2. Paris : vaut-il mieux s'y intéresser ?
def zone(lieu):
    dep = resumer.departement(lieu)
    if dep == "75":
        return "Paris (75)"
    if dep in {"92", "93", "94"}:
        return "Petite couronne (92, 93, 94)"
    if dep in IDF:
        return "Reste de l'Île-de-France"
    if resumer.region(lieu) == "Île-de-France":
        return "Île-de-France (département non précisé)"
    return "Hors Île-de-France" if dep not in ("Non précisé", "Région seule") or resumer.region(lieu) != "Non précisé" else "Lieu non précisé"


def question_paris(postes):
    sortie = {}
    for cle, p in postes.items():
        offres = p["offres"]
        zones = {}
        for o in offres:
            zones.setdefault(zone(o["lieu"]), []).append(o)
        lignes = []
        for nom, os_ in sorted(zones.items(), key=lambda x: -len(x[1])):
            sal = [v for v in (resumer.salaire_mensuel_brut(o["salaire"]) for o in os_) if v]
            avec_exp = [o for o in os_ if o["experience"]]
            lignes.append({"zone": nom, "n": len(os_), "part": pct(len(os_), len(offres)), "salaires": len(sal), "mediane": mediane(sal),
                           "debutant": pct(sum(1 for o in avec_exp if "débutant" in o["experience"].lower()), len(avec_exp)) if avec_exp else None,
                           "n_experience": len(avec_exp)})
        idf = [o for o in offres if resumer.region(o["lieu"]) == "Île-de-France"]
        reste = [o for o in offres if resumer.region(o["lieu"]) not in ("Île-de-France", "Non précisé")]
        sal = lambda os_: [v for v in (resumer.salaire_mensuel_brut(o["salaire"]) for o in os_) if v]
        sortie[cle] = {"n": len(offres), "idf_n": len(idf), "idf_part": pct(len(idf), len(offres)), "zones": lignes,
                       "salaire_idf": {"n": len(sal(idf)), "mediane": mediane(sal(idf))},
                       "salaire_reste": {"n": len(sal(reste)), "mediane": mediane(sal(reste))}}
    return sortie


# ---- 3. Missions récurrentes
VERBE = re.compile(r"^[\s\-–•*·▪✓>]*(?:\d+[.)]\s*)?([A-ZÉÈÀ][a-zéèêëàâîïôùûüç]+(?:er|ir|re))\b")
VERBES_EXCLUS = {"rejoindre", "postuler", "envoyer", "bénéficier", "avoir", "choisir", "découvrir", "contacter", "candidater"}
THEMES = [
    ("Stratégie et plan marketing", r"stratégi|plan marketing|plan d.actions?|positionnement|feuille de route"),
    ("Campagnes (conception, pilotage, suivi)", r"campagne"),
    ("Contenus et supports (création, rédaction)", r"contenu|support|rédig|rédac|visuel|brochure|plaquette|création|créer"),
    ("Réseaux sociaux et communication digitale", r"réseaux sociaux|social media|community|instagram|linkedin|facebook|tiktok"),
    ("Emailing, newsletters, CRM, fidélisation", r"e-?mailing|newsletter|\bcrm\b|fidélisation|marketing automation|base de données"),
    ("Site web, SEO, acquisition, e-commerce", r"site (?:web|internet)|\bseo\b|référencement|\bsea\b|acquisition|trafic|google ads|e-?commerce|marketplace|boutique en ligne"),
    ("Analyse, reporting, études, veille", r"reporting|analys|indicateurs|\bkpi|tableau de bord|étude|veille|benchmark|performance|bilan"),
    ("Budget, prestataires et agences", r"budget|prestataire|agence|fournisseur|appel d.offres|partenaire"),
    ("Événements, salons, webinaires", r"événement|évènement|salon|congrès|webinaire"),
    ("Appui commercial, ventes, promotion", r"commercia|vente|promotion|prospect|trade marketing|point de vente"),
    ("Produit, offre, catalogue, merchandising", r"catalogue|produit|offre|assortiment|merchandising|fiche"),
    ("Management et coordination d'équipe", r"manag|encadr|dirig|(?:animer|piloter|coordonner|diriger) (?:une |l[’']?|les )?équipes?|coordonn"),
    ("Communication interne et externe, presse", r"communication|presse|relations publiques|relations médias"),
    ("Suivi administratif, planning, coordination", r"administratif|planning|suivi des|saisie|commande|facturation"),
]
THEMES = [(n, re.compile(rx, re.I)) for n, rx in THEMES]


def lignes_missions(texte):
    morceaux = re.split(r"\n+|(?<=[.;!?])\s+(?=[A-ZÉÈ])", texte)
    sortie = []
    for m in morceaux:
        v = VERBE.match(m)
        if v and v.group(1).lower() not in VERBES_EXCLUS and len(m.strip()) > 25:
            sortie.append((v.group(1).lower(), m))
    return sortie


def question_missions(postes, textes):
    def analyser(offres):
        avec = []
        for o in offres:
            lm = lignes_missions(textes.get(o["id"], ""))
            if lm:
                avec.append(lm)
        themes, verbes = Counter(), Counter()
        for lm in avec:
            blob = " ".join(t for _, t in lm)
            for nom, rx in THEMES:
                if rx.search(blob):
                    themes[nom] += 1
            for v in {v for v, _ in lm}:
                verbes[v] += 1
        n = len(avec)
        return {"offres": len(offres), "avec_missions": n, "couverture": pct(n, len(offres)),
                "themes": [{"nom": k, "n": v, "part": pct(v, n)} for k, v in themes.most_common()],
                "verbes": [{"nom": k, "part": pct(v, n)} for k, v in verbes.most_common(8)]}
    par_poste = {cle: analyser(p["offres"]) for cle, p in postes.items()}
    toutes = [o for p in postes.values() for o in p["offres"]]
    return {"par_poste": par_poste, "tous": analyser(toutes)}


# ---- 4. Expérience demandée
def question_experience(postes):
    sortie = {}
    for cle, p in postes.items():
        offres = [o for o in p["offres"] if o["experience"]]
        cases = Counter()
        for o in offres:
            e = o["experience"].lower()
            m = re.search(r"(\d+)\s*an", e)
            if "débutant" in e:
                cases["Débutant accepté"] += 1
            elif m:
                n = int(m.group(1))
                cases["1 à 2 ans" if n <= 2 else "3 à 5 ans" if n <= 5 else "6 ans et plus"] += 1
            else:
                cases["Expérience exigée, durée non précisée"] += 1
        cadre = sum(1 for o in p["offres"] if re.search(r"(?<!non[- ])cadre", o["statut"], re.I))
        ordre = ["Débutant accepté", "1 à 2 ans", "3 à 5 ans", "6 ans et plus", "Expérience exigée, durée non précisée"]
        sortie[cle] = {"n": len(offres), "sur": len(p["offres"]), "repartition": [{"nom": k, "n": cases[k], "part": pct(cases[k], len(offres))} for k in ordre if cases[k]],
                       "cadre": pct(cadre, len(p["offres"]))}
    return sortie


# ---- 5. Qui recrute : type d'entreprise, secteur, taille
def type_employeur(naf):
    if not naf:
        return None
    d = naf[:2]
    if d == "78":
        return ("Intérim, recrutement, RH", True)
    if d == "73" or naf.startswith("70.21"):
        return ("Agence de publicité, communication, études de marché", True)
    if d in ("62", "63", "74", "82") or naf.startswith("70.22"):
        return ("Conseil, informatique, services aux entreprises", True)
    if d == "85":
        return ("Formation, enseignement", None)
    if d in ("58", "59", "60"):
        return ("Édition, presse, audiovisuel", None)
    if d.isdigit() and 10 <= int(d) <= 33:
        return ("Industrie", False)
    if d.isdigit() and 45 <= int(d) <= 47:
        return ("Commerce, distribution", False)
    if d in ("55", "56", "79", "90", "91", "92", "93"):
        return ("Tourisme, hôtellerie, loisirs", False)
    if d in ("64", "65", "66", "68"):
        return ("Banque, assurance, immobilier", False)
    if d in ("21", "86", "87", "88"):
        return ("Santé, pharmacie, action sociale", False)
    return ("Autres secteurs", False)


def question_recruteurs(postes):
    sortie = {}
    for cle, p in postes.items():
        offres = p["offres"]
        types, clients, secteurs, tailles = Counter(), Counter(), Counter(), Counter()
        for o in offres:
            t = type_employeur(o["naf"])
            if t:
                types[t[0]] += 1
                clients["clients" if t[1] else "formation_medias" if t[1] is None else "entreprise"] += 1
                secteurs[o["secteur"]] += 1
            taille = o["effectif_etab"]
            if taille:
                m = re.match(r"(\d+)", taille)
                n = int(m.group(1)) if m else 0
                tailles["Moins de 10 salariés" if n < 10 else "10 à 49" if n < 50 else "50 à 249" if n < 250 else "250 salariés et plus"] += 1
        connus = sum(types.values())
        sortie[cle] = {
            "n": len(offres), "secteur_connu": connus, "sans_nom": sum(1 for o in offres if o["entreprise"] == "Non précisé"),
            "types": [{"nom": k, "n": v} for k, v in types.most_common()],
            "pour_clients": clients["clients"], "pour_eux_memes": clients["entreprise"], "formation_medias": clients["formation_medias"],
            "secteurs": [{"nom": k, "n": v} for k, v in secteurs.most_common(5)],
            "taille_connue": sum(tailles.values()),
            "tailles": [{"nom": k, "n": tailles[k]} for k in ["Moins de 10 salariés", "10 à 49", "50 à 249", "250 salariés et plus"] if tailles[k]],
        }
    return sortie


def main():
    textes = resumer.charger_textes()
    postes = charger_postes(textes)
    plus_fourni = max(postes, key=lambda k: len(postes[k]["offres"]))
    resultat = {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "regle": "vrais CDI et CDD, une offre comptée une fois",
        "poste_de_reference": plus_fourni,
        "postes": {k: {"libelle": p["libelle"], "n": len(p["offres"]), "depuis": p["depuis"], "jours": p["jours"]} for k, p in postes.items()},
        "outils": question_outils(postes, textes),
        "paris": question_paris(postes),
        "missions": question_missions(postes, textes),
        "experience": question_experience(postes),
        "recruteurs": question_recruteurs(postes),
    }
    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=2)
    print("questions.json écrit :", {k: v["n"] for k, v in resultat["postes"].items()}, "| poste de référence :", plus_fourni)


if __name__ == "__main__":
    main()
