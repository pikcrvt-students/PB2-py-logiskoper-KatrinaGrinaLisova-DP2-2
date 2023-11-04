"""
Programma pārbauda punkta koordinātas figūrai, rinķim, ar vertikālām malām x=1 un x=-1 līnijām un horizontālām
līnijām y=1 un y=-1.

"""
import doctest

def parbaudit_punkta_koordin_rinkim(punkta_x, punkta_y : float) -> int:

    """
    Funkcija pārbauda punkta koordinātas figūrai, rinķim, ar vertikālām malām x=1 un x=-1 līnijām un horizontālām
    līnijām y=1 un y=-1.
    Funkcija paņem divus parametrus punkta koordanātas x un y:
    punkta_x un punkta_y.
    Funkcija atgriež atbildes.
    1 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas iekša rinķi.
    2 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas uz rinķa robežlīnijas.
    3 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas ārpusē rinķi.

    >>> parbaudit_punkta_koordin_rinkim(1, 1)
    3
    >>> parbaudit_punkta_koordin_rinkim(-0.6, 1.2)
    3
    >>> parbaudit_punkta_koordin_rinkim(0, 1)
    2
    >>> parbaudit_punkta_koordin_rinkim(0.2,0.1)
    1
    >>> parbaudit_punkta_koordin_rinkim(0.2,0.7)
    1
    >>> parbaudit_punkta_koordin_rinkim(1, 0)
    2
    >>> parbaudit_punkta_koordin_rinkim(0.5, 0.5)
    1
    >>> parbaudit_punkta_koordin_rinkim(-0.3, 0)
    1
    >>> parbaudit_punkta_koordin_rinkim(0, 0)
    1
    >>> parbaudit_punkta_koordin_rinkim(1.5, 0)
    3
    >>> parbaudit_punkta_koordin_rinkim(0.75,0.66)
    1
    >>> parbaudit_punkta_koordin_rinkim(-0.6, 0.8)
    2
    >>> parbaudit_punkta_koordin_rinkim(0.75,0)
    1
    >>> parbaudit_punkta_koordin_rinkim(-1.5,1)
    3
    >>> parbaudit_punkta_koordin_rinkim(2,2)
    3
    >>> parbaudit_punkta_koordin_rinkim(-0.70, -0.71)
    1
    >>> parbaudit_punkta_koordin_rinkim(0,-1)
    2
    >>> parbaudit_punkta_koordin_rinkim(0.5,0.1)
    1
    >>> parbaudit_punkta_koordin_rinkim(0,-0.5)
    1
    >>> parbaudit_punkta_koordin_rinkim(-3,0)
    3
    >>> parbaudit_punkta_koordin_rinkim(0.1,0.1)
    1
    
    """
    R = 1

    if punkta_x ** 2 + punkta_y ** 2 <= R ** 2:
        if punkta_x ** 2 + punkta_y ** 2 == R ** 2:
            return 2
        else:
            return 1
    else:
        return 3

doctest.testmod(verbose=True) 

lietotaja_x = float(input("Ievadiet punkta x: "))
lietotaja_y = float(input("Ievadiet punkta y: "))

if parbaudit_punkta_koordin_rinkim(lietotaja_x , lietotaja_y) == 2:
    print("Atrodas uz robežlinijā")
elif parbaudit_punkta_koordin_rinkim(lietotaja_x, lietotaja_y) == 1: 
    print("Atrodas iekšā figurā")
else:
    print("Atrodas ārpus figurā")
