
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.tracer(0)

out_of_screen = 360
is_game_over = False
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while not is_game_over:
    screen.update()
    time.sleep(1)
    snake.move_snake()


#     Food and snake
    if snake.head.distance(food) < 10:
        food.new_location()
        snake.add_tail()
        score.update_scoreboard()

#     Detect collision with the wall
    condition1 = snake.head.xcor() > 280 or snake.head.xcor() < -280
    condition2 = snake.head.ycor() > 280 or snake.head.ycor() < -280
    if condition1 or condition2:
        is_game_over = True
        score.game_over()

#     Detect collision with the tail.
    for segment in snake.segment:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            is_game_over = True
            score.game_over()


screen.exitonclick()
