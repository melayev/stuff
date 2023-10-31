class TicTacToe:
    def __init__(self, state):
        self.state = state

    def winner(self):
        for segment in [self.state, zip(*self.state), self.diagonals()]:
            winner = self.check_win(segment)
            if winner in [0, 1]:
                return winner
        return None

    def diagonals(self):
        n = len(self.state)
        main_diagonal = [self.state[i][i] for i in range(n)]
        anti_diagonal = [self.state[i][n - i - 1] for i in range(n)]
        return [main_diagonal, anti_diagonal]

    def check_win(self, segment):
        for row in segment:
            if all(cell == 0 for cell in row):
                return 0
            if all(cell == 1 for cell in row):
                return 1
        return None

state = [[1, 0, 0], [1, 1, None], [1, 0, 1]]
game = TicTacToe(state)
winner = game.winner()

print(f"Player {winner} wins" if winner is not None else "No winner")
