from kd_funktion import add_item, remove_item, show_inventory

# TODO: Bei mehr Funktionen anpassen
def show_menu():
    print('--- Wähle bitte die gewünschte Funktion ---')
    print('1: Produkt hinzufügen')
    print('2: Produkt entfernen')
    print('3: Inventar anzeigen')
    print('ENTER zum Beenden')

    eingabe = input('Deine Auswahl: ')

    # Ende?
    if not eingabe:
        return None
    
    # Eingabe überprüfen
    if not eingabe.isdigit():
        print('Bitte eine Zahl eingeben')
        return None
    
    # Rückgabe der Eingabe
    return int(eingabe)

def eingabe_produkt_menge(eingabe):
    produkt = input('Produktname (oder ENTER zum Beenden): ').strip()

    # Ende bei leerer Eingabe
    if not produkt:
        produkt = None

    # Eingabe eines Produkts
    menge = input(f'Wie viele {produkt} sollen {eingabe} werden? ').strip()

    # Menge überprüfen
    if not menge.isdigit():
        print('Bitte eine Zahl eingeben.')
        menge = None

    return produkt, menge

# Nutzer die Eingabe von Produkten ermöglichen
def user_input(inventar):
    while True:
        # Bedienungsmenü anzeigen
        funktion = show_menu()

        # Eingabe verarbeiten
        # TODO: An bestehende Funktionen anpassen
        match funktion:
            # Produkt hinzufügen
            case 1:
                produkt, menge = eingabe_produkt_menge('hinzugefügt')
                # Ende bei leerer Eingabe
                if produkt == None:
                    break
                # Menge überprüfen
                if menge == None:
                    continue
                
                # Produkt wird hinzugefügt
                add_item(inventar, produkt, menge)

            # Produkt entfernen
            case 2:
                produkt, menge = eingabe_produkt_menge('entfernt')
                # Ende bei leerer Eingabe
                if produkt == None:
                    break
                # Menge überprüfen
                if menge == None:
                    continue

                # Produkt entfernen
                remove_item(inventar, produkt, menge)

            # Inventar anzeigen
            case 3:
                show_inventory(inventar)

            # Default
            case _:
                return
        