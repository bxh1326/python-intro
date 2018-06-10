import turtle
import random

numTurtles = int(turtle.numinput('race', 'How many turtles?'))
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'black', 'magenta', 'cyan', 'brown']

# Initialize an empty turtle list
turtles = []
# Create each turtle object and push them to the turtles list
for i in range(numTurtles):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(colors[i])
    t.speed(1)
    turtles.append(t)

# Position each turtle at their starting coordinates
for i in range(numTurtles):
    t = turtles[i]
    t.write(t.position)

# Set up empty winner variable
winner = ''

# Let all the turtles move 100 steps at a random pixel in each step
for j in range(100):
    for i in range(numTurtles):
       t = turtles[i]
       t.forward(random.randint(0,5))

    if winner == '':
        if t.ycor() >= 100


# Print all the turtles' final position
for i in range(numTurtles):
   t = turtles[i]
   t.write(t.position)

turtle.done()
