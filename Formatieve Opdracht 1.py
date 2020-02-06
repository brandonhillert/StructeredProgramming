"""Opdracht 1 Piramide
Samen gemaakt samen met Julian van der Geest
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













