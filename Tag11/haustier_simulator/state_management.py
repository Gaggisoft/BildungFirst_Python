# ---------------------------------------------------------
# Level 3 – Zustandsverwaltung
# ---------------------------------------------------------

def get_pet_state():
    """Erstellt den initialen Zustand des Haustiers.
    
    Returns:
        Dictionary mit den Startwerten für Hunger, Energie und Laune.
        Alle Werte beginnen bei 5 (mittlerer Zustand).
    """
    return {
        "hunger": 5,   # 0 = satt, 10 = verhungert
        "energie": 5,  # 0 = erschöpft, 10 = hyperaktiv
        "laune": 5     # 0 = schlecht, 10 = super
    }

def update_state(state, action):
    """Aktualisiert den Zustand des Haustiers basierend auf der gewählten Aktion.
    
    Args:
        state: Dictionary mit den aktuellen Zustandswerten
        action: String mit der gewählten Aktion ("füttern", "spielen", "schlafen")
    
    Returns:
        Dictionary mit den aktualisierten Zustandswerten
    """
    if action == "füttern":
        # Füttern reduziert Hunger stark und erhöht Energie leicht
        state["hunger"] = max(0, state["hunger"] - 3)
        state["energie"] = min(10, state["energie"] + 1)
    elif action == "spielen":
        # Spielen kostet Energie, erhöht Laune und macht hungrig
        state["energie"] = max(0, state["energie"] - 2)
        state["laune"] = min(10, state["laune"] + 2)
        state["hunger"] = min(10, state["hunger"] + 1)
    elif action == "schlafen":
        # Schlafen regeneriert Energie stark und macht leicht hungrig
        state["energie"] = min(10, state["energie"] + 3)
        state["hunger"] = min(10, state["hunger"] + 1)
    return state

def show_state(state):
    """Zeigt den aktuellen Zustand des Haustiers in der Konsole an.
    
    Args:
        state: Dictionary mit den aktuellen Zustandswerten
    """
    print("\n--- Zustand des Haustiers ---")
    print(f"Hunger : {state['hunger']}/10")
    print(f"Energie: {state['energie']}/10")
    print(f"Laune  : {state['laune']}/10")
    print("-----------------------------\n")