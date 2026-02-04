# Frage den Nutzer nach dem Alter
alter = input('Gib bitte dein Alter ein: ')

# Wandle die Eingabe in eine Zahl um
alter = int(alter)

# Berechne das Alter in 5 Jahren
alter_in_5_jahren = alter + 5

# Gib den Satz aus: 'In 5 Jahren bist du ... Jahre alt.'
print('In 5 Jahren bist du ' + str(alter_in_5_jahren) + ' Jahre alt.')