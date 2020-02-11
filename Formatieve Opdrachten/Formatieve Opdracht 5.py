"""
Opdracht 5 - Sorteren
Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert.
"""

def sorteren():
    lijst_getallen = [13,2,1,4,6,6,6783]
    nieuwe_lijst = []

    while lijst_getallen != []:
        x = min(lijst_getallen)
        nieuwe_lijst.append(x)
        lijst_getallen.remove(x)

    print(nieuwe_lijst)

sorteren()