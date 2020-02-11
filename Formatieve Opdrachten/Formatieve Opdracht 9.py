""""
Opdracht 9 - Cyclisch verschuiven
Schrijf een functie met twee parameters. De eerste parameter, ch, is een character. De tweede parameter, n, geeft aan hoeveel posities de bitjes van ch opgeschoven moeten
worden. Als n > 0 is dan worden de bitjes naar links geschoven. Als n < 0 is dan worden de bitjes naar rechts geschoven. De bitjes die wegvallen worden aan de andere kant van
de byte weer teruggeplaatst.
Voorbeeld 1: ch met bitwaarde 1011000 en n is gelijk aan 3 resulteert in een ch met de bitwaarde: 1000101.
Voorbeeld 2: ch met bitwaarde 1011100 en n is gelijk aan -4 resulteert in een ch met de bitwaarde: 1100101."""


def verschuiving_links(ch, n):

    lijst_nummers = []
    nieuwe_lijst = []

    for char in ch:
        lijst_nummers.append(char)

    counter = 0

    for x in range(counter, n):
        nieuwe_lijst.append(ch[x])
        lijst_nummers.remove(ch[x])

    for char in nieuwe_lijst:
        lijst_nummers.append(char)

    return lijst_nummers





def verschuiving_rechts(ch, n):

    lijst_nummers = []
    nieuwe_lijst = []

    for char in ch:
        lijst_nummers.append(char)

    counter = 0

    for x in range(counter, n):
        nieuwe_lijst.append(ch[x])
        lijst_nummers.remove(ch[x])

    for char in nieuwe_lijst:
        lijst_nummers.append(char)

    return lijst_nummers



print(verschuiving_links("1011000", 3))
