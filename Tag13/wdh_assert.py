x = 5
assert x < 10, 'x ist nicht kleiner als 10'
#assert x > 10, 'x ist nicht größer als 10'

######################################################################

def summe(summand1, summand2):
    return summand1 + summand2

assert summe(0, 5) == 5, 'Die Summe aus 0 und 5 ergibt nicht 5.'
assert summe(2, 5) == 7, 'Die Summe aus 2 und 5 ergibt nicht 7.'


print('Ende')