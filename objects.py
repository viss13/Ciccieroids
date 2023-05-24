import pygame, math

class Player:
    def __init__(self, pos, size, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('immagini/prof ferro.png')
        self.image = pygame.transform.scale(self.image, size)
        self.pos = [pos[0], pos[1]]
        self.vel = [0,0]
        self.vel_move = 4
        self.vel_rot = 2
        self.angolo = 0
    
    def muovi(self):
        # if math.sqrt(self.vel[0]**2 + self.vel[1]**2) > 1:
        #     self.vel[0] /= math.sqrt(2)
        #     self.vel[1] /= math.sqrt(2)
        # self.angolo = math.radians(self.angolo)
        rad = math.radians(self.angolo) - math.pi/2
        self.vel = (math.cos(rad), math.sin(rad))

        self.pos[0] += self.vel[0] * self.vel_move
        self.pos[1] += self.vel[1] * self.vel_move

        # if self.rect.right > self.screen.get_width():
        #     self.rect.right = self.screen.get_width()
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.bottom > self.screen.get_height():
        #     self.rect.bottom = self.screen.get_height()
        # if self.rect.top < 0:
        #     self.rect.top = 0
    
    def blit_rotate_center(self, screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, new_rect.topleft)
    
    def draw(self):
        self.blit_rotate_center(self.screen, self.image, self.pos, -self.angolo)

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

class Bullet:
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
