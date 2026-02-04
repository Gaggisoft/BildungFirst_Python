# Nutzer soll die aktuelle Farbe einer Ampel eingeben => Variable ampel
ampel = input('Welche Farbe zeigt die Ampel aktuell (rot / rot-gelb / gelb / grün)?\n').lower()

# Ampel zeigt rot an => man muss stehen bleiben
if ampel == 'rot':
    print('STOP!')
# Ampel zeigt gelb-rot an => gleich wird die Ampel rot
elif ampel == 'gelb-rot':
    print('Mach dich bereit zum Weiterfahren.')
# Ampel zeigt gelb an => gleich muss man stehen bleiben
elif ampel == 'gelb':
    print('Achtung, die Ampel springt gleich auf rot!')
# Ampel zeigt grün an => man darf fahren
elif ampel == 'grün':
    print('Du kannst weiterfahren.')
# eine unbekannte Farbe wurde eingegeben
else:
    print('Unbekannte Farbe')