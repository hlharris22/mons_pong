import pygame
import sys
from paddle import Paddle
from ball import Ball
from transformer import Transformer
import random

pygame.init()
pygame.key.set_repeat(120)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(1200, 800))

left_paddle = Paddle("assets/images/Paddle.png", 100, 400, 20)
left_paddle_group = pygame.sprite.GroupSingle()
left_paddle_group.add(left_paddle)

right_paddle = Paddle("assets/images/Paddle.png", 1100, 400, 20)
right_paddle_group = pygame.sprite.GroupSingle()
right_paddle_group.add(right_paddle)

poke_x_rand = random.randint(-5, 5)
poke_y_rand = random.choice([-4, 4])
poke_ball_surface = pygame.image.load("assets/images/Pokeballs.png")
poke_ball_image = Transformer.clip(poke_ball_surface, 0, 0, 119, 119)
poke_ball_image_scaled = pygame.transform.scale(poke_ball_image, (40, 40))
poke_ball = Ball(poke_ball_image_scaled, 600, 400, poke_x_rand, poke_y_rand)
poke_ball_group = pygame.sprite.GroupSingle()
poke_ball_group.add(poke_ball)

key_down_w = False
key_down_s = False
key_down_p = False
key_down_l = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key_down_w = True
            if event.key == pygame.K_s:
                key_down_s = True
            if event.key == pygame.K_p:
                key_down_p = True
            if event.key == pygame.K_l:
                key_down_l = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_down_w = False
            if event.key == pygame.K_s:
                key_down_s = False
            if event.key == pygame.K_p:
                key_down_p = False
            if event.key == pygame.K_l:
                key_down_l = False

    screen.fill((255, 255, 255))

    if key_down_w:
        left_paddle_group.sprite.move(-1)
    if key_down_s:
        left_paddle_group.sprite.move(1)
    if key_down_p:
        right_paddle_group.sprite.move(-1)
    if key_down_l:
        right_paddle_group.sprite.move(1)

    left_paddle_group.update()
    left_paddle_group.draw(screen)

    right_paddle_group.update()
    right_paddle_group.draw(screen)

    poke_ball_group.update()
    poke_ball_group.draw(screen)

    pygame.display.update()
    clock.tick(120)
