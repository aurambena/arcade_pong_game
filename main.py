"""This script is a arcade game called PONG, it is made for two players, each player is 
represented by a pallet and the goal is avoid that the ball pass trought your horizontal
side, if the ball pass trought your side you lost one point, the game is set to play 5 
rounds, the game ends when one of the players has 0 points"""

#import standar modules
import turtle

#import other modules
import player_1
import player_2
import ball

#called to the subclass of Turtle.Screen
screen = turtle.Screen()

# --- To player 1 --
#create an instance of player 1 move
move_player1 = player_1.MovePlayer1()
#enable movement of player 1, calling the left and right movement method
move_player1.go_backward()
move_player1.go_forward()
#lift the pen, so the move is no drawed
player_1.penup()
#turtle.onkey method allows to use the keyboard, in this case, player 1 use
#the arrows left and right
screen.onkey(move_player1.go_backward, "Left")
screen.onkey(move_player1.go_forward, 'Right')
#Set focus on TurtleScreen (in order to collect key-events)
screen.listen()

# --- To player 2 ---
#create an instance of player 2 move
move_player2 = player_2.MovePlayer2()
#enable movement of player 2, calling the left and right movement method
move_player2.go_backward()
move_player2.go_forward()
#lift the pen, so the move is no drawed
player_2.penup()
#turtle.onkey method allows to use the keyboard, in this case, player 2 use
#the keys 's' and 'f'
screen.onkey(move_player2.go_backward, "s")
screen.onkey(move_player2.go_forward, 'f')
#Set focus on TurtleScreen (in order to collect key-events)
screen.listen()

# --- To the ball ---
#create an instance to move ball
move_ball = ball.MoveBall()
#enable movement of the ball, calling the moving_ball method
move_ball.moving_ball()
#enable detection of collision between the ball and the pallets,
#calling the collision method
move_ball.collision()

#Starts event loop - calling Tkinter’s mainloop function, to keep the screen open
screen.mainloop()
