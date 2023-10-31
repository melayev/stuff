class TicTacToe:
    def __init__(self, state):
        self.state = state

    def getWinner(self):
        horizontal_win = self.isWin(self.state)
        if horizontal_win in [0, 1]:
            return horizontal_win

        vertical_win = self.isWin(list(map(list, zip(*self.state))))
        if vertical_win in [0, 1]:
            return vertical_win

        # diagonal win
        return self.isWin(self.diagonals())

    def diagonals(self):
        n = len(self.state)
        main_diagonal = [self.state[i][i] for i in range(n)]
        anti_diagonal = [self.state[i][n-i-1] for i in range(n)]
        return [main_diagonal, anti_diagonal]


    def isWin(self, rows):
        for row in rows:
            if all(x == 0 for x in row):
                return 0
            if all(x == 1 for x in row):
                return 1
        return None




state = [[1, 0, 0], [1, 1, None], [1, 0, 1]]

game = TicTacToe(state)
winner = game.getWinner()

if winner is None:
    print("No winners")
else:
    print(f"Player {winner} wins")