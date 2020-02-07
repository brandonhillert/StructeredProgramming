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
    string_nummer_1 = str(input())

    print("Geef een string:")
    string_nummer_2 = str(input())

    list_string_1 = []
    list_string_2 = []

    for letter in string_nummer_1:
        list_string_1.append(letter)

    for letter in string_nummer_2:
        list_string_2.append(letter)

    if len(list_string_1) > len(list_string_2):
        list_string_1 - list_string_2
        print(list_string_1)


zoek_verschillende_waarde()