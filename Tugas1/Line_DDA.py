from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 
    
def plotLine(x1,y1,x2,y2):
    
    deltaX = x2-x1
    deltaY = y2-y1

    steps = 0
    if(abs(deltaX)>abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)

    Xincrement = deltaX/steps
    Yincrement = deltaY/steps

    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,0.0,0.0) 
    glPointSize(10.0) 
    glBegin(GL_POINTS)

    for step in range(1,steps+1): 
        glVertex2f(round(x1),round(y1))
        x1 = x1 + Xincrement 
        y1 = y1 + Yincrement 
    
    glEnd()
    glFlush()
        
os.system('cls')
os.system('clear')
def main():
    # Ask for choice
    choice = 0
    while (choice != 2):
        choice = input("Please Choose \n\t1. Plot a New line\n\t2. Exit\n")
        if int(choice) == 1:
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("DDA")
            glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2)) 
            glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))
            init()
            glutMainLoop()
        elif int(choice) == 2:
            sys.exit()
        else: 
            print("Invalid choice")
            choice = 0
main()