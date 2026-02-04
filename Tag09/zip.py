#name_liste = ['Anna', 'Ben', 'Clara', 'Otto']
#alter_liste = [42, 37, 50]

#for name, alter in zip(name_liste, alter_liste):
#    print(f'{name} ist {alter} Jahre alt.')

gezippt = [('Anna', 42), ('Ben', 37), ('Clara', 50)]
name_liste, alter_liste = zip(*gezippt)

# Casten zu Listen
name_liste = list(name_liste)
alter_liste = list(alter_liste)

print(name_liste)
print(alter_liste)

# Tupel
x = 1
y = 2
z = 3
# ALternative
tupel = (1, 2, 3)
x, y, z = tupel