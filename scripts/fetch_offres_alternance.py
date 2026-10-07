"""Récupère les offres d'alternance (et le marché caché) pour le métier ciblé
(code ROME M1620) via l'API La Bonne Alternance, et les enregistre dans un CSV
daté dans data/, au même format que le CSV France Travail.
"""
import csv
import html
import os
from datetime import date

import requests
from dotenv import load_dotenv

import textes

load_dotenv()

API_KEY = os.environ["LABONNEALTERNANCE_API_KEY"]
CODE_ROME = "M1620"
SEARCH_URL = "https://api.apprentissage.beta.gouv.fr/api/job/v1/search"


def fetch_jobs_and_recruiters():
    response = requests.get(
        SEARCH_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"romes": CODE_ROME},
    )
    response.raise_for_status()
    data = response.json()
    return data.get("jobs") or [], data.get("recruiters") or []


def identifiant(job):
    ident = job.get("identifier") or {}
    return ident.get("partner_job_id") or ident.get("id") or ""


def extraire_champs_offre(job):
    offer = job.get("offer", {})
    workplace = job.get("workplace", {})
    contract = job.get("contract", {})
    skills = " | ".join(offer.get("desired_skills") or [])

    return {
        "intitule": html.unescape(offer.get("title", "")),
        "entreprise": workplace.get("name") or workplace.get("legal_name") or "Non précisé",
        "lieu": (workplace.get("location") or {}).get("address", ""),
        "contrat": ", ".join(contract.get("type") or []),
        "alternance": "Oui",
        "nature_contrat": ", ".join(contract.get("type") or []),
        "salaire": "Non précisé",
        "date_publication": (offer.get("publication") or {}).get("creation", ""),
        "competences": skills,
        "source": job.get("identifier", {}).get("partner_label", "La Bonne Alternance"),
        "id": identifiant(job),
        "url": (job.get("apply") or {}).get("url") or "",
    }


def extraire_champs_recruteur(recruiter):
    workplace = recruiter.get("workplace", {})
    return {
        "intitule": f"[Marché caché] Candidature spontanée — {CODE_ROME}",
        "entreprise": workplace.get("name") or workplace.get("legal_name", ""),
        "lieu": (workplace.get("location") or {}).get("address", ""),
        "contrat": "Non précisé (pas d'offre publiée)",
        "alternance": "Oui",
        "nature_contrat": "Candidature spontanée",
        "salaire": "Non précisé",
        "date_publication": "",
        "competences": "",
        "source": "La Bonne Alternance (recruteur sans offre)",
        "id": "",
        "url": "",
    }


def main():
    print(f"Récupération des offres La Bonne Alternance pour {CODE_ROME}...")
    jobs, recruiters = fetch_jobs_and_recruiters()

    recues = len(jobs)
    vus = set()
    distinctes = []
    for j in jobs:
        cle = identifiant(j)
        if cle and cle in vus:
            continue
        vus.add(cle)
        distinctes.append(j)
    jobs = distinctes
    print(f"{recues} lignes reçues de l'API, {len(jobs)} offres distinctes (l'API renvoie chaque offre en double)")

    nouveaux_textes = textes.enregistrer(
        {"id": identifiant(j), "source": j.get("identifier", {}).get("partner_label", "La Bonne Alternance"),
         "intitule": html.unescape((j.get("offer") or {}).get("title", "")),
         "description": html.unescape((j.get("offer") or {}).get("description") or "")}
        for j in jobs
    )

    lignes = [extraire_champs_offre(j) for j in jobs]
    lignes += [extraire_champs_recruteur(r) for r in recruiters]

    os.makedirs("data", exist_ok=True)
    chemin_csv = f"data/offres_alternance_{CODE_ROME}_{date.today().isoformat()}.csv"

    with open(chemin_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(lignes[0].keys()) if lignes else [])
        writer.writeheader()
        writer.writerows(lignes)

    print(f"\nOffres d'alternance récupérées : {len(jobs)}")
    print(f"Entreprises du marché caché (sans offre publiée) : {len(recruiters)}")
    print(f"Textes d'annonces nouveaux ajoutés à data/textes.jsonl : {nouveaux_textes}")
    print(f"Fichier : {chemin_csv}\n")

    print("Aperçu des 5 premières lignes :")
    for ligne in lignes[:5]:
        print(f"- {ligne['intitule']} | {ligne['entreprise']} | {ligne['lieu']} | source: {ligne['source']}")


if __name__ == "__main__":
    main()
