"""
Opdracht 2 - Tekstcheck
Schrijf een functie die de eerste index teruggeeft waarop twee strings een verschillende waarde hebben.
Bedenk zelf een goede functienaam.
Het complete programma vraagt om twee strings aan de gebruiker en print de index waarop deze twee strings verschillen.
Zorg je dat de functie goed test. Let op: een string mag spaties bevatten!
"""


def zoek_verschil(string_1, string_2):

    counter = 0
    lijst_1 = []
    lijst_2 = []

    for char in string_1:
        lijst_1.append(char)

    for char in string_2:
        lijst_2.append(char)

    print(lijst_1)
    print(lijst_2)


    for letter in range(100):

        if string_1[counter] == string_2[counter]:
            print(string_1[counter] + str(" is gelijk aan ") + string_2[counter])
        else:
            print("fout op de " + str(letter + 1) + "de karakter")
            break

        counter += 1

        if counter == len(string_1):
            break



zoek_verschil("hallo", "hallow")