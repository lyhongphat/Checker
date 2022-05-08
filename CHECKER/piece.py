# Định nghĩa quân cờ ở đây

class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False