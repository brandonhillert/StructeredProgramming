import itertools
import random

def code_invullen():
    code = " "

    print("Vul een code in: ")
    code = input()

    for i in code:
        if i not in "abcdef" or len(code) != 4:
            print("Foutmelding")
            print("Vul een code in")
            code = input()
    return list(code)


def feedback_geven_mens():
    feedback = []

    print("Geef aantal zwarten pinnen: ")
    zwarten_pinnen = int(input())

    print("Geef aantal witte pinnen: ")
    witte_pinnen = int(input())

    feedback.append(zwarten_pinnen)
    feedback.append(witte_pinnen)

    return feedback


def gok():
    letters_antwoord = ""

    for letter in "abcdef":
        print(letter * 4)
        mogelijke_feedback = [[1, 0], [2, 0], [3, 0], [4, 0]]
        feedback = feedback_geven_mens()

        if feedback == [1, 0]:
            letters_antwoord += letter

        if feedback == [2, 0]:
            for i in range(2):
                letters_antwoord += letter


        if feedback == [3, 0]:
            for i in range(3):
                letters_antwoord += letter


        if feedback == [4, 0]:
            for i in range(4):
                letters_antwoord += letter


    return letters_antwoord


"""Deze functie retouneert een lijst met alle mogelijke combinaties van abcdef"""
"""https://stackoverflow.com/questions/45990454/generating-all-possible-combinations-of-characters-in-a-string"""
def lijst_combinaties(gok):
    lijst = []

    for x in itertools.product(*([gok] * 4)):
        lijst.append(''.join(x))

    return lijst



code_invullen()
print(lijst_combinaties(gok()))


