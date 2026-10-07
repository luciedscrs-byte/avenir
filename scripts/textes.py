"""Garde le texte de chaque annonce dans data/textes.jsonl, une seule fois par
identifiant d'offre (le texte ne change presque jamais d'un jour à l'autre)."""
import json
import os
from datetime import date

CHEMIN = "data/textes.jsonl"


def ids_connus():
    if not os.path.exists(CHEMIN):
        return set()
    with open(CHEMIN, encoding="utf-8") as f:
        return {json.loads(ligne)["id"] for ligne in f if ligne.strip()}


def enregistrer(annonces):
    """annonces : liste de dicts {id, source, intitule, description}.
    Retourne le nombre de textes ajoutés."""
    os.makedirs("data", exist_ok=True)
    connus = ids_connus()
    nouveaux = 0
    with open(CHEMIN, "a", encoding="utf-8") as f:
        for a in annonces:
            if not a["id"] or a["id"] in connus:
                continue
            connus.add(a["id"])
            f.write(json.dumps({**a, "date_vue": date.today().isoformat()}, ensure_ascii=False) + "\n")
            nouveaux += 1
    return nouveaux
