import pygame, sys, random
from pygame.locals import *
from objects import *

# settaggi base finestra
WINDOW_SIZE = (900, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Ciccieroids')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

# ciclo fondamentale

player = Player((300, 300), (100, 100), screen)
asteroidi = []

tick = 0
spawn_tick = 0
target = 1200
sub = 1

while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # qui metterei le modifiche da fare ad ogni frame
    keys = pygame.key.get_pressed()

    if keys[K_d]:
        player.angolo += player.vel_rot
    elif keys[K_a]:
        player.angolo -= player.vel_rot
    
    if keys[K_w]:
        player.muovi()

    # player.vel[0] = 1 if  else -1 if keys[K_a] else 0
    # player.vel[1] = 1 if keys[K_s] else -1 if keys[K_w] else 0

    # spawna asteroidi
    if spawn_tick == 0:
        spawn_rand = random.randint(0, 3)
        rand_pos = [0, 0]
        rand_dir = [0, 0]

        if spawn_rand == 0:
            rand_pos[0] = -player.rect.size[0]
            rand_pos[1] = random.randint(0, screen.get_height())

            rand_dir[0] = 1*sub
        elif spawn_rand == 1:
            rand_pos[1] = -player.rect.size[1]
            rand_pos[0] = random.randint(0, screen.get_width())

            rand_dir[1] = 1*sub
        elif spawn_rand == 2:
            rand_pos[0] = screen.get_width()
            rand_pos[1] = random.randint(0, screen.get_height())

            rand_dir[0] = -1*sub
        elif spawn_rand == 3:
            rand_pos[1] = screen.get_height()
            rand_pos[0] = random.randint(0, screen.get_width())

            rand_dir[1] = -1*sub

        # ast = Asteroide(rand_pos, (100, 100), rand_dir, screen)
        # asteroidi.append(ast)

    # qui ridisegnerei tutti gli elementi
    screen.fill((0,0,0,1))
    player.draw()

    for ast in asteroidi:
        ast.draw()
        ast.muovi()
    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossmo frame
    clock.tick(fps)
    tick += 1
    spawn_tick += 1
    if spawn_tick > fps:
        spawn_tick = 0
    if tick % target == 0 and sub <= 5 and tick != 0:
        sub += 1
