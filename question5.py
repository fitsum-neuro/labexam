import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import * 
pygame.init

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(128, 0, 128)
    glVertex2f(-0.8, -0.8)
    glVertex2f(0.8, -0.8)
    glVertex2f(0.0, 0.8)
    glEnd()

def main():
    display = (400, 190)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50)
    glTranslatef(0, 0, -8)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()


if __name__ == "msn":
    main()