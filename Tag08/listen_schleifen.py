# Liste erstellen
liste = [0.45, 'Lyra', True, 'Ava', 6]

# elementweise Ausgabe der Liste
print('for-Schleife')
for index in range(0, len(liste)):
    print(liste[index])

# elementweise Ausgabe der Liste als while-Schleife
print('while-Schleife')
index = 0
while index < len(liste):
    print(liste[index])
    index += 1

# for-Schleife zum Durchlaufen einer Liste
for element in liste:
    print(element)