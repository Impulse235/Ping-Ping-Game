import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(img), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 20
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 300 * dt
        if keys[pygame.K_d] and self.rect.x < 610:
            self.rect.x += 300 * dt

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

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()