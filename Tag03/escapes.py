print('Orion sagt: "Hallo Welt"')
# ' werden zur Markierung des Strings verwendet (außen)
# " werden als Teil des Strings interpretiert (innen + anders)
# kein Escape, da unterschiedliche Anführungszeichen

print("It's a beautiful day")
# " werden zur Markierung des Strings verwendet (außen)
# ' wird als Teil des Strings interpretiert (innen + anders)
# kein Escape, da unterschiedliche Anführungszeichen

print("Orion sagt: \"Hallo Welt\"")
# äußere " zur Markierung des Strings
# innere " identisch => Konflikt
# Escape \ => folgendes Zeichen gehört zum String (hier: \")

print('It\'s a beautiful day')
# äußere ' zur Markierung des Strings
# einzelnes ' innerhalb des Strings => Konflikt
# Escape \ => einzelnes ' wird als Teil des Strings interpretiert

# \n Zeilenumbruch
print("abc\ndef")

# \t horizontaler Tabulator
print("abc\tdef")
print("abcde\tdef")

# \\ Backslash als Teil des Strings
print("\\")

# \' und \" Anführungszeichen
print('\'', "\"")

# \r Carriage Return (Zeilenanfang)
print("abc\rde")

# \b Backspace (ein Zeichen zurück)
print("abc\b")
print("abc\bd")

# \f Form Feed (Seitenvorschub)
print("abc\fde\fge")

# \v vertikaler Tabulator
print("abc\vde\vfg")