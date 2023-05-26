import pygame, sys, random, os, time
from pygame.locals import *
from objects import *

os.system("cls")

# settaggi base finestra
WINDOW_SIZE = (900, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Ciccieroids')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

# ciclo fondamentale

player = Player((300, 300), (40, 40), screen)
asteroidi = []
proiettili = []

asteroid_spawn_rate = 2*fps

shoot_key_pressed = False

while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # qui metterei le modifiche da fare ad ogni frame
    keys = pygame.key.get_pressed()

    if keys[K_d] or keys[K_RIGHT]:
        player.target_angolo += player.vel_rot
    elif keys[K_a] or keys[K_LEFT]:
        player.target_angolo -= player.vel_rot
    
    player.move = keys[K_w] or keys[K_UP]
    player.muovi()

    if keys[K_SPACE]:
        if not shoot_key_pressed:
            bullet = Bullet(player.rect.center, (15, 15), player.angolo-90, screen)
            bullet.vel_move += player.vel
            proiettili.append(bullet)
            shoot_key_pressed = True
    elif shoot_key_pressed:
        shoot_key_pressed = False

    # spawna asteroidi
    if int(time.time()*100) % asteroid_spawn_rate == 0:
        spawn_rand = random.randint(0, 3)
        rand_pos = [0, 0]
        rand_angolo = 0.0

        if spawn_rand == 0:
            rand_pos[0] = -60
            rand_pos[1] = random.randint(0, screen.get_height())

            rand_angolo = random.randint(-45, 45)
        elif spawn_rand == 1:
            rand_pos[1] = -60
            rand_pos[0] = random.randint(0, screen.get_width())

            rand_angolo = random.randint(45, 135)
        elif spawn_rand == 2:
            rand_pos[0] = screen.get_width()
            rand_pos[1] = random.randint(0, screen.get_height())

            rand_angolo = random.randint(-135, 135)
        elif spawn_rand == 3:
            rand_pos[1] = screen.get_height()
            rand_pos[0] = random.randint(0, screen.get_width())

            rand_angolo = random.randint(-135, -45)

        ast = Asteroide(rand_pos, (60, 60), rand_angolo, screen)
        asteroidi.append(ast)

    # qui ridisegnerei tutti gli elementi
    screen.fill((0,0,0,1))
    player.draw()

    for ast in asteroidi:
        ast.muovi()
        ast.draw()
        for p in proiettili:
            if ast.rect.colliderect(p.rect):
                asteroidi.remove(ast)
                proiettili.remove(p)
    
    for p in proiettili:
        p.muovi()
        p.draw()
    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossimo frame
    clock.tick(fps)
