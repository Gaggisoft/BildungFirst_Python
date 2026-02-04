# Nutzer wird nach seinem Alter gefragt => Variablen alter
alter = int(input('Wie alt bist du?\n'))

# Test auf Volljährigkeit (mindestens 18 Jahre alt)
if alter < 18:      # alter <= 17
    print('Du bist noch mindestjährig.')
else:
    print('Du bist volljährig.')

# Alternative
if alter > 17:      # alter >= 18
    print('Du bist volljährig.')
else:
    print('Du bist noch mindestjährig.')

eingabe = int(input('\n\n\nGib 3 oder eine andere Zahl ein.'))
if eingabe != 3:
    print('Das war eine andere Zahl.')
else:
    print('Du hast die Zahl 3 eingegeben.')