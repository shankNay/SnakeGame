from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())   # reads the value stored in the high_score.txt file and saves it to the self.high_score variable
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))  # initial score
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))  # updates score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as write_score:   # w mode to overwrite
                write_score.write(f"{self.high_score}")  # writes the new high_score to the high_score file (Overwritten)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):  # increases score called when the snake eats the food
        self.score += 1
        self.update_scoreboard()
