import pygame 
pygame.init
import OpenGL
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
screen = pygame.display.set_mode((500,400))

def main():
 screen = pygame.display.set_mode((500,400))
 pygame.display.set_caption("polygons")
 screen.fill((255, 255, 255))
 run = False
 while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                pygame.quit()
        pygame.display.update()

pygame.draw.line(screen,(255,0,0),(50, 50), (250,250),0  )
Blue = (0,0,255)
pygame.draw.polygon(screen, Blue, (0,1),(0,-1),(0,1),)



