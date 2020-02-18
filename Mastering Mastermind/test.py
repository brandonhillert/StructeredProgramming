import itertools

"""Deze functie retouneert een lijst met alle mogelijke combinaties van abcdef"""
"""https://stackoverflow.com/questions/45990454/generating-all-possible-combinations-of-characters-in-a-string"""
def lijst_combinaties():
    lijst = []

    for x in itertools.product(*(['abcdef'] * 4)):
        lijst.append(''.join(x))

    return lijst

lijst_combinaties()
