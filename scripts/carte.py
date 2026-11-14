"""Carte territoire × secteur : recoupe la liste des entreprises (marché caché) avec les offres publiées
(les trois postes, vrais CDI / CDD) par département. Sortie : data/carte.json, lue par entreprises.html.

Entreprises : département du siège (data/entreprises.csv). Offres : département du lieu de travail,
chaque offre comptée une fois depuis le début du suivi de son poste."""
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone

import questions
import resumer
from entreprises import VILLES


def main():
    entreprises = defaultdict(Counter)
    ville = {}
    with open("data/entreprises.csv", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            entreprises[r["departement"]][r["groupe"]] += 1
            ville[r["departement"]] = r["grande_ville"]

    textes = resumer.charger_textes()
    postes = questions.charger_postes(textes)
    offres = defaultdict(Counter)
    sans_lieu = Counter()
    for cle, p in postes.items():
        for o in p["offres"]:
            d = resumer.departement(o["lieu"])
            if d in ("Région seule", "Non précisé"):
                sans_lieu[cle] += 1
            else:
                offres[d][cle] += 1

    deps = {}
    for d in sorted(set(entreprises) | set(offres)):
        deps[d] = {
            "ville": ville.get(d, ""),
            "couvert": d in VILLES,
            "entreprises": dict(entreprises[d]) | {"total": sum(entreprises[d].values())},
            "offres": dict(offres[d]) | {"total": sum(offres[d].values())},
        }
    resultat = {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "regle": "entreprises : département du siège ; offres : département du lieu de travail, vrais CDI / CDD, chaque offre comptée une fois",
        "postes": {k: {"libelle": p["libelle"], "n": len(p["offres"]), "depuis": p["depuis"]} for k, p in postes.items()},
        "groupes": sorted({g for d in entreprises.values() for g in d}),
        "offres_sans_departement": dict(sans_lieu),
        "departements": deps,
    }
    with open("data/carte.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
    total_offres = sum(d["offres"]["total"] for d in deps.values())
    hors_couverture = sum(d["offres"]["total"] for d in deps.values() if not d["couvert"])
    print(f"carte.json : {len(deps)} départements, {total_offres} offres localisées dont {hors_couverture} hors des départements couverts, "
          f"{sum(sans_lieu.values())} sans département")


if __name__ == "__main__":
    main()
