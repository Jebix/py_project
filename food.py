import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 1 , stretch_wid = 1)
        self.color("red")
        self.speed("fastest")

    def refresh (self) :
            ran_x = random.randint(-280 , 280)
            ran_y = random.randint(-280 ,280)
            self.goto(ran_x,ran_y)