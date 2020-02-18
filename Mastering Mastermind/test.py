import random
import itertools

def lijst_combinaties():
    lijst = []

    for x in itertools.product(*(['abcdef'] * 4)):
        lijst.append(''.join(x))

    return lijst

lijst = lijst_combinaties()

"""Deze functie genereert een random combinatie uit de lijst"""
def random_combinatie_computer(lijst):
    return random.choice(lijst)



print(random_combinatie_computer(lijst))