import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 800))

FONT = pygame.font.Font("Pixel Font.ttf", 80)

score = FONT.render("0", True, "black")
score_rect = score.get_rect(center=(500, 100))

window_rect = screen.get_rect()

coins = 0

screen.fill((255, 70, 231))

clock = pygame.time.Clock()

playerimg = pygame.image.load("Mario.png")
coinimg = pygame.image.load("Coin Icon.png")

pygame.display.set_caption('Hello World!')

coinimg = pygame.transform.scale(coinimg, (50, 50))
playerimg = pygame.transform.scale(playerimg, (55, 60))


coin = coinimg.get_rect(center = (random.randint(50, 950), random.randint(50, 750)))
player = playerimg.get_rect(center = (50, 400))




while True:

  clock.tick(240)

  keys = pygame.key.get_pressed()

  if keys[pygame.K_UP] and player.y > 0:
      player.y -= 2
  if keys[pygame.K_DOWN] and player.y < 740:
      player.y += 2
  if keys[pygame.K_RIGHT] and player.x < 1000 - 55:
      player.x += 2
  if keys[pygame.K_LEFT] and player.x > 0:
      player.x -= 2

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  collide = player.colliderect(coin)

  if collide:
    coin = coinimg.get_rect(center = (random.randint(50, 950), random.randint(50, 750)))
    coins += 1

  screen.fill((255, 70, 231))

  score = FONT.render(f"{coins}", True, "black")

  screen.blit(score, score_rect)
  
  screen.blit(coinimg, coin)
  screen.blit(playerimg, player)
  
  pygame.display.update()
