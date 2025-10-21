from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

x0, y0 = 500, 100
x1, y1 = 100, 500

def get_zero(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx >= 0 and dy < 0:
            zone = 7
        elif dx < 0 and dy >= 0:
            zone = 3
        else:
            zone = 4
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx >= 0 and dy < 0:
            zone = 6
        elif dx < 0 and dy >= 0:
            zone = 2
        else:
            zone = 5

    return zone


def convert_to_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def convert_back_from_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def midPointLine(x1, y1, x2, y2):
    points = []
    zone = get_zero(x1, y1, x2, y2)

    x0_zone0, y0_zone0 = convert_to_zone0(x1, y1, zone)
    x1_zone0, y1_zone0 = convert_to_zone0(x2, y2, zone)
    dx = x1_zone0 - x0_zone0
    dy = y1_zone0 - y0_zone0
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x0_zone0
    y = y0_zone0

    while x <= x1_zone0:
        x_real, y_real = convert_back_from_zone0(x, y, zone)
        points.append((x_real, y_real))
        if d <= 0:
            d += incE
        else:
            d += incNE
            y += 1
        x += 1

    return points


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.5, 1.0)   
    glPointSize(4.0)

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

    for (x1, y1, x2, y2) in edges:
        points = midPointLine(x1, y1, x2, y2)

        glBegin(GL_POINTS)
        for x, y in points:
            glVertex2f(x, y)
        glEnd()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"Midpoint Line Drawing Algorithm - Simple Call")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()

