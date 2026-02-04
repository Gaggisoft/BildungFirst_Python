text = input('Gib bitte einen Text ein:\n')
zu_suchender_string = input('Nach welchem Text soll gesucht werden?\n')

# zählen, wie oft g oder G vorkommt
print(text.count('g') + text.count('G'))
print(text.upper().count('G'))

# zu_suchender_string suchen in text
print(f'Der String \'{zu_suchender_string}\' kommt im Text \'{text}\' insgesamt {text.count(zu_suchender_string)} mal vor.')

# count mit Start und Ende verwenden
print(text.count('e', 3, 7))