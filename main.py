
from board import Board

import pygame
pygame.init()


screen = pygame.display.set_mode((800, 800))
B1 = Board(0,8,screen)
B1.make_board()
running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    screen.fill((255, 0, 0))
    B1.draw_board()
    
   
    
    pygame.display.flip()


pygame.quit()


