import pygame, math

class Player:
    def __init__(self, pos, size, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('immagini/protagonista2.png')
        self.image = pygame.transform.scale(self.image, size)
        self.vel = [0,0]
        self.vel_orizz = 10
        self.vel_verti = 10
    
    def muovi(self):
        if math.sqrt(self.vel[0]**2 + self.vel[1]**2) > 1:
            self.vel[0] /= math.sqrt(2)
            self.vel[1] /= math.sqrt(2)

        self.rect.left += self.vel[0] * self.vel_orizz
        self.rect.top += self.vel[1] * self.vel_verti

        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
        if self.rect.top < 0:
            self.rect.top = 0
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

class Asteroide:
    def __init__(self, pos, size, dir, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('immagini/cattivo.png')
        self.image = pygame.transform.scale(self.image, size)
        self.dir = dir
        self.vel = dir * 10
    
    def muovi(self):
        self.rect.left += self.vel[0]
        self.rect.top += self.vel[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)
