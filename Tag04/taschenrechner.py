# Eingabe der ersten Zahl
erste_zahl = int(input('Gib bitte die erste ganze Zahl ein:\t'))
# Eingabe der zweiten Zahl
zweite_zahl = int(input('Gib bitte die zweite ganze Zahl ein:\t'))

# Menü für Rechenart
print('\nWelche Rechenart möchtest du verwenden?')
print('1 - Addition')
print('2 - Subtraktion')
print('3 - Multiplikation')
print('4 - Division')
print('5 - Ganzzahlige Division')
print('6 - Modulo (Rest der Division)')
print('7 - Alle Rechenarten')

auswahl = input('Gib die Nummer ein (1-7): ')

# Berechnung basierend auf Auswahl
if auswahl == '1':
    print('Summe: ' + str(erste_zahl + zweite_zahl))
elif auswahl == '2':
    print('Differenz: ' + str(erste_zahl - zweite_zahl))
elif auswahl == '3':
    print('Produkt: ' + str(erste_zahl * zweite_zahl))
elif auswahl == '4':
    if zweite_zahl != 0:
        print('Quotient: ' + str(erste_zahl / zweite_zahl))
    else:
        print('Fehler: Division durch Null ist nicht erlaubt!')
elif auswahl == '5':
    if zweite_zahl != 0:
        print('ganzzahliger Quotient: ' + str(erste_zahl // zweite_zahl))
    else:
        print('Fehler: Division durch Null ist nicht erlaubt!')
elif auswahl == '6':
    if zweite_zahl != 0:
        print('Rest der Division: ' + str(erste_zahl % zweite_zahl))
    else:
        print('Fehler: Division durch Null ist nicht erlaubt!')
elif auswahl == '7':
    print('Summe: ' + str(erste_zahl + zweite_zahl))
    print('Differenz: ' + str(erste_zahl - zweite_zahl))
    print('Produkt: ' + str(erste_zahl * zweite_zahl))
    if zweite_zahl != 0:
        print('Quotient: ' + str(erste_zahl / zweite_zahl))
        print('ganzzahliger Quotient: ' + str(erste_zahl // zweite_zahl))
        print('Rest der Division: ' + str(erste_zahl % zweite_zahl))
    else:
        print('Fehler: Division durch Null ist nicht erlaubt!')
else:
    print('Ungültige Eingabe!')