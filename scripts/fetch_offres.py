"""Récupère toutes les offres d'emploi pour le métier ciblé (code ROME M1620)
via l'API France Travail 'Offres d'emploi v2', et les enregistre dans un CSV
daté dans data/.
"""
import csv
import os
from datetime import date

import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ["FRANCE_TRAVAIL_CLIENT_ID"]
CLIENT_SECRET = os.environ["FRANCE_TRAVAIL_CLIENT_SECRET"]
CODE_ROME = "M1620"

TOKEN_URL = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"
SEARCH_URL = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"

PAGE_SIZE = 150


def get_token():
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": "api_offresdemploiv2 o2dsoffre",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    return response.json()["access_token"]


def fetch_all_offres(token):
    headers = {"Authorization": f"Bearer {token}"}
    offres = []
    start = 0

    while True:
        end = start + PAGE_SIZE - 1
        response = requests.get(
            SEARCH_URL,
            headers=headers,
            params={"codeROME": CODE_ROME, "range": f"{start}-{end}"},
        )

        if response.status_code not in (200, 206):
            print(f"Arrêt : réponse inattendue ({response.status_code}) — {response.text[:200]}")
            break

        page = response.json().get("resultats", [])
        offres.extend(page)

        content_range = response.headers.get("Content-Range", "")
        total = int(content_range.split("/")[-1]) if "/" in content_range else len(offres)

        if len(offres) >= total or not page:
            return offres, total

        start += PAGE_SIZE


def extraire_champs(offre):
    lieu = offre.get("lieuTravail", {}).get("libelle", "")
    entreprise = offre.get("entreprise", {}).get("nom", "Non précisé")
    salaire = offre.get("salaire", {}).get("libelle", "Non précisé")
    competences = ", ".join(c.get("libelle", "") for c in offre.get("competences", []))

    return {
        "intitule": offre.get("intitule", ""),
        "entreprise": entreprise,
        "lieu": lieu,
        "contrat": offre.get("typeContratLibelle", ""),
        "alternance": "Oui" if offre.get("alternance") else "Non",
        "nature_contrat": offre.get("natureContrat", ""),
        "salaire": salaire,
        "date_publication": offre.get("dateCreation", ""),
        "competences": competences,
    }


def main():
    print(f"Connexion à l'API pour le code ROME {CODE_ROME}...")
    token = get_token()

    print("Récupération des offres...")
    offres_brutes, total = fetch_all_offres(token)

    lignes = [extraire_champs(o) for o in offres_brutes]

    os.makedirs("data", exist_ok=True)
    chemin_csv = f"data/offres_{CODE_ROME}_{date.today().isoformat()}.csv"

    with open(chemin_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(lignes[0].keys()) if lignes else [])
        writer.writeheader()
        writer.writerows(lignes)

    nb_alternance = sum(1 for l in lignes if l["alternance"] == "Oui")

    print(f"\nTotal d'offres déclaré par l'API : {total}")
    print(f"Total d'offres récupérées et enregistrées : {len(lignes)}")
    print(f"Dont alternance : {nb_alternance}")
    print(f"Fichier : {chemin_csv}\n")

    print("Aperçu des 5 premières offres :")
    for ligne in lignes[:5]:
        marque = " [ALTERNANCE]" if ligne["alternance"] == "Oui" else ""
        print(f"- {ligne['intitule']} | {ligne['entreprise']} | {ligne['lieu']} | {ligne['contrat']}{marque}")


if __name__ == "__main__":
    main()
