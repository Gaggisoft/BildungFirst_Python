from taschenrechner import summe, differenz, produkt, quotient

def test_summe():
    assert summe(2, 3) == 5
    assert summe(1, 0) == 1
    assert summe(1, -1) == 0

def test_differenz():
    assert differenz(5, 3) == 2
    assert differenz(2, 5) == -3
    assert differenz(3, 3) == 0

def test_produkt():
    assert produkt(2, 3) == 6
    assert produkt(0, 4) == 0
    assert produkt(5, 0) == 0
    assert produkt(-2, 4) == -8
    assert produkt(-2, -3) == 6

def test_quotient_normal():
    assert quotient(6, 3) == 2
    assert quotient(-5, 2) == -2.5

def test_quotient_teilen_durch_null():
    assert quotient(4, 0) == None