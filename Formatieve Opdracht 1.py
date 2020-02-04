print("Geef een grootte:")
grootte = int(input())


for x in range(grootte):
    x = x + 1
    print("lol" * x)

for x in range(grootte):
    grootte = (grootte - 1)
    print("lol" * grootte)
