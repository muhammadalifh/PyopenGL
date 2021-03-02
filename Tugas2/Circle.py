from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import os
import sys
import time

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 

def drawPixel(x,y):
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_LINE_SMOOTH)
    glVertex2i(x,y)
    glEnd()
    glFlush()


def createCircle(xc, yc, radius):
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_LINE_LOOP)
    x = xc - radius
    target = xc + radius
    glVertex2f(x, yc)
    glVertex2f(target, yc)
    factor = 7500
    incr = 1 / factor
    x += incr
    while x < target:
        adder = math.sqrt(radius * radius - (x - xc) * (x - xc))
        glVertex2f(x, yc + adder)
        glVertex2f(x, yc - adder)
        x += incr
    glEnd()
    glFlush()


os.system('cls')
def main():
    choice = 0
    while (choice != -1):
        choice = input("Please Choose \n\t1. Create Circle\n\t2. Exit\n")
        if int(choice) == 1:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Circle using Non Polar Circle")
            glutDisplayFunc(lambda: createCircle(x,y,r)) 
            glutIdleFunc(lambda: createCircle(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 2:
            sys.exit()
        else: 
            print("Invalid choice")
            time.sleep(2)
            os.system('cls')
            choice = 0

main()