import turtle
import winsound  #to use sound in windows
#turtle need not be installed seperately
window=turtle.Screen()
window.title("PongGame")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1,stretch_wid=7)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1,stretch_wid=7)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("Courier",24,"normal"))

#score
scoreA=0
scoreB=0


#function
def paddle_a_up():
	y=paddle_a.ycor()
	y+=25
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=25
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=25
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=25
	paddle_b.sety(y)



#keyboard input
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")




#main game loop
while True:
	window.update()
	

	#ball movement
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	#border checking
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy*=-1	
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx*=-1
		scoreA +=10
		pen.clear()
		pen.write("Player A:{}  Player B:{}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))
		
		
	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx*=-1
		scoreB+=10
		pen.clear()
		pen.write("Player A:{}  Player B:{}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))
		

	#stricking te paddle
	if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
		ball.setx(340)
		ball.dx*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
	if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
		ball.setx(-340)
		ball.dx*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
	#if(ball.xcor()>350):
		#scoreA=scoreA+10
	#if(ball.xcor()<-350):
		#scoreB=scoreB+10