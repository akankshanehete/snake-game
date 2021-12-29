from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("light sky blue")
        self.speed("fastest")
        # creating a new object of the food class will make the food show up at a random location
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

