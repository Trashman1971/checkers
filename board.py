import pygame

class Board:
    def __init__(self, board, square_size, screen):
        self.board = board
        self.square_size = square_size
        self.screen = screen

    def make_board(self):
       
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        print(self.board)  

    def draw_board(self):
        print(len(self.board))
        for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if row % 2 == 0:
                        if col % 2 == 1:
                            pygame.draw.rect(self.screen, (0, 0, 0), (100*row, 100*col, 100, 100))

                    if row % 2 == 1:
                        if col % 2 == 0:
                            pygame.draw.rect(self.screen, (0, 0, 0), (100*row, 100*col, 100, 100))
                    
