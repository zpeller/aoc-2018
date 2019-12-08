#!/usr/local/bin/ruby

require 'pp'

input = (ARGV.empty? ? DATA : ARGF).each_line.map { |l|
	l.scan(/-?\d+/).map(&:to_i)
}[0].freeze

def add_marbles(num_players, last_marble)
	scores = Hash.new(0)
	marbles = [0]
	act_player = 0
	(1..last_marble).each {|marble|
		act_player += 1
		act_player = 1 if act_player > num_players
		if marble % 23 == 0
			scores[act_player] += marble
#			Single element move at large arrays is way faster than n rotate/slice/pop!
#			marbles.rotate!(-7)
			7.times { marbles.unshift(marbles.pop) }
			scores[act_player] += marbles.pop
			marbles << marbles.shift
			next
		end
		marbles << marbles.shift
		marbles << marble
	}
	return scores.values.max
end

pp add_marbles(9, 27)
pp add_marbles(10, 1618)
pp add_marbles(30, 5807)
pp add_marbles(input[0], input[1])
pp add_marbles(input[0], 100*input[1])

__END__
462 players; last marble is worth 71938 points
