from turtle import  Turtle , Screen

tim = Turtle()

# code 1
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.left(90)
# tim.bk(100)
# tim.left(90)
# tim.forward(100)

#code 2
# for i in range(0 , 15):
#
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# code 3
# import  random
# colours = ["red","yellow","green","blue","purple"]
# def draw (num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.fd(100)
#         tim.right(angle)

# for i in range (3,11):
#     tim.color(random.choice(colours))
#     draw(i)

# heart
from turtle import  *
bgcolor("black")
color("red")
begin_fill()
pensize(4)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

# random colour
# import  random
# colours = ["red","yellow","green","blue","purple"]
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# import  random
# colours = ["red","yellow","green","blue","purple"]
# def size(user):
#     for i in range(int(360 / user)):
#         tim.speed("fastest")
#         tim.color(random.choice(colours))
#         tim.circle(100)
#         current = tim.heading()
#         tim.setheading(current +10)
#         tim.circle(100)
# size(int(input("enter the size")))
#



screen = Screen()
screen.exitonclick()
