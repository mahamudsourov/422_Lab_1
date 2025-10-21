from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

vertices = {
    'A': (2, 2), 'B': (5, 2), 'C': (5, 5), 'D': (2, 5),
    'E': (1, 3), 'F': (4, 3), 'G': (4, 6), 'H': (1, 6)
}

edges = [
    ('A','B'), ('B','C'), ('C','D'), ('D','A'),
    ('E','F'), ('F','G'), ('G','H'), ('H','E'),
    ('A','E'), ('B','F'), ('C','G'), ('D','H')
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

    if dx > dy:  
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
    glColor3f(1, 0, 0)
    glPointSize(4)
    glLineWidth(2)

    for edge in edges:
        p1 = vertices[edge[0]]
        p2 = vertices[edge[1]]
        points = midPoint(p1[0], p1[1], p2[0], p2[1])

        glBegin(GL_POINTS)
        for px, py in points:
            glVertex2f(px, py)
        glEnd()

        
        glBegin(GL_LINE_STRIP)
        for px, py in points:
            glVertex2f(px, py)
        glEnd()

    
    glColor3f(0, 1, 0)
    glPointSize(6)
    glBegin(GL_POINTS)
    for v in vertices.values():
        glVertex2f(v[0], v[1])
    glEnd()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"2D Cube using Generalized Midpoint Line Algorithm")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0, 0, 0, 1)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
