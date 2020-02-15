import random


def code_genereren():
    code = []

    for nummer in range(4):
        code.append(random.randint(0, 9))
    return code



"""Deze functie controleert of de gok van de gebruiker voloet aan de eisen:
    1. De gok moet bestaan uit 4 karakters
    2. Iedere karakter moet een getal zijn
"""
def keuzes_invullen(gok):
    gok_lijst = []

    while len(gok) != 4 or not gok.isdigit():
        print("Code is ongeldig!")
        print('Geef 4 getallen: ')
        gok = input()

    for nummer in gok:
        gok_lijst.append(nummer)

    return gok_lijst






def feedback():
    print("hello")


code_genereren()