""""
Opdracht 6 - Gemiddelde berekenen
Schrijf een functie die het gemiddelde van een lijst met cijfers berekend.
Schrijf er ook een die als input een lijst van lijsten met cijfers berekend.
"""

def gem_berekenen():
    lijst = [1, 2, 3, 5, 6]
    totaal = 0

    for getal in lijst:
        totaal += getal

    gemiddelde = totaal / len(lijst)
    print(gemiddelde)

gem_berekenen()


def