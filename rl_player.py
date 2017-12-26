class Player(object):

    def __init__(self):
        self.breed = 'human'

    def start_game(self):
        pass

    def move(self, board):
        return int(raw_input('Your move? '))

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']
