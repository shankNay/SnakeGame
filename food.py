from turtle import Turtle
import random


class Food(Turtle):     # places the food on the screen in a random location
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):       # refreshes whenever the snake eats the food
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)

