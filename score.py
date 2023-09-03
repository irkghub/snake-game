from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0,265)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, "center",("Arial", 24, "normal"))

    def update_scoreboard(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over",False,"center",("Arial",24,"normal"))






