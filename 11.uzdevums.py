"""
Programma pārbauda punkta  koordinātes figurai, trapecei, ar x = -3 un x = -2.5 un x = 4 un x = 8.2, y = 2 un y = 8.
"""

import doctest
def parbaudit_punkta_koordin_trapecei(punkta_x, punkta_y: float )->int:

    """
    Funkcija pārbauda figuru, trapece, ar x = -3 un x = -2.5 un x = 4 un x = 8.2, y = 2 un y = 8. 
    Funkcija paņem 2 parametrus punkta koordinātes x un y :
    punkta_x un punkta_y.
    Funkcija atgriež atbildes:
    1 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas iekšā trapeci.
    2 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas uz trapeces robežlīnijas.
    3 ja punkts ar koordinatām(punkta_x, punkta_y) atrodas ārpus trapeci.

    >>> parbaudit_punkta_koordin_trapecei(-3,2)
    2
    >>> parbaudit_punkta_koordin_trapecei(-2.5,8)
    2
    >>> parbaudit_punkta_koordin_trapecei(4,8)
    2
    >>> parbaudit_punkta_koordin_trapecei(8.2,2)
    2
    >>> parbaudit_punkta_koordin_trapecei(3,2)
    2
    >>> parbaudit_punkta_koordin_trapecei(1,8)
    2
    >>> parbaudit_punkta_koordin_trapecei(-2.5,5)
    1
    >>> parbaudit_punkta_koordin_trapecei(6,5.27)
    3
    >>> parbaudit_punkta_koordin_trapecei(2,3)
    1
    >>> parbaudit_punkta_koordin_trapecei(-1,7)
    1
    >>> parbaudit_punkta_koordin_trapecei(0,6)
    1
    >>> parbaudit_punkta_koordin_trapecei(5,6)
    1
    >>> parbaudit_punkta_koordin_trapecei(7,2.5)
    1
    >>> parbaudit_punkta_koordin_trapecei(-2,4)
    1
    >>> parbaudit_punkta_koordin_trapecei(1,1)
    3
    >>> parbaudit_punkta_koordin_trapecei(-4,5)
    3
    >>> parbaudit_punkta_koordin_trapecei(8.2,8)
    3
    >>> parbaudit_punkta_koordin_trapecei(2,8.5)
    3
    >>> parbaudit_punkta_koordin_trapecei(6,6)
    3
    >>> parbaudit_punkta_koordin_trapecei(3,1.9)
    3

    """
    if round(6*punkta_x + 4.3*punkta_y-58.4,2)<=0 and round(6*punkta_x-1.1*punkta_y+26.2,2)>=0 and -4<=punkta_x<=8.3 and 2<=punkta_y<=8:
        if  round(6*punkta_x + 4.3*punkta_y-58.4,2)==0 or round(6*punkta_x-1.1*punkta_y+26.2,2)==0 or punkta_y==8 or punkta_y==2 and-4<=punkta_x<=8.3 :
            return 2 
        else:    
            return 1
    else:
        return 3 

doctest.testmod(verbose= True)

lietotaja_x = float(input("Ievadiet punkta x koordinātas: "))
lietotaja_y = float(input("Ievadiet punkta y koordinātas: "))

if parbaudit_punkta_koordin_trapecei(lietotaja_x, lietotaja_y) == 1:
    print("Punkts atrodas iekšā figūras.")
elif parbaudit_punkta_koordin_trapecei(lietotaja_x, lietotaja_y) == 2:
    print("Punkts atrodas figūras robežlīnija.")
else:
    print("Punkts atrodas figūras ārpusē.")












    
