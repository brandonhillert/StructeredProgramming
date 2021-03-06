"""
Opdracht 12 - FizzBuzz
Schrijf een programma dat de getallen 1 tot 100 print, maar print voor veelvouden van drie “fizz” in plaats van het getal en voor veelvouden van vijf print “buzz” in plaats van
het getal. Getallen die zowel veelvoud zijn van drie als van vijf worden afgedrukt als “fizzbuzz”

Het FizzBuzz-probleem was een tijdje populair bij sollicitatiegesprekken voor programmeurs.
Het probleem kan op verschillende manieren opgelost worden (ook afhankelijk van de programmeertaal) en
de verschillende uitwerkingen hebben andere voor- en nadelen die interessant zijn om te
bespreken tijdens een sollicitatiegesprek.

"""

getal = 0

for i in range(101):

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else: print(i)



