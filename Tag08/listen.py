# Liste erstellen
liste = [0.45, 'Lyra', True, 'Ava', 6]

# Ausgabe der Liste
print(liste)

# Zugriff auf das dritte (Index: 2) Listenelement + Ausgabe
print(liste[2])

# Liste um ein Element erweitern: String 'neues Element'
liste.append('neues Element')

# Ausgabe der Liste
print(liste)

# Anzahl der Elemente der Liste ausgeben
print(len(liste))

# Abbruchbedingung für while-Schleife
weiter = True
# leere Liste, wird mit EIngaben gefüllt
liste = []
while weiter:
    # Eingabe durch Nutzer
    eingabe = input('Gib bitte eine Zahl ein: ')
    # leere Eingabe beendet Schleife
    if len(eingabe) == 0:
        weiter = False
    # Eingabe an Liste anhängen
    else:
        liste.append(int(eingabe))
print(liste)

# Element an der Stelle mit dem Index 2 einfügen
liste.insert(2, 'neues Element')
print(liste)

# Element aus Liste entfernen
# remove
#liste.remove('neues Element')
# Überprüfung, ob Wert in Liste enthalten ist
if 'neues Element' in liste:
    print('\'neues Element\' ist in Liste enthalten.')
else:
    print('\'neues Element\' ist nicht in Liste enthalten.')

if 'neues Eleent' in liste:
    print('\'neues Eleent\' ist in Liste enthalten.')
else:
    print('\'neues Eleent\' ist nicht in Liste enthalten.')

# pop
#wert = liste.pop(1)

#print(f'{wert} wurde aus Liste entfernt')
# del
#del liste[1]      # Element mit Index 1 wird gelöscht
#print(liste)
#del liste[5:7]    # Elemente mit den Indizes 5 bis 6 werden gelöscht
#print(liste)

# clear (Liste komplett leeren)
liste.clear()
print(liste)