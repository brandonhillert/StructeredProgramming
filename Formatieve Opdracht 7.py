from random import randrange

"""
Opdracht 7 - Random
Schrijf een programma dat een willekeurig getal kiest en de gebruiker net zo lang laat gokken tot dat ze het goed hebben.
"""

print("Ik heb een getal in mijn hoofd, raad jij hem? ")
print("Wat denk je dat het getal is:")
getal_gegokt = int(input())

getal_gegokt = 0

het_getal = randrange(100)

while getal_gegokt != het_getal:
    print("Helaas, dat is niet correct")
    print("Wat denk je dat het getal is:")
    getal_gegokt = int(input())

    if getal_gegokt == 999:
        print("Het antwoord is " + str(het_getal))

print("Gefeliciteerd, je hebt het getal goed gegokt")