# Liste zur Speicherung von Produkten mit ihren Preisen
produktliste = []

# Endlosschleife für die Eingabe von Produkten und Preisen
while True:
    # Benutzer wird aufgefordert, einen Produktnamen einzugeben
    produkt = input('Produkt eingeben: ')
    
    # Nur wenn ein Produkt eingegeben wurde (nicht leer)
    if len(produkt) != 0:
        # Spezialfall: defektes Produkt wird übersprungen
        if produkt == 'kaputt':
            print('Produkt defekt, wird nicht gescannt.')
            continue  # Nächste Iteration ohne Hinzufügen zur Liste
        
        # Spezialfall: STOP beendet die Eingabe
        if produkt == 'STOP':
            print('Eingabe beendet.')
            break  # Schleife verlassen
        
        # Benutzer wird aufgefordert, den Preis des Produkts einzugeben
        preis = float(input('Preis eingeben: '))
        
        # Produkt und Preis als Liste zur produktliste hinzufügen
        produktliste.append([produkt, preis])

# Ausgabe aller eingescannten Produkte mit Preisen
print('\nProdukte:', produktliste)
# Ausgabe der Gesamtanzahl der Produkte
print('Anzahl der Produkte:', len(produktliste))