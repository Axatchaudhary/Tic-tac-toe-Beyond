


class TicTacToe:
    """
    this is tic-tac-toe beyond. It goes beyond simple 3x3 board game and simple rules
    """
    def __init__(self, n, playerX, playerO):
        # initialize bord
        self.n = n
        self.board = [' '] * n ** 2

        # initialize players
        self.playerX, self.playerO = playerX, playerO

        # assign first turn
        self.playerX_turn = True

    def display_board(self):
        """
        everytime function is called it updates to latest state
        """
        padding = '{:{fill}>6}'
        middle = '{:^5}{}'

        def draw_row(board, row_num, n):
            bottom_line = '_' if row_num < n-1 else ' '

            # draw upper side of the row
            row = '   '+padding.format('|',fill=' ')*(n-1)+'\n'

            # draw middle side of the row
            row += str(row_num+1)+'  ' # display row number on left side
            for i in range(n-1):
                row += middle.format(board[row_num*n + i], '|')
            row += middle.format(board[row_num*n + n - 1], '')+'\n'

            # draw lower side of the row
            row += '   '+padding.format('|',fill=bottom_line)*(n-1)
            row += padding.format(' ',fill=bottom_line)+'\n'

            # display column numbers on bottom of the board
            if row_num == n - 1:
                row += '\n   '+' '.join(map(lambda x: '{:^5}'.format(x), range(1,n+1)))

            return row

        display = ''
        for i in range(self.n):
            display+=draw_row(self.board, i, self.n)
        print display

    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def player_wins(self, char):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if char == self.board[a] == self.board[b] == self.board[c]:
                return True

        return False

    def play_game(self, train=True):
        if not train:
            print '\nNew game!'

        self.playerX.start_game()
        self.playerO.start_game()
        while True:
            if self.playerX_turn:
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            if player.breed == "human":
                self.display_board()

            move = player.move(self.board)
            self.board[move - 1] = char

            if self.player_wins(char):
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                if not train:
                    # self.display_board()
                    print char + ' wins!'
                break

            if self.board_full():
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                if not train:
                    # self.display_board()
                    print 'Draw!'
                break

            other_player.reward(0, self.board)
            self.playerX_turn = not self.playerX_turn
