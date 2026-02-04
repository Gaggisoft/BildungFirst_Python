text = input('Gib einen beliebigen Text ein:\n')

# Anzahl der Zeichen im Text zählen
print(f'Der Text besteht aus {len(text)} Zeichen.')
# Leerzeichen im String entfernen mit replace
text_ohne_leerzeichen = text.replace(' ', '')
print(text_ohne_leerzeichen)
print(f'Der Text besteht aus {len(text_ohne_leerzeichen)} Zeichen.')
# Leerzeichen am Anfang und am Ende eines Strings entfernen mit strip
text_ohne_leerzeichen = text.strip()
print(text_ohne_leerzeichen)
print(f'Der Text besteht aus {len(text_ohne_leerzeichen)} Zeichen.')
# Anzahl der Vorkommnisse eines Teilstrings innerhalb eines Strings
print(f'Der Buchstabe e kommt im String \'{text}\' insgesamt {text.count('te')} vor.')