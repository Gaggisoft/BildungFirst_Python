schueler = {
    'name': 'Lena',
    'alter': 16,
    'kurse': ['Mathe', 'Informatik', 'Englisch'],
    'note_informatik': 1
}

schueler['note_informatik'] = 2

print(schueler)

for schluessel in schueler:
    print(schluessel, '->', schueler[schluessel])