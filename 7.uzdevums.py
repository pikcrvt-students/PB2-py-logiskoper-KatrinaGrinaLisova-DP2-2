"""
Programma pārbauda punkta koordinates figurai, taisnstūrim, ar vertikalu un horizontālam malām x = -1 un x = 3 līnijam un horizontālam mālam līnijas y = -2 un y = 1.
"""
import doctest

def parbaudit_punkta_koordin_taisnsturiml(punkta_x, punkta_y : float) -> int:
    """
    Funkcija pārbauda figuru ar vertikālam un horizontālam malām x = -1 un x = 3 līnijam in horizontālam ,alām līnijas y = -2 un y = 1.
    Funkcija paņem divus parametrus punkta koordanātas x un y:
    punkta_x un punkta_y.
    Funkcija atgriež atbildes.
    1 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas iekša taisnstūri.
    2 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas uz taisnstūra robežlīnijas.
    3 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas ārpusē taisnstūri.

    >>> parbaudit_punkta_koordin_taisnsturiml(2,-1)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(1,1)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(-1,1)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(-1,-1)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(4,2)
    3
    >>> parbaudit_punkta_koordin_taisnsturiml(0,-2)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(3,-1.5)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(3,1)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(-1,-2)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(3,-2)
    2
    >>> parbaudit_punkta_koordin_taisnsturiml(0,0)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(2.5,0.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(-0.5,0.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(-0.5,-1)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(3,-3)
    3
    >>> parbaudit_punkta_koordin_taisnsturiml(1,-2.1)
    3
    >>> parbaudit_punkta_koordin_taisnsturiml(1.5,0.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturiml(2.9,-3)
    3
    """
    if punkta_x >= -1 and punkta_x <= 3 and punkta_y >= -2 and punkta_y <= 1:
        if punkta_x == -1 or punkta_x == 3 or punkta_y == -2 or punkta_y == 1:
            return 2
        else:
            return 1
    else:
            return 3
doctest.testmod(verbose = True)

lietotaja_x = float(input("Ievadiet punkta x: "))
lietotaja_y = float(input("Ievadiet punkta y: "))
if  parbaudit_punkta_koordin_taisnsturiml(lietotaja_x , lietotaja_y) == 2:
    print("Uz robežlīnijas")
elif parbaudit_punkta_koordin_taisnsturiml(lietotaja_x, lietotaja_y) == 1:
    print("Figuras iekšā")
else:
    print("Figuras ārpusē")
