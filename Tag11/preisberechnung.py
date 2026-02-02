# Funktion zur Berechnung des Gesamtpreises
# zwei Parameter: preis, steuersatz (in Prozent)
# Standardwert für Steuer (19 %)
# Rückgabe: Endpreis
def berechne_preis(preis, steuersatz=19):
    anteil_steuer = preis * steuersatz / 100
    gesamtpreis = preis + anteil_steuer
    return gesamtpreis

print(f'{100}€ versteuert mit {16}% ergibt eine Gesamtpreis von {berechne_preis(100, 16):.2f}€.')

# 2. Berechnung für mehrere Produkte (Liste)
# preise = [10, 25, 99, 5]