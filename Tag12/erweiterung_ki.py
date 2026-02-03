def wort_zaehlen(text):
    return len(text.split())

text = input('Bitte Text eingeben: ')
print('Anzahl Wörter:', wort_zaehlen(text))