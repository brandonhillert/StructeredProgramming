import itertools
import random


"""Deze functie genereert een random combinatie uit de lijst
https://pynative.com/python-random-choice/"""
def random_combinatie_computer(lijst):
    return random.choice(lijst)

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


""" Deze functie krijgt 2 waardes die worden meegegeven:
1. De random waarde die wordt gekozen door de computer in een lijst = de gok 
2. De lijst met nog alle combinaties die mogelijk zijn

De functie gaat de lijst door met alle combinaties die mogelijk zijn. Hij vergelijkt de combinatie in die lijst met de gok van de computer.
Ieder getal krijgt hiervoor een bepaalde feedback. Deze lijst kan vervolgens in een andere functie worden gebruikt, om de feedback met de code te vergelijken met de feedback van de gok. 

"""
def feedback_analyseren_comp(gok_computer , lijst ):
    lijst_feedback = []

    for combinatie in lijst:
        zwarte_pinnen = 0
        witte_pinnen = 0

        #stopt de waardes in een lijst, zodat deze bewerkt kan worden
        combinatie_in_lijst = list(combinatie)
        gok_in_lijst = list(gok_computer)

        for i in range(len(combinatie_in_lijst)):
            if combinatie_in_lijst[i] == gok_in_lijst[i]:
                zwarte_pinnen += 1
                combinatie_in_lijst[i] = 0
                gok_in_lijst[i] = 1

            if combinatie_in_lijst[i] in gok_in_lijst:
                witte_pinnen += 1
                combinatie_in_lijst[i] = 0
                gok_in_lijst[i] = 1

        feedback_per_combinatie = [zwarte_pinnen, witte_pinnen]
        lijst_feedback.append(feedback_per_combinatie)

    return lijst_feedback






"""" Vergelijk de feeedback ( feedback_geven_mens) met de lijst die alle feedback van de gok heeft
       Alle elementen in die lijst, die niet gelijk staan aan de feedback verwijderen
       Ook alle combinaties in lijst_combinaties verwijderen met dezelfde index als de feedback"""

def feedback_verwijderen_lijst(feedback, lijst_combinaties, lijst_feedback ):
    nieuwe_lijst_feedback = []
    lijst_mogelijke_combinaties = []

    index = 0

    for i in lijst_feedback:
        if i == feedback:
            nieuwe_lijst_feedback.append(i)
            lijst_mogelijke_combinaties.append(lijst_combinaties[index])
        index += 1

    return lijst_mogelijke_combinaties





















def hoofd_programma():

    #Lijst met alle mogelijke combinaties
    lijst = lijst_combinaties()

    #Code invullen
    code = code_invullen()

    for i in range(10):
        #computer doet een random gok
        gok_computer = random_combinatie_computer(lijst)
        print(gok_computer)

        #Persoon geeft feedback
        feedback = feedback_geven_mens()

        #Computer vergelijkt eerst gok met alle waardes in lijst, voor feedback per combinatie
        lijst_feedback = feedback_analyseren_comp(gok_computer, lijst)

        #computer vergelijkt feedback, met feedback in lijst
        #computer haalt alle elementen die 100% niet kunne
        #computer keert een nieuwe lijst terug, waar de code in kan zitten
        lijst = feedback_verwijderen_lijst(feedback,lijst, lijst_feedback )

        print("mogelijkheden zijn:")
        print(lijst)




hoofd_programma()




















