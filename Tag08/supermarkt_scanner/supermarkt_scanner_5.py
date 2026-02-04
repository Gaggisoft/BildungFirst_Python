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
        
        # Validierung des Preises: Schleife bis ein gültiger Preis eingegeben wurde
        preis_korrekt = False
        while not preis_korrekt:
            try:
                # Versuch, den Preis als Dezimalzahl zu konvertieren
                preis = float(input('Preis eingeben: '))
                # Überprüfung: Preis muss positiv sein
                if preis > 0 and preis == round(preis, 2):
                    preis_korrekt = True        # Wenn erfolgreich, Schleife beenden
                else:
                    print('Ungültiger Preis. Bitte geben Sie nur positive Zahlen mit maximal zwei Nachkommastellen an.')
            except ValueError:
                # Fehlerbehandlung: wenn keine gültige Zahl eingegeben wurde
                print('Ungültiger Preis. Bitte geben Sie eine Zahl ein.')
        
        # Produkt und Preis zur Liste hinzufügen
        produktliste.append([produkt, preis])

# Ausgabe aller eingescannten Produkte mit Preisen
print('\nProdukte:', produktliste)
# Ausgabe der Gesamtanzahl der Produkte
print('Anzahl der Produkte:', len(produktliste))

# Initialisierung: Variablen für teuerstes Produkt und Gesamtpreis
teuerster_preis = -1
teuerstes_produkt = ''
gesamtpreis = 0

# Schleife durch alle Produkte zur Berechnung von Statistiken
for produkt_element in produktliste:
    # Gesamtpreis summieren (Preis ist an Index 1)
    gesamtpreis += produkt_element[1]
    
    # Überprüfung: wenn dieses Produkt teurer ist, als das bisherige teuerste
    if produkt_element[1] > teuerster_preis:
        teuerster_preis = produkt_element[1]
        teuerstes_produkt = produkt_element[0]

# Ausgabe des teuersten Produkts
print(f'teuerstes Produkt: {teuerstes_produkt} für {teuerster_preis} €')
# Berechnung und Ausgabe des Durchschnittspreises
print('Durchschnittspreis:', gesamtpreis / len(produktliste))
# Ausgabe des Gesamtpreises
print('Gesamtpreis:', gesamtpreis)