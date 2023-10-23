"""this script set the characteristics of player 1, size of the pallet, movements,
keys on the keyboard and the background of the screen"""

#import standars modules
from turtle import *
import turtle

#called to the subclass of Turtle.Screen
screen = turtle.Screen()
#create a rectangle (using the parameters) to be the pallet of player 2 
#and register the new shapescreen = turtle.Screen()
screen.register_shape("rectangle", (((0,0),(0,60),(10,60),(10,0))))
#create an instance of player 2
player2 = turtle.Turtle()
#call the method shape using the register parameter 'rectangle'
player2.shape('rectangle')
#call the method color to set the shape color
player2.color('orange')
#lift the pen, so the move is no drawed
player2.penup()
#call the method 'goto' to move the pallet to the start 
player2.goto(-200, 200)

#definition of the class MovePlayer2
class MovePlayer2:
    def __init__(self) -> None:
        pass
        
    def go_forward(self):
        """method to set the parameters to move the player's 2 pallet to the right
        with a speed set to the method turtle.speed"""
        player2.speed(100)
        player2.forward(50)
        
    def go_backward(self):
        """method to set the parameters to move the player's 2 pallet to the left
        with a speed set to the method turtle.speed"""
        player2.speed(100)
        player2.backward(50)