import pygame
#testing commit

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
        self.xspeed = 1
        self.yspeed = 1
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed


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
ball = Ball(300, 100, 15, 222, 20, 13)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
running = True
game_on = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    if game_on:
        screen.fill((173, 216, 230))
        players.update()
        players.draw(screen)
        ball.update()
        screen.blit(ball.image, ball.rect)
        collision = pygame.sprite.spritecollide(ball, players, False)
        if collision:
            ball.xspeed *= -1
            ball.yspeed *= -1

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
