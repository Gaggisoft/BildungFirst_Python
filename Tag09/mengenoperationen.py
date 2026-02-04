a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

print('A:', a)
print('B:', b)

# Vereinigung
print('Vereinigung:', a | b)

# Schnittmenge
print('Schnittmenge:', a & b)

# Differenz A\B
print('Differenz A\B:', a - b)

# symmetrische Differenz
print('symmetrische Differenz:', a ^ b)

print('##################################################')

a = {1, 2}
b = {1, 2, 3}
c = {1, 2, 3}

print('A:', a)
print('B:', b)
print('C:', c)

# Teilmenge
print('A ist Teilmenge von B:', a.issubset(b))
print('B ist Teilmenge von A:', b.issubset(a))
print('B ist Teilmenge von C:', b.issubset(c))

# Obermenge
print('A ist Obermenge von B:', a.issuperset(b))
print('B ist Obermenge von A:', b.issuperset(a))
print('B ist Obermenge von C:', b.issuperset(c))