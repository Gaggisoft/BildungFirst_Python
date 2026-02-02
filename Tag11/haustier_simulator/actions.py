# ---------------------------------------------------------
# Level 2 – Aktionen
# Dieses Modul enthält die verschiedenen Aktionen, die der Spieler
# mit seinem Haustier durchführen kann, sowie deren humorvolle Reaktionen.
# ---------------------------------------------------------

import random  # Für zufällige Auswahl der Reaktionen

def feed():
    """Gibt eine zufällige humorvolle Reaktion zurück, wenn das Haustier gefüttert wird.
    
    Returns:
        String mit einer zufälligen Fütterungs-Reaktion
    """
    # Liste möglicher humorvoller Reaktionen beim Füttern
    reactions = [
        "Es frisst alles auf – inklusive deiner Hausaufgaben.",
        "Es schnuppert am Futter und entscheidet sich dann für deine Socke.",
        "Es isst… und isst… und isst…",
        "Es hat den Snack versteckt. Niemand weiß wo."
    ]
    return random.choice(reactions)

def play():
    """Gibt eine zufällige humorvolle Reaktion zurück, wenn mit dem Haustier gespielt wird.
    
    Returns:
        String mit einer zufälligen Spiel-Reaktion
    """
    # Liste möglicher humorvoller Spielszenarien
    actions = [
        "Ihr spielt Fangen. Es gewinnt. Haushoch.",
        "Ihr baut einen Turm aus Kissen. Es zerstört ihn sofort.",
        "Ihr spielt Verstecken. Es versteckt sich zu gut.",
        "Ihr spielt Ball. Es bringt den Ball nie zurück."
    ]
    return random.choice(actions)

def sleep():
    """Gibt eine zufällige humorvolle Reaktion zurück, wenn das Haustier schlafen soll.
    
    Returns:
        String mit einer zufälligen Schlaf-Reaktion
    """
    # Liste möglicher humorvoller Schlafszenarien
    sleeps = [
        "Es schläft ein… schnarcht… und murmelt etwas von Pizza.",
        "Es rollt sich ein und schläft sofort.",
        "Es versucht zu schlafen, aber ist plötzlich wieder wach.",
        "Es schläft ein, fällt vom Kissen, schläft weiter."
    ]
    return random.choice(sleeps)