# Nutzer nach seinem Budget fragen => Variable budget
budget = int(input('Wie viel Geld hast du heute Abend?\n'))

# ausreichendes Budget (mindestens 30)
if (budget >= 30):
    print('Restaurant oder Kino möglich.')

# nicht ausreichendes Budget (maximal 29)
# if budget < 30
if not (budget >= 30):
    print('Lieber zu Hause bleiben.')