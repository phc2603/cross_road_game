from turtle import Turtle


class Tartaruga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def cima(self):
        self.forward(10)

    def baixo(self):
        self.backward(10)
