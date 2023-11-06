"""
Programma pārbauda punkta  koordinātes figurai, piecstūrim, ar stūriem (-7,0),(-6.2,2), (3.9,2), (5,-3), (-4.7,-3).
"""

import doctest
def parbaudit_punkta_koordin_piecsturis(punkta_x, punkta_y: float )->int:

    """
    Funkcija pārbauda figuru, piecstūri, ar stūriem (-7,0),(-6.2,2), (3.9,2), (5,-3), (-4.7,-3).
    Funkcija paņem 2 parametrus punkta koordinātes x un y :
    punkta_x un punkta_y.
    Funkcija atgriež atbildes:
    1 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas iekšā piecstūri.
    2 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz piecstūra robežlīnijas.
    3 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas ārpus piecstūra.

    >>> parbaudit_punkta_koordin_piecsturis(0,3)
    2
    >>> parbaudit_punkta_koordin_piecsturis(-2.8,-2)
    2
    >>> parbaudit_punkta_koordin_piecsturis(-2,3)
    2
    >>> parbaudit_punkta_koordin_piecsturis(3.5,-2)
    2
    >>> parbaudit_punkta_koordin_piecsturis(-2.6,-2)
    2
    >>> parbaudit_punkta_koordin_piecsturis(-4,0)
    2
    >>> parbaudit_punkta_koordin_piecsturis(3,0)
    2
    >>> parbaudit_punkta_koordin_piecsturis(-3.5,0.30)
    1
    >>> parbaudit_punkta_koordin_piecsturis(0,0)
    1
    >>> parbaudit_punkta_koordin_piecsturis(-2,-1.5)
    1
    >>> parbaudit_punkta_koordin_piecsturis(1.5,-1)
    1
    >>> parbaudit_punkta_koordin_piecsturis(-3,0.75)
    1
    >>> parbaudit_punkta_koordin_piecsturis(0,4)
    3
    >>> parbaudit_punkta_koordin_piecsturis(3,3)
    3
    >>> parbaudit_punkta_koordin_piecsturis(5,-1)
    3
    >>> parbaudit_punkta_koordin_piecsturis(-4,2.5)
    3
    >>> parbaudit_punkta_koordin_piecsturis(-2,4)
    3
    >>> parbaudit_punkta_koordin_piecsturis(-7,-2)
    3
    >>> parbaudit_punkta_koordin_piecsturis(-6,1)
    3

    """

    if punkta_y >= -2 and punkta_y <= 3 and punkta_y <= 1.5*punkta_x + 6 and punkta_y >= -(5/3)*punkta_x - 20/3 and punkta_y <= -2*punkta_x + 6:
        if punkta_y == -2 or punkta_y == 3 or punkta_y == 1.5*punkta_x + 6 or punkta_y == -(5/3)*punkta_x - 20/3 or punkta_y == -2*punkta_x + 6:
            return 2
        else:
            return 1
    else:
        return 3

doctest.testmod(verbose= True)

lietotaja_x = float(input("Ievadiet punkta x koordinātas: "))
lietotaja_y = float(input("Ievadiet punkta y koordinātas: "))

if parbaudit_punkta_koordin_piecsturis(lietotaja_x, lietotaja_y) == 1:
    print("Punkts atrodas iekšā figūras.")
elif parbaudit_punkta_koordin_piecsturis(lietotaja_x, lietotaja_y) == 2:
    print("Punkts atrodas figūras robežlīnija.")
else:
    print("Punkts atrodas figūras ārpusē.")

