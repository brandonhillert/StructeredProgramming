""""
Opdracht 3 - Lijstcheck
a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.
"""
def count(lijst , x):
    aantal = 0

    for getal in lijst:
        if x == getal:
            aantal += 1

    return aantal

#count([1,4,5,6,2,6,6,6], 6 )

""""
b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.
"""
def grootste_verschil(lijst):

    counter = 1
    index = 0
    lege_lijst = []

    while counter < len(lijst):
        lege_lijst.append(abs(lijst[index + 1]))
        counter += 1
        index += 1
        print(lege_lijst)

grootste_verschil([1,1,4,4,5,6,7])






""""c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave."""

def lijst_nullen_enen(lijst):

    boolean = False

    for getal in lijst:
        if getal !=  1 and getal != 0:
            boolean = False
            break
        else: boolean = True


    aantal_enen = count(lijst, 1)
    aantal_nullen = count(lijst, 0)


    if aantal_enen <= aantal_nullen:
        boolean = False

    elif aantal_nullen > 12:
        boolean = False

    return boolean

lijst = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]





















