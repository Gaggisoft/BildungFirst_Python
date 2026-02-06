# Funktionalität

# TODO: menge ist aktuell Wert, später andere Umsetzung je nach Umfang
def add_item(inventory, product_name, quantity=1):
    # Produktname als Schlüssel
    key = product_name.strip().lower()

    # Schlüssel leer?
    if not key:
        return
    
    # Schlüssel bereits enthalten => Menge erhöhen
    # Schlüssel noch nicht enthalten => Produkt anlegen und Menge eintragen
    inventory[key] = inventory.get(key, 0) + int(quantity)

# TODO: menge ist aktuell Wert, später andere Umsetzung je nach Umfang
def remove_item(inventory, product_name, quantity=1):
    # Produktname als Schlüssel
    key = product_name.strip().lower()

    # Schlüssel leer?
    if not key:
        return
    
    # Schlüssel bereits enthalten => Menge reduzieren
    # Schlüssel noch nicht enthalten => Produkt anlegen und Menge=0
    inventory[key] = inventory.get(key, 0) - int(quantity)
    # Menge darf nicht negativ werden
    inventory[key] = max(0, inventory[key])
    
    # TODO: Produkt entfernen bei Menge=0 später eventuell nicht mehr sinnvoll
    # bei Menge 0 kann das Produkt entfernt werden
    if inventory[key] == 0:
        inventory.pop(key, None)

# TODO: Bei Anpassung des Aufbau des Inventars anpassen
def show_inventory(inventory):
    if not inventory:
        print('Dein Kühlschrank ist leer.')
        return
    
    print('Kühlschrank-Inventar:')
    for product in sorted(inventory):
        print(f'- {product.title()}: {inventory[product]}')
