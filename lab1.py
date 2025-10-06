# ------------------------------------------------------------
# PyOpenGL + GLUT Example
# Demonstrates:
# 1️⃣ Single Line
# 2️⃣ Multiple Lines
# 3️⃣ Square
# 4️⃣ Rectangle
# ------------------------------------------------------------

from OpenGL.GL import *       # Core OpenGL functions (glBegin, glVertex, glClear, etc.)
from OpenGL.GLU import *      # Utility library (gluOrtho2D)
from OpenGL.GLUT import *     # GLUT functions (window creation, event handling)
import sys

print("OpenGL and GLUT imported successfully ✅")

# ------------------------------------------------------------
# Window configuration
# ------------------------------------------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ------------------------------------------------------------
# Display callback
# ------------------------------------------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)       # Clear window

    # ----- Task 1: Draw a Single Line -----
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)           # Red line
    glBegin(GL_LINES)
    glVertex2f(100, 100)
    glVertex2f(300, 300)
    glEnd()

    # ----- Task 2: Draw Multiple Lines -----
    glLineWidth(2.0)
    glColor3f(0.0, 1.0, 0.0)           # Green lines
    glBegin(GL_LINES)
    glVertex2f(400, 100)
    glVertex2f(600, 300)
    glVertex2f(400, 300)
    glVertex2f(600, 100)
    glEnd()

    # ----- Task 3: Draw a Square -----
    glColor3f(0.0, 0.0, 1.0)           # Blue square
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 400)
    glVertex2f(250, 400)
    glVertex2f(250, 550)
    glVertex2f(100, 550)
    glEnd()

    # ----- Task 4: Draw a Rectangle -----
    glColor3f(1.0, 1.0, 0.0)           # Yellow rectangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(400, 400)
    glVertex2f(650, 400)
    glVertex2f(650, 520)
    glVertex2f(400, 520)
    glEnd()

    glutSwapBuffers()                  # Swap front and back buffers


# ------------------------------------------------------------
# Reshape callback (handles resizing)
# ------------------------------------------------------------
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)    # 2D coordinate system (0,0) bottom-left
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# ------------------------------------------------------------
# Window Initialization
# ------------------------------------------------------------
def init_glut_window():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"OpenGL Line, Square, Rectangle Demo")

    # Register callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0.0, 0.0, 0.0, 1.0)   # Set background color (black)


# ------------------------------------------------------------
# Main function
# ------------------------------------------------------------
def main():
    init_glut_window()
    print("OpenGL window initialized successfully ✅")
    glutMainLoop()                     # Enter main loop


# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
