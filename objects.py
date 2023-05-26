import pygame, math

cartella_immagini = "immagini_gioco"

class Player:
    def __init__(self, pos, size, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(cartella_immagini+'/player.png')
        self.image = pygame.transform.scale(self.image, size)
        self.pos = [pos[0], pos[1]]

        self.vel = 0
        self.vel_max = 4
        self.accel = 0.08
        self.fric = 0.04

        self.vel_rot = 4
        self.accel_rot = 4
        self.angolo = 0
        self.target_angolo = 0

        self.move = False
    
    def muovi(self):
        if self.move:
            if self.vel < self.vel_max: self.vel += self.accel
            else: self.vel = self.vel_max
        else:
            if self.vel > 0: self.vel -= self.fric
            else: self.vel = 0
        
        if self.angolo > self.target_angolo:
            self.angolo -= self.accel_rot
            if self.vel > 0: self.vel -= self.fric
        elif self.angolo < self.target_angolo:
            self.angolo += self.accel_rot
            if self.vel > 0: self.vel -= self.fric
        
        rad = math.radians(self.angolo) - math.pi/2

        self.pos[0] += math.cos(rad) * self.vel
        self.pos[1] += math.sin(rad) * self.vel

        if self.pos[0] + self.rect.size[0] < 0:
            self.pos[0] = self.screen.get_width()
        if self.pos[0] > self.screen.get_width():
            self.pos[0] = -self.rect.size[0]
        if self.pos[1] + self.rect.size[1] < 0:
            self.pos[1] = self.screen.get_height()
        if self.pos[1] > self.screen.get_height():
            self.pos[1] = -self.rect.size[1]
    
    def blit_rotate_center(self, screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        self.rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, self.rect.topleft)
    
    def draw(self):
        self.blit_rotate_center(self.screen, self.image, self.pos, -self.target_angolo)

class Asteroide:
    def __init__(self, pos, size, angolo, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(cartella_immagini+'/rock.png')
        self.image = pygame.transform.scale(self.image, size)
        self.angolo = math.radians(angolo)
        self.dir = (math.cos(self.angolo), math.sin(self.angolo))
        self.vel_move = 3.0
        self.vel = (self.dir[0] * self.vel_move, self.dir[1] * self.vel_move)
    
    def muovi(self):
        self.rect.left += self.vel[0]
        self.rect.top += self.vel[1]
    
    def blit_rotate_center(self, screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        self.rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, self.rect.topleft)
    
    def draw(self):
        self.blit_rotate_center(self.screen, self.image, self.rect.topleft, self.angolo)

class Bullet:
    def __init__(self, pos, size, angolo, screen) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(cartella_immagini+'/bullet.png')
        self.image = pygame.transform.scale(self.image, size)
        self.angolo = angolo
        self.dir = (math.cos(math.radians(angolo)), math.sin(math.radians(angolo)))
        self.vel_move = 15.0
        self.vel = (self.dir[0] * self.vel_move, self.dir[1] * self.vel_move)
    
    def muovi(self):
        self.rect.left += self.vel[0]
        self.rect.top += self.vel[1]
    
    def blit_rotate_center(self, screen, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        self.rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        screen.blit(rotated_image, self.rect.topleft)
    
    def draw(self):
        self.blit_rotate_center(self.screen, self.image, self.rect.topleft, self.angolo)
