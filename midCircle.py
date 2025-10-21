from OpenGL.GL import *      
from OpenGL.GLU import *     
from OpenGL.GLUT import *    
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def midPointCirclePoints(x_centre, y_centre, r):
    points = []
    x = r
    y = 0
    P = 1 - r

    while x >= y:
        points.extend([
            (x + x_centre, y + y_centre),
            (-x + x_centre, y + y_centre),
            (x + x_centre, -y + y_centre),
            (-x + x_centre, -y + y_centre),
            (y + x_centre, x + y_centre),
            (-y + x_centre, x + y_centre),
            (y + x_centre, -x + y_centre),
            (-y + x_centre, -x + y_centre)
        ])

        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

    return points


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3.0)
    glColor3f(1.0, 0.0, 0.0)

    cx, cy, r = 0, 0, 100
    points = midPointCirclePoints(cx, cy, r)

    glBegin(GL_POINTS)
    for (x, y) in points:
        glVertex2i(int(x), int(y))
    glEnd()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-width // 2, width // 2, -height // 2, height // 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_glut_window():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"Midpoint Circle Drawing Algorithm (Single Circle)")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
