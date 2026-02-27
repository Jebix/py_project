from turtle import Turtle

MOVE_DISTANCE = 20
SP = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]   # keep track of the snake’s head

    def create_snake(self):
        for i in SP:
            self.addd_segment(i)
    def addd_segment(self,i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.addd_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[i - 1].xcor()
            ny = self.segments[i - 1].ycor()
            self.segments[i].goto(nx, ny)
        self.head.forward(MOVE_DISTANCE)

    # 👇 direction controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

