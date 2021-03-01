from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

width,height = 500,500
sys.setrecursionlimit(15000)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)


def setPixel(x, y, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def boundaryFill(x, y, boundaryColor, fillColor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color != boundaryColor).any() and (color != fillColor).any():
        setPixel(x, y, fillColor)
        boundaryFill(x+1, y, boundaryColor, fillColor)
        boundaryFill(x-1, y, boundaryColor, fillColor)
        boundaryFill(x, y+1, boundaryColor, fillColor)
        boundaryFill(x, y-1, boundaryColor, fillColor)


def mouse(btn, state, x, y):
    y = 500 - y
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        fillcolor = [0, 0, 1]
        boundaryColor = [0, 1, 1]
        boundaryFill(x, y, boundaryColor, fillcolor)


def display():
    w1 = 20 + width/2
    w2 = 30 + width/2
    w3 = 50 + width/2
    w4 = 80 + width/2
    w5 = 100 + width/2
    w6 = 120 + width/2
    w7 = 20 + width/2
    h1 = 10 + height/2
    h2 = 60 + height/2
    h3 = 40 + height/2
    h4 = 80 + height/2
    h5 = 40 + height/2
    h6 = 20 + height/2
    h7 = 10 + height/2
    glLineWidth(2)
    # glPointSize(1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(w1, h1)
    glVertex2f(w2, h2)
    glVertex2f(w3, h3)
    glVertex2f(w4, h4)
    glVertex2f(w5, h5)
    glVertex2f(w6, h6)
    glVertex2f(w7, h7)
    glEnd()
    glFlush()


def main():
    os.system('cls')
    print("CLICK LEFT MOUSE BUTTON BOUNDARY FILLING IN THE DESIRED AREA.")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(500, 100)
    glutCreateWindow("Boundary Fill Algorithms")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()


main()
