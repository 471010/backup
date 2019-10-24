# Calculations, printing, and variables

# Printing to the screem
# The built in fumction print(), prints to the screen
# It will print both strings and numbers
print("Print to the screen...")
print("hello")
print('hello again')
print(6) # Is a number
print("6") # Is a string
print(6+6) # This creates an equation
print("6" + "6") # This puts the number together
#print("6" + 6) # This would cause an error

# Performing Calculations
# Addition +
# Subtraction -
# Multiplcation *
# Division /
# Exponents **
# Modulo %

print(4-2) # Subtraction = 2
print(4*2) # Multiplcation = 8
print(4/2) # Division = 2
print(4**2) # Exponents = 16
print("Modulo operator test...")
print(5%3)
print(10%2)
print(16%3)
# Modulo gives remainders
# Python operators follow the same order of operations as Math
print(4-2*2) # Should give zero
print((4-2)*2)

# Variables
# Variables are used to hold data
# Variables are declared and set to a value (Initializing)
badLuck = 13 # Declared a variable called badLuck and initialized it to 13
# You can print the variable using it's name
print("badLuck = " + str(badLuck)) # Cast it to a string
# Lets do another one
goodLuck = "4" # String variable
print("goodLuck = " + goodLuck) # Don't have to cast because the variable is already a string
badLuck + 5 # This is pointless
print(badLuck)
badLuck = badLuck + 5 # Now badLuck is 18
print(badLuck)

# You can also save input into variables
# Using input(), A prompt goes inside the ()
name = input("What is your name?")
print("Hello " + name)
print(name * 10) # Prints name ten times
name = name + "\n" # Escape character 
print(name * 10)
# Lets try some math
base = input("enter the base number: ")
exp = input("Enter exponent: ")
print(int(base) ** int(exp))