from board import Board
from logic import Logic
from piece import piece
import pygame
pygame.init()


screen = pygame.display.set_mode((800, 800))
B1 = Board(0,8,screen)

B1.make_board()
ll = Logic(B1.print_board())
running = True
i = 0
clock = pygame.time.Clock()
while running:
    i = i + 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get mouse position
        mouse_pos = event.pos  
        self.mousepress = not self.mousepress
        x, y = pygame.mouse.get_pos()
        col = x // 125  
        row = y // 125
        piece_on = row, col
        if self.brd[piece_on[0]][piece_on[1]] == "X":
            if piece_on == self.selected:
                self.clear_possible_moves()
                return
            self.clear_possible_moves()
            self.selected = piece_on
        # or pygame.mouse.get_pos()
        #print(f"Mouse clicked at {mouse_pos}")

        # Check which button was clicked
        if event.button == 1:
            pie = B1.get_piece_at(0,5)
            B1.move_piece((5,5),pie)
        elif event.button == 2:
            print("Middle click")
        elif event.button == 3:
            print("Right click")
        elif event.button == 4:
            print("Scroll up")
        elif event.button == 5:
            print("Scroll down")
        
    screen.fill((54, 31, 9))
    B1.draw_board()
    B1.draw_pieces()
    ll.update()
   
   
    
    pygame.display.flip()


pygame.quit()

