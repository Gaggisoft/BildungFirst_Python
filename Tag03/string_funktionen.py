wort = "Pythonprogrammierung"
#       012345...               Index
#      -...           654321    Index negativ

# Indexing
print(wort[1])  # y
print(wort[-1]) # g

# Slicing
print(wort[0:6])    # Python (Index 6 ist exklusive, also nicht enthalten)
print(wort[:6])     # Python
print(wort[6:])     # programmierung
print(wort[2:5])    # tho

# wichtige Funktionen
print(wort.upper()) # Großbuchstaben
print(wort.lower()) # Kleinbuchstaben
print(wort.replace("Python", "Java"))   # Ersetzen des ersten Teilstrings mit dem zweiten