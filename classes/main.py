from turtle import Screen
from tartaruga import Tartaruga
from blocos import Blocos
from fase import Fase
import time

tela = Screen()
tela.setup(width=800, height=600)
tela.tracer(0)
tartaruga = Tartaruga()
tela.onkey(tartaruga.cima, "Up")
tela.onkey(tartaruga.baixo, "Down")
tela.listen()
blocos = Blocos()
fase = Fase()
jogando = True
tela.update()

'#spawnando, inicialmente, 50 blocos'
def spawn_inicial():
    for i in range(0, 50):
        blocos.criacao_bloco()
        blocos.movendo_bloco(tartaruga)


spawn_inicial()
while jogando:
    tela.update()
    time.sleep(0.1)
    blocos.criacao_bloco()
    colisao = blocos.movendo_bloco(tartaruga)
    if colisao:
        fase.game_over()
        jogando = False
    if tartaruga.ycor() > 285:
        fase.alterando_fase()
        blocos.mudando_fase()
        tartaruga.goto(0, -280)
        spawn_inicial()

tela.exitonclick()