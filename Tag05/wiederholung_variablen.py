# Nutzer nach seinem Namen fragen => Variable name
name = input('Bitte gib deinen Namen an: ')
# Nutzer nach seinem Alter fragen => Variable alter
alter = int(input('Bitte gib dein Alter an: '))

# Begrüßung des Nutzers und Ausgabe des Alters in 10 Jahren
print(f'Hallo {name}! Du bist in 10 Jahren {alter+10} Jahre alt.')



# Kleine Preisberechnung

# Name des Produkts => Variable produkt
produkt = input('Welches Produkt kaufst du?\n')
# Preis des Produkts => Variable preis
preis = float(input('Wie ist der Preis in €?\n'))
# Anzahl des Produkts => Variable anzahl
anzahl = int(input('Wie viele kaufst du?\n'))

# Gesamtpreis berechnen
gesamt = preis * anzahl

# Ausgabe
print(f'{anzahl} x {produkt} für je {preis}€ kostet {gesamt}€.')