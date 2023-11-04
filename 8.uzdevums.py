"""
Programma pārbauda punkta  koordinātes figurai, taisnstūrim, ar vertikālam malām x = -5 un x = 2 līnijām un horizontālām malām y = -1 un y = 3.
"""

import doctest
def parbaudit_punkta_koordin_taisnsturim(punkta_x, punkta_y: float )->int:

    """
    Funkcija pārbauda figuru, taisnstūri ar vertikalām malām x = -5
    x = 2  linijām un horizontālām malām līnijas  y = -1 un
    y = 3.
    Funkcija paņem 2 parametrus punkta koordinātes x un y :
    punkta_x un punkta_y.
    Funkcija atgriež atbildes:
    1 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas iekšā taisnstūri.
    2 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz taisnstūra robežlīnijas.
    3 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz ārpus taisnstūra.

    >>> parbaudit_punkta_koordin_taisnsturim(2,-1)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(-5,-1)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(-5,3)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(2,3)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(-1,-1)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(-5,1)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(0,3)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(2,1.5)
    2
    >>> parbaudit_punkta_koordin_taisnsturim(-2,2)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(1,1.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(-4,2.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(1,-0.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(-2,1)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(-1,0.5)
    1
    >>> parbaudit_punkta_koordin_taisnsturim(2.5,2)
    3
    >>> parbaudit_punkta_koordin_taisnsturim(-6,1)
    3
    >>> parbaudit_punkta_koordin_taisnsturim(-2,-1.5)
    3
    >>> parbaudit_punkta_koordin_taisnsturim(0,4)
    3
    >>> parbaudit_punkta_koordin_taisnsturim(3,-2)
    3
    >>> parbaudit_punkta_koordin_taisnsturim(-3,-3)
    3
    
    """

    if punkta_x<=2 and punkta_x>=-5 and punkta_y<=3 and punkta_y>=-1:
        if punkta_x ==-5 or punkta_x == 2 or punkta_y == -1 or punkta_y == 3:
            return 2
        else:
            return 1
    else:
        return 3

doctest.testmod(verbose= True)

lietotaja_x = float(input("Ievadiet punkta x koordinātas: "))
lietotaja_y = float(input("Ievadiet punkta y koordinātas: "))

if parbaudit_punkta_koordin_taisnsturim(lietotaja_x, lietotaja_y) == 1:
    print("Punkts atrodas iekšā figūras.")
elif parbaudit_punkta_koordin_taisnsturim(lietotaja_x, lietotaja_y) == 2:
    print("Punkts atrodas figūras robežlīnija.")
else:
    print("Punkts atrodas figūras ārpusē.")
