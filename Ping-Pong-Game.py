import pygame
import random
#testing commit

pygame.mixer.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(img), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 20
        self.player_type = "temp"
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_x, ball_y, radius, shade_1, 
                 shade_2, shade_3):
        super().__init__()
        self.color = (shade_1, shade_2, shade_3)
        self.radius = radius
        diameter = self.radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y
        self.xspeed = 7
        self.yspeed = 5
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        if self.rect.y < 0 or self.rect.y > 470:
            self.yspeed *= -1

class Middle(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y,size_x, size_y, shade_1, 
                 shade_2, shade_3):
        super().__init__()
        self.color = (shade_1, shade_2, shade_3)
        self.size_x = size_x
        self.size_y = size_y
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.randomM = -1
    def update(self):
        if self.randomM > 0:
            self.rect.y -= 300 * dt
            if self.rect.y < 0:
                self.randomM *= -1
        if self.randomM < 0:
            self.rect.y += 300 * dt
            if self.rect.y > 390:
                self.randomM *= -1


class Player(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y,size_x, size_y, shade_1, 
                 shade_2, shade_3, player_type):
        super().__init__()
        self.color = (shade_1, shade_2, shade_3)
        self.size_x = size_x
        self.size_y = size_y
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player = player_type
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0 and self.player == "player_one":
            self.rect.y -= 300 * dt
        if keys[pygame.K_s] and self.rect.y < 390 and self.player == "player_one":
            self.rect.y += 300 * dt
        if keys[pygame.K_UP] and self.rect.y > 0 and self.player == "player_two":
            self.rect.y -= 300 * dt
        if keys[pygame.K_DOWN] and self.rect.y < 390 and self.player == "player_two":
            self.rect.y += 300 * dt


players = pygame.sprite.Group()
players.add(Player(40, 300, 15, 125, 161, 156, 156, "player_one"))
players.add(Player(650, 300, 15, 125, 161, 156, 156, "player_two"))
MiddlePaddle = Middle(350, 0, 15, 50, 0, 0, 0)
ball = Ball(300, 100, 15, 181, 4, 212)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
end_text = pygame.font.SysFont('Verdana', 75)
bounce_effect = pygame.mixer.Sound("Bounce.mp3")
P1Win_effect = pygame.mixer.Sound("P1Win.mp3")
P2Win_effect = pygame.mixer.Sound("P2Win.mp3")
change_effect = pygame.mixer.Sound("ChangeSound.mp3")
running = True
game_on = True
timer = 0
randomc = 0
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    if game_on:
        screen.fill((173, 216, 230))
        timer += dt
        players.update()
        players.draw(screen)
        MiddlePaddle.update()
        ball.update()
        screen.blit(ball.image, ball.rect)
        screen.blit(MiddlePaddle.image, MiddlePaddle.rect)
        collision = pygame.sprite.spritecollide(ball, players, False)
        if pygame.sprite.collide_rect(ball, MiddlePaddle):
            ball.xspeed *= -1
            bounce_effect.play()
        if timer >= 10:
            timer = 0
            change_effect.play()
            randomc = random.randint(1, 3)
            if randomc == 1:
                ball.xspeed *= 0.75
                ball.yspeed *= 0.75
                ball.color = (14, 150, 12)
                randomc = 0
            if randomc == 2:
                ball.xspeed *= 1.25
                ball.yspeed *= 1.25
                ball.color = (212, 160, 4)
                randomc = 0
            if randomc == 3:
                ball.xspeed *= 1.5
                ball.yspeed *= 1.5
                ball.color = (252, 3, 3)
                randomc = 0
        if collision:
            ball.xspeed *= -1
            bounce_effect.play()
        if ball.rect.x > 700:
            game_on = False
            gameover = end_text.render('Player 1 Wins', True, 'red')
            P1Win_effect.play()
            screen.blit(gameover, (75, 150))
        if ball.rect.x < -50:
            game_on = False
            gameover = end_text.render('Player 2 Wins', True, 'red')
            P2Win_effect.play()
            screen.blit(gameover, (75, 150))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
