"""Lit tous les CSV France Travail datés de data/ et produit data/resume.json,
le seul fichier que le site affiche."""
import csv
import glob
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone

CODE_ROME = "M1620"
TOP = 10


def lire(chemin):
    with open(chemin, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def decouper_competences(texte):
    if not texte:
        return []
    return [c.strip() for c in texte.split(" | " if " | " in texte else ", ") if c.strip()]


def departement(lieu):
    m = re.match(r"^(\d{2,3}|2[AB])\s*-", lieu or "")
    return m.group(1) if m else "Non précisé"


def top(compteur, cle):
    return [{cle: k, "n": n} for k, n in compteur.most_common(TOP)]


def main():
    fichiers = sorted(glob.glob(f"data/offres_{CODE_ROME}_*.csv"))
    serie = []
    for chemin in fichiers:
        jour = re.search(r"(\d{4}-\d{2}-\d{2})\.csv$", chemin).group(1)
        lignes = lire(chemin)
        serie.append({
            "date": jour,
            "total": len(lignes),
            "alternance": sum(1 for l in lignes if l["alternance"] == "Oui"),
        })

    offres = lire(fichiers[-1])
    derniere_date = serie[-1]["date"]

    entreprises = Counter(o["entreprise"] for o in offres if o["entreprise"] != "Non précisé")
    competences = Counter(c for o in offres for c in decouper_competences(o["competences"]))
    avec_salaire = sum(1 for o in offres if not o["salaire"].startswith("Non précisé"))

    resume = {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "metier": "Assistant / Assistante marketing",
        "code_rome": CODE_ROME,
        "requete": f"API France Travail — Offres d'emploi v2, codeROME={CODE_ROME}, France entière",
        "serie": serie,
        "derniere": {
            "date": derniere_date,
            "total": len(offres),
            "alternance": serie[-1]["alternance"],
            "part_salaire_affiche": round(100 * avec_salaire / len(offres)),
            "contrats": top(Counter(o["contrat"].split(" - ")[0] for o in offres), "nom"),
            "natures": top(Counter(o["nature_contrat"] for o in offres), "nom"),
            "departements": top(Counter(departement(o["lieu"]) for o in offres), "nom"),
            "entreprises": top(entreprises, "nom"),
            "competences": top(competences, "nom"),
        },
    }

    with open("data/resume.json", "w", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=2)
    print(f"resume.json écrit : {len(serie)} extraction(s), dernière = {derniere_date}, {len(offres)} offres")


if __name__ == "__main__":
    main()
