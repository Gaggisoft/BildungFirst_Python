# Nutzer nach seinem Alter fragen => Variable alter
alter = int(input('Alter: '))

# Nutzer nach Budget fragen => Variable budget
budget = int(input('Budget: '))

# Erwachsene + genug Budget
if alter >= 18 and budget >= 50:
    print('Du darfst rein und hast genug Budget.')
# Erwachsene + wenig Budget
elif alter >= 18 and budget < 50:       # alter >= 18 reicht
    print('Du bist alt genug, aber Geld wird knapp.')
# Minderjährig
else:
    print('Kein Zutritt')

# Erwachsene + genug Budget
if alter >= 18:
    if budget >= 50:
        print('Du darfst rein und hast genug Budget.')
    # Erwachsene + wenig Budget
    else:
        print('Du bist alt genug, aber Geld wird knapp.')
# Minderjährig
else:
    print('Kein Zutritt')