"""Test de connexion à l'API La Bonne Alternance : vérifie que le jeton
fonctionne, sans rien afficher de sensible."""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("LABONNEALTERNANCE_API_KEY")
SEARCH_URL = "https://api.apprentissage.beta.gouv.fr/api/job/v1/search"

if not API_KEY:
    print("❌ Clé manquante dans .env")
    sys.exit(1)

response = requests.get(
    SEARCH_URL,
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"romes": "M1620"},
)

if response.status_code == 200:
    data = response.json()
    print("✅ Connexion réussie !")
    print(f"   Clés présentes dans la réponse : {list(data.keys())}")
else:
    print(f"❌ Échec (code {response.status_code})")
    print(f"   Réponse : {response.text[:300]}")
