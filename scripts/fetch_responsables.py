"""Postes de responsable (marketing, e-commerce) : offres de vrais CDI / CDD, via l'API France Travail.

Une offre est retenue si son titre contient l'intitulé visé ET si c'est un emploi : CDI ou CDD, sans
alternance, sans stage ni apprentissage dans le titre, sans annonce de formation à distance.
Sortie : data/offres_<série>_<date>.csv, même colonnes que l'extraction M1620, dont l'expérience demandée et le statut."""
import csv
import os
import re
import time
from datetime import date

import requests

import fetch_offres
import textes
from postes import SERIES

SEARCH_URL = fetch_offres.SEARCH_URL

STAGE = re.compile(r"(?i)\bstage\b|stagiaire|altern|apprenti")
PUB_FORMATION = re.compile(r"(?i)en suivant la formation|formation .{0,40}à distance")


def est_un_emploi(offre):
    return (offre.get("typeContrat") in ("CDI", "CDD")
            and offre.get("natureContrat") == "Contrat travail"
            and not offre.get("alternance")
            and not STAGE.search(offre.get("intitule", ""))
            and not PUB_FORMATION.search(offre.get("description") or ""))


def rechercher(token, **filtre):
    headers = {"Authorization": f"Bearer {token}"}
    resultats, debut = [], 0
    while True:
        time.sleep(0.3)
        r = requests.get(SEARCH_URL, headers=headers, params={**filtre, "range": f"{debut}-{debut + 149}"})
        if r.status_code not in (200, 206):
            break
        resultats += r.json().get("resultats", [])
        total = int(r.headers.get("Content-Range", "/0").split("/")[-1])
        if len(resultats) >= total:
            break
        debut += 150
    return resultats


def extraire(serie, token):
    candidates = {}
    for code in serie["codes"]:
        for o in rechercher(token, codeROME=code):
            candidates[o["id"]] = o
    for mots in serie["mots"]:
        for o in rechercher(token, motsCles=mots):
            candidates[o["id"]] = o
    au_bon_titre = [o for o in candidates.values() if serie["titre"].search(o.get("intitule", ""))]
    retenues = [o for o in au_bon_titre if est_un_emploi(o)]
    return len(candidates), len(au_bon_titre), retenues


def main():
    token = fetch_offres.get_token()
    os.makedirs("data", exist_ok=True)
    for nom, serie in SERIES.items():
        vues, au_bon_titre, retenues = extraire(serie, token)
        lignes = [fetch_offres.extraire_champs(o) for o in retenues]
        textes.enregistrer(
            {"id": o.get("id"), "source": "France Travail", "intitule": o.get("intitule", ""), "description": o.get("description", "")}
            for o in retenues
        )
        chemin = f"data/offres_{nom}_{date.today().isoformat()}.csv"
        colonnes = list(fetch_offres.extraire_champs({}).keys())
        with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=colonnes)
            w.writeheader()
            w.writerows(lignes)
        print(f"{serie['libelle']} : {vues} offres examinées, {au_bon_titre} au bon titre, {len(lignes)} vrais CDI/CDD → {chemin}")
        for l in lignes[:5]:
            print(f"  - {l['intitule'][:48]} | {l['entreprise'][:22]} | {l['lieu'][:24]} | {l['contrat'][:12]}")


if __name__ == "__main__":
    main()
