from collections import Counter

def wort_zaehlen(text):
    return len(text.split())

def erweiterte_analyse(text):
    woerter = text.lower().split()
    return Counter(woerter).most_common(5)

text = input('Bitte geben Sie einen Text ein: ')
anzahl = wort_zaehlen(text)

print(f'\n{"="*50}')
print(f'Analyseergebnis:')
print(f'{"="*50}')
print(f'Eingegebener Text: "{text}"')
print(f'Anzahl der Wörter: {anzahl}')
print(f'{"="*50}\n')