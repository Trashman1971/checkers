import pygame

class Logic:
    def __init__(self,board):
        self.board = board
    def selection(self):
        pass
    def update(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != 0:
                    pos = row, col 
                    if self.board[row][col].position != pos: 
                        self.board[row][col].position = pos 
    def handle_move(self,sp,ep):
        x,y = sp
        piece = self.board.get_piece_at(x,y)
        valid = piece.valid_moves()
        # intersect valid and sp


"""1. Get selected piece	Ensures the move starts from a valid piece	Game logic
2. Check valid moves	Prevents illegal moves	Game logic + Piece
3. Move the piece	Updates piece position, removes captures	Game logic → Board
4. Handle special rules	Manages promotions, multi-jumps, etc.	Game logic
5. Check game end	Determines if the game has been won	Game logic
6. Switch turn	Passes control to the next player	Game logic
7. Update display (optional)	Redraws or updates status	Game/UI"""

