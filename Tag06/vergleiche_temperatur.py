# Nutzer wird nach Temperatur gefragt => Variable temperatur
eingabe = input('Gib bitte eine Temperatur in Grad Celsius ein: ')

if eingabe.isdigit():
    print('Das sieht nach einer gültigen Zahl aus.')
    # Eingabe in Zahl umwandeln
    temperatur = int(eingabe)
    # Temperatur verarbeiten
    # Gefrierpunkt 0
    if temperatur == 0:
        print('Es ist genau 0 Grad - Gefrierpunkt')
    # < 10 => kalt
    if temperatur < 10:
        print('Es ist unter 10 Grad - sehr kalt')
    # < 20 => frisch
    elif temperatur < 20:
        print('Es ist unter 20 Grad - frisch')
    # > 30 => heiß
    elif temperatur > 30:
        print('Es ist über 30 Grad - sehr heiß')
    # 20-30 => angenehm
    else:
        print('Es ist zwischen 20 und 30 Grad - sehr angenehm')
# negative Zahl
elif '-' in eingabe:
    print('Vielleicht wolltest du eine negative Zahl eingeben? Das Programm unterstützt nur positive Temperaturen.')
# Kommazahl
elif ',' in eingabe:
    print('Das sieht nach einer Kommazahl aus. Das Programm unterstützt nur ganzzahlige Temperaturen.')
elif '.' in eingabe:
    print('Das sieht nach einer Kommazahl aus. Das Programm unterstützt nur ganzzahlige Temperaturen.')
# Schlüsselwort exit
elif eingabe.lower() == 'exit':
    print('Das Programm wird beendet.')
# ungültige Eingabe
else:
    print('Die Eingabe ist ungültig.')