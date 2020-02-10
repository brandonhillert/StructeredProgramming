"""
Opdracht 2 - Tekstcheck
Schrijf een functie die de eerste index teruggeeft waarop twee strings een verschillende waarde hebben.
Bedenk zelf een goede functienaam.
Het complete programma vraagt om twee strings aan de gebruiker en print de index waarop deze twee strings verschillen.
Zorg je dat de functie goed test. Let op: een string mag spaties bevatten!
"""

#def geef_index():
def zoek_verschillende_waarde():

    print("Geef een string:")
    string_nummer_1 = input()

    print("Geef een string:")
    string_nummer_2 = input()

    list_string_1 = []
    list_string_2 = []

    for letter in string_nummer_1:
        list_string_1.append(letter)

    for letter in string_nummer_2:
        list_string_2.append(letter)

    print(list_string_1)
    print(list_string_2)

    for i in range(len(string_nummer_1)):
        if list_string_1[i] == list_string_2[i]:
            print("gelijk")
        else: print("de index waar ze ongelijk zijn is" + str(i) )





zoek_verschillende_waarde()