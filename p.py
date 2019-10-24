from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()
myTurtle.speed(1)
myTurtle.penup()
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.pensize(10)
myTurtle.pencolor("red")
myTurtle.write("Press 'p' to enter name", move=True, align="center", font=("Times New Roman", 40, "normal"))
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.forward(300)

def printname():
	name = screen.textinput("Name?", "What is your name, please?")
	myTurtle.write(name, move=True, align="left", font=("Times New Roman", 40, "normal"))
	screen.listen()
screen.onkey(printname, "p")

screen.listen()
screen.mainloop()