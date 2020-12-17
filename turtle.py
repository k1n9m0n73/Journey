from turtle import Turtlescreen, Turtle


king_turtle = Turtle()
screen = screen()

king_turtle.speed(5)

def shape():
  king_turtle.forward(200)
  king_turtle.right(45)
  king_turtle.forward(100)
  king_turtle.right(135)
  king_turtle.forward(100)
  king_turtle.right(90)
  king_turtle.forward(100)

def shape1():
	king_turtle.backward(100)
	king_turtle.left(90)

"""square()
king_turtle.forward(200)
square()"""

elephant_weight = 2300
ant_weight = 0.5

#if elephant_weight  > ant_weight:
	#square()
#else:
	#square()
	#king_turtle.forward(200)
	#square()

#chris = "happy"
#while chris == "happy":
	#king_turtle.forward(1)

for count in range(4):
	shape()
	shape1()