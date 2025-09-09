import pygame
import random
pygame.init()
WIDTH ,HEIGHT=500,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Clorful Bounce")
sprite_width,sprite_height=50,50
x,y=100,100
dx,dy =5,4
sprite_color=(0,0,225)
bg_color=(0,0,0)
def random_color():
     return random.randint(0,255), random.randint(0,255) , random.randint(0,255)
running= True
clock = pygame.time.Clock()
while running:
   for event in pygame.event.get():
     if event.type ==pygame.QUIT:
       running:False
   x +=dx
   y +=dx

   if x <=0 or x + sprite_width>=WIDTH:
     dx = -dx 
     sprite_color = random_color()
     bg_color=random_color()
   screen.fill(bg_color)
pygame.draw.rect(screen, sprite_color,(x,y, sprite_width,sprite_height))


pygame.display.flip()
clock.tick(60)
pygame.QUIT()


   




