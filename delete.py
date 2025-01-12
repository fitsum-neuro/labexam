import pygame 
from pygame.locals import*
pygame.init
pygame.display.set_mode((500,500))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

    pygame.display.update()

pygame.draw.rect(screen , Green, (50,60,50,100))
#while True:
   # for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
     #       pygame.quit()
     #   elif event.type == KEYDOWN:
      #     if event.key == K_ESCAPE:
       #         print(" Escape  pressed")
       #    elif event.key == K_SPACE:
        #       print("space  pressed")
       # pygame.display.update()

#myColor = pygame.Color(255, 0, 0, 128)
#if event.type = KEYDOWN
  # if event.key = pygame.key_Space

