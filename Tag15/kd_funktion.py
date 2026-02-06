# Funktionalität

# TODO: menge ist aktuell Wert, später andere Umsetzung je nach Umfang
def add_item(inventar, produktname, menge=1):
    # Produktname als Schlüssel
    schluessel = produktname.strip().lower()

    # Schlüssel leer?
    if not schluessel:
        return
    
    # Schlüssel bereits enthalten => Menge erhöhen
    # Schlüssel noch nicht enthalten => Produkt anlegen und Menge eintragen
    inventar[schluessel] = inventar.get(schluessel, 0) + int(menge)

# TODO: menge ist aktuell Wert, später andere Umsetzung je nach Umfang
def remove_item(inventar, produktname, menge=1):
    # Produktname als Schlüssel
    schluessel = produktname.strip().lower()

    # Schlüssel leer?
    if not schluessel:
        return
    
    # Schlüssel bereits enthalten => Menge reduzieren
    # Schlüssel noch nicht enthalten => Produkt anlegen und Menge=0
    inventar[schluessel] = inventar.get(schluessel, 0) - int(menge)
    # Menge darf nicht negativ werden
    inventar[schluessel] = max(0, inventar[schluessel])
    
    # TODO: Produkt entfernen bei Menge=0 später eventuell nicht mehr sinnvoll
    # bei Menge 0 kann das Produkt entfernt werden
    if inventar[schluessel] == 0:
        inventar.pop(schluessel, None)

# TODO: Bei Anpassung des Aufbau des Inventars anpassen
def show_inventory(inventar):
    if not inventar:
        print('Dein Kühlschrank ist leer.')
        return
    
    print('Kühlschrank-Inventar:')
    for produkt in sorted(inventar):
        print(f'- {produkt.title()}: {inventar[produkt]}')
