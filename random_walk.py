import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

screen.screensize(50, 50)

colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet',
           'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
           'turquoise', 'lightgreen', 'green', 'darkgreen',
           'chocolate', 'brown', 'black', 'gray']

directions = [0, 45, 135, 180, 270, 315, 360]

tim.pensize(10)
tim.speed('fastest')

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(directions))
