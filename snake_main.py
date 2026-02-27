import time
from  turtle import  Turtle ,Screen
from food import  Food
from  scoreboard import Score
from  snakebody import Snake


sc = Screen()
sc.setup(600 , 600)
sc.bgcolor("black")
sc.title("snake game")
sc.tracer(0)

segment = []
snake = Snake()
food = Food()
scoreboard = Score()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")




game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(.1)

    snake.move()

    #food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on =False
            scoreboard.game_over()

sc.exitonclick()