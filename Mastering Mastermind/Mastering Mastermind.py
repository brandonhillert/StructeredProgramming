import random




def code_genereren():
    code = []

    for nummer in range(4):
        code.append(random.randint(0, 9))

    return code



def feedback():



    print("hello")

def keuzes_invullen():
    print("hello")



code = code_genereren()
print(code)