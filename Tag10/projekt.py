# Import des Quiz-Moduls
import modul_quiz
import modul_planer

# Titel ausgeben
print('--- NOVA ASSISTENT ---')

# Steuervariable für Hauptschleife
weiter = True

# Menüoptionen
menue_optionen = ['quiz', 'neue Frage', 'planer', 'ende / quit / exit']

# Liste zum Speichern der Vorschläge
vorschlag_verlauf = []

# Hauptschleife
while weiter:
    # Ausgabe des Menüs
    print('\nMenü')
    for nummer, eintrag in enumerate(menue_optionen, start=1):
        print(f'{nummer} - {eintrag}')
    
    # Nutzer um Wahl der gewünschten Option bitten
    wahl = input('Deine Wahl: ').lower()

    if wahl in ['1', 'quiz']:
        print('Quiz startet...')
        # Aufruf Quiz einfügen
        modul_quiz.quiz_starten()
    
    if wahl in ['2', 'neue Frage']:
        print('Eine neue Frage wird zum Quiz hinzugefügt...')
        # neue Frage dem Quiz hinzufügen
        modul_quiz.quiz_erweitern()
    
    elif wahl in ['3', 'planer']:
        print('Planer startet...')
        # Planer einfügen
        vorschlag_verlauf.append(modul_planer.planer_starten())

    elif wahl in ['4', 'ende', 'quit', 'exit']:
        print('Tschüss')
        weiter = False
    
    elif wahl == '':
        print('Bitte triff eine Auswahl aus dem Menü.')

    else:
        print('Ungültige Eingabe')

if len(vorschlag_verlauf) > 0:
    print(f'Die gemachten Vorschläge des Planers waren: {vorschlag_verlauf}.')