from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700,500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('table.png'),(700,500))

clock = time.Clock()
FPS = 60



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

raketka_l = Player('raketka.png',20,10,5,10,100)
raketka_r = Player('raketka.png',680,10,5,10,100)
ball = GameSprite('ball.png',325,225,5,50,50)

speed_x = 4
speed_y = 4


game = True
finish = False
font.init()
font1 = font.SysFont('Arial',30)
font2 = font.SysFont('Arial',70)
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background,(0,0))
        raketka_l.update_l()
        raketka_l.reset()
        raketka_r.update_r()
        raketka_r.reset() #отскок мяча от ракеток
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.y >= 450:
            speed_y *= -1
        if sprite.collide_rect(raketka_l, ball) or sprite.collide_rect(raketka_r, ball):
            speed_x *= -1
        ball.reset()
        
        


    display.update()
    clock.tick(FPS)
