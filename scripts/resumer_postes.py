"""Résumé des séries « postes de responsable » : data/resume_postes.json, lu par le site."""
import glob
import json
import re
import statistics
from collections import Counter
from datetime import datetime, timezone

import resumer
from postes import SERIES


def resume_serie(nom, libelle, codes):
    fichiers = sorted(glob.glob(f"data/offres_{nom}_*.csv"))
    if not fichiers:
        return None
    serie = []
    for chemin in fichiers:
        jour = re.search(r"(\d{4}-\d{2}-\d{2})\.csv$", chemin).group(1)
        serie.append({"date": jour, "total": len(resumer.lire(chemin))})
    offres = resumer.lire(fichiers[-1])
    n = len(offres) or 1
    salaires = [v for v in (resumer.salaire_mensuel_brut(o["salaire"]) for o in offres) if v]
    entreprises = Counter(o["entreprise"] for o in offres if o["entreprise"] != "Non précisé")
    return {
        "libelle": libelle,
        "codes": codes,
        "depuis": serie[0]["date"],
        "serie": serie,
        "derniere": {
            "date": serie[-1]["date"],
            "total": len(offres),
            "contrats": dict(Counter(o["contrat"].split(" - ")[0] for o in offres)),
            "regions": [{"nom": k, "n": v} for k, v in Counter(resumer.region(o["lieu"]) for o in offres).most_common(5)],
            "debutant_accepte": round(100 * sum(1 for o in offres if "débutant" in o["experience"].lower()) / n),
            "cadre": round(100 * sum(1 for o in offres if re.search(r"(?<!non[- ])cadre", o["statut"], re.I)) / n),
            "salaire_affiche": {"offres": len(salaires), "mediane_mensuelle": round(statistics.median(salaires)) if salaires else None},
            "sans_nom_employeur": sum(1 for o in offres if o["entreprise"] == "Non précisé"),
            "entreprises": [{"nom": k, "n": v} for k, v in entreprises.most_common(5)],
        },
    }


def main():
    resume = {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "regle": "CDI ou CDD seulement ; sans alternance, stage, intérim ni annonce de formation",
        "postes": {nom: resume_serie(nom, s["libelle"], s["codes"]) for nom, s in SERIES.items()},
    }
    with open("data/resume_postes.json", "w", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=2)
    for nom, p in resume["postes"].items():
        if p:
            print(f"{p['libelle']} : {p['derniere']['total']} offres le {p['derniere']['date']} (suivi depuis le {p['depuis']})")


if __name__ == "__main__":
    main()
