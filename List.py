favFoods = ["Gucamole", "Steak", "Water"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# Adds to the end of the list
favFoods.append("Milk")
print(favFoods)
print("One of my favorite foods is " + favFoods[3])
# Insert adds to an indeex in a list
favFoods.insert(1, "Chinken Nuggets")
print(favFoods)
# Remove an item
favFoods.remove("Gucamole")
print(favFoods)
# Remove by index
favFoods.pop(1)
print(favFoods)

# Loop through a list
for food in favFoods:
	print(food)

numList = [3, 5, 7, 9, 11, 12, 11, 11]

# Loop through the list and add all the numbers together, then print the sum

sum = 0
for num in numList:
	sum += num


print(sum)
# Function to get the length of the list
print(len(numList))
# Make a prompt for favorite music
# Prompt for favorite movie
nyFood = input("What is your favorite food?")
favFoods.append(favFoods)
print(favFoods)

favMovies = ["The Wolverine", "Avengers", "Spider-Man 3"]
myMovie = input("What movies do you enjoy?")
favMovies.append(myMovie)
print(favMovies)
# List Methods
# append - adds to the end of a list
# insert - adds an item to a specific place in the list
# remove - takes out a specifis item in a list
# pop - removes items from a specific index
# len - returns the length of a list
