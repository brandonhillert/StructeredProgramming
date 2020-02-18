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

x = feedback_geven_mens()


"""De computer analyseert de feedback die is gegeven, """

def feedback_analyseren_comp(x):

























