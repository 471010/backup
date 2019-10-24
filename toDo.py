# Aaron Fuller
# Period 1

toDo = []

print("Welcome to To Do List")

while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print your List")
	print("Enter q to quit")
	choice = input("Choose: ")

	if choice == "q":
		break

	elif choice == "a":
		toDo.append(input("What would you like to add?"))

	elif choice == "r":
		toDo.remove(input("What would you like to remove?"))

	elif choice == "p":
		print(toDo)

	elif choice == "s":
		pass

	else:
		print("You chose an invalid option.")