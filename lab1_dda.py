from OpenGL.GL import *             # Core OpenGL drawing functions (glVertex, glClear, etc.)
from OpenGL.GLU import *            # Utility library (gluOrtho2D)
from OpenGL.GLUT import *           # GLUT functions (window creation, main loop)
import math                         # Utility library for mathematical operations

# Window size constants (used for the orthographic projection and viewport)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


X0, Y0 = 100, 80
X1, Y1 = 200, 520


def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

   
    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        return

    x_increment = dx / steps
    y_increment = dy / steps

    # Starting position
    x = x1
    y = y1

    # Create a list to store all points
    points = []

    # Generate line points using DDA
    for i in range(int(steps) + 1):
        pixel_x = round(x)
        pixel_y = round(y)
        points.append((pixel_x, pixel_y))
        x += x_increment
        y += y_increment

    # Draw all computed points (red line)
    glBegin(GL_POINTS)
    for (px, py) in points:
        glVertex2f(px, py)
    glEnd()

    # Draw start and end points in green for clarity
    glColor3f(0.0, 1.0, 0.0)   # green color
    glPointSize(8.0)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def display():
    # Clear the screen (color buffer)
    glClear(GL_COLOR_BUFFER_BIT)

    # Set current drawing color (r, g, b). Values in [0,1].
    glPointSize(4.0)
    glColor3f(1.0, 0.0, 0.0)  # red color for line points

    # Compute and draw the line using DDA algorithm
    dda_line(X0, Y0, X1, Y1)

    # Swap front and back buffers
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
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"DDA Line Drawing Algorithm - PyOpenGL + GLUT")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
