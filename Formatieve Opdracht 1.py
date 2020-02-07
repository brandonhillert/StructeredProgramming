"""Opdracht 1 Piramide
Samen gemaakt samen met Julian van der Geest
Opdracht 1 - PyramidePyramide.png
Schrijf een programma dat een piramide van variabele lengte afdrukt, zoals in het voorbeeld.
Druk ieder character apart af. De gebruiker geeft aan hoe groot de piramide
is. Implementeer je programma twee keer, de eerste keer met twee for loops,
en daarna met twee while loops. Maak ook versies die de pyramide
een andere kant op laten wijzen.
"""

print("Geef een grootte:")
grootte = int(input())

for x in range(grootte):
    x = x + 1
    print("*" * x)

for x in range(grootte):
    grootte = (grootte - 1)
    print("*" * grootte)


""""
Opdracht 1 piramide Do-while Loop"""

print("Geef een grootte:")
grootte = int(input())

x = 1
while x < grootte + 1:
    print('*' * x)
    x = x + 1

x = 1
while x < grootte + 1:
    print((grootte - x) * "*")
    x = x + 1

"""Opdracht 1 : piramide de andere kant op 
Samen gemaakt met Julian van Der Geest ( heb het hem uitgelegd )"""

print("Geef een grootte:")
grootte = int(input())

for x in range(grootte):
    aantalspaties = str(" " * (grootte - (x + 1)))
    aantalfiguren = str((x + 1) * "*")
    print(aantalspaties + aantalfiguren)

for x in range(grootte):
    aantalspaties = str("*" * (grootte - (x + 1)))
    aantalfiguren = str((x + 1) * " ")
    print(aantalfiguren + aantalspaties)



""""
Opdracht 1 piramide Do-while Loop"""

print("Geef een grootte:")
grootte = int(input())

x = 1
while x < grootte + 1:
    print((" " * (grootte - x)) + ('*' * x))
    x = x + 1

x = 1
while x < grootte + 1:
    print((' ' * x) + ("*" * (grootte - x)))
    x = x + 1













