'''
Clayton Walker
12/1/11
COP-3223H
turtle - program 6
Uses turtle import to draw my name and a triangle
'''

import turtle
import math

def c_letter(x, y):
    #draws the letter C
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    x+=10
    turtle.setposition(x,y)

    x-=10
    turtle.setposition(x,y)
 
    y+=20
    turtle.setposition(x,y)

    x+=10
    turtle.setposition(x,y)
    
    turtle.up()

def l_letter(x, y):
    #draws the letter L
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()

    y+=20
    turtle.setposition(x,y)

    y-=20
    turtle.setposition(x,y)

    x+=10
    turtle.setposition(x,y)
    
    
    turtle.up()

def a_letter(x, y):
    #draws the letter A
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()

    x+=5
    y+=20
    turtle.setposition(x,y)

    x+=5
    y-=20
    turtle.setposition(x,y)

    turtle.up()

    x-= 7.5
    y+= 10
    turtle.setposition(x,y)
    turtle.down()

    x+= 5
    turtle.setposition(x,y)
    
    
    turtle.up()

    
def y_letter(x, y):
    #draws the letter Y
    turtle.up()
    x+=5
    turtle.setposition(x,y)
    turtle.down()

    y+=15
    turtle.setposition(x,y)

    x-=5
    y+=5
    turtle.setposition(x,y)

    x+=5
    y-=5
    turtle.setposition(x,y)

    x+=5
    y+=5
    turtle.setposition(x,y)
    
    turtle.up()
    
def t_letter(x, y):
    #draws the letter T
    turtle.up()
    y+=20
    turtle.setposition(x,y)
    turtle.down()

    x+=10
    turtle.setposition(x,y)

    x-=5
    turtle.setposition(x,y)
    
    y-=20
    turtle.setposition(x,y)
    
    turtle.up()

    
def o_letter(x, y):
    #draws the letter O
    turtle.up()
    y+=20
    turtle.setposition(x,y)
    turtle.down()

    x+=10
    turtle.setposition(x,y)

    x-=10
    turtle.setposition(x,y)

    y-=20
    turtle.setposition(x,y)

    x+=10
    turtle.setposition(x,y)

    y+=20
    turtle.setposition(x,y)

    turtle.up()

    
def n_letter(x, y):
    #draws the letter N
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()

    y+=20
    turtle.setposition(x,y)

    x+=10
    y-=20
    turtle.setposition(x,y)

    y+=20
    turtle.setposition(x,y)


    turtle.up()

def myname():

#gives the turtle some room to write my name
    turtle.up()

#calls each letter function to draw my name
#then gives 15 space between letters after each function call
    x = -100
    y = 0
    c_letter(x, y)
    x +=15
    l_letter(x, y)
    x +=15
    a_letter(x, y)
    x +=15
    y_letter(x, y)
    x +=15
    t_letter(x, y)
    x +=15
    o_letter(x, y)
    x +=15
    n_letter(x, y)
    x +=15

def triangle():

#draws a triangle with n sides, each side with certain length,
#increasing by 10 each time drawn


#define length of each side, and # of sides to be drawn
    length = 20
    n = 8

#moves turtle up 200 pixels, and
#prepares turtle to draw triangle

    turtle.up()
    turtle.home()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.down()
    turtle.pencolor('red')
    turtle.ht()

#set up while loop to draw each side, turn, and draw another side
#that is 10 longer than last

    i = 0
    while i < n:
        turtle.forward(length)
        turtle.right(120)
        length = length + 10
        i = i + 1


def main():   

#calls myname and triangle
    myname()
    
    triangle()


main()



