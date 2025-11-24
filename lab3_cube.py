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
    glColor3f(1.0, 0.0, 0.0)   
    glPointSize(4.0)

    
    vertices = {
        'A': (200, 200), 'B': (500, 200), 'C': (500, 500), 'D': (200, 500),
        'E': (100, 300), 'F': (400, 300), 'G': (400, 600), 'H': (100, 600)
    }

    edges = [
        ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),  
        ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'E'),   
        ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H')   
    ]

    for (v1, v2) in edges:
        x1,y1 = vertices[v1]
        x2,y2 = vertices[v2]
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

# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import math

# def MidpointCircle(r, x0, y0):
#     x = 0
#     y = r
#     d = 1 - r
#     Circlepoints(x, y, x0, y0)

#     while x <= y:
#         x += 1
#         if d < 0:
#             d += 2 * x + 1
#         else:
#             y -= 1
#             d += 2 * (x - y) + 1
#         Circlepoints(x, y, x0, y0)

# def Circlepoints(x, y, x0, y0):
#     draw_points(x + x0, y + y0)
#     draw_points(y + x0, x + y0)
#     draw_points(y + x0, -x + y0)
#     draw_points(x + x0, -y + y0)
#     draw_points(-x + x0, -y + y0)
#     draw_points(-y + x0, -x + y0)
#     draw_points(-y + x0, x + y0)
#     draw_points(-x + x0, y + y0)

# def draw_points(x, y):
#     glPointSize(4)
#     glBegin(GL_POINTS)
#     glVertex2f(x, y)
#     glEnd()


# def get_zero(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1

#     if abs(dx) >= abs(dy):
#         if dx >= 0 and dy >= 0:
#             zone = 0
#         elif dx >= 0 and dy < 0:
#             zone = 7
#         elif dx < 0 and dy >= 0:
#             zone = 3
#         else:
#             zone = 4
#     else:
#         if dx >= 0 and dy >= 0:
#             zone = 1
#         elif dx >= 0 and dy < 0:
#             zone = 6
#         elif dx < 0 and dy >= 0:
#             zone = 2
#         else:
#             zone = 5

#     return zone

# def convert_to_zone0(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return y, -x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return -y, x
#     elif zone == 7:
#         return x, -y

# def convert_back_from_zone0(x, y, zone):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return -y, x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return y, -x
#     elif zone == 7:
#         return x, -y

# def midPointLine(x1, y1, x2, y2):
#     points = []

#     zone = get_zero(x1, y1, x2, y2)

#     x0zone0, y0zone0 = convert_to_zone0(x1, y1, zone)
#     x1zone0, y1zone0 = convert_to_zone0(x2, y2, zone)

#     dx = x1zone0 - x0zone0
#     dy = y1zone0 - y0zone0
#     d = 2 * dy - dx
#     incE = 2 * dy
#     incNE = 2 * (dy - dx)

#     x = x0zone0
#     y = y0zone0

#     while x <= x1zone0:
#         xr, yr = convert_back_from_zone0(x, y, zone)
#         draw_points(xr, yr)

#         if d <= 0:
#             d += incE
#         else:
#             d += incNE
#             y += 1

#         x += 1


# def iterate():
#     glViewport(0, 0, 800, 600)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluOrtho2D(0, 800, 0, 600)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     glColor3f(1.0, 0.0, 0.0)

#     MidpointCircle(140, 300, 150)
#     MidpointCircle(110, 300, 360)
#     MidpointCircle(10, 300, 380)
#     MidpointCircle(10, 300, 320)
#     MidpointCircle(80, 300, 520)
#     MidpointCircle(10, 260, 560)
#     MidpointCircle(10, 340, 560)

#     midPointLine(300, 540, 300, 510)
#     midPointLine(300, 540, 350, 525)
#     midPointLine(300, 510, 350, 525)

#     r = 40
#     cx, cy = 300, 520
#     x = 0
#     y = r
#     d = 1 - r

#     while x <= y:
#         draw_points(cx + x, cy - y)
#         draw_points(cx - x, cy - y)
#         draw_points(cx + y, cy - x)
#         draw_points(cx - y, cy - x)

#         x += 1
#         if d < 0:
#             d += 2*x + 1
#         else:
#             y -= 1
#             d += 2*(x - y) + 1

#     glutSwapBuffers()


# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
# glutInitWindowSize(800, 600)
# glutInitWindowPosition(400, 100)
# glutCreateWindow(b"Zone-Based Midpoint Line + Midpoint Circle (Exact Output)")
# glutDisplayFunc(showScreen)
# glutMainLoop()


# draw_points(cx + x, cy + y)   # upper right
# draw_points(cx - x, cy + y)   # upper left
# draw_points(cx + y, cy + x)   # upper right (steep)
# draw_points(cx - y, cy + x)   # upper left (steep)
