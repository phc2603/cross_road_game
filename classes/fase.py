from turtle import Turtle


class Fase(Turtle):
    def __init__(self):
        super().__init__()
        self.fase = 1
        self.criando_fase()

    def criando_fase(self):
        self.penup()
        self.goto(-340, 265)
        self.hideturtle()
        self.write(f"Fase: {self.fase}", align="center", font=('Calibri', 20, 'bold'))

    def alterando_fase(self):
        self.fase += 1
        self.clear()
        self.criando_fase()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=('Impact', 32, 'bold'))

