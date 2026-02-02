import random

# Zielpunktestand
print('\n' + '='*60)
print('🎯  SPIELKONFIGURATION  🎯'.center(60))
print('='*60)
limit_korrekt = False
# Nutzer kann Limit wählen
try:
    limit = int(input('Gib den Zielpunktestand zum Gewinnen ein: '))
    # negatives Limit ist nicht erlaubt
    if limit > 0:
        limit_korrekt = True
    else:
        print('❌ Ungültige Eingabe. Standardwert 20 wird verwendet.')
except ValueError:
    # fehlerhafte Eingabe
    print('❌ Ungültige Eingabe. Standardwert 20 wird verwendet.')
# Standardwert verwenden
if not limit_korrekt:
    limit = 20
print('='*60)

# Variablen zur Speicherung der Gesamtpunkte
punkte_spieler = 0
punkte_computer = 0

# ersten Spieler bestimmen
print('\n' + '='*60)
print('🎲 Der Startspieler wird ermittelt...'.center(60))
print('='*60)
spieler_am_zug = random.choice([True, False])
if spieler_am_zug:
    print('👤 Du darfst anfangen!'.center(60))
else:
    print('🤖 Der Computer fängt an!'.center(60))
print('='*60)

# Ausgabe zum Spielstart
print('\n' + '='*60)
print(f'🎲  GLÜCKSWÜRFEL SPIEL  🎲'.center(60))
print('='*60)
print(f'Ziel: Erreiche {limit} Punkte, um zu gewinnen!'.center(60))
print('='*60)

while punkte_computer < limit and punkte_spieler < limit:
    punkte_spieler_runde = 0
    spieler_letzer_wurf = 0
    punkte_computer_runde = 0
    computer_letzer_wurf = 0

    if spieler_am_zug:
        print("\n" + "-"*60)
        print("👤  DU BIST AN DER REIHE".center(60))
        print("-"*60)
    else:
        print("\n" + "-"*60)
        print("🤖  DER COMPUTER IST AN DER REIHE".center(60))
        print("-"*60)

    # Spieler ist dran
    while spieler_am_zug:
        # würfeln
        spieler_wurf = random.randint(1, 6)
        print(f"\n🎲 Du würfelst eine {spieler_wurf}")
        # zählt Wurf? (kleiner als vorheriger beendet Runde)
        if spieler_wurf < spieler_letzer_wurf:
            print("❌ Dein Wurf ist kleiner als dein letzter Wurf!")
            print("💔 Du verlierst alle Punkte dieser Runde!")
            punkte_spieler_runde = 0
            spieler_am_zug = False
        # Wurf zählt
        else:
            # Rundenpunkte aktualisieren
            punkte_spieler_runde += spieler_wurf
            print(f"✅ Deine Punkte in dieser Runde: {punkte_spieler_runde}")
            spieler_letzer_wurf = spieler_wurf
            # Entscheidung des Spielers, ob weitergespielt oder gespeichert wird
            print(f'💾 Wenn Du speichest, hättest du {punkte_spieler + punkte_spieler_runde} Punkte.')
            weiterspielen = input("▶️  [Enter] = Weiterspielen | [Beliebige Taste] = Speichern: ")
            # Speichern wurde gewählt
            if len(weiterspielen) != 0:
                # aktuelle Punkte zu den Gesamtpunkten addieren
                punkte_spieler += punkte_spieler_runde
                # Runde für Spieler beenden
                spieler_am_zug = False

    # Computer ist dran
    while not spieler_am_zug:
        # würfeln
        computer_wurf = random.randint(1, 6)
        print(f"\n🎲 Der Computer würfelt eine {computer_wurf}")
        # zählt Wurf? (kleiner als vorheriger beendet Runde)
        if computer_wurf < computer_letzer_wurf:
            print("❌ Der Computer hat einen kleineren Wurf als sein letzter Wurf!")
            print("💔 Er verliert alle Punkte dieser Runde!")
            punkte_computer_runde = 0
            spieler_am_zug = True
        # Wurf zählt
        else:
            # Rundenpunkte aktualisieren
            punkte_computer_runde += computer_wurf
            print(f"✅ Punkte des Computers in dieser Runde: {punkte_computer_runde}")
            computer_letzer_wurf = computer_wurf
            # Entscheidung des Computers, ob weitergespielt oder gespeichert wird
            weiterspielen = random.choice([True, False])
            # Speichern wurde gewählt
            if not weiterspielen:
                # aktuelle Punkte zu den Gesamtpunkten addieren
                punkte_computer += punkte_computer_runde
                # Runde für Computer beenden
                spieler_am_zug = True

    # Gesamtpunkte ausgeben
    print("\n" + "="*60)
    print("📊  ZWISCHENSTAND".center(60))
    print("="*60)
    print(f"👤 Du:       {punkte_spieler:>3} Punkte")
    print(f"🤖 Computer: {punkte_computer:>3} Punkte")
    print(f"🎯 Ziel:     {limit:>3} Punkte")
    print("="*60)

# Gewinner ermitteln
print("\n" + "="*60)
print("🏁  SPIELENDE  🏁".center(60))
print("="*60)
if punkte_spieler >= limit and punkte_computer >= limit:
    print("🤝 Unentschieden! Beide haben gut gespielt!".center(60))
elif punkte_spieler >= limit:
    print("🎉 HERZLICHEN GLÜCKWUNSCH! DU HAST GEWONNEN! 🎉".center(60))
else:
    print("😔 Der Computer hat gewonnen! Viel Glück beim nächsten Mal!".center(60))
print("="*60)
print(f"Endstand - Du: {punkte_spieler}, Computer: {punkte_computer}".center(60))
print("="*60)