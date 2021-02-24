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

def midPointCircleDraw(x_centre, y_centre, r): 
    x = r 
    y = 0  
    drawPixel(x+x_centre,y+y_centre)
    if (r > 0) : 
        drawPixel(x+x_centre,-y+y_centre)
        drawPixel(y+x_centre,x+y_centre)
        drawPixel(y+x_centre,x+y_centre)
        drawPixel(-y+x_centre,x+y_centre)
 
    P = 1 - r  
  
    while x > y: 
        y += 1
        if P <= 0:  
            P = P + 2 * y + 1
 
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y): 
            break
 
        drawPixel(x+x_centre,y+y_centre)  
        drawPixel(-x+x_centre,y+y_centre)  
        drawPixel(x+x_centre,-y+y_centre)  
        drawPixel(-x+x_centre,-y+y_centre)  

        if x != y: 
            drawPixel(y+x_centre,x+y_centre)  
            drawPixel(-y+x_centre,x+y_centre)  
            drawPixel(y+x_centre,-x+y_centre)  
            drawPixel(-y+x_centre,-x+y_centre) 

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
            glutCreateWindow("Plot Circle using Midpoint Circle Drawing Algorithm")
            glutDisplayFunc(lambda: midPointCircleDraw(x,y,r)) 
            glutIdleFunc(lambda: midPointCircleDraw(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 2:
            sys.exit()
        else: 
            print("Invalid choice")
            choice = 0
main()