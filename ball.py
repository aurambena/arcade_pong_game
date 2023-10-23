"""This script set the characteristics of ball, size, movements, collision,
counts the number of points, print the results and announces the winner"""

#import standars modules
from turtle import *
import turtle
import time

#import other modules
import player_1 
import player_2

#called to the subclass of Turtle.Screen
screen = turtle.Screen()

# --- To the ball ---
#create an instance of ball
ball = turtle.Turtle()
#call the method shape using 'circle'
ball.shape('circle')
#call the method color to set the shape color
ball.color('white')
#lift the pen, so the move is no drawed
ball.penup()

#This is one way to replace the score showed on the screen, you create a shape that
#cover the changing number and the next number is written above this shape
#create a rectangle (using the parameters) and register the new shape
screen.register_shape("rectangle_text", (((0,0),(0,30),(30,30),(30,0))))
#create an instance of the chape
erase_score = turtle.Turtle()
#call the method shape using the register parameter 'rectangle_text'
erase_score.shape('rectangle_text')
#lift the pen, so the move is no drawed
erase_score.penup()
#call the method color to set the shape color
erase_score.color('black')

#create an instance of the score
score = turtle.Turtle()
#set the position of the score board
score.setposition(150, -250)
#call the method color to set the text color
score.color('red')

#definition of the class MoveBall
#This class inherits from player_1 and player_2
class MoveBall(player_1.MovePlayer1, player_2.MovePlayer2):
    def __init__(self) -> None:
        """Set the new attributes"""
        super().__init__()
        self.ping = True
        self.pong = False
        self.player1 = player_1.MovePlayer1()
        self.player2 = player_2.MovePlayer2()
        self.counter_player1 = 5
        self.counter_player2 = 5
        
    def moving_ball(self):
        """The ball's move is forward, but it change the angle if a collision is
        detected"""
        #the old score is erased
        erase_score.goto(237, -230)
        
        #firts condition, the ball starts moving down the board
        if self.ping == True:
            ball.right(90)
                #this bucle move the ball and call the method collision to detected a pallet
                #pounch or a point lost
            for i in range(200):
                #set the speed ball
                ball.speed(400)
                #set the forward move
                ball.fd(5)
                #reset the ping and pong parameters
                self.ping = False
                self.pong = False
                #call the method collision
                self.collision()
        
        #second condition, the ball starts moving up the board
        elif self.pong == True:
            #change the angle
            ball.right(270)
            for i in range(200):
                #set the speed
                ball.speed(400)
                #set the forward move
                ball.fd(5)
                #reset the parameters
                self.pong = False
                self.ping = False
                #call the collision method
                self.collision()
    
    def collision(self):
        """this method detect the collision with the pallets or not"""
        #condition to detect the collision with the player2's pallet
        if ball.ycor() == 200 and (player_2.player2.xcor() <= ball.xcor() <= player_2.player2.xcor()+ float(70.00)):
            self.ping = True
            #call the method moving_ball to change the ball trajectory
            self.moving_ball()
        
        #condition to detect not collision
        elif ball.ycor()  == 210:
            #this buble is counting the points to define the winner
            if self.counter_player2 != 0:
                #Countdown
                self.counter_player2 -= 1
                #print on the screen the score
                p2 = 'P1, P2',self.counter_player2, self.counter_player1
                score.write( p2, font=('Arial', 15, 'normal'))
                #send the ball to the zero point
                ball.goto(0,0)
                #time showing the score
                time.sleep(1)
                #call the method moving_ball to restart the game
                self.moving_ball()
            #this buble is counting the points to define the winner
            elif self.counter_player2 == 0:
                #lift the pen, so the move is no drawed
                score.penup()
                #set the text to position 0,0
                score.setposition(0,0)
                #set the text color
                score.color('red')
                #print the victory 
                score.write('Player 1! VICTORY', align='center',font=('Arial', 40, 'normal'))

        #condition to detect the collision with the player2's pallet
        elif ball.ycor() == -200 and (player_1.player1.xcor() <= ball.xcor() <= player_1.player1.xcor()+ float(70.00)):
            self.pong = True
            #call the method moving_ball to change the ball trajectory
            self.moving_ball()

        #condition to detect not collision
        elif ball.ycor()  == -210:
            #this buble is counting the points to define the winner
            if self.counter_player1 != 0:
                #Countdown
                self.counter_player1 -= 1
                #print on the screen the score
                p1 = 'P1, P2',self.counter_player2, self.counter_player1
                score.write(p1, font=('Arial', 15, 'normal'))
                #send the ball to the zero point
                ball.goto(0,0)
                #call the method moving_ball to restart the game
                time.sleep(1)
                #call the method moving_ball to restart the game
                self.moving_ball()
            #this buble is counting the points to define the winner
            elif self.counter_player1 == 0:
                #lift the pen, so the move is no drawed
                #set the text to position 0,0
                score.setposition(0,0)
                #set the text color
                score.color('red')
                #print the victory 
                score.write('Player 2! VICTORY', align='center',font=('Arial', 40, 'normal'))

    
        