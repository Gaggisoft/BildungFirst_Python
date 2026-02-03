# FEHLERHAFTE VERSION - Verwendet mutable Default-Argument
# Problem: Die Liste 'gesammelt' wird nur einmal beim Funktionsaufruf erstellt
# und behält ihren Zustand zwischen mehreren Funktionsaufrufen bei
def neue_woerter(text, gesammelt=[]):
    for wort in text.split():
        if wort not in gesammelt:
            gesammelt.append(wort)
    return gesammelt

# KORREKTE VERSION - Microsoft Copilot Lösung
# Verwendet None als Default-Wert und erstellt eine neue Liste pro Aufruf
def neue_woerter(text, gesammelt=None):
    # Prüfe, ob eine Liste übergeben wurde, sonst erstelle eine neue
    if gesammelt is None:
        gesammelt = []
    # Durchlaufe jedes Wort im Text (getrennt durch Leerzeichen)
    for wort in text.split():
        # Füge nur Wörter hinzu, die noch nicht in der Liste sind
        if wort not in gesammelt:
            gesammelt.append(wort)
    return gesammelt


# Test 1: Erster Aufruf mit "hallo nova core"
print(neue_woerter('hallo nova core'))
# Test 2: Zweiter Aufruf mit "hallo explorer heute"
# 'hallo' sollte nicht erneut hinzugefügt werden
print(neue_woerter('hallo explorer heute'))