# Nutzer nach seinem Budget fragen => Variable budget
budget = int(input('Wie viel Geld hast du heute Abend?\n'))

# Nutzer fragen, ob Begleitung mitkommt => Variable freunde
freunde = input('Kommen Freunde mit (ja / nein)?\n').lower()
# Umwandeln in Boolean (True wenn freunde == 'ja')
freunde = (freunde == 'ja')

# ausreichendes Budget (mindestens 50)
if budget >= 50:
    print('Restaurant oder Kino möglich.')

# nicht ausreichendes Budget (maximal 49)
# if budget < 50
if not (budget >= 50):
    print('Lieber zu Hause bleiben.')

# Erweiterung
if budget >= 50 and freunde:
    print('Perfekt für einen gemeinsamen Abend!')
elif budget < 50 and freunde:
    print('Gemeinsam zu Hause ist es auch gemütlich.')