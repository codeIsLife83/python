import turtle

# # # Create a screen
# screen = turtle.Screen()
# t = turtle.Pen()
# numberOfSides = int(input("Enter number of sides: "))
# angle = 365 / numberOfSides
# t.color("purple")
# t.begin_fill()  # Start filling the shape
# for i in range(0, numberOfSides):
#     t.forward(50)
#     t.left(angle)
# t.end_fill()  # End filling the shape

# # Keep the window open until it is clicked
# screen.exitonclick()


# t = turtle.Pen()
# numberOfSides =  int(input("Enter number of sides: "))
# angle = 365 / numberOfSides
# t.color("purple")
# for i in range(0, numberOfSides):
#     t.forward(50)
#     t.left(angle)

# # for i in range(1,38):
# #     t.forward(100)
# #     t.left(175)

# # for i in range(1, 20):
# #     t.forward(100)
# #     t.left(95)


# # for i in range(1, 38):
# #     t.forward(100)
# #     t.left(175)

# turtle.done()


# # Create a screen
# screen = turtle.Screen()

# # Create two turtle objects
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# # Set different colors for each turtle
# t1.color("blue")
# t2.color("green")

# # Move the first turtle
# t1.penup()
# t1.goto(-50, -50)
# t1.pendown()

# for i in range(1, 20):
#     t1.forward(100)
#     t1.left(95)


# # Move the second turtle
# t2.penup()
# t2.goto(-50, 0)
# t2.pendown()

# for i in range(1, 38):
#     t2.forward(100)
#     t2.left(175)


# # Keep the window open until it is clicked
# screen.exitonclick()


def upperleft(side_length):
    for i in range(4):
        t.forward(side_length)
        t.left(90)


def lowerleft(side_length):
    for i in range(4):
        t.forward(side_length)
        t.right(90)


def lowerright(side_length):
    for i in range(4):
        t.backward(side_length)
        t.left(90)


def upperright(side_length):
    for i in range(4):
        t.backward(side_length)
        t.right(90)


# # Create a screen
screen = turtle.Screen()
t = turtle.Pen()

for i in range(0, 200, 10):
    upperleft(i)

for i in range(0, 200, 10):
    lowerleft(i)

for i in range(0, 200, 10):
    lowerright(i)

for i in range(0, 200, 10):
    upperright(i)

# Keep the window open until it is clicked
screen.exitonclick()
