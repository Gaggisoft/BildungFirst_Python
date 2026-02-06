from kd_funktion import add_item, remove_item, show_inventory
from kd_json import save_inventory, load_inventory

# TODO: Bei mehr Funktionen anpassen
def show_menu():
    print('\n--- Wähle bitte die gewünschte Funktion ---')
    print('1: Produkt hinzufügen')
    print('2: Produkt entfernen')
    print('3: Inventar anzeigen')
    print('4: Speichern des Inventars')
    print('5: Laden des Inventars')
    print('ENTER zum Beenden')

    selection = input('Deine Auswahl: ')

    # Ende?
    if not selection:
        return None
    
    # Eingabe überprüfen
    if not selection.isdigit():
        print('Bitte eine Zahl eingeben')
        return None
    
    # Rückgabe der Eingabe
    return int(selection)

def input_product_quantity(action):
    product = input('Produktname (oder ENTER zum Beenden): ').strip()

    # Ende bei leerer Eingabe
    if not product:
        product = None
        return product, None

    # Eingabe eines Produkts
    quantity = input(f'Wie viele {product} sollen {action} werden? ').strip()

    # Menge überprüfen
    if not quantity.isdigit():
        print('Bitte eine Zahl eingeben.')
        quantity = None

    return product, quantity

# Nutzer die Eingabe von Produkten ermöglichen
def user_input(inventory):
    while True:
        # Bedienungsmenü anzeigen
        function = show_menu()

        # Eingabe verarbeiten
        # TODO: An bestehende Funktionen anpassen
        match function:
            # Produkt hinzufügen
            case 1:
                product, quantity = input_product_quantity('hinzugefügt')
                # Ende bei leerer Eingabe oder keiner Menge
                if product == None:
                    break

                if quantity == None:
                    continue
                
                # Produkt wird hinzugefügt
                add_item(inventory, product, quantity)

            # Produkt entfernen
            case 2:
                product, quantity = input_product_quantity('entfernt')
                # Ende bei leerer Eingabe
                # Ende bei leerer Eingabe oder keiner Menge
                if product == None:
                    break

                if quantity == None:
                    continue

                # Produkt entfernen
                remove_item(inventory, product, quantity)

            # Inventar anzeigen
            case 3:
                show_inventory(inventory)
            
            # Speichern des Inventars als JSON
            case 4:
                save_inventory(inventory)

            # Laden des Inventars aus JSON
            case 5:
                # load_inventory gibt ein neues dict zurück
                loaded_inventory = load_inventory()
                # Inventar leeren
                inventory.clear()
                # Inhalt des neuen dict in Inventar laden
                inventory.update(loaded_inventory)
                # neues dict löschen
                del loaded_inventory

            # Default
            case _:
                return
        