# for-Schleife

# Startwert: 0, Endwert: 10, Schrittweite: +3
# Schleifenvariable: schleifenvariable
for schleifenvariable in range(0, 10, 3):
    print(f'Die Schleife läuft noch, die Schleifenvariable ist: {schleifenvariable}.')
print('Ende der Schleifendurchführung')

#negative Schrittweite
for schleifenvariable in range(10,0,-1):
    print(f'Die Schleife läuft noch, die Schleifenvariable ist: {schleifenvariable}.')
print('Ende der Schleifendurchführung')

# Standardschrittweite: +1
for schleifenvariable in range(0,5):
    print(f'Die Schleife läuft noch, die Schleifenvariable ist: {schleifenvariable}.')
print('Ende der Schleifendurchführung')

# Standardschrittweite: +1
# Standardstartwert; 0
for schleifenvariable in range(5):
    print(f'Die Schleife läuft noch, die Schleifenvariable ist: {schleifenvariable}.')
print('Ende der Schleifendurchführung')