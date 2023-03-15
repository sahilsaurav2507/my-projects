import random


z = "r"

while z == "r":
	
	print("\n========++++++++ ROLL YOUR DICE ++++++++========\n")
	


	inputt = random.randint(1,6)
	
	if inputt == 1:
		print(" ------- ")
		print("|       |")
		print("|   *   |")
		print("|       |")
		print(" ------- ")
	if inputt == 2:
		print(" ------- ")
		print("|   *   |")
		print("|       |")
		print("|   *   |")
		print(" ------- ")
	if inputt == 3:
		print(" ------- ")
		print("|       |")
		print("| * * * |")
		print("|       |")
		print(" ------- ")
	if inputt == 4:
		print(" ------- ")
		print("| *   * |")
		print("|       |")
		print("| *   * |")
		print(" ------- ")
	if inputt == 5:
		print(" ------- ")
		print("| *   * |")
		print("|   *   |")
		print("| *   * |")
		print(" ------- ")
	if inputt == 6:
		print(" ------- ")
		print("| * * * |")
		print("|       |")
		print("| * * * |")
		print(" ------- ")
		
	z=input("\npress r to roll again and x to exit:")
	print("\n")