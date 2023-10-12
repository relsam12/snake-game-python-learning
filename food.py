from turtle import Turtle
import random


class Food(Turtle):
    """class untuk membuat food yang menjadi objektif dari snake untuk di makan"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
