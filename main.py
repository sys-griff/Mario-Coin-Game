import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((400, 300))

screen.fill((255, 70, 231))

playerimg = pygame.image.load("Mario.png")
coinimg = pygame.image.load("Coin Icon.png")
pygame.display.set_caption('Hello World!')

coinimg = pygame.transform.scale(coinimg, (50, 50))
playerimg = pygame.transform.scale(playerimg, (55, 60))

coin = coinimg.get_rect(center = (200, 150))
player = playerimg.get_rect(center = (50, 150))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  screen.blit(coinimg, coin)
  screen.blit(playerimg, player)
  
  pygame.display.update()
