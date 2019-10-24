

age = input("What is your age?") # Prompot for age

#Check if age is more tham 17, so the person can see R rated movies
age = int(age)
if age > 17: # Everything in the If statement only runs if the condidtion is true
	print("You can see R rated movies")

else:
	print("You cannot see an R rated movie, too bad so sad")

print("Have a nice day!")

myNum = 7
guess = input("Guessing number between 1 and 10:")
guess = int(guess)
if guess == myNum:
	print("You guessed correct!")
elif  guess > myNum:
	print("Too high")
else:
	print("Too low")
print("Thanks for playing")