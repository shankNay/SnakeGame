from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

food_color = ['red', 'yellow', 'green', 'white']
screen = Screen()
screen.setup(600, 600)  # setting the resolution of the screen
screen.bgcolor('black')  # setting the background of the screen to black
screen.title("Snake game")  # game title

screen.tracer(0)  # to turn off animations

snake = Snake()  # snake module

scoreboard = ScoreBoard()  # scoreboard constructor

food = Food()

# game controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True # switch to turn the game on and off

while game_is_on:  # to move the snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # if the snake eats food
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:   # checks if it hits the wall
        # game_is_on = False
        scoreboard.reset()   # to reset the scoreboard
        snake.reset()    # to reset the snake position

    for snakey in snake.snakes[1:]:    # if the snake hits its tail
        if snake.head.distance(snakey) < 10:
            # game_is_on = False
            scoreboard.reset() # to reset the scoreboard
            snake.reset()  # to reset the snake position


screen.exitonclick()
