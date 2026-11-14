"""Définition des séries « postes de responsable » : intitulés visés et façon de les repérer."""
import re

SERIES = {
    "responsable-marketing": {
        "libelle": "Responsable marketing",
        "codes": ["M1705", "M1716", "M1718", "M1711"],
        "mots": ["responsable marketing", "responsable marketing digital", "responsable webmarketing"],
        "titre": re.compile(r"(?i)responsable\s+(?:du\s+|de\s+|des\s+)?(?:webmarketing|marketing)"),
    },
    "responsable-ecommerce": {
        "libelle": "Responsable e-commerce",
        "codes": ["E1113"],
        "mots": ["responsable e-commerce", "e-commerce manager"],
        "titre": re.compile(r"(?i)responsable\s+(?:de\s+l[’']?\s*|du\s+|des\s+)?(?:\S+\s+)?e-?\s?commerce|e-?\s?commerce\s+manager"),
    },
}
