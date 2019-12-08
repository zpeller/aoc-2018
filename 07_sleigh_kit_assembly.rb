#!/usr/local/bin/ruby

require 'pp'

input = (ARGV.empty? ? DATA : ARGF).each_line.map { |l|
	tokens = l.strip.scan(/Step (.).*step (.)/)[0].freeze
	[tokens[0], tokens[1]]
}.freeze

# pp input


def build_depend_hash(depends_on, depends_list)
	depends_list.each { |step_first, step_after|
		depends_on[step_after] += [step_first]
		depends_on[step_first] = [] if not depends_on.key?(step_first)
	}
#	pp depends_on
end

def move_list_single(depends_on)
	depends_on = Marshal.load(Marshal.dump(depends_on))
	move_list = ''
	while depends_on.length>0
		move = depends_on.select { |k, v| v.length == 0 }.min[0]
		depends_on.transform_values! { |v| v-[move] }
		depends_on.delete(move)
		move_list += move
	end
	return move_list
end

def move_list_parallel(depends_on, num_workers)
	depends_on = Marshal.load(Marshal.dump(depends_on))
	done_list = ''

	work_list = {}
	0.step {|time|

		work_list.each { |move, v|
			if v <= time
				work_list.delete(move)
				depends_on.transform_values! { |d| d-[move] }
				done_list += move
			end
		}

		if work_list.length < num_workers 
			depends_on.select { |k, v| v.length == 0 }.sort.each {|move, _|
				depends_on.delete(move)
				work_list[move] = time + WORK_TIME + move.ord-"A".ord + 1
				break if work_list.length >= num_workers
			}
		end

		break [time, done_list] if depends_on.length <= 0 and work_list.length <= 0
	}
end

WORK_TIME = 60

depends_on = Hash.new([].freeze)
build_depend_hash(depends_on, input)

print move_list_single(depends_on), "\n"
print move_list_parallel(depends_on, 5), "\n"

__END__
Step O must be finished before step C can begin.
Step Y must be finished before step D can begin.
Step N must be finished before step D can begin.
Step G must be finished before step F can begin.
Step C must be finished before step Z can begin.
Step H must be finished before step K can begin.
Step W must be finished before step T can begin.
Step T must be finished before step F can begin.
Step S must be finished before step I can begin.
Step X must be finished before step B can begin.
Step J must be finished before step A can begin.
Step K must be finished before step D can begin.
Step Z must be finished before step A can begin.
Step A must be finished before step B can begin.
Step L must be finished before step V can begin.
Step F must be finished before step M can begin.
Step B must be finished before step V can begin.
Step M must be finished before step Q can begin.
Step D must be finished before step E can begin.
Step I must be finished before step U can begin.
Step R must be finished before step V can begin.
Step E must be finished before step U can begin.
Step P must be finished before step V can begin.
Step V must be finished before step Q can begin.
Step U must be finished before step Q can begin.
Step P must be finished before step U can begin.
Step O must be finished before step F can begin.
Step T must be finished before step M can begin.
Step I must be finished before step Q can begin.
Step M must be finished before step U can begin.
Step R must be finished before step E can begin.
Step T must be finished before step R can begin.
Step H must be finished before step S can begin.
Step L must be finished before step B can begin.
Step S must be finished before step Q can begin.
Step E must be finished before step Q can begin.
Step B must be finished before step Q can begin.
Step S must be finished before step M can begin.
Step C must be finished before step D can begin.
Step S must be finished before step R can begin.
Step G must be finished before step D can begin.
Step T must be finished before step E can begin.
Step T must be finished before step Q can begin.
Step N must be finished before step I can begin.
Step S must be finished before step P can begin.
Step N must be finished before step J can begin.
Step X must be finished before step L can begin.
Step G must be finished before step K can begin.
Step N must be finished before step E can begin.
Step H must be finished before step D can begin.
Step H must be finished before step P can begin.
Step O must be finished before step A can begin.
Step V must be finished before step U can begin.
Step F must be finished before step D can begin.
Step B must be finished before step P can begin.
Step T must be finished before step L can begin.
Step I must be finished before step P can begin.
Step K must be finished before step Z can begin.
Step G must be finished before step M can begin.
Step F must be finished before step Q can begin.
Step J must be finished before step L can begin.
Step H must be finished before step Q can begin.
Step W must be finished before step R can begin.
Step R must be finished before step U can begin.
Step P must be finished before step Q can begin.
Step D must be finished before step V can begin.
Step G must be finished before step C can begin.
Step Z must be finished before step B can begin.
Step O must be finished before step H can begin.
Step S must be finished before step A can begin.
Step J must be finished before step Q can begin.
Step N must be finished before step F can begin.
Step L must be finished before step R can begin.
Step O must be finished before step R can begin.
Step W must be finished before step M can begin.
Step J must be finished before step F can begin.
Step G must be finished before step W can begin.
Step K must be finished before step U can begin.
Step D must be finished before step U can begin.
Step W must be finished before step I can begin.
Step E must be finished before step V can begin.
Step Y must be finished before step Q can begin.
Step L must be finished before step E can begin.
Step S must be finished before step B can begin.
Step T must be finished before step V can begin.
Step C must be finished before step U can begin.
Step M must be finished before step P can begin.
Step G must be finished before step S can begin.
Step B must be finished before step R can begin.
Step K must be finished before step M can begin.
Step X must be finished before step A can begin.
Step R must be finished before step P can begin.
Step B must be finished before step I can begin.
Step C must be finished before step X can begin.
Step O must be finished before step P can begin.
Step D must be finished before step Q can begin.
Step F must be finished before step B can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step I can begin.
Step M must be finished before step D can begin.
Step F must be finished before step U can begin.
