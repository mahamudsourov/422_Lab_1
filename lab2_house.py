from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

edges = [
    (250, 350, 150, 250),
    (250, 350, 350, 250),
    (250, 350, 450, 350),
    (350, 250, 550, 250),
    (450, 350, 550, 250),
    (260, 340, 170, 250),
    (150, 250, 170, 250),
    (525, 175, 525, 250),
    (350, 250, 350, 150),
    (170, 250, 170, 175),
    (170, 175, 350, 150),
    (350, 150, 525, 175),
    (410, 225, 460, 225),
    (410, 225, 410, 160),
    (460, 225, 460, 165),
    (225, 225, 275, 225),
    (225, 225, 225, 170),
    (275, 225, 275, 165)
]

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    points = []
    if steps == 0:
        points.append((round(x1), round(y1)))
        return points

    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 0.5, 1.0)  

    for x1, y1, x2, y2 in edges:
        points = dda_line(x1, y1, x2, y2)

        glBegin(GL_POINTS)
        for px, py in points:
            glVertex2f(px, py)
        glEnd()

        glBegin(GL_LINE_STRIP)
        for px, py in points:
            glVertex2f(px, py)
        glEnd()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"2D House using Classic DDA (Scaled Directly)")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
