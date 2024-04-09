import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 800))

screen.fill((255, 70, 231))

clock = pygame.time.Clock()

playerimg = pygame.image.load("Mario.png")
coinimg = pygame.image.load("Coin Icon.png")
pygame.display.set_caption('Hello World!')

coinimg = pygame.transform.scale(coinimg, (50, 50))
playerimg = pygame.transform.scale(playerimg, (55, 60))

coin = coinimg.get_rect(center = (500, 400))
player = playerimg.get_rect(center = (50, 400))

while True:

  clock.tick(240)

  keys = pygame.key.get_pressed()

  if keys[pygame.K_UP] or keys[pygame.K_w]:
    player.y -= 2

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
  screen.fill((255, 70, 231))

  screen.blit(coinimg, coin)
  screen.blit(playerimg, player)
  
  pygame.display.update()
