from turtle import *

scoreSquib = Turtle()
myScreen = scoreSquib.getscreen()
scoreSquib.penup()
scoreSquib.goto(myScreen.window_width()/2-200, myScreen.window_height()/2-50)
scoreSquib.hideturtle()
score = 0

def updatescore():
	scoreSquib.clear()
	scoreSquib.write("Score: " + str(score), False, "left", font=("Times New Roman", 20, "normal"))

updatescore()

myScreen.mainloop()