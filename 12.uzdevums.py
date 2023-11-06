"""
Programma pārbauda punkta  koordinātes figurai, rinķim, ja centrs ir (-4,3), rādiuss - 2.
"""

import doctest
def parbaudit_punkta_koordin_rinkim(punkta_x, punkta_y: float )->int:

    """
    Funkcija pārbauda figuru, rinķis, ja centrs ir (-4,3), rādiuss - 2.
    Funkcija paņem 2 parametrus punkta koordinātes x un y :
    punkta_x un punkta_y.
    Funkcija atgriež atbildes:
    1 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas iekšā rinķi.
    2 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz rinķa robežlīnijas.
    3 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz ārpus rinķi.

    >>> parbaudit_punkta_koordin_rinkim(-4,1)
    2
    >>> parbaudit_punkta_koordin_rinkim(-2,3)
    2
    >>> parbaudit_punkta_koordin_rinkim(-4,4.5)
    1
    >>> parbaudit_punkta_koordin_rinkim(-6,3)
    2
    >>> parbaudit_punkta_koordin_rinkim(-4,3)
    1
    >>> parbaudit_punkta_koordin_rinkim(-5,3)
    1
    >>> parbaudit_punkta_koordin_rinkim(-3,2)
    1
    >>> parbaudit_punkta_koordin_rinkim(-3.5,3.5)
    1
    >>> parbaudit_punkta_koordin_rinkim(-2,1)
    3
    >>> parbaudit_punkta_koordin_rinkim(-7,3)
    3
    >>> parbaudit_punkta_koordin_rinkim(0,2)
    3
    >>> parbaudit_punkta_koordin_rinkim(1,5)
    3
    >>> parbaudit_punkta_koordin_rinkim(-5.5,4)
    2
    >>> parbaudit_punkta_koordin_rinkim(-5.8,3.4)
    1
    >>> parbaudit_punkta_koordin_rinkim(-5.6,1.8)
    1

    """

    if (punkta_x+4)**2+(punkta_y-3)**2 <= 4 and punkta_y <= 2*punkta_x + 15:
        if (punkta_x+4)**2+(punkta_y-3)**2 == 4 or punkta_y == 2*punkta_x + 15:
            return 2
        else:
            return 1
    else:
        return 3 

doctest.testmod(verbose= True)

lietotaja_x = float(input("Ievadiet punkta x koordinātas: "))
lietotaja_y = float(input("Ievadiet punkta y koordinātas: "))

if parbaudit_punkta_koordin_rinkim(lietotaja_x, lietotaja_y) == 2:
    print("Punkts atrodas iekšā figūras.")
elif parbaudit_punkta_koordin_rinkim(lietotaja_x, lietotaja_y) == 1:
    print("Punkts atrodas figūras robežlīnija.")
else:
    print("Punkts atrodas figūras ārpusē.")





    
