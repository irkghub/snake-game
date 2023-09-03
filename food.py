from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("cyan")
        self.speed("fastest")
        val_x = random.randint(-280,280)
        val_y = random.randint(-280,280)
        position = val_x,val_y
        self.goto(position)
        self.new_location()

    def new_location(self):
        val_x = random.randint(-280, 280)
        val_y = random.randint(-280, 280)
        position = val_x, val_y
        self.goto(position)


