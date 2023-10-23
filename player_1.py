"""this script set the characteristics of player 1, size of the pallet, movements,
keys on the keyboard and the background of the screen"""

#import standars modules
from turtle import *
import turtle

#called to the subclass of Turtle.Screen
screen = turtle.Screen()
#create a rectangle (using the parameters) to be the pallet of player 1 
#and register the new shape
screen.register_shape("rectangle", (((0,0),(0,60),(10,60),(10,0))))
#create an instance of player 1
player1 = turtle.Turtle()
#call the method shape using the register parameter 'rectangle'
player1.shape('rectangle')
#call the method color to set the shape color
player1.color('orange')
#lift the pen, so the move is no drawed
player1.penup()
#call the method 'goto' to move the pallet to the start 
player1.goto(-200, -200)

#create the background (using the parameters) 
screen.register_shape("rectangle_frame", (((-300,-350),(300,-350),(300,350),(-300,350))))
#create an instance of background
frame = turtle.Turtle()
#call the method shape using the register parameter 'rectangle_frame'
frame.shape('rectangle_frame')
#call the method color to set the shape color
frame.color('black')
#lift the pen, so the move is no drawed
frame.penup()

#definition of the class MovePlayer1
class MovePlayer1:
    def __init__(self) -> None:
        pass

    def go_forward(self):
        """method to set the parameters to move the player's 1 pallet to the right
        with a speed set to the method turtle.speed"""
        player1.speed(100)
        player1.forward(50)
                
    def go_backward(self):
        """method to set the parameters to move the player's 1 pallet to the left
        with a speed set to the method turtle.speed"""
        player1.speed(100)
        player1.backward(50)