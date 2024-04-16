import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 800))

FONT = pygame.font.Font("Pixel Font.ttf", 80)

score = FONT.render("0", True, "black")
score_rect = score.get_rect(center=(500, 100))

window_rect = screen.get_rect()

game = True

lives = 3

enemy_speed = 1

coins = 0

screen.fill((255, 70, 231))

clock = pygame.time.Clock()

playerimg = pygame.image.load("Mario.png")
coinimg = pygame.image.load("Coin Icon.png")
enemyimg = pygame.image.load("Goomba.png")
livesimg = pygame.image.load("Heart.png")

pygame.display.set_caption('Mario Game')

coinimg = pygame.transform.scale(coinimg, (50, 50))
playerimg = pygame.transform.scale(playerimg, (55, 60))
enemyimg = pygame.transform.scale(enemyimg, (55, 60))
livesimg = pygame.transform.scale(livesimg, (60, 60))

coin = coinimg.get_rect(center = (random.randint(50, 950), random.randint(50, 750)))
player = playerimg.get_rect(center = (50, 400))
enemy = enemyimg.get_rect(center = (1000, random.randint(50, 750)))
lives3 = livesimg.get_rect(center = (350, 100))
lives2 = livesimg.get_rect(center = (250, 100))
lives1 = livesimg.get_rect(center = (150, 100))

while game == True:

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

  enemy.x -= enemy_speed

  if enemy.x < 0:
    enemy = enemyimg.get_rect(center = (1000, random.randint(50, 750)))
    if enemy_speed < 6:
       enemy_speed += 1
  
  enemy_collide = player.colliderect(enemy)

  if enemy_collide:
    lives -= 1
    enemy = enemyimg.get_rect(center = (1000, random.randint(50, 750)))
    if lives == 2:
      lives3 = livesimg.get_rect(center = (5000, 5000))
    if lives == 1:
      lives2 = livesimg.get_rect(center = (5000, 5000))
    if lives == 0:
      lives1 = livesimg.get_rect(center = (5000, 5000))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  coin_collide = player.colliderect(coin)

  if coin_collide:
    coin = coinimg.get_rect(center = (random.randint(50, 950), random.randint(50, 750)))
    coins += 1

  screen.fill((255, 70, 231))

  score = FONT.render(f"{coins}", True, "black")

  screen.blit(score, score_rect)
  
  screen.blit(coinimg, coin)
  screen.blit(playerimg, player)
  screen.blit(enemyimg, enemy)
  screen.blit(livesimg, lives3)
  screen.blit(livesimg, lives2)
  screen.blit(livesimg, lives1)

  if lives == 0:
     game = False

  pygame.display.update()
