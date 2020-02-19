import mastermind_me_vs_comp
import mastermind_comp_vs_me

print("Welkom bij mastermind")

print("*Melding: Spelen tegen de computers is met getallen, andersom is het met letters!")
print("Maak een keuze:")
print("Typ 1 voor spelen tegen de computer")
print("Typ 2 voor computer tegen jou te laten spelen")

keuze = int(input())
if keuze == 1:
    mastermind_me_vs_comp.spelen_tegen_computer()
if keuze == 2:
    mastermind_comp_vs_me.hoofd_programma()

