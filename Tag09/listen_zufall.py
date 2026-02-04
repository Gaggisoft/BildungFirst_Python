# Import des Moduls random
import random

# Liste mit Zahlen
zahlen = [4, 7, 1.5, 9, -3.4]

# kleinster Wert einer Liste
print('kleinster Wert:', min(zahlen))

# größter Wert einer Liste
print('größter Wert:', max(zahlen))

# zufälliger Wert aus Liste
print(f'zufälliger Wert aus Liste {zahlen}: {random.choice(zahlen)}')

namen = ['Anna', 'Ben', 'Otto']
print(f'zufälliger Name aus Liste {namen}: {random.choice(namen)}')

# Zufallszahl zwischen 1 und 6 (Würfel)
print('Zufallwurf eines sechsseitigen Würfels:', random.randint(1, 6))