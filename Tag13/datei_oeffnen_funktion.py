from pathlib import Path

# Funktion lese_datei()
def lese_datei(dateiname):
    if '__file__' in globals():
        basis_ordner = Path(__file__).parent

    else:
        basis_ordner = Path.cwd()

    datei_pfad = basis_ordner / dateiname       #'beispiel.txt' # dateiname

    try:
        with datei_pfad.open('r', encoding='utf-8') as datei:
            inhalt = datei.read()
            return inhalt
    except FileNotFoundError:
        return 'Datei nicht gefunden'
    except UnicodeDecodeError:
        return "Encoding-Problem"
    
print(lese_datei('beispiel.txt'))