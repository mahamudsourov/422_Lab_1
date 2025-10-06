# ------------------------------------------------------------
# DDA Line Drawing Algorithm using PyOpenGL + GLUT
# ------------------------------------------------------------

from OpenGL.GL import *       # Core OpenGL drawing functions
from OpenGL.GLU import *      # For gluOrtho2D (2D projection)
from OpenGL.GLUT import *     # For window and event handling

print("OpenGL and GLUT imported successfully ✅")

# ------------------------------------------------------------
# Window size
# ------------------------------------------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ------------------------------------------------------------
# Line endpoints (you can change these)
# ------------------------------------------------------------
X0, Y0 = 100, 80
X1, Y1 = 600, 400

# ------------------------------------------------------------
# DDA Algorithm Implementation
# ------------------------------------------------------------
def dda_line(x1, y1, x2, y2):
    # Step 1: Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Step 2: Decide how many steps to take
    steps = int(max(abs(dx), abs(dy)))  # The greater difference decides steps

    # Step 3: Calculate small increments for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Step 4: Start from the first point
    x = x1
    y = y1

    # Step 5: Plot points one by one
    glBegin(GL_POINTS)
    for i in range(steps + 1):
        glVertex2f(round(x), round(y))  # Plot the pixel (rounded to nearest integer)
        x += x_increment
        y += y_increment
    glEnd()

# ------------------------------------------------------------
# Display callback
# ------------------------------------------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)        # Clear the screen

    glColor3f(1.0, 0.0, 0.0)            # Red color for line
    glPointSize(2.0)                    # Set point size
    dda_line(X0, Y0, X1, Y1)            # Call the DDA algorithm

    # Draw endpoints in green (for clarity)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(6.0)
    glBegin(GL_POINTS)
    glVertex2i(int(X0), int(Y0))
    glVertex2i(int(X1), int(Y1))
    glEnd()

    glutSwapBuffers()                   # Swap buffers for smooth display

# ------------------------------------------------------------
# Reshape callback (handles resizing)
# ------------------------------------------------------------
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)     # 2D coordinate system
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ------------------------------------------------------------
# Window initialization
# ------------------------------------------------------------
def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"DDA Line Drawing Algorithm - PyOpenGL + GLUT")

    # Register callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0.0, 0.0, 0.0, 1.0)    # Background color (black)

# ------------------------------------------------------------
# Main function
# ------------------------------------------------------------
def main():
    init_glut_window()
    print("DDA Line Drawing Window Initialized ✅")
    glutMainLoop()

# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
