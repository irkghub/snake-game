from turtle import Turtle
INITIAL_POSITIONS =[(0,0),(-20,0),(-40,0)]
DISTANCE_TO_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        body = Turtle("square")
        body.shapesize(stretch_wid=1, stretch_len=1)
        body.color("White")
        body.penup()
        body.goto(position)
        self.segment.append(body)


    def add_tail(self):
        self.add_segment(self.segment[-1].position())
    def move_snake(self):
        for segment_no in range(len(self.segment) - 1, 0, -1):
            x_value = self.segment[segment_no - 1].xcor()
            y_value = self.segment[segment_no - 1].ycor()
            new_position = x_value, y_value
            self.segment[segment_no].goto(new_position)
        self.head.forward(DISTANCE_TO_MOVE)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #     heading can be set to 270 as well
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #     heading can be set to 180 as well

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # heading can be set to 0 as well

