import pygame, sys
from pygame.locals import *

# settaggi base finestra
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Giochino')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

# ciclo fondamentale


while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # qui metterei le modifiche da fare ad ogni frame

    # qui ridisegnerei tutti gli elementi
    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossmo frame
    clock.tick(fps)