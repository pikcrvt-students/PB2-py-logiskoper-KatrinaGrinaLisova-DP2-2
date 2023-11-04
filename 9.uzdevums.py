"""
Programma pārbauda punkta koordinātas figūrai, trijstūrim, ar vertikālām malām x=0 un x=2 līnijām un horizontālām
līnijām y=-1 un y=3
"""

import doctest

def parbaudit_punkta_koordin_trijsturim(punkta_x, punkta_y : float) -> int: 
    """
    Funkcija pārbauda punkta koordinātas figūrai, trijstūrim, ar vertikālām malām x=0 un x=2 līnijām un horizontālām
    līnijām y=-1 un y=3
    Funkcija paņem divus parametrus punkta koordanātas x un y:
    punkta_x un punkta_y.
    Funkcija atgriež atbildes.
    1 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas iekša trijstūri.
    2 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas uz trijstūra robežlīnijas.
    3 ja punkts uz koordinātes (punkta_x ; punkta_y) atrodas ārpusē trijstūri.

    
    >>> parbaudit_punkta_koordin_trijsturim(0,-1)
    2
    >>> parbaudit_punkta_koordin_trijsturim(0,3)
    2
    >>> parbaudit_punkta_koordin_trijsturim(0,0.5)
    2
    >>> parbaudit_punkta_koordin_trijsturim(0,1)
    2
    >>> parbaudit_punkta_koordin_trijsturim(1,1.5)
    2
    >>> parbaudit_punkta_koordin_trijsturim(2,-1)
    2
    >>> parbaudit_punkta_koordin_trijsturim(1,-1)
    2
    >>> parbaudit_punkta_koordin_trijsturim(1,0)
    1
    >>> parbaudit_punkta_koordin_trijsturim(0.5,2)
    1
    >>> parbaudit_punkta_koordin_trijsturim(2,-0.5)
    1
    >>> parbaudit_punkta_koordin_trijsturim(0.5,0.5)
    1
    >>> parbaudit_punkta_koordin_trijsturim(1.5,0.5)
    1
    >>> parbaudit_punkta_koordin_trijsturim(2,1)
    3
    >>> parbaudit_punkta_koordin_trijsturim(-2,1)
    3
    >>> parbaudit_punkta_koordin_trijsturim(0,4)
    3
    >>> parbaudit_punkta_koordin_trijsturim(0,-2)
    3
    >>> parbaudit_punkta_koordin_trijsturim(2.5,1.5)
    3
    >>> parbaudit_punkta_koordin_trijsturim(1,-2)
    3

    """
    if punkta_x>=0 and punkta_y>=-1 and punkta_y<=-1.5*punkta_x+3:
        if punkta_x==0 or punkta_y ==-1 or punkta_y==-1.5*punkta_x+3:
            return 2
        else:
            return 1
    else:
        return 3 

doctest.testmod(verbose=True) 

lietotaja_x = float(input("Ievadiet punkta x: "))
lietotaja_y = float(input("Ievadiet punkta y: "))

if parbaudit_punkta_koordin_trijsturim(lietotaja_x , lietotaja_y) == 2:
    print("Atrodas uz robežlinijā")
elif parbaudit_punkta_koordin_trijsturim(lietotaja_x, lietotaja_y) == 1: 
    print("Atrodas iekšā figurā")
else:
    print("Atrodas arpus figurā")
