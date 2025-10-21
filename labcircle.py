from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MidpointCircle(r, x0, y0):
    x = 0
    y = r
    d = 1 - r 

    Circlepoints(x, y, x0, y0)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        Circlepoints(x, y, x0, y0)

def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)#konokichur color set (RGB)
    #call the draw methods here

    x = 250
    y = 250
    x1 = 250 + 75
    y1 = 250
    x2 = 250 
    y2 = 250 + 75
    x3 = 250 - 75
    y3 = 250
    x4 = 250 
    y4 = 250 - 75

    x5 = 250 + 52
    y5 = 250 + 52

    x6 = 250 - 52
    y6 = 250 + 52
    
    x7 = 250 - 52 
    y7 = 250 - 52
    x8 = 250 + 52 
    y8 = 250 - 52

    MidpointCircle(150, x, y)

    MidpointCircle(75, x1, y1)
    MidpointCircle(75, x2, y2)
    MidpointCircle(75, x3, y3)
    MidpointCircle(75, x4, y4)
    MidpointCircle(75, x5, y5)
    MidpointCircle(75, x6, y6)
    MidpointCircle(75, x7, y7)
    MidpointCircle(75, x8, y8)
    

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Two Circles (Midpoint Circle Algorithm) - OpenGL")
glutDisplayFunc(showScreen)
glutMainLoop()