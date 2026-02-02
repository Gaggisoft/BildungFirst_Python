# Einbinden des Moduls random
#import random

# Funktion Quiz starten
def quiz_starten():
    # Liste mit Fragen
    # TODO: weitere Fragen hinzufügen
    fragen_liste = [
        'Wie ist die Hauptstradt von Frankreich?',
        'Wie lautet das Ergebnis von 3 + 4?',
        'Bei welcher Farbe einer Ampel darf man fahren?'
    ]

    # Liste mit Antworten
    # TODO: weitere Antworten hinzufügen
    antworten_liste = [
        ['paris'],
        ['7'],
        ['grün', 'gruen']
    ]

    # Punktestand
    punktestand = 0

    # verbinden von Fragen und Antworten
    for frage, antwort in zip(fragen_liste, antworten_liste):
        # Frage stellen und Antwort annehmen
        # TODO: Fragen zufällig wählen
        eingabe = input(frage + '\n').lower()

        # Antworten prüfen
        if eingabe in antwort:
            # Antwort war korrekt
            print('Richtig')
            # Punkte bei korrekter Antwort aktualisieren
            punktestand += 1
        else:
            # Antwort war nicht korrekt
            print('Falsch')

    # Ende: Punkte anzeigen
    # TODO: Anpassung bei zufälliger Fragenauswahl nötig
    print(f'Punktestand: {punktestand} / {len(fragen_liste)}')

    # Ausgabe abhängig von der Leistung
    if punktestand == len(fragen_liste):
        print('Top Leistung!')
    elif punktestand >= len(fragen_liste) // 2:
        print('Gut gemacht. Noch ein Versuch?')
    else:
        print('Nicht schlimm. Übung macht den Meister.')
    
    # Rückkehr
    return