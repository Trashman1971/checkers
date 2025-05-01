import pygame
from piece import piece
from logic import Logic
class Board:
    def __init__(self, board, square_size, screen):
        self.board = board
        self.square_size = square_size
        self.screen = screen

    def make_board(self):
        self.board = []

        for row in range(8):
            current_row = []
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row < 3:
                        current_row.append(piece(self.board,(28, 28, 27),(row,col),False))  # Top player/Black
                    elif row > 4:
                        current_row.append(piece(self.board,(92, 64, 51),(row,col),False))  # Bottom player/Brown
                    else:
                        current_row.append(0)  # Empty playable square
                else:
                    current_row.append(0)  # Light square, not used
            self.board.append(current_row)

        #print(self.board)


    def draw_board(self):
        #print(len(self.board))
        for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if row % 2 == 0:
                        if col % 2 == 1:
                            pygame.draw.rect(self.screen, (245, 191, 140), (100*row, 100*col, 100, 100))

                    if row % 2 == 1:
                        if col % 2 == 0:
                            pygame.draw.rect(self.screen, (245, 191, 140), (100*row, 100*col, 100, 100))
    def draw_pieces(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[col][row] != 0:
                    pygame.draw.circle(self.screen, self.board[col][row].color, (100*row+50, 100*col+50), 45)
                    #print(self.board[col][row].valid_moves())

                    """if self.board[col][row] == "o":
                        pygame.draw.circle(self.screen, (92, 64, 51), (100*row+50, 100*col+50), 45) #bottom
                    if self.board[col][row] == "x":
                        pygame.draw.circle(self.screen, (212, 205, 199), (100*row+50, 100*col+50), 45) #top"""
    def print_board(self):
        return self.board
    
    def get_piece_at(self,x,y):
        return self.board[x][y]
    def move_piece(self,pos,piece):
        x,y = pos 
        if piece!= 0:
            xx,yy = piece.get_pos()
            self.board[xx][yy] = 0
            self.board[x][y] = piece
            #print(piece.get_pos())wd
