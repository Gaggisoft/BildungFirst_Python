# Lege eine Variable mit deinem Vornamen an.
vorname = 'Susanne'
# Lege eine Variable mit deinem Alter an.
alter = 41
# Gib beide Variablen einzeln mit print() aus.
print(vorname)
print(alter)
# Baue mit Concatenation (+) einen ganzen Satz:
# Mein Name ist (dein Name) und ich bin (dein Alter) Jahre alt.
satz = 'Mein Name ist '+ vorname + ' und ich bin ' + str(alter) + ' Jahre alt.'
# Gib den Satz mit print() aus.
print(satz)

# f-String
print(f'Mein Name ist {vorname} und ich bin {alter} Jahre alt.')