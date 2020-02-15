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


    print("code:" + str(lijst_code))
    print("gok:"+ str(lijst_gok) )
    print(feedback_lijst)




feedback(keuzes_invullen("3456"), code_genereren())


