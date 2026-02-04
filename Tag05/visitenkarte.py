# Nutzer nach seinem Namen fragen => Variable name
name = input('Bitte gib deinen Namen an: ')
# Nutzer nach seinem Alter fragen => Variable alter
alter = input('Bitte gib dein Alter an: ')
# Nutzer nach seinem Wohnort fragen => Variable wohnort
wohnort = input('Bitte gib deinen Wohnort an: ')

# Casting: Umwandeln des Alters in eine Zahl (int)
alter = int(alter)

# Begrüßung ausgeben
print(f'Hallo {name}! Du wohnst in {wohnort} und bist {alter} Jahre alt.')

# Alle String-Funktionen sollen den Namen betreffen
# komplett groß schreiben
print(name.upper())
# komplett klein schreiben
print(name.lower())
# alle a durch @ ersetzen
print(name.replace('a', '@'))

# Visitenkarte
# -------------------------------
#  Name:        ...
#  Stadt:       ...
#  Alter:       ...
#  Geburtsjahr: ...
# -------------------------------
print(f'''
    -----------------------------------
     Name:\t\t{name}
     Stadt:\t\t{wohnort}
     Alter:\t\t{alter}
     Geburtsjahr:\t{2026-alter} oder {2026-alter+1}
    -----------------------------------
    ''')

# KI-Vorschlag für alternative Formatierung
print("=" * 35)
print(f"  Name:        {name}")
print(f"  Stadt:       {wohnort}")
print(f"  Alter:       {alter}")
print(f"  Geburtsjahr: {2026 - alter}")
print("=" * 35)