# Programmtitel
print('Supermarkt-Scanner')

# Liste zur Speicherung von Produkten mit ihren Preisen
produktliste = []

# Hauptschleife für das Menüsystem
while True:
    # Menü anzeigen
    print('''\nWähle bitte den gewünschten Menüpunkt:
1 - Produkt eingeben
2 - Liste anzeigen
3 - teuerstes Produkt anzeigen
4 - Programm beenden''')
    
    # Benutzer wählt einen Menüpunkt
    auswahl = input('Deine Wahl: ')

    # Menüpunkt 1: Produkt eingeben
    if auswahl == '1':
        print('\n#############################################')
        print('# Produkt eingeben                          #')
        print('#############################################')
        
        # Produktname eingeben
        produkt = input('Produkt eingeben: ')
        
        # Nur wenn Produktname nicht leer ist
        if len(produkt) != 0:
            # Spezialfall: defektes Produkt
            if produkt == 'kaputt':
                print('Produkt defekt, wird nicht gescannt.')
                continue
            
            # Spezialfall: Programm beenden
            if produkt == 'STOP':
                print('Eingabe beendet.')
                break
            
            # Preiseingabe mit Validierung
            preis_korrekt = False
            while not preis_korrekt:
                try:
                    # Preis als Dezimalzahl eingeben
                    preis = float(input('Preis eingeben: '))
                    
                    # Überprüfung: Preis muss positiv sein
                    if preis > 0 and preis == round(preis, 2):
                        preis_korrekt = True        # Wenn erfolgreich, Schleife beenden
                    else:
                        print('Ungültiger Preis. Bitte geben Sie nur positive Zahlen mit maximal zwei Nachkommastellen an.')
                except ValueError:
                    # Fehlerbehandlung: keine gültige Zahl eingegeben
                    print('Ungültiger Preis. Bitte geben Sie eine Zahl ein.')
            
            # Produkt und Preis zur Liste hinzufügen
            produktliste.append([produkt, preis])

    # Menüpunkt 2: Liste anzeigen
    elif auswahl == '2':
        print('\n#############################################')
        print('# Liste anzeigen                               #')
        print('#############################################')
        
        # Ausgabe aller Produkte
        print('\nProdukte:', produktliste)
        # Anzahl der eingegebenen Produkte
        print('Anzahl der Produkte:', len(produktliste))

    # Menüpunkt 3: Statistiken anzeigen
    elif auswahl == '3':
        print('\n#############################################')
        print('# teuerstes Produkt anzeigen                   #')
        print('#############################################')
        
        # Initialisierung: Variablen für Berechnungen
        teuerster_preis = -1
        teuerstes_produkt = ''
        gesamtpreis = 0
        
        # Schleife durch alle Produkte zur Berechnung von Statistiken
        for produkt_element in produktliste:
            # Gesamtpreis summieren
            gesamtpreis += produkt_element[1]
            
            # Überprüfung: wenn teurer als bisheriges Maximum
            if produkt_element[1] > teuerster_preis:
                teuerster_preis = produkt_element[1]
                teuerstes_produkt = produkt_element[0]
        
        # Ausgabe des teuersten Produkts
        print(f'teuerstes Produkt: {teuerstes_produkt} für {teuerster_preis:.2f} €')
        
        # Berechnung und Ausgabe des Durchschnittspreises (mit Prüfung ob Liste nicht leer)
        if len(produktliste) > 0:
            print(f'Durchschnittspreis: {(gesamtpreis / len(produktliste)):.2f} €')
        else:
            print('Keine Produkte in der Liste.')
        
        # Ausgabe des Gesamtpreises
        print(f'Gesamtpreis: {gesamtpreis:.2f} €')
    
    # Menüpunkt 4: Programm beenden
    elif auswahl == '4':
        print('\n#############################################')
        print('# Programm beenden                             #')
        print('#############################################')
        print('Programm wird beendet.')
        break

    # Ungültige Eingabe
    else:
        print('\n#############################################')
        print('# Ungültige Auswahl. Bitte versuche es erneut. #')
        print('#############################################')