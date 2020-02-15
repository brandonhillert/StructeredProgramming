import random

"""Deze functie creeërt een code die voldoet aan de volgende eisen:
    1. De code bestaat uit 4 getallen
    2. De code moet een willekeurig getal zijn, die een waarde heeft tussen 0000 en 9999
"""

def code_genereren():
    code = []
    for nummer in range(4):
        code.append(str(random.randint(0, 9)))
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

"""Deze functie controleert of de gok van de gebruiker overeenkomt met de gegenereerde code
    De code moet x teruggeven als het getal er in zit
    De code moet Y teruggeven als het getal op de goede plek zit
    de code print " " als er niks aan de hand is
"""
def feedback( lijst_gok, lijst_code):

    feedback_lijst = []
    index = 0

    for nummer in lijst_gok:
        if nummer in lijst_code:
            if nummer == lijst_code[index]:
                feedback_lijst.append("Y")
            else:
                feedback_lijst.append("x")
        else:
            feedback_lijst.append(" ")

        index += 1

    return feedback_lijst

"""Algemene code om progamma te runnen"""
def spelen_tegen_computer():
    code = code_genereren()


    print("Welkom bij Mastermind")
    print("De code is gezet, het is aan jouw om de code te kraken!")
    print("Na iedere poging zal de computer jouw feedback geven, door deze feedback kun jij kijken of je steeds dichter bij de code komt")
    print("De X geeft aan dat de nummer in de code zit")
    print("De Y geeft aan dat de nummer op de juiste plek zit")
    print("Veel succes met spelen!")

    for i in range(10):
        print("Poging: "+ str(i +1) + "______________________________________")
        print("Doe een gok: ")
        gok = input()

        print(feedback(keuzes_invullen(gok), code))
        if keuzes_invullen(gok) == code:
            print("Gefeliciteerd, je hebt de code gekraakt")
            break

    if keuzes_invullen(gok) != code:
        print("Helaas, het is je niet gelukt om de code te kraken, de code was: ")

    print(code)
