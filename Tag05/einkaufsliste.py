print('Meine Einkaufsliste\n\n')

# Nutzer nach seinem Namen fragen => Variable name
name = input('Gib bitte deinen Namen ein:\n')

# Begrüßung ausgeben
print(f'Hallo {name}, bitte gib die folgenden Informationen zu deinen Einkäufen ein:\n')

# Nutzer nach Namen des ersten Produkts fragen => Variable produkt1_name
produkt1_name = input('1. Produkt: ')
# Nutzer nach Preis des ersten Produkts fragen => Variable produkt1_preis
produkt1_preis = float(input('Preis: '))

# Nutzer nach Namen des zweiten Produkts fragen => Variable produkt2_name
produkt2_name = input('\n2. Produkt: ')
# Nutzer nach Preis des zweiten Produkts fragen => Variable produkt2_preis
produkt2_preis = float(input('Preis: '))

# Nutzer nach Namen des dritten Produkts fragen => Variable produkt3_name
produkt3_name = input('\n3. Produkt: ')
# Nutzer nach Preis des dritten Produkts fragen => Variable produkt3_preis
produkt3_preis = float(input('Preis: '))

# Gesamtpreis berechnen
gesamt_preis = produkt1_preis + produkt2_preis + produkt3_preis

# Ausgabe
print('\n\n--- EINKAUFSLISTE ---')
print(f'{produkt1_name}: {produkt1_preis} €')
print(f'{produkt2_name}: {produkt2_preis} €')
print(f'{produkt3_name}: {produkt3_preis} €')
print('-----------------------')
print(f'GESAMT: {gesamt_preis} €')