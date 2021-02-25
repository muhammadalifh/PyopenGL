from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 

def drawPixel(x,y):
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush() 

def drawCircle (xc, yc, x, y):
    drawPixel(xc+x, yc+y)
    drawPixel(xc-x, yc+y)
    drawPixel(xc+x, yc-y)
    drawPixel(xc-x, yc-y)
    drawPixel(xc+y, yc+x)
    drawPixel(xc-y, yc+x)
    drawPixel(xc+y, yc-x)
    drawPixel(xc-y, yc-x)

def circleBres (xc, yc, r):
    x = 0 
    y = r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1 
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y)


os.system('cls')
def main():
    choice = 0
    while (choice != 2):
        choice = input("Please Choose \n\t1. Plot a new Circle\n\t2. Exit\n\t\n")
        if int(choice) == 1:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Circle using Bressenham Circle Drawing Algorithm")
            glutDisplayFunc(lambda: circleBres(x,y,r)) 
            glutIdleFunc(lambda: circleBres(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 2:
            sys.exit()
        else: 
            print("Invalid choice")
            choice = 0
main()
