class TicTacToe
    attr_reader :state

    def initialize(state)
      @state = state
    end

    def getWinner
      horizontal_win = win?(state)
      return horizontal_win if [0, 1].include?(horizontal_win)

      vertical_win = win?(state.transpose)
      return vertical_win if [0, 1].include?(vertical_win)

      # diagonal win
      win?(diagonals)
     end

     def diagonals
      n = state.length
      main_diagonal = (0...n).map { |i| state[i][i] }
      anti_diagonal = (0...n).map { |i| state[i][n-i-1] }
      [main_diagonal, anti_diagonal]
     end

     def win?(rows)
      rows.each do |row|
          return 0 if row.all?{|x| x == 0}
          return 1 if row.all?{|x| x == 1}
      end

      nil
     end

end

state = [[nil, 0, 0], [1, 1, nil], [0, 1, 1]]

game = TicTacToe.new(state)
winner = game.getWinner()

if winner.nil?
    puts "No winners"
else
    puts "Player #{winner} wins"
end
