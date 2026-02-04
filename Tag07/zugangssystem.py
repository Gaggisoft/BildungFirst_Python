# Zugangssystem für Freizeitpark

# Variablen
# alter: int
alter = 14
# hat_ticket: bool
hat_ticket = True
# hat_vip_pass: bool
hat_vip_pass = True
# hat_begleitperson: bool
hat_begleitperson = True
# hat_gesundheitsfreigabe: bool
hat_gesundheitsfreigabe = False
# steht_auf_blacklist: bool
steht_auf_blacklist = False

# Allgemeiner Parkzutritt
# 1. Eintritt ist erlaubt, wenn die Person ein Ticket hat und nicht Blacklist steht.
# 2. Oder: Die Person hat einen VIP-Pass - dann darf sie immer rein.
if (hat_ticket and not steht_auf_blacklist) or hat_vip_pass:
    eintritt = 'erlaubt'
else:
    eintritt = 'verweigert'
# 3. Wenn die Person kein Ticket hat, gib zusätzlich "Ticket fehlt" aus.
if not hat_ticket:
    print('Ticket fehlt')

# Zugang zur Achterbahn
# 1. Mindestalter: 12 Jahre
# 2. Die Person braucht eine Gesundheitsfreigabe.
# 3. Oder: Eine Begleitperson ist dabei, dann reicht das Alter allein.
# 4. Personen auf der Blacklist dürfen nicht fahren.
if not steht_auf_blacklist and (alter >= 12) and (hat_gesundheitsfreigabe or hat_begleitperson):
    achterbahn = 'erlaubt'
else:
    achterbahn = 'verweigert'

# Zugang zur Geistervilla
# 1. Mindestalter: 16 Jahre
# 2. Oder: Person ist VIP
# 3. Personen mit Begleitperson dürfen trotzdem nicht hinein.
# 4. Personen auf der Blacklist dürfen ebenfalls nicht hinein.
if not steht_auf_blacklist and (alter >= 16 or hat_vip_pass) and not hat_begleitperson:
    geistervilla = 'erlaubt'
else:
    geistervilla = 'verweigert'

# Ausgabe der Zusammenfassung
# Parkeintritt: erlaubt / verweigert
print('Parkeintritt:', eintritt)
# Achterbahn: erlaubt / verweigert
print('Achterbahn:', achterbahn)
# Geistervilla: erlaubt / verweigert
print('Geistervilla:', geistervilla)