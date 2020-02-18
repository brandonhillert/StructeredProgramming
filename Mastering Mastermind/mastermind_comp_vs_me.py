import itertools

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


def feedback():
