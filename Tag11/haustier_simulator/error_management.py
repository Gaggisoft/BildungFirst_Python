# ---------------------------------------------------------
# Level 5 – Fehlerbehandlung
# Dieses Modul kümmert sich um sichere Benutzereingaben,
# Validierung von Aktionen und die Durchführung einer Spielrunde.
# ---------------------------------------------------------

import actions              # Enthält die Aktions-Reaktionen (feed, play, sleep)
import state_management     # Verwaltung des Haustier-Zustands
import chaos_events         # Zufällige Chaos-Ereignisse

def safe_input(prompt):
    """Sichere Eingabefunktion mit Fehlerbehandlung.
    
    Args:
        prompt: Der Text, der dem Benutzer angezeigt wird
    
    Returns:
        String mit der Benutzereingabe (bereinigt und in Kleinbuchstaben)
        oder leerer String bei einem Fehler
    """
    try:
        # Entferne Leerzeichen und wandle in Kleinbuchstaben um
        return input(prompt).strip().lower()
    except Exception:
        print("Eingabefehler. Versuch es nochmal.")
        return ""

def validate_action(action):
    """Überprüft, ob die gewählte Aktion gültig ist.
    
    Args:
        action: String mit der Benutzeraktion
    
    Returns:
        True wenn die Aktion gültig ist, sonst False
    """
    return action in ["füttern", "spielen", "schlafen"]

def run_turn(state):
    """Führt eine komplette Spielrunde durch.
    
    Diese Funktion koordiniert den gesamten Ablauf einer Runde:
    1. Benutzereingabe erfassen und validieren
    2. Gewählte Aktion ausführen
    3. Zustand aktualisieren
    4. Zufälliges Chaos-Event auslösen (mit 30% Wahrscheinlichkeit)
    
    Args:
        state: Dictionary mit dem aktuellen Zustand des Haustiers
    
    Returns:
        Dictionary mit dem aktualisierten Zustand
    """
    # Hole sichere Benutzereingabe
    action = safe_input("Was möchtest du tun? (füttern/spielen/schlafen): ")

    # Prüfe, ob die Aktion gültig ist
    if not validate_action(action):
        print("Ungültige Aktion. Dein Haustier schaut dich verwirrt an.")
        return state

    # Führe die entsprechende Aktion aus und zeige die Reaktion
    if action == "füttern":
        print(actions.feed())
    elif action == "spielen":
        print(actions.play())
    elif action == "schlafen":
        print(actions.sleep())
    
    # Aktualisiere den Zustand basierend auf der Aktion
    state = state_management.update_state(state, action)

    # Prüfe, ob ein zufälliges Chaos-Event eintritt (30% Chance)
    event = chaos_events.random_event()
    if event:
        name, text, _ = event
        print(f"\n*** CHAOS-EVENT: {name}! ***")
        print(text)
        # Wende die Effekte des Events auf den Zustand an
        state = chaos_events.apply_event(state, event)

    return state