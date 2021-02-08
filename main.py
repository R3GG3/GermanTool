###LIBRARIES###
from translate import translate
from perfekt import perfect
from os import name, system

###MAIN###
def main():
	if name == "nt":
		system("cls")
	else:
		system("clear")
	print("\n[[NARZEDZIE NA NIEMIECKI v0.1]]")
	print("--------------------------------")
	print("")
	print("Co chcesz zrobic?")
	print("1. Tlumaczenie")
	print("2. Forma Perfekt")
	choice = input()
	print("")
	if choice == "1":
		translate(input("Wpisz slowo po niemiecku: "))
	elif choice == "2":
		perfect(input("Wpisz wyraz: "))
	else:
		exit(0)


#Rest
while True:
	main()