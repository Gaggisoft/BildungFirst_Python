# math_utils.py
# Hilfsfunktionen rund um Primzahlen
# Effizient für n bis 1_000_000
# Verwendet nur die Python-Standardbibliothek


def is_prime(n):
    """
    Prüft, ob n eine Primzahl ist.
    Gibt True zurück, wenn n prim ist, sonst False.
    """

    # Negative Zahlen, 0 und 1 sind keine Primzahlen
    if n < 2:
        return False

    # 2 ist die einzige gerade Primzahl
    if n == 2:
        return True

    # Gerade Zahlen größer als 2 sind keine Primzahlen
    if n % 2 == 0:
        return False

    # Prüfe nur ungerade Teiler bis zur Quadratwurzel von n
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


def primes_up_to(n):
    """
    Gibt eine Liste aller Primzahlen zurück,
    die kleiner als n sind.
    Verwendet das Sieb des Eratosthenes.
    """

    if n <= 2:
        return []

    # Boolean-Liste zur Markierung von Primzahlen
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    limit = int(n ** 0.5) + 1

    # Sieb des Eratosthenes
    for i in range(2, limit):
        if sieve[i]:
            # Markiere Vielfache von i als nicht prim
            for multiple in range(i * i, n, i):
                sieve[multiple] = False

    # Alle Indizes sammeln, die als prim markiert sind
    return [i for i, is_p in enumerate(sieve) if is_p]


def next_prime(n):
    """
    Gibt die kleinste Primzahl zurück,
    die größer als n ist.
    """

    # Starte mit der nächsten Zahl
    candidate = n + 1

    # Falls gerade, direkt zur nächsten ungeraden Zahl springen
    if candidate > 2 and candidate % 2 == 0:
        candidate += 1

    # So lange prüfen, bis eine Primzahl gefunden wird
    while not is_prime(candidate):
        candidate += 2

    return candidate
