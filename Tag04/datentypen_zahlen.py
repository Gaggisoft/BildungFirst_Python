# Zahlen

# ganze Zahl: Integer (int)
ganze_zahl = 1 + 3
print(ganze_zahl)
print(type(ganze_zahl))

# Kommazahlen (float)
kommazahl = 5.8
print(kommazahl)
print(type(kommazahl))

summe_ganze_kommazahl = ganze_zahl + kommazahl
print(summe_ganze_kommazahl)
print(type(summe_ganze_kommazahl))

# Casten in int
print(int(summe_ganze_kommazahl))
# Runden (round to even, also Runden zur nächsten geraden Zahl)
print(round(summe_ganze_kommazahl))
print(round(2.5))
print(round(3.5))

# Begrenzen der Nachkommastellen auf zwei Stellen
# Variante 1
pi = 3.14159
pi = pi * 100
pi = round(pi)
pi = pi / 100.0
print(pi)
# Variante 2
pi = 3.14159
pi = round(pi, 2)
print(pi)