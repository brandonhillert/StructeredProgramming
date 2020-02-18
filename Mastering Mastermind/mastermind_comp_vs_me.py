import itertools
import random

"""Deze functie retouneert een lijst met alle mogelijke combinaties van abcdef"""
"""https://stackoverflow.com/questions/45990454/generating-all-possible-combinations-of-characters-in-a-string"""
def lijst_combinaties():
    lijst = []

    for x in itertools.product(*(['abcdef'] * 4)):
        lijst.append(''.join(x))

    return lijst


"""Deze functie vraagt de gebruiker om een code in te voeren en checkt de code op invoer"""
def code_invullen():
    code = " "

    print("Vul een code in: ")
    code = input()

    for i in code:
        if i not in "abcdef" or len(code) != 4:
            print("Foutmelding")
            print("Vul een code in")
            code = input()
    return code


"""Deze functie genereert een random combinatie uit de lijst
https://pynative.com/python-random-choice/"""
def random_combinatie_computer(lijst):
    return random.choice(lijst)


"""" Hier zou ik nog een if/else/while/for loop kunnen maken die de input controleert":
Als zwartpinnen is 0, moet witte pinnen 0 tm 4 zijn
Als zwartepinnen is 1, moeten witte pinnen 0 tm 3 zijn
Als zwartepinnen is 2 moeten witte pinnen 0 tm 2 zijn
Als zwartepinnen is 3, moeten witte pinnen 0 tm 1 zijn
Als zwartepinnen is 4, moeten wittte pinnen 0 zijn
"""
def feedback_geven_mens():
    feedback = []

    print("Geef aantal zwarten pinnen: ")
    zwarten_pinnen = int(input())

    print("Geef aantal witte pinnen: ")
    witte_pinnen = int(input())

    feedback.append(zwarten_pinnen)
    feedback.append(witte_pinnen)

    return feedback


"""De computer vergelijkt gok met de code
    De mens geeft feedback
    De computer analyseert de feedback die is gegeven, en keert een lijst met waardes terug 
waarbij alle mogelijkheden die 100% niet kunnen, zijn verwijderd uit de lijst
 """
""""Computer krijgt lijst[feedback]
    computer vergelijkt gok met lijst
    Computer moet lijst maken met feedback [0,0] [2,1] etc
    Computer moeten zoeken naar lijst met dezelfde feedback die gegeven is
"""


def feedback_analyseren_comp():
    gok_computer = random_combinatie_computer(lijst_combinaties())
    lijst = lijst_combinaties()
    lijst_feedback = []

    #feedback_mens = feedback_geven_mens() #Moet gelijk zijn aan de feedback van de computer in lijst per combinatie
    #Iedere combinatie in de lijst door

    for combinatie in lijst:
        a = 0
        b = 0
        index = 0

        for letter in combinatie:
            if letter == gok_computer[index]:
                a += 1
                b -= 1
            if letter in gok_computer:
                b += 1
            index += 1

        feedback_per_combinatie = [a, b]
        lijst_feedback.append(feedback_per_combinatie)


    for i in lijst_feedback:
        print(i)
    print(len(lijst_feedback))






feedback_analyseren_comp()






















