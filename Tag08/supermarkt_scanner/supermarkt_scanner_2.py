# Liste zur Speicherung aller eingescannten Produkte
produktliste = []

# Endlosschleife für die Eingabe von Produkten
while True:
    # Benutzer wird aufgefordert, ein Produkt einzugeben
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
        
        # Normales Produkt zur Liste hinzufügen
        produktliste.append([produkt])

# Ausgabe der eingescannten Produkte
print('\nProdukte:', produktliste)
# Ausgabe der Gesamtanzahl
print('Anzahl der Produkte:', len(produktliste))