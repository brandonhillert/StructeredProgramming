import random




def code_genereren():
    code = []

    for nummer in range(4):
        code.append(random.randint(0, 9))

    return code

def keuzes_invullen():

    gok_in_lijst = []

    print('Geef 4 getallen: ')
    gok = input()


"""https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float"""
    if gok.isdigit():
        for nummer in gok:
        gok_in_lijst.append(nummer)
    else:
    print('Geef 4 getallen: ')
    gok = input()




    print(gok_in_lijst)



def feedback():




    print("hello")



keuzes_invullen()