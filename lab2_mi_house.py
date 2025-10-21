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

def midPoint(X1, Y1, X2, Y2):
    points = []

    dx = X2 - X1
    dy = Y2 - Y1

    x, y = X1, Y1

    sx = 1 if dx >= 0 else -1
    sy = 1 if dy >= 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:  # slope < 1
        d = 2*dy - dx
        for _ in range(dx + 1):
            points.append((x, y))
            if d >= 0:
                y += sy
                d -= 2*dx
            x += sx
            d += 2*dy
    else:  
        d = 2*dx - dy
        for _ in range(dy + 1):
            points.append((x, y))
            if d >= 0:
                x += sx
                d -= 2*dy
            y += sy
            d += 2*dx

    return points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 0.5, 1.0)  

    for x1, y1, x2, y2 in edges:
        points = midPoint(x1, y1, x2, y2)

        
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
    glutCreateWindow(b"2D House using Midpoint Line Algorithm")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
