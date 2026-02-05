# Tupels für feste Daten
position_lyra = (10, 20)
farbe_lyra = (120, 200, 255)

position_ava = (5, 15)
farbe_ava = (255, 180, 100)

# Dictionary mit Figuren
figuren = {
    'Lyra': {
        'rolle': 'Mentorin',
        'alter': 35
    },
    'Ava': {
        'rolle': 'Mentorin',
        'alter': 28
    },
    'Orion': {
        'rolle': 'Mentor',
        'alter': 42
    }
}

# Neue Eigenschaft hinzufügen
figuren['Lyra']['lieblingswerkzeug'] = 'Debug-Brille'
figuren['Orion']['lieblingswerkzeug'] = 'Sternenkompass'


# Ausgabe
print('Figurenübersicht:')
print(figuren)

print()
print('Lyra sitzt bei:', position_lyra, 'in Farbe:', farbe_lyra)
print('Ava sitzt bei:', position_ava, 'in Farbe:', farbe_ava)