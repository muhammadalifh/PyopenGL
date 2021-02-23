from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 
    

def plotLine(x1,y1,x2,y2):
    # Bresenham Algo
    m = 2 * (y2 - y1)
    pk = m - (x2 - x1)
    y = y1 

    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,0.0,0.0) 
    glPointSize(10.0) 
    glBegin(GL_POINTS)

    for x in range(x1,x2+1):
        glVertex2f(x,y)
        pk = pk + m
        if (pk >= 0):
            y = y+1
            pk = pk - 2 * (x2 - x1)
    glEnd() 
    glFlush()

os.system('clear')
os.system('cls')
def main():
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
            glutCreateWindow("Bresenham Algorithm")
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