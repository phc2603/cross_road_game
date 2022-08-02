import turtle
from turtle import Turtle
import random
from tartaruga import Tartaruga
turtle.colormode(255)


class Blocos:
    def __init__(self):
        self.velocidade = 5
        self.lista_blocos = []
        self.criacao_bloco()

    def criacao_bloco(self):
        deve_criar_ou_nao = random.randint(1, 6) #isso serve para evitar que hajam muitos blocos na tela
        if deve_criar_ou_nao == 6:
            bloco = Turtle()
            bloco.shape("square")
            bloco.shapesize(stretch_wid=1, stretch_len=2)
            bloco.penup()
            r = random.randint(0, 254)
            g = random.randint(0, 254)
            b = random.randint(0, 254)
            bloco.color((r, g, b))
            bloco.setheading(180)
            cord_aleatoria_y = random.randint(-245, 270)
            bloco.goto(380, cord_aleatoria_y)
            self.lista_blocos.append(bloco)

    def movendo_bloco(self, tart):
        for bloco in self.lista_blocos:
            bloco.forward(self.velocidade)
            if tart.distance(bloco) < 20:
                return True

    def mudando_fase(self):
        for bloco in self.lista_blocos:
            bloco.goto(500, 500)
        self.lista_blocos.clear()
        self.velocidade *= 1.1

