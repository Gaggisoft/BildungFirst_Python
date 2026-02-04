#Endlosschleife (Bedingung weiter ist bei Überprüfung immer True)
#weiter = True
#zaehler = 0
#while weiter:
#    zaehler += 1
#    if zaehler >= 10:
#        weiter = False
#    print(f'Die Schleife läuft noch, Schleifendurchlauf #{zaehler}')
#    weiter = True

# break
while True:
    eingabe = input('Gib etwas ein: ')
    if len(eingabe) == 0:
        break
    print(eingabe)
print('Ende der Schleifenausführung (break)\n\n')

# continue
zaehler = 0
while zaehler < 5:
    zaehler += 1
    if zaehler == 2:
        continue
    print(zaehler)
print('Ende der Schleifendurchführung (continue)')