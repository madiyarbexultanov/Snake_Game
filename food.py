from turtle import Turtle
import random

#Inheriting from Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)