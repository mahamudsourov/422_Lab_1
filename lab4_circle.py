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
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)#konokichur color set (RGB)
    #call the draw methods here

    x = 250
    y = 250
    radius = 150

    MidpointCircle(radius, x, y)

    MidpointCircle(75, 325, 250)
    MidpointCircle(75, 250, 325)
    MidpointCircle(75, 175, 250)
    MidpointCircle(75, 250, 175)
    MidpointCircle(75, 303, 303)
    MidpointCircle(75, 198, 303)
    MidpointCircle(75, 198,198)
    MidpointCircle(75,303,198)
    MidpointCircle(75,400,250)
    MidpointCircle(75,250,400)
    MidpointCircle(75,100, 250)
    MidpointCircle(75,250,100)
    MidpointCircle(75, 144, 144)
    MidpointCircle(75, 356,144)
    MidpointCircle(75,144,356)
    MidpointCircle(75,356,356)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Two Circles (Midpoint Circle Algorithm) - OpenGL")
glutDisplayFunc(showScreen)
glutMainLoop()