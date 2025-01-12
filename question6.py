import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(p1, p2):
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(p1[0], p1[1])
        glVertex2f(p2[0], p2[1])
        glEnd()
        pygame.display.flip()
    
    pygame.quit()


