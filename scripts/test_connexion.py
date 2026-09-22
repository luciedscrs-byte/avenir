"""Test de connexion à l'API France Travail : vérifie que les identifiants
et l'abonnement à l'API 'Offres d'emploi v2' fonctionnent, sans rien afficher
de sensible."""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("FRANCE_TRAVAIL_CLIENT_ID")
CLIENT_SECRET = os.environ.get("FRANCE_TRAVAIL_CLIENT_SECRET")

TOKEN_URL = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"

if not CLIENT_ID or not CLIENT_SECRET:
    print("❌ Identifiants manquants dans .env")
    sys.exit(1)

response = requests.post(
    TOKEN_URL,
    data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": f"api_offresdemploiv2 o2dsoffre",
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"},
)

if response.status_code == 200:
    print("✅ Connexion réussie ! Le jeton d'accès a bien été obtenu.")
    print(f"   Type de jeton : {response.json().get('token_type')}")
    print(f"   Expire dans : {response.json().get('expires_in')} secondes")
else:
    print(f"❌ Échec de connexion (code {response.status_code})")
    print(f"   Réponse : {response.text[:300]}")
