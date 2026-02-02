# Funktion zum Addieren von zwei Parametern, der zweite ist optiona mit Defaultwert 0
def addieren (summand1: int, summand2: int=0) -> int:
    summe = summand1 + summand2
    #print(summe)
    return summe

input1 = int(input('Gib die erste Zahl ein:  '))
input2 = int(input('Gib die zweite Zahl ein: '))
ergebnis = addieren(input1, input2)
print(f'{input1} + {input2} = {ergebnis}')
#addieren(summand1, input2)
print(addieren(10))
print(addieren('Test', 'test'))