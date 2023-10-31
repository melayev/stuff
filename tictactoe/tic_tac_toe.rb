class TicTacToe
  attr_reader :state

  def initialize(state)
    @state = state
  end

  def winner
    [state, state.transpose, diagonals].each do |segment|
      winner = win?(segment)
      return winner unless winner.nil?
    end
    nil
  end

  private

  def diagonals
    n = state.length
    main_diagonal = (0...n).map { |i| state[i][i] }
    anti_diagonal = (0...n).map { |i| state[i][n - i - 1] }
    [main_diagonal, anti_diagonal]
  end

  def win?(segment)
    segment.each do |line|
      return 0 if line.all? { |cell| cell == 0 }
      return 1 if line.all? { |cell| cell == 1 }
    end
    nil
  end
end

state = [[nil, 0, 0], [1, 1, nil], [0, 1, 1]]
game = TicTacToe.new(state)

puts game.winner.nil? ? "No winner" : "Player #{game.winner} wins"