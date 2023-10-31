class TicTacToe
    attr_reader :state

    def initialize(state)
      @state = state
    end

    def getWinner()
        horizontal_win = win?(state)
        return horizontal_win if [0, 1].include?(horizontal_win)

        vertical_win = win?(state.transpose)
        return vertical_win if [0, 1].include?(vertical_win)

        # diagonal win
        win?([
            [state[0][0], state[1][1], state[2][2]],
            [state[0][2], state[1][1], state[2][0]]
            ])
     end

     def win?(rows)
        rows.each do |row|
            return 0 if row.uniq == [0]
            return 1 if row.uniq == [1]
        end
        nil
     end

end

state = [[0, 0, 0], [1, 0, nil], [1, nil, nil]]

game = TicTacToe.new(state)
winner = game.getWinner()

if winner.nil?
    puts "No winners"
else
    puts "Player #{winner} wins"
end
