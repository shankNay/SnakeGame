from turtle import Turtle

snake_coordinates = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


# creates and adds snake segments as the snake eats the food
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in snake_coordinates:
            self.grow_snake(i)

    def grow_snake(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.goto(position)
        snake.color("white")
        self.snakes.append(snake)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        # add a new snake to snakes
        self.grow_snake(self.snakes[-1].position())

    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.head.forward(move_distance)

    # actual game controls
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
