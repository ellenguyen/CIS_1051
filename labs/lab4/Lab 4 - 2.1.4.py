#CIS1051
#Section009
#LinhNguyen

import turtle

bob = turtle.Turtle()
bob.speed(0)

def drawSquare(myTurtle, squareSize):
    for i in range(4):
        bob.forward(squareSize)
        bob.left(90)
        
def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        bob.forward(squareSize)
        
def drawGrid(myTurtle, size, squareSize):
    y = 0
    for i in range(size):
        drawRow(myTurtle, size, squareSize)
        y += squareSize
        bob.penup()
        bob.setpos(0, y)
        bob.pendown()

def drawSquareStairs(myTurtle, height, squareSize):
    y = 0
    row = height
    for i in range(height):
        drawRow(myTurtle, row, squareSize)
        row -= 1
        y += squareSize
        bob.penup()
        bob.setpos(0, y)
        bob.pendown()

drawSquareStairs(bob, 5, 50)
