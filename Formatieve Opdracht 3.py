""""
Opdracht 3 - Lijstcheck
a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.

b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave.
"""


def count(lijst , x ):
    aantal = 0

    for getal in lijst:
        if x == getal:
            aantal += 1

    return print(aantal)

count([1,4,5,6,2,6,6,6], 6 )








