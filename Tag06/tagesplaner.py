# Überschrift für den Tagesplaner
# ACHTUNG: Hier ist ein FEHLER im Code
# Das schließende Anführungszeichen ist ein typografisches Zeichen (‘)
# Python erwartet ein normales einfaches oder doppeltes Anführungszeichen
print('--- DEIN TAGESPLANER ---\n')

# Der Nutzer wird nach seinem Namen gefragt
name = input('Wie heißt du? ')

# Arbeitsort abfragen
arbeitsort = input('Wo arbeitest du (Homeoffice/Büro)? ').lower()

# Abfrage der wichtigsten Aufgabe
aufgabe = input('Wichtigste Aufgabe heute: ')

# Abfrage der Dauer in Stunden
# input() liefert immer einen String
# int() wandelt die Eingabe in eine Zahl um
dauer = int(input('Wie viele Stunden dauert sie? '))

# Abfrage der Priorität
# .lower() sorgt dafür, dass Groß- und Kleinschreibung keine Rolle spielt
prio = input('Priorität (sehr hoch/hoch/mittel/niedrig/spaßprojekt): ').lower()

# TODO: Emoji
# Ausgabe zum Arbeitsort
if arbeitsort == 'homeoffice':
    print('Ort: Homeoffice\nTipp: Wasser bereitstellen, Handy weg, Fokus an')
elif arbeitsort == 'büro':
    print('Ort: Büro\nTipp: Kopfhörer aufsetzen, kleine Pausen einplanen')
else:
    print('Ort: Unbekannt\nTipp: Hauptsache, du findest deinen Flow.')

# TODO: Emoji
# Persönliche Einleitung mit f-String
print(f'\n{name}, hier ist dein Plan für heute:\n')

# Ausgabe der Aufgabe inklusive Dauer
print(f'▶ Aufgabe: {aufgabe} ({dauer} Std.)')
# TODO: Emoji
# Entscheidung basierend auf der Priorität
if prio == 'sehr hoch':
    print('Priorität: Sofort starten, Fokusmodus an!')

elif prio == 'hoch':
    print('Priorität: Als Erstes erledigen, alle Störungen aus.')

elif prio == 'mittel':
    print('Priorität: Nachmittagsblock einplanen.')

elif prio == 'niedrig':
    print('Priorität: Locker angehen, du hast Luft.')

# else greift bei "spaßprojekt" und allen anderen Eingaben
else:
    print('Priorität: Kurze kreative Session und dann zurück.')

# Zweiter Entscheidungsblock
# Bewertung der Dauer der Aufgabe
if dauer > 3:
    print('Tipp: Plane eine kurze Pause pro Stunde ein.')

elif dauer > 1:
    print('Tipp: Halbzeit-Pause einbauen.')

else:
    print('Tipp: Danach etwas Schönes einplanen.')

# Abschließende Motivation
# TODO: Emoji
if prio == 'sehr hoch':
    print('Motivation: Eine Sache, voller Fokus. Du packst das!')

elif prio == 'hoch':
    print('Motivation: Schritt für Schritt.')

elif prio == 'mittel':
    print('Motivation: Nicht perfekt, dran bleiben!')

elif prio == 'niedrig':
    print('Motivation: Konsequent, kleine Schritte sind auch Schritte!')

# else greift bei "spaßprojekt" und allen anderen Eingaben
else:
    print('Motivation: Kreativität ist kein Luxus.')