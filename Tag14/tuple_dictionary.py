# Tuple
print('\nTUPLE\n')
position = (10, 20)

# Werte eines Tuples können nicht geändert werden
#position[0] = 5 #-> TypeError

print('X-Koordinate:', position[0])
print('Y-Koordinate:', position[1])

# mehrere Wertzuweisungen mit Tuple
(x, y) = (10, 20)       # x, y = 10, 20
print(x)
x = 5
print(x)

# Rückgabe mehrerer Werte mit Tuple
def division_rest(zahl1, zahl2):
    if zahl2 != 0:
        return zahl1//zahl2, zahl1%zahl2
    return None

print(division_rest(9, 4))
(quotient, rest) = division_rest(9, 4)
print('9 // 4 =', quotient)
print('9 % 4 =', rest)

# Dictionary
print('\nDICTIONARY\n')
# als Schlüssel erlaubt: hashable (Listen und Dictionaries sind nicht erlaubt)
student = {
    'name': 'Anna',
    'noten': (1.3, 2.0, 1.7),
    'alter': 25
}
print(student['noten'])
print(student['noten'][1])

print(student.keys())
print(student.values())