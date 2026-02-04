# Liste zur Speicherung aller eingegebenen Produkte
produktliste = []

# Steuerungsvariable für die Schleife
ende = False

# Endlosschleife bis der Benutzer ein leeres Produkt eingibt
while not ende:
    # Benutzer wird aufgefordert, ein Produkt einzugeben
    produkt = input('Produkt eingeben: ')
    
    # Prüfung: wenn leeres Produkt eingegeben wurde, Schleife beenden
    if len(produkt) == 0:
            ende = True
    # Ansonsten: Produkt zur Liste hinzufügen
    else:
        produktliste.append([produkt])

# Ausgabe der gesammelten Produkte
print('\nProdukte:', produktliste)
# Ausgabe der Anzahl der eingegebenen Produkte
print('Anzahl der Produkte:', len(produktliste))