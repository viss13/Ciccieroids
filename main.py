import pygame, sys, random, os, time
from pygame.locals import *
from objects import *

os.system("cls")
pygame.mixer.init()

# settaggi base finestra
WINDOW_SIZE = (900, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Asteroids')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

# ciclo fondamentale

in_game = False

player = Player((300, 300), (40, 40), screen)
asteroidi = []
proiettili = []

asteroid_spawn_rate = fps

shoot_key_pressed = False

punteggio = 0

timer = 0
tempo_inizio = int(time.time()*100)
sub = 1

pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(),int(50), bold = True, italic = False)

while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            
            record = 0
            with open("info.txt", 'r', encoding='utf-8') as f:
                record = int(f.readline())
                f.close()
            with open("info.txt", 'w', encoding='utf-8') as f:
                if record < punteggio:
                    f.write(f"{punteggio}")
                else:
                    f.write(f"{record}")
                f.close()
            
            pygame.quit()
            sys.exit()
    
    if int(time.time()*100) - tempo_inizio % 1 == 0:
        sub += 0.5

    # qui metterei le modifiche da fare ad ogni frame
    keys = pygame.key.get_pressed()

    if in_game:
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

        if player.inv:
            if timer < 3*fps:
                timer += 1
            else:
                player.inv = False
                timer = 0

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

            ast = Asteroide(rand_pos, (60, 60), rand_angolo, sub, screen)
            asteroidi.append(ast)

        # qui ridisegnerei tutti gli elementi
        screen.fill((0,0,0,1))
        player.draw()

        asteroidi_da_cancellare = []

        for ast in asteroidi:
            ast.muovi()
            ast.draw()

            if ast.rect.colliderect(player.rect) and not player.inv:
                if player.damage():
                    in_game = False
                asteroidi_da_cancellare.append(ast)

            for p in proiettili:
                if ast.rect.colliderect(p.rect):
                    if ast.rect.size > (60, 60):
                        asteroidi_da_cancellare.append(ast)
                        proiettili.remove(p)
                        punteggio += 30

                        asteroidi.append(Asteroide(ast.rect.center, (30, 30), random.randint(0,360), sub, screen))
                        asteroidi.append(Asteroide(ast.rect.center, (30, 30), random.randint(0,360), sub, screen))
                    else:
                        asteroidi_da_cancellare.append(ast)
                        proiettili.remove(p)
                        punteggio += 60
        
        for ast in asteroidi_da_cancellare:
            asteroidi.remove(ast)

        for p in proiettili:
            p.muovi()
            p.draw()
        
        for i in range(player.vite):
            cuore_rect = pygame.Rect(i*(40) + 25, 25, 40, 40)
            cuore_image = pygame.image.load('immagini_gioco/player.png')
            cuore_image = pygame.transform.scale(cuore_image, cuore_rect.size)
            screen.blit(cuore_image, cuore_rect)
        
        img_txt = font.render(f"Score: {punteggio}", True, (255, 255, 255))
        screen.blit(img_txt, pygame.Rect(screen.get_width()-img_txt.get_width()-10,10,10,10))
    else:
        screen.fill((0, 0, 0))

        with open("info.txt", 'r', encoding='utf-8') as f:
            record = int(f.readline())
            img_txt = font.render(f"Best Score: {record}", True, (255, 255, 255))
            screen.blit(img_txt, pygame.Rect(screen.get_width()-img_txt.get_width()-10,10,10,10))
            f.close()

        img_txt = font.render(f"Premi Spazio per giocare", True, (255, 255, 255))
        screen.blit(img_txt, pygame.Rect(screen.get_width()/2 - img_txt.get_width()/2, screen.get_height()/2,10,10))

        font2 = pygame.font.SysFont(pygame.font.get_default_font(),int(30), bold = False, italic = True)
        img_txt2 = font2.render(f"Premi Invio per il gioco serio", True, (255, 255, 255))
        screen.blit(img_txt2, pygame.Rect(screen.get_width()/2 - img_txt2.get_width()/2, screen.get_height()/2+40,10,10))

        player.vite = 3
        player.pos = [300, 300]
        punteggio = 0
        asteroidi = []
        proiettili = []
        player.inv = False
        
        if keys[K_SPACE]:
            in_game = True
    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.flip()

    # aspetto il prossimo frame
    clock.tick(fps)
