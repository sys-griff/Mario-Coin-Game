import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1000, 800))

FONT1 = pygame.font.Font("Pixel Font.ttf", 80)
FONT2 = pygame.font.Font("Pixel Font.ttf", 200)

score = FONT1.render("0", True, "black")
score_rect = score.get_rect(center = (500, 100))

levelup_text = FONT2.render("LEVEL UP", True, "black")
levelup_text_rect = score.get_rect(center = (185, 400))

gameover_text = FONT2.render("GAME OVER", True, "black")
gameover_text_rect = score.get_rect(center = (185, 400))

win_text = FONT2.render("YOU WIN", True, "black")
win_text_rect = score.get_rect(center = (185, 400))

window_rect = screen.get_rect()

pause = 2500
level_up = False
game_over = False
level = 1
lives = 3
enemy_speed = 1
coins = 0

screen_color = (255, 70, 231)

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

while True:

  clock.tick(240)

  keys = pygame.key.get_pressed()

  enemy_speed = level

  if level_up == False and game_over == False:
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
  
  enemy_collide = player.colliderect(enemy)

  if enemy_collide:
    lives -= 1
    enemy = enemyimg.get_rect(center = (1000, random.randint(50, 750)))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  coin_collide = player.colliderect(coin)

  if coin_collide:
    coin = coinimg.get_rect(center = (random.randint(50, 950), random.randint(50, 750)))
    coins += 1

  if coins == 10 * level:
    enemy = enemyimg.get_rect(center = (1000, random.randint(50, 750)))
    level_up = True
    coins = 0
    screen_color = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    level += 1
  
  screen.fill(screen_color)

  score = FONT1.render(f"{coins}", True, "black")

  screen.blit(score, score_rect)
  
  screen.blit(coinimg, coin)
  screen.blit(playerimg, player)
  screen.blit(enemyimg, enemy)
  if lives == 3:
    screen.blit(livesimg, lives3)
  if lives >= 2:
    screen.blit(livesimg, lives2)
  if lives >= 1:
    screen.blit(livesimg, lives1)

  if level == 5:
    screen.blit(win_text, win_text_rect)

  if lives == 0:
    screen.blit(gameover_text, gameover_text_rect)
    game_over = True

  if level_up == True:
    lives = 3
    pause -= 10.4166
    if pause > 0:
      screen.blit(levelup_text, levelup_text_rect)
    else:
      level_up = False
      pause = 2500
  pygame.display.update()


