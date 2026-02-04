# Einlesen von zwei Zahlen mit dem Typ float (Kommazahl)
erste_zahl = float(input('Zahl 1: '))
zweite_zahl = float(input('Zahl 2: '))

# Summe
print(f'{erste_zahl} + {zweite_zahl} = {erste_zahl + zweite_zahl}')
# Differenz
print(f'{erste_zahl} - {zweite_zahl} = {erste_zahl - zweite_zahl}')
# Produkt
print(f'{erste_zahl} * {zweite_zahl} = {erste_zahl * zweite_zahl}')
# Quotien
print(f'{erste_zahl} / {zweite_zahl} = {erste_zahl / zweite_zahl}')

# Operationen machen mit Integer mehr Sinn als mit Gleitkommazahlen, funktionieren aber auch
print(f'{erste_zahl} // {zweite_zahl} = {int(erste_zahl // zweite_zahl)}')
print(f'{erste_zahl} % {zweite_zahl} = {erste_zahl % zweite_zahl}')