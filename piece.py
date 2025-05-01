class piece:
    def __init__(self, screen, color,position, is_king):
        self.screen = screen
        self.color = color
        self.position = position
        self.is_king = is_king
    def valid_moves(self):
        if self.color == (92, 64, 51):# bottom white
            pass
        elif self.color == (28, 28, 27):#top black
            pass
            #return self.position[0]+1, self.position[1]+1
    def get_pos(self):
        return self.position
