print('Bitte geben Sie Ihre Daten ein.')
vorname = input('Vorname:\t')
# Der Nutzer wird aufgefordert, seinen Vornamen einzugeben.
# Die Eingabe wird als String in der Variablen vorname gespeichert.
nachname = input('Nachname:\t')
# Der Nutzer wird aufgefordert, seinen Nachnamen einzugeben.
# Die Eingabe wird als String in der Variablen nachname gespeichert.

print('Hallo ' + vorname + ' ' + nachname + '!')
# Ausgabe einer Begrüßung des Nutzers.

print(f'Hallo {vorname} {nachname}!')
# Alternative als f-String