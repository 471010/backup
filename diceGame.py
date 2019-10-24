# Aaron Fuller
# Period 1
# Dice Roller

# Imports
import random
# Variables
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
# List
x = 1
print("Welcome to the Dice Roller")
# Main Loop
while x <= s:
	s = int(input("How many numbers would you like:"))
	print(random.randint(1,6))
	x += 1
	if s == "0":
		print("Thanks for rolling")
		break
	print("Total Rolls:"+ str(s))
	print("1s:" + str(s1))
	print("2s:" + str(s2))
	print("3s:" + str(s3))
	print("4s:" + str(s4))
	print("5s:" + str(s5))
	print("6s:" + str(s6))

	if diceRoll == "1":
		s1 += 1

	elif diceRoll == "2":
		s2 += 1

	elif diceRoll == "3":
		s3 += 1

	elif diceRoll == "4":
		s4 += 1

	elif diceRoll == "5":
		s5 += 1

	elif diceRoll == "6":
		s6 += 1
