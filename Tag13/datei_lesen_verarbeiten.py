from pathlib import Path

# Funktion zum Einlesen mehrerer Textdateien
def lese_textdateien(ordnername):
    # Basispfad
    if '__file__' in globals():
        basis = Path(__file__).parent
    else:
        basis = Path.cwd()

    # Ordner zum Basispfad hinzufügen
    ordner = basis / ordnername

    # Falls Ordner nicht existiert => Ordner anlegen
    ordner.mkdir(parents=True, exist_ok=True)

    # alle .txt-Dateien sammeln
    # ordner.glob('*.txt) gibt alle .txt-Dateien im Ordner mit dem Pfad ordner als Path-Objekt zurück
    # sorted sortiert die Pfade alphabetisch
    dateien = sorted(ordner.glob('*.txt'))

    # Dateien lesen und Inhalt in Ergebnisliste speichern
    ergebnisse = []
    for aktuelle_datei in dateien:
        try:
            text = aktuelle_datei.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            text = ''
        ergebnisse.append((aktuelle_datei, text))
    
    # Rückgabe des Ordnerpfads und der Ergebnisliste
    return ordner, ergebnisse

# Zählen von Zeilen und Wörtern
def analysiere_text(text):
    # leerer Text
    if not text:
        return 0, 0
    
    # Aufteilen des Texts in Liste von Strings (ein String pro Zeile)
    zeilen = text.splitlines()
    # Aufteilen der Liste von Zeilen in Liste von Wörtern (ein String pro Wort)
    woerter = ' '.join(zeilen).split()

    # Rückgabe von Anzahl Zeilen und Anzahl Wörtern
    return len(zeilen), len(woerter)

def schreibe_report(inhalt, zielpfad):
    ausgabe = []
    gesamtanzahl_zeilen = 0
    gesamtanzahl_woerter = 0

    # Ausgabe aufbauen (Liste mit Strings, ein String pro Zeile)
    for pfad, anzahl_zeilen, anzahl_woerter in inhalt:
        # Aufbau der jeweiligen Zeile der späteren Ausgabe
        ausgabe.append(f'{pfad.name} -> {anzahl_zeilen} Zeilen, {anzahl_woerter} Wörter')
        # Aktualisierung der Gesamtanzahlen
        gesamtanzahl_zeilen += anzahl_zeilen
        gesamtanzahl_woerter += anzahl_woerter

    # Gesamtanzahl an Ausgabe anhängen
    ausgabe.append('---')
    ausgabe.append(f'Gesamt -> {gesamtanzahl_zeilen} Zeilen, {gesamtanzahl_woerter} Wörter')

    # Schreiben der Zieldatei
    zielpfad.write_text('\n'.join(ausgabe), encoding='utf-8')
    # Rückgabe des Zielpfads
    return zielpfad

def datareader_main(ordnername='daten'):
    # Dateien laden
    ordner, dateien = lese_textdateien(ordnername)

    # Ausgabe des Pfads des Datenordners
    print('Datenordner:', ordner.resolve())

    # keine Dateien gefunden
    if not dateien:
        print('Keine .txt-Dateien gefunden in', ordnername)
        print('Lege .txt-Dateien hier ab:', ordner.resolve())
        return
    
    # Analysieren des Texts
    zusammenfassung = []
    # aktuelle_datei => pfad, text => text 
    for pfad, text in dateien:
        # Anzahl der Zeilen und Anzahl der Wörter für die aktuelle Datei bestimmen
        anzahl_zeilen, anzahl_woerter = analysiere_text(text)
        # Zusammenfassung aktualisieren
        zusammenfassung.append((pfad, anzahl_zeilen, anzahl_woerter))
    
    # Report schreiben
    report_pfad = ordner / 'report.txt'
    report = schreibe_report(zusammenfassung, zielpfad=report_pfad)

    print('Report erstellt:', report.resolve())
    # Optional: Report-Inhalt direkt anzeigen
    #print('\n--- Inhalt der report.txt ---')
    #print(report.read_text(encoding='utf-8'))

if __name__ == '__main__':
    datareader_main('daten')