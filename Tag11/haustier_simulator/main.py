import random

# Import der anderen Module im Projekt
import state_management     # Verwaltung des Haustier-Zustands (Hunger, Energie, Laune)
import error_management     # Eingabevalidierung und Rundenverwaltung

# ---------------------------------------------------------
# Level 1 – Grundfunktionen
# ---------------------------------------------------------

def greet_pet(name):
    """Begrüßt das Haustier mit seinem Namen."""
    return f"Hallo {name}! Dein Chaos-Haustier ist bereit für Unfug."

def pet_status():
    """Gibt einen zufälligen Anfangs-Status für das Haustier zurück."""
    status = [
        "hungrig", "schläfrig", "hyperaktiv", "philosophisch",
        "leicht verwirrt", "dramatisch", "übermotiviert"
    ]
    return random.choice(status)

# ---------------------------------------------------------
# Level 6 – Komplettes Spiel
# ---------------------------------------------------------

def check_end(state, round_number):
    """Prüft die Endbedingungen des Spiels.
    
    Args:
        state: Dictionary mit den Zustandswerten des Haustiers
        round_number: Aktuelle Rundennummer
    
    Returns:
        String mit dem Spielende-Grund oder None, wenn das Spiel weitergeht
    """
    # Prüfe, ob das Haustier verhungert ist
    if state["hunger"] >= 10:
        return "verhungert"
    # Prüfe, ob das Haustier erschöpft ist
    if state["energie"] <= 0:
        return "erschöpft"
    # Prüfe, ob das Haustier zu traurig ist
    if state["laune"] <= 0:
        return "depressiv"
    # Prüfe, ob alle Runden erfolgreich überstanden wurden
    if round_number >= 10:
        return "gewonnen"
    return None

def end_game(result):
    """Zeigt die Endnachricht basierend auf dem Spielergebnis an.
    
    Args:
        result: String mit dem Spielende-Grund (gewonnen, verhungert, erschöpft, depressiv)
    """
    print("\n=== SPIEL ENDE ===")
    # Zeige je nach Spielergebnis eine passende Nachricht
    if result == "gewonnen":
        print("Du hast 10 Runden Chaos überlebt. Dein Haustier ist glücklich und hat nichts angezündet. Bravo.")
    elif result == "verhungert":
        print("Dein Haustier ist verhungert. Es war zu sehr damit beschäftigt, deine Socken zu sortieren.")
    elif result == "erschöpft":
        print("Dein Haustier ist völlig erschöpft. Vielleicht war das Kissenburg-Bauen zu viel.")
    elif result == "depressiv":
        print("Dein Haustier ist traurig. Vielleicht hättest du mehr spielen sollen.")
    print("===================\n")

def start_game():
    """Hauptfunktion zum Starten und Durchführen des Haustier-Simulators.
    
    Diese Funktion initialisiert das Spiel, fragt nach dem Namen des Haustiers
    und führt die Spielrunden durch, bis ein Endbedingung erreicht wird.
    """
    # Begrüße den Spieler und frage nach dem Namen
    print("🐾 Willkommen zum Chaos-Haustier-Simulator! 🐾")
    name = input("Wie heißt dein Haustier? ")
    print(greet_pet(name))
    print(f"Es ist aktuell {pet_status()}.\n")

    # Initialisiere den Haustier-Zustand
    state = state_management.get_pet_state()

    # Spiele alle Runden (maximal 10)
    for round_number in range(1, 11):
        print(f"--- Runde {round_number} ---")
        state_management.show_state(state)
        # Führe eine Spielrunde aus (Eingabe, Aktion, Chaos-Event)
        state = error_management.run_turn(state)

        # Prüfe, ob eine Endbedingung erreicht wurde
        result = check_end(state, round_number)
        if result:
            end_game(result)
            return

    # Wenn alle Runden überstanden wurden, hat der Spieler gewonnen
    end_game("gewonnen")

# ---------------------------------------------------------
# Spiel starten
# ---------------------------------------------------------
start_game()