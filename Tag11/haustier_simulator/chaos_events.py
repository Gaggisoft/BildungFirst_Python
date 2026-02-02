# ---------------------------------------------------------
# Level 4 – Chaos-Ereignisse
# Dieses Modul verwaltet zufällige Events, die während des Spiels
# auftreten können und den Zustand des Haustiers beeinflussen.
# ---------------------------------------------------------

import random  # Für Zufallsentscheidungen und Event-Auswahl

def random_event(chance=0.3):
    """Generiert mit einer bestimmten Wahrscheinlichkeit ein zufälliges Chaos-Event.
    
    Args:
        chance: Wahrscheinlichkeit für ein Event (Standard: 0.3 = 30%)
    
    Returns:
        Tuple (name, text, effects) wenn ein Event eintritt, sonst None
        - name: Kurzer Name des Events
        - text: Beschreibungstext des Events
        - effects: Dictionary mit Zustandsänderungen (z.B. {"laune": +1})
    """
    # Prüfe mit Zufallszahl, ob ein Event eintritt
    if random.random() < chance:
        # Liste aller möglichen Chaos-Events mit ihren Effekten
        events = [
            ("WLAN", "Dein Haustier hat dein WLAN-Passwort geändert.", {"laune": +1}),
            ("Reime", "Es spricht jetzt nur noch in Reimen.", {"laune": +2}),
            ("Socken", "Es hat sich in einer Sockenschublade versteckt.", {"energie": -1}),
            ("Drama", "Es hält eine dramatische Rede über Existenz.", {"laune": +3}),
            ("Chaos", "Es hat beschlossen, dass Schwerkraft optional ist.", {"energie": +2})
        ]
        # Wähle ein zufälliges Event aus der Liste
        return random.choice(events)
    return None

def apply_event(state, event):
    """Wendet die Effekte eines Chaos-Events auf den Haustier-Zustand an.
    
    Args:
        state: Dictionary mit dem aktuellen Zustand des Haustiers
        event: Tuple (name, text, effects) oder None
    
    Returns:
        Dictionary mit dem aktualisierten Zustand
    """
    # Wenn kein Event vorliegt, gib den Zustand unverändert zurück
    if event is None:
        return state
    
    # Extrahiere die Effekte aus dem Event-Tuple
    _, _, effects = event
    
    # Wende alle Effekte auf den Zustand an
    for key, value in effects.items():
        # Stelle sicher, dass die Werte im gültigen Bereich (0-10) bleiben
        state[key] = max(0, min(10, state[key] + value))
    
    return state