"""Marché caché : liste des entreprises des grandes villes de France susceptibles d'avoir besoin
d'un profil marketing, via l'API Recherche d'entreprises (data.gouv, gratuite, sans clé).

Sortie : data/entreprises.csv et data/entreprises_resume.json. Données d'entreprises uniquement,
aucun nom de personne (voir README : règle RGPD)."""
import csv
import json
import os
import re
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date

import requests

from resumer import REGION_DE, REGIONS

URL = "https://recherche-entreprises.api.gouv.fr/search"
CACHE = ".cache/entreprises"  # un fichier par code NAF ; supprimer le dossier pour tout re-télécharger

# Grandes villes = communes de plus de 100 000 habitants (geo.api.gouv.fr), regroupées par département.
VILLES = {
    "75": "Paris", "13": "Marseille, Aix-en-Provence", "69": "Lyon, Villeurbanne", "31": "Toulouse",
    "06": "Nice", "44": "Nantes", "34": "Montpellier", "67": "Strasbourg", "33": "Bordeaux", "59": "Lille",
    "35": "Rennes", "83": "Toulon", "51": "Reims", "42": "Saint-Étienne", "76": "Le Havre, Rouen",
    "21": "Dijon", "49": "Angers", "38": "Grenoble", "974": "Saint-Denis, Saint-Paul (La Réunion)",
    "30": "Nîmes", "63": "Clermont-Ferrand", "72": "Le Mans", "29": "Brest", "37": "Tours", "80": "Amiens",
    "74": "Annecy", "87": "Limoges", "57": "Metz", "66": "Perpignan", "92": "Boulogne-Billancourt",
    "25": "Besançon", "45": "Orléans", "93": "Saint-Denis, Montreuil", "14": "Caen", "95": "Argenteuil",
    "68": "Mulhouse", "54": "Nancy",
}
# « Nord » = ville plus haute que Paris en latitude, hors Île-de-France.
DEPTS_NORD = {"59", "51", "76", "80", "57", "14"}

# Salariés : à partir de 6 (codes INSEE de tranche). Mettre "01,02,03,..." pour descendre à 1 salarié.
TRANCHES = "03,11,12,21,22,31,32,41,42,51,52,53"
TRANCHE_LIBELLE = {
    "03": "6 à 9", "11": "10 à 19", "12": "20 à 49", "21": "50 à 99", "22": "100 à 199", "31": "200 à 249",
    "32": "250 à 499", "41": "500 à 999", "42": "1 000 à 1 999", "51": "2 000 à 4 999", "52": "5 000 à 9 999",
    "53": "10 000 et plus",
}

AGENCES = {
    "73.11Z": "Agences de publicité", "73.12Z": "Régie publicitaire de médias",
    "70.21Z": "Conseil en relations publiques et communication", "73.20Z": "Études de marché et sondages",
    "74.10Z": "Design spécialisé",
}
AUTRES = {
    "E-commerce": {"47.91A": "Vente à distance sur catalogue général", "47.91B": "Vente à distance sur catalogue spécialisé"},
    "Numérique": {
        "58.29A": "Édition de logiciels système et de réseau", "58.29B": "Édition de logiciels outils de développement",
        "58.29C": "Édition de logiciels applicatifs", "62.01Z": "Programmation informatique",
        "62.02A": "Conseil en systèmes et logiciels informatiques", "63.11Z": "Traitement de données, hébergement",
        "63.12Z": "Portails Internet",
    },
    "Édition et médias": {
        "58.11Z": "Édition de livres", "58.13Z": "Édition de journaux", "58.14Z": "Édition de revues et périodiques",
        "58.19Z": "Autres activités d'édition", "59.11A": "Production de films pour la télévision",
        "59.11B": "Production de films institutionnels et publicitaires", "59.11C": "Production de films pour le cinéma",
        "60.20A": "Édition de chaînes généralistes", "63.91Z": "Activités des agences de presse",
    },
    "Événementiel": {"82.30Z": "Organisation de salons professionnels et congrès"},
    "Marques et commerce spécialisé": {
        "20.42Z": "Fabrication de parfums et produits de toilette", "47.75Z": "Commerce de détail de parfumerie et beauté",
        "47.71Z": "Commerce de détail d'habillement", "47.78C": "Autres commerces de détail spécialisés",
    },
}
# Industrie manufacturière (section C de la NAF), ajoutée le 14/11/2026 : les offres de responsable marketing
# viennent d'abord de l'industrie (alimentaire, chimie-cosmétique, pharmacie, électronique, machines, meubles…).
# L'API ne filtre pas par division, donc on prend toute la section C, à partir de 20 salariés : un poste de
# responsable marketing existe rarement en dessous (parmi les offres lues, 11 établissements sur 12 dont la taille est connue ont 20 salariés ou plus).
TRANCHES_INDUSTRIE = "12,21,22,31,32,41,42,51,52,53"
DIVISIONS_INDUSTRIE = {
    "10": "Industries alimentaires", "11": "Fabrication de boissons", "12": "Fabrication de produits à base de tabac",
    "13": "Fabrication de textiles", "14": "Industrie de l'habillement", "15": "Industrie du cuir et de la chaussure",
    "16": "Travail du bois", "17": "Industrie du papier et du carton", "18": "Imprimerie et reproduction",
    "19": "Cokéfaction et raffinage", "20": "Industrie chimique (dont cosmétique, détergents)", "21": "Industrie pharmaceutique",
    "22": "Caoutchouc et plastique", "23": "Autres produits minéraux non métalliques", "24": "Métallurgie",
    "25": "Produits métalliques", "26": "Produits informatiques, électroniques et optiques", "27": "Équipements électriques",
    "28": "Machines et équipements", "29": "Industrie automobile", "30": "Autres matériels de transport",
    "31": "Fabrication de meubles", "32": "Autres industries manufacturières", "33": "Réparation et installation de machines",
}
CODES = {c: ("Agences", lib) for c, lib in AGENCES.items()}
for groupe, codes in AUTRES.items():
    CODES.update({c: (groupe, lib) for c, lib in codes.items()})

COLONNES = ["section", "type", "groupe", "region", "grande_ville", "departement", "commune", "adresse", "nom", "siren",
            "naf", "activite", "effectif", "taille", "date_creation", "fiche"]
ORDRE_SECTION = {"principale": 0, "industrie": 1, "agences": 2, "nord": 3}
RANG_TAILLE = {code: i + 1 for i, code in enumerate(TRANCHE_LIBELLE)}


def appeler(params):
    for essai in range(6):
        time.sleep(0.16)
        try:
            r = requests.get(URL, params=params, timeout=40)
        except requests.exceptions.RequestException:  # connexion coupée : on réessaie
            time.sleep(3 * (essai + 1))
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(2 * (essai + 1))
            continue
        r.raise_for_status()
    raise RuntimeError(f"API indisponible : {params}")


def lignes_pour(code, departements, filtre=None, tranches=TRANCHES):
    """Toutes les entreprises du code NAF (ou du filtre donné) dans les départements donnés (plafond API : 10 000 résultats)."""
    base = {"etat_administratif": "A", "tranche_effectif_salarie": tranches,
            "departement": ",".join(departements), "per_page": 25, **(filtre or {"activite_principale": code})}
    premier = appeler({**base, "page": 1})
    total = premier["total_results"]
    if total >= 10000 and len(departements) > 1:
        print(f"  {code} : {total} résultats, plafond atteint → découpage par département")
        return [r for d in departements for r in lignes_pour(code, [d], filtre, tranches)]
    resultats = list(premier["results"])
    pages = range(2, premier["total_pages"] + 1)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for page_resultats in pool.map(lambda p: appeler({**base, "page": p})["results"], pages):
            resultats += page_resultats
    return resultats


def reduire(r):
    s = r["siege"]
    return {"siren": r["siren"], "nom_complet": r["nom_complet"], "date_creation": r.get("date_creation"),
            "activite_principale": r.get("activite_principale"),
            "tranche_effectif_salarie": r.get("tranche_effectif_salarie"),
            "siege": {"departement": s.get("departement"), "adresse": s.get("adresse"),
                      "tranche_effectif_salarie": s.get("tranche_effectif_salarie")}}


def charger(code, departements, filtre=None, tranches=TRANCHES):
    chemin = f"{CACHE}/{code}.json"
    if os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    brut = [reduire(r) for r in lignes_pour(code, departements, filtre, tranches)]
    os.makedirs(CACHE, exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(brut, f, ensure_ascii=False)
    return brut


def commune(adresse):
    m = re.search(r"\b\d{5}\s+(.+)$", adresse or "")
    return m.group(1).title() if m else ""


def main():
    departements = list(VILLES)
    vus, hors_siege, tranche_inconnue = {}, 0, 0
    # (code ou clé de cache, groupe, libellé, filtre API, tranches)
    taches = [(c, g, lib, None, TRANCHES) for c, (g, lib) in CODES.items()]
    taches.append(("industrie", "Industrie", "", {"section_activite_principale": "C"}, TRANCHES_INDUSTRIE))
    for i, (code, groupe, libelle, filtre, tranches) in enumerate(taches, 1):
        brut = charger(code, departements, filtre, tranches)
        gardees = 0
        for r in brut:
            s = r["siege"]
            dep = s.get("departement")
            if dep not in VILLES:
                hors_siege += 1
                continue
            if r["siren"] in vus:
                continue
            gardees += 1
            naf = r.get("activite_principale") if filtre else code
            if filtre:
                libelle_ligne = DIVISIONS_INDUSTRIE.get((naf or "")[:2], "Industrie")
            else:
                libelle_ligne = libelle
            est_agence = code in AGENCES
            if dep in DEPTS_NORD:
                section = "nord"
            elif filtre:
                section = "industrie"
            else:
                section = "agences" if est_agence else "principale"
            effectif = r.get("tranche_effectif_salarie") or s.get("tranche_effectif_salarie") or ""
            if effectif not in TRANCHE_LIBELLE:
                tranche_inconnue += 1
                effectif = ""
            vus[r["siren"]] = {
                "section": section, "type": "agence" if est_agence else "entreprise", "groupe": groupe,
                "region": REGION_DE.get(dep, ""), "grande_ville": VILLES[dep], "departement": dep, "commune": commune(s.get("adresse")),
                "adresse": s.get("adresse") or "", "nom": re.sub(r"^(.+) \(\1\)$", r"\1", r["nom_complet"]), "siren": r["siren"], "naf": naf,
                "activite": libelle_ligne, "effectif": effectif, "taille": TRANCHE_LIBELLE.get(effectif, ""),
                "date_creation": r.get("date_creation") or "",
                "fiche": f"https://annuaire-entreprises.data.gouv.fr/entreprise/{r['siren']}",
            }
        print(f"[{i}/{len(taches)}] {code} {libelle} : {len(brut)} reçues, {gardees} nouvelles gardées")

    lignes = sorted(vus.values(), key=lambda x: (ORDRE_SECTION[x["section"]], -RANG_TAILLE.get(x["effectif"], 0), x["nom"]))
    with open("data/entreprises.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLONNES)
        w.writeheader()
        w.writerows(lignes)

    resume = {
        "genere_le": date.today().isoformat(),
        "total": len(lignes),
        "sections": dict(Counter(l["section"] for l in lignes)),
        "par_groupe": dict(Counter(l["groupe"] for l in lignes)),
        "par_ville": dict(Counter(l["grande_ville"] for l in lignes).most_common()),
        "regions": {
            region: {
                "entreprises": n,
                "departements_couverts": sum(1 for d in REGIONS[region].split() if d in VILLES),
                "departements_total": len(REGIONS[region].split()),
            }
            for region, n in Counter(l["region"] for l in lignes).most_common()
        },
        "taille_min": "6 salariés (20 pour l'industrie)",
        "ecartees_siege_hors_villes": hors_siege,
        "taille_inconnue": tranche_inconnue,
    }
    with open("data/entreprises_resume.json", "w", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=2)
    print(f"\n{len(lignes)} entreprises → data/entreprises.csv  ({resume['sections']})")
    print(f"{hors_siege} résultats écartés : siège hors des villes visées ; {tranche_inconnue} entreprises sans taille connue")


if __name__ == "__main__":
    main()
