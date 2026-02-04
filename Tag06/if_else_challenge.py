temperatur = input('Wie ist die Temperatur (warm/kalt)?\n')
temperatur = temperatur.lower()

if temperatur == 'warm':
    print('Es ist also warm.')
    print('Zieh T-Shirt und Sonnenbrille an!')
if temperatur == 'kalt':
    print('Es ist also kalt.')
    print('Zieh einen Pulli an!')

print('Ende des Programms')