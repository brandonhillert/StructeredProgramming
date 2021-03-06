"""
Opdracht 4 - Palindroom
Schrijf een functie die checkt of een woord een palindroom is.
Schrijf een versie die gebruikt maakt van een bibliotheekfunctie die een string voor je omdraait.
Maak ook een versie waarbij jij zelf het omdraaien verzorgt. Probeer zo min mogelijk code te gebruiken.
"""


def palindroom_check(woord):
    woord_van_voren = []
    woord_achterstevoren = []

    for letter in woord:
        woord_van_voren.append(letter)
        woord_achterstevoren.append(letter)

    woord_achterstevoren.reverse()

    if woord_van_voren == woord_achterstevoren:
        print(str(woord) + " is een palindroom")
    else:
        print(str(woord) + " is geen palindroom")


palindroom_check("lepel")
palindroom_check("steellepel")

def palindroom_check_2(woord):
    woord_van_voren = []
    woord_achterstevoren = []

    for letter in woord:
        woord_van_voren.append(letter)
        woord_achterstevoren.append(letter)

    woord_achterstevoren.reverse()

    if woord_van_voren == woord_achterstevoren:
        print("Het woord is een palindroom")
    else:
        print("Geen palindroom")
