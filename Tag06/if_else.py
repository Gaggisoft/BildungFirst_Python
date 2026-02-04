# Nutzer nach dem aktuellen Wetter fragen => Variable wetter
wetter = input('Wie ist das Wetter heute? (Sonne, Regen, Wolken)\n')

if wetter == 'Regen':
    print('Nimm bitte einen Schirm mit!')
else:
    print('Es ist kein Schirm nötig.')


# Erweiterung, die Groß- und Kleinschreibung ignoriert
if wetter.lower() == 'regen':
    print('Nimm bitte einen Schirm mit!')
else:
    print('Es ist kein Schirm nötig.')

# Alternative
if wetter.upper() == 'REGEN':
    print('Nimm bitte einen Schirm mit!')
else:
    print('Es ist kein Schirm nötig.')