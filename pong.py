import turtle
import time

tela = turtle.Screen()
tela.title('Jogo Pong B2')
tela.bgcolor('black')
tela.setup(width=800, height=600)
tela.tracer(0)

#placar
ponto1 = 0
ponto2 = 0

#elementos dos jogos
jogador1 = turtle.Turtle()
jogador1.speed(0)
jogador1.shape("square")
jogador1.color("white")
jogador1.shapesize(stretch_wid=5, stretch_len=1)
jogador1.penup()
jogador1.goto(-350,0)

jogador2 = turtle.Turtle()
jogador2.speed(speed=None)
jogador2.shape("square")
jogador2.color("white")
jogador2.shapesize(stretch_wid=5, stretch_len=1)
jogador2.penup()
jogador2.goto(350,0)

bola= turtle.Turtle()
bola.speed(0.1)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 2
bola.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jogador 1: 0      Jogador 2: 0", align="center", font=("Courier", 24, "normal") )

#movimentação
def jogador1_up():
    y = jogador1.ycor()
    y +=20
    jogador1.sety(y)
    
def jogador1_down():
    y = jogador1.ycor()
    y -=20
    jogador1.sety(y)
    
def jogador2_up():
    y = jogador2.ycor()
    y +=20
    jogador2.sety(y)
    
def jogador2_down():
    y = jogador2.ycor()
    y -=20
    jogador2.sety(y)

tela.listen()
tela.onkeypress(jogador1_up, "w")
tela.onkeypress(jogador1_down, "s")
tela.onkeypress(jogador2_up, "Up")
tela.onkeypress(jogador2_down, "Down")

#main loop
while True:
    time.sleep(1/120)
    tela.update()
    
    #movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    
    #ao bater na borda a bola muda de direção
    if bola.ycor() >290:
        bola.sety(290)
        bola.dy *=-1
        
    elif bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *=-1
     
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *=-1
        ponto1 += 1
        pen.clear()
        pen.write("Jogador 1: {}      Jogador 2: {}".format(ponto1, ponto2), align="center", font=("Courier", 24, "normal") )
        
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *=-1
        ponto2 +=1
        pen.clear()
        pen.write("Jogador 1: {}      Jogador 2: {}".format(ponto1, ponto2), align="center", font=("Courier", 24, "normal") )
        
    if bola.xcor() < -340 and bola.ycor() < jogador1.ycor() + 50 and bola.ycor() > jogador1.ycor() - 50:
        bola.dx *= -1

    if bola.xcor() > 340 and bola.ycor() < jogador2.ycor() + 50 and bola.ycor() > jogador2.ycor() - 50:
        bola.dx *= -1