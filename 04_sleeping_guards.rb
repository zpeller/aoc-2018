#!/usr/local/bin/ruby

require 'pp'

input = (ARGV.empty? ? DATA : ARGF).sort.each.map { |l|
	tokens = l.strip.scan(/:(\d+)\] .{5} (?:#?)(\d+|\w+)/)[0].freeze
	[tokens[0].to_i, tokens[1]]
}.freeze

#pp input
#
#input.each {|l|
#	print(l, "\n")
#}

def record_guards(guards, sleeping_list)
	guard_no = -1
	sleep_time = -1
	sleeping_list.each { |minute, token|
		case token
		when "asleep"
			sleep_time = minute
		when "up"
			up_time = minute
			guards[guard_no] += [[sleep_time, up_time]]
		else
			guard_no = token.to_i
		end
	}
	return guards
end

def guard_minute_with_most_sleep(guards)
	minutes = Hash.new(0)
	max_guard = guards.max_by{|k, v| v.inject(0) { |s, t| s + t[1]-t[0] }}[0]
	guards[max_guard].each { |t0, t1|
		(t0..t1-1).each { |t| minutes[t] += 1}
	}
	return minutes.max_by { |k, v| v }[0] * max_guard
end

def guard_most_minute(guards)
	max_m = [0, []]
	guards.each { |g, minute_list|
		minutes = Hash.new(0)
		minute_list.each { |t0, t1|
			(t0..t1-1).each { |t| minutes[t] += 1 }
		}
		max_minutes = minutes.max_by { |k, v| v }
		max_m = [max_m, [max_minutes[1], max_minutes[0], g]].max
	}
	return max_m[1] * max_m[2]
end


guards = Hash.new {[].freeze}
guards = record_guards(guards, input)
print("P1: max minute: #{guard_minute_with_most_sleep(guards)}\n")
print("P2: max minute: #{guard_most_minute(guards)}\n")

__END__
[1518-06-25 23:58] Guard #1069 begins shift
[1518-09-16 00:24] falls asleep
[1518-04-06 00:56] wakes up
[1518-11-04 00:48] wakes up
[1518-04-24 00:19] falls asleep
[1518-06-02 23:59] Guard #1697 begins shift
[1518-08-06 00:00] Guard #947 begins shift
[1518-11-01 00:41] falls asleep
[1518-03-14 00:43] falls asleep
[1518-09-06 00:47] wakes up
[1518-08-02 00:17] falls asleep
[1518-06-01 00:12] falls asleep
[1518-05-18 23:58] Guard #1697 begins shift
[1518-07-09 00:47] wakes up
[1518-10-04 00:46] falls asleep
[1518-04-19 00:23] falls asleep
[1518-08-23 00:59] wakes up
[1518-03-24 00:30] wakes up
[1518-08-18 00:15] falls asleep
[1518-07-17 23:57] Guard #2339 begins shift
[1518-10-08 00:10] falls asleep
[1518-05-29 23:59] Guard #1097 begins shift
[1518-09-05 23:59] Guard #3229 begins shift
[1518-09-02 00:52] wakes up
[1518-10-18 00:02] falls asleep
[1518-04-01 00:55] wakes up
[1518-07-14 00:27] falls asleep
[1518-04-17 00:29] falls asleep
[1518-05-24 00:00] falls asleep
[1518-10-07 00:53] wakes up
[1518-07-20 00:15] falls asleep
[1518-03-14 00:00] Guard #1901 begins shift
[1518-06-26 00:17] falls asleep
[1518-05-03 00:59] wakes up
[1518-05-11 00:40] falls asleep
[1518-03-22 00:15] falls asleep
[1518-03-12 00:02] Guard #947 begins shift
[1518-04-01 00:01] Guard #641 begins shift
[1518-10-06 00:25] falls asleep
[1518-04-19 23:52] Guard #1889 begins shift
[1518-04-13 00:45] falls asleep
[1518-09-18 00:20] falls asleep
[1518-03-19 00:45] wakes up
[1518-03-20 00:51] wakes up
[1518-06-05 00:10] falls asleep
[1518-10-01 23:59] Guard #3433 begins shift
[1518-08-22 00:04] Guard #2039 begins shift
[1518-06-19 00:14] falls asleep
[1518-07-03 00:31] falls asleep
[1518-08-13 00:12] falls asleep
[1518-11-21 00:18] wakes up
[1518-08-14 00:55] wakes up
[1518-10-14 00:58] wakes up
[1518-10-12 00:04] Guard #1663 begins shift
[1518-10-13 00:02] Guard #2003 begins shift
[1518-09-17 00:57] wakes up
[1518-10-03 00:49] falls asleep
[1518-10-06 23:59] Guard #2039 begins shift
[1518-08-14 00:51] falls asleep
[1518-10-11 00:02] falls asleep
[1518-03-14 00:09] falls asleep
[1518-08-08 00:01] Guard #1069 begins shift
[1518-05-01 00:48] wakes up
[1518-07-12 00:38] wakes up
[1518-09-25 23:58] Guard #1783 begins shift
[1518-09-29 00:50] wakes up
[1518-04-22 00:31] wakes up
[1518-04-23 00:29] falls asleep
[1518-03-24 00:26] falls asleep
[1518-10-28 00:52] falls asleep
[1518-10-17 00:35] falls asleep
[1518-11-05 00:41] wakes up
[1518-06-10 23:54] Guard #1237 begins shift
[1518-05-05 00:17] falls asleep
[1518-09-14 00:25] falls asleep
[1518-05-22 00:25] falls asleep
[1518-10-24 00:47] falls asleep
[1518-05-15 00:28] falls asleep
[1518-07-25 00:26] wakes up
[1518-04-03 00:07] falls asleep
[1518-06-15 00:38] wakes up
[1518-07-09 23:56] Guard #947 begins shift
[1518-08-27 00:38] wakes up
[1518-03-04 00:10] wakes up
[1518-08-29 00:41] falls asleep
[1518-05-03 00:52] wakes up
[1518-06-10 00:22] wakes up
[1518-05-17 00:07] falls asleep
[1518-03-10 00:44] wakes up
[1518-11-09 00:32] wakes up
[1518-06-20 00:00] Guard #1697 begins shift
[1518-07-18 00:36] wakes up
[1518-05-04 00:20] wakes up
[1518-08-31 00:01] Guard #1901 begins shift
[1518-07-24 00:27] falls asleep
[1518-10-16 00:37] wakes up
[1518-11-03 00:01] Guard #1783 begins shift
[1518-03-16 00:09] falls asleep
[1518-11-18 23:52] Guard #1237 begins shift
[1518-10-18 00:39] wakes up
[1518-09-11 00:30] wakes up
[1518-10-09 00:35] falls asleep
[1518-03-16 00:52] falls asleep
[1518-03-29 00:52] wakes up
[1518-05-23 23:51] Guard #277 begins shift
[1518-03-17 00:46] falls asleep
[1518-03-15 00:54] wakes up
[1518-04-26 00:57] wakes up
[1518-06-15 00:32] falls asleep
[1518-03-16 00:58] wakes up
[1518-04-29 00:56] falls asleep
[1518-09-28 23:51] Guard #277 begins shift
[1518-06-28 00:03] Guard #1889 begins shift
[1518-04-17 00:59] wakes up
[1518-04-10 00:35] falls asleep
[1518-08-29 00:53] wakes up
[1518-04-05 00:00] Guard #3229 begins shift
[1518-10-09 00:19] wakes up
[1518-03-09 00:26] wakes up
[1518-10-20 00:47] falls asleep
[1518-10-09 00:50] wakes up
[1518-08-30 00:45] wakes up
[1518-05-12 23:51] Guard #1237 begins shift
[1518-08-23 00:39] wakes up
[1518-10-02 23:57] Guard #1901 begins shift
[1518-04-25 00:32] wakes up
[1518-08-15 00:16] falls asleep
[1518-10-30 00:52] wakes up
[1518-07-08 00:29] falls asleep
[1518-07-14 23:57] Guard #863 begins shift
[1518-03-30 00:50] wakes up
[1518-06-27 00:58] wakes up
[1518-04-11 00:25] wakes up
[1518-10-26 00:45] wakes up
[1518-05-20 00:02] Guard #2039 begins shift
[1518-04-11 00:03] Guard #2161 begins shift
[1518-07-10 00:59] wakes up
[1518-04-30 00:54] falls asleep
[1518-06-28 00:29] wakes up
[1518-05-05 00:02] Guard #863 begins shift
[1518-07-26 00:45] falls asleep
[1518-06-10 00:42] falls asleep
[1518-05-26 00:06] falls asleep
[1518-04-01 00:06] falls asleep
[1518-08-13 23:49] Guard #947 begins shift
[1518-08-31 00:59] wakes up
[1518-10-24 00:49] wakes up
[1518-08-18 00:51] wakes up
[1518-10-05 00:01] Guard #1697 begins shift
[1518-10-17 23:47] Guard #3559 begins shift
[1518-07-13 23:46] Guard #2161 begins shift
[1518-07-23 00:39] falls asleep
[1518-04-16 00:55] wakes up
[1518-06-05 00:56] wakes up
[1518-04-11 00:23] falls asleep
[1518-08-31 23:57] Guard #3461 begins shift
[1518-09-25 00:35] falls asleep
[1518-11-16 00:00] falls asleep
[1518-09-27 00:04] falls asleep
[1518-04-11 00:38] falls asleep
[1518-04-15 00:28] falls asleep
[1518-09-15 00:20] falls asleep
[1518-06-05 23:56] Guard #3229 begins shift
[1518-06-08 00:58] wakes up
[1518-06-14 00:02] Guard #947 begins shift
[1518-10-21 00:03] Guard #2003 begins shift
[1518-07-03 00:50] wakes up
[1518-05-18 00:48] wakes up
[1518-05-30 00:46] falls asleep
[1518-07-11 00:07] falls asleep
[1518-07-25 00:29] falls asleep
[1518-04-26 00:49] falls asleep
[1518-03-08 00:50] wakes up
[1518-06-24 00:40] falls asleep
[1518-08-20 00:53] wakes up
[1518-10-30 23:56] Guard #1097 begins shift
[1518-10-31 00:51] falls asleep
[1518-05-23 00:56] wakes up
[1518-04-24 00:02] Guard #1901 begins shift
[1518-06-14 00:56] wakes up
[1518-08-16 00:58] wakes up
[1518-06-22 00:04] Guard #2339 begins shift
[1518-05-30 00:48] wakes up
[1518-04-05 23:59] Guard #3559 begins shift
[1518-07-31 00:51] wakes up
[1518-06-27 00:40] falls asleep
[1518-04-06 00:23] wakes up
[1518-10-04 00:55] wakes up
[1518-09-07 00:37] wakes up
[1518-09-19 00:58] wakes up
[1518-04-28 23:57] Guard #2161 begins shift
[1518-05-23 00:04] Guard #863 begins shift
[1518-07-19 00:53] wakes up
[1518-03-11 00:54] falls asleep
[1518-07-24 00:51] wakes up
[1518-05-23 00:31] wakes up
[1518-11-08 00:36] wakes up
[1518-10-17 00:39] wakes up
[1518-08-21 00:34] wakes up
[1518-07-16 00:30] falls asleep
[1518-04-24 00:43] falls asleep
[1518-04-07 00:03] falls asleep
[1518-11-07 23:49] Guard #3433 begins shift
[1518-04-15 00:42] falls asleep
[1518-03-31 00:52] wakes up
[1518-05-09 00:51] wakes up
[1518-08-17 23:57] Guard #1783 begins shift
[1518-07-08 00:02] Guard #1097 begins shift
[1518-07-14 00:28] wakes up
[1518-08-25 00:50] wakes up
[1518-06-21 00:39] wakes up
[1518-08-22 00:57] wakes up
[1518-07-17 00:12] falls asleep
[1518-06-30 23:56] Guard #1901 begins shift
[1518-10-13 00:18] falls asleep
[1518-07-23 00:08] falls asleep
[1518-06-24 00:00] Guard #1889 begins shift
[1518-06-16 00:21] falls asleep
[1518-07-11 00:24] wakes up
[1518-09-23 00:34] falls asleep
[1518-08-08 00:31] wakes up
[1518-08-02 00:40] falls asleep
[1518-06-25 00:42] wakes up
[1518-04-09 23:56] Guard #863 begins shift
[1518-10-11 00:17] wakes up
[1518-04-22 00:21] falls asleep
[1518-09-15 00:35] wakes up
[1518-09-04 00:34] wakes up
[1518-05-29 00:04] Guard #2003 begins shift
[1518-09-21 00:26] wakes up
[1518-09-14 00:26] wakes up
[1518-09-22 00:01] Guard #1237 begins shift
[1518-10-24 00:59] wakes up
[1518-11-23 00:40] wakes up
[1518-10-09 00:59] wakes up
[1518-11-01 00:02] Guard #2339 begins shift
[1518-03-12 23:58] Guard #1697 begins shift
[1518-10-16 00:28] falls asleep
[1518-07-28 00:25] falls asleep
[1518-09-22 00:24] falls asleep
[1518-05-26 00:00] Guard #1783 begins shift
[1518-05-21 00:34] falls asleep
[1518-11-06 00:42] wakes up
[1518-04-24 00:39] wakes up
[1518-07-26 23:58] Guard #2003 begins shift
[1518-07-12 00:00] Guard #1069 begins shift
[1518-06-23 00:55] wakes up
[1518-07-29 23:59] Guard #1237 begins shift
[1518-04-03 00:57] wakes up
[1518-05-27 23:56] Guard #3461 begins shift
[1518-11-22 00:56] wakes up
[1518-11-21 00:05] falls asleep
[1518-10-02 00:56] wakes up
[1518-10-01 00:24] falls asleep
[1518-09-23 00:46] falls asleep
[1518-09-04 00:49] falls asleep
[1518-03-14 00:10] wakes up
[1518-04-09 00:22] falls asleep
[1518-09-12 00:28] falls asleep
[1518-04-05 00:55] wakes up
[1518-10-17 00:19] wakes up
[1518-07-04 00:14] falls asleep
[1518-11-11 00:03] Guard #3229 begins shift
[1518-11-07 00:01] falls asleep
[1518-08-17 00:49] wakes up
[1518-05-08 00:20] falls asleep
[1518-05-24 00:44] wakes up
[1518-11-13 00:52] wakes up
[1518-10-07 00:49] falls asleep
[1518-06-13 00:43] falls asleep
[1518-08-14 00:27] wakes up
[1518-05-09 23:46] Guard #1889 begins shift
[1518-04-18 00:10] falls asleep
[1518-11-23 00:04] falls asleep
[1518-07-02 00:45] wakes up
[1518-06-19 00:39] wakes up
[1518-09-12 00:21] wakes up
[1518-10-10 00:57] wakes up
[1518-10-10 23:54] Guard #2039 begins shift
[1518-05-12 00:53] wakes up
[1518-03-10 00:26] falls asleep
[1518-11-12 23:48] Guard #2339 begins shift
[1518-09-28 00:47] falls asleep
[1518-08-11 00:03] Guard #739 begins shift
[1518-07-27 00:50] wakes up
[1518-11-02 00:59] wakes up
[1518-09-15 00:50] falls asleep
[1518-04-12 00:54] wakes up
[1518-11-21 00:49] wakes up
[1518-10-27 00:47] wakes up
[1518-05-29 00:31] falls asleep
[1518-05-10 00:00] falls asleep
[1518-08-25 00:39] falls asleep
[1518-08-06 00:44] wakes up
[1518-11-04 00:33] falls asleep
[1518-06-02 00:51] falls asleep
[1518-09-03 00:04] falls asleep
[1518-04-29 00:13] falls asleep
[1518-05-09 00:48] falls asleep
[1518-06-06 00:37] wakes up
[1518-11-11 00:47] wakes up
[1518-06-06 00:45] falls asleep
[1518-08-05 00:00] Guard #641 begins shift
[1518-05-17 00:42] wakes up
[1518-10-07 00:46] wakes up
[1518-04-15 23:59] Guard #613 begins shift
[1518-08-06 00:55] wakes up
[1518-11-14 00:56] wakes up
[1518-07-24 00:43] falls asleep
[1518-11-10 00:53] wakes up
[1518-07-21 00:39] wakes up
[1518-11-17 23:57] Guard #1901 begins shift
[1518-08-27 23:58] Guard #641 begins shift
[1518-07-04 00:29] wakes up
[1518-06-12 00:35] falls asleep
[1518-07-06 00:55] wakes up
[1518-04-28 00:57] wakes up
[1518-08-28 23:57] Guard #1889 begins shift
[1518-05-11 00:00] Guard #277 begins shift
[1518-07-19 00:49] falls asleep
[1518-04-24 23:58] Guard #1889 begins shift
[1518-04-25 00:39] falls asleep
[1518-07-31 00:38] wakes up
[1518-10-07 00:43] falls asleep
[1518-09-12 23:57] Guard #3433 begins shift
[1518-11-12 00:45] falls asleep
[1518-09-24 23:58] Guard #2339 begins shift
[1518-09-19 00:56] falls asleep
[1518-10-23 00:01] Guard #1069 begins shift
[1518-09-30 00:37] wakes up
[1518-08-31 00:52] falls asleep
[1518-03-17 00:00] Guard #739 begins shift
[1518-05-05 00:40] falls asleep
[1518-03-26 00:11] falls asleep
[1518-03-21 00:00] Guard #2339 begins shift
[1518-09-02 00:31] wakes up
[1518-06-17 00:38] falls asleep
[1518-05-18 00:56] falls asleep
[1518-11-01 00:46] wakes up
[1518-05-07 00:28] falls asleep
[1518-08-09 00:06] wakes up
[1518-03-17 00:17] falls asleep
[1518-08-17 00:39] wakes up
[1518-07-10 23:57] Guard #3433 begins shift
[1518-10-08 00:41] wakes up
[1518-04-24 00:55] falls asleep
[1518-09-18 00:29] wakes up
[1518-09-11 23:58] Guard #739 begins shift
[1518-07-29 00:04] Guard #1237 begins shift
[1518-07-26 00:00] Guard #2039 begins shift
[1518-05-03 00:47] falls asleep
[1518-04-02 00:25] falls asleep
[1518-04-26 00:29] wakes up
[1518-06-10 00:21] falls asleep
[1518-03-08 00:00] Guard #2003 begins shift
[1518-09-08 23:59] Guard #1697 begins shift
[1518-03-17 00:28] wakes up
[1518-08-21 00:00] Guard #1069 begins shift
[1518-03-04 00:56] falls asleep
[1518-07-24 23:56] Guard #863 begins shift
[1518-04-30 00:28] wakes up
[1518-11-21 23:56] Guard #1097 begins shift
[1518-05-17 00:45] falls asleep
[1518-07-20 00:44] wakes up
[1518-04-06 00:50] falls asleep
[1518-05-02 00:40] falls asleep
[1518-10-16 23:59] Guard #1697 begins shift
[1518-07-10 00:45] falls asleep
[1518-04-16 00:16] falls asleep
[1518-11-21 00:26] falls asleep
[1518-06-17 00:40] wakes up
[1518-11-02 00:02] Guard #641 begins shift
[1518-08-28 00:50] wakes up
[1518-10-07 23:57] Guard #1783 begins shift
[1518-09-03 00:32] falls asleep
[1518-03-25 00:00] Guard #2089 begins shift
[1518-08-15 00:17] wakes up
[1518-09-21 00:23] falls asleep
[1518-10-30 00:03] falls asleep
[1518-08-24 00:16] falls asleep
[1518-06-06 00:49] wakes up
[1518-03-12 00:12] wakes up
[1518-04-25 00:06] falls asleep
[1518-04-18 23:56] Guard #3433 begins shift
[1518-08-04 00:03] Guard #3229 begins shift
[1518-08-22 00:44] falls asleep
[1518-04-21 23:59] Guard #277 begins shift
[1518-07-24 00:45] wakes up
[1518-09-08 00:04] Guard #2039 begins shift
[1518-10-02 00:35] wakes up
[1518-05-16 00:54] wakes up
[1518-11-09 00:03] Guard #3229 begins shift
[1518-11-18 00:54] falls asleep
[1518-05-19 00:52] wakes up
[1518-08-20 00:00] Guard #641 begins shift
[1518-05-21 00:01] Guard #1901 begins shift
[1518-06-03 00:43] wakes up
[1518-08-01 00:02] Guard #1069 begins shift
[1518-11-06 00:23] wakes up
[1518-04-25 00:52] wakes up
[1518-03-21 00:56] falls asleep
[1518-08-13 00:37] wakes up
[1518-06-20 00:08] falls asleep
[1518-04-27 00:57] wakes up
[1518-04-29 00:58] wakes up
[1518-08-03 00:04] Guard #3559 begins shift
[1518-11-14 00:14] falls asleep
[1518-10-05 00:51] wakes up
[1518-07-28 00:10] falls asleep
[1518-11-15 00:46] wakes up
[1518-05-18 00:01] Guard #641 begins shift
[1518-06-30 00:57] wakes up
[1518-04-09 00:57] wakes up
[1518-07-18 00:26] falls asleep
[1518-11-18 00:58] wakes up
[1518-07-19 23:57] Guard #2339 begins shift
[1518-05-26 00:12] wakes up
[1518-09-22 00:46] wakes up
[1518-05-13 23:58] Guard #3461 begins shift
[1518-03-06 00:56] falls asleep
[1518-07-15 00:39] wakes up
[1518-07-07 00:03] falls asleep
[1518-05-13 00:06] wakes up
[1518-09-23 00:58] wakes up
[1518-06-24 00:54] wakes up
[1518-06-25 00:11] falls asleep
[1518-08-03 00:23] falls asleep
[1518-10-28 00:47] wakes up
[1518-08-07 00:45] wakes up
[1518-09-26 00:40] wakes up
[1518-09-23 23:51] Guard #2039 begins shift
[1518-09-29 00:01] falls asleep
[1518-06-06 00:32] falls asleep
[1518-09-27 00:50] wakes up
[1518-07-09 00:24] falls asleep
[1518-11-17 00:56] wakes up
[1518-03-09 00:02] Guard #739 begins shift
[1518-07-12 23:59] Guard #1697 begins shift
[1518-05-18 00:13] falls asleep
[1518-08-24 00:00] Guard #863 begins shift
[1518-08-26 00:33] falls asleep
[1518-04-08 00:18] falls asleep
[1518-07-13 00:08] falls asleep
[1518-03-21 00:15] falls asleep
[1518-08-24 00:38] wakes up
[1518-03-03 23:48] Guard #863 begins shift
[1518-08-06 00:53] falls asleep
[1518-04-30 23:51] Guard #3559 begins shift
[1518-05-18 00:29] falls asleep
[1518-04-15 00:00] Guard #863 begins shift
[1518-09-17 00:33] wakes up
[1518-07-20 00:51] falls asleep
[1518-11-06 00:08] falls asleep
[1518-06-07 00:43] wakes up
[1518-09-30 00:00] Guard #277 begins shift
[1518-05-18 00:59] wakes up
[1518-04-26 00:24] falls asleep
[1518-04-27 00:34] falls asleep
[1518-05-07 00:02] Guard #2039 begins shift
[1518-08-02 00:59] wakes up
[1518-04-02 00:39] wakes up
[1518-11-13 23:59] Guard #613 begins shift
[1518-05-31 00:41] falls asleep
[1518-09-19 23:53] Guard #2161 begins shift
[1518-08-10 00:58] wakes up
[1518-10-21 00:18] wakes up
[1518-08-12 00:23] falls asleep
[1518-05-05 00:32] wakes up
[1518-08-29 23:58] Guard #3433 begins shift
[1518-07-26 00:56] wakes up
[1518-11-10 00:38] falls asleep
[1518-10-24 00:54] wakes up
[1518-09-07 00:14] falls asleep
[1518-03-06 00:58] wakes up
[1518-10-29 00:20] falls asleep
[1518-04-12 00:36] falls asleep
[1518-09-17 00:25] falls asleep
[1518-03-07 00:13] falls asleep
[1518-11-14 00:30] wakes up
[1518-08-09 00:51] wakes up
[1518-07-14 00:44] wakes up
[1518-04-10 00:54] wakes up
[1518-11-11 00:18] falls asleep
[1518-03-05 00:35] falls asleep
[1518-07-01 00:19] falls asleep
[1518-03-14 00:27] wakes up
[1518-10-03 23:57] Guard #1237 begins shift
[1518-06-03 00:31] falls asleep
[1518-05-16 23:59] Guard #3433 begins shift
[1518-10-25 00:59] wakes up
[1518-04-30 00:03] Guard #2039 begins shift
[1518-08-20 00:20] falls asleep
[1518-08-09 00:02] falls asleep
[1518-11-05 00:25] falls asleep
[1518-11-06 00:41] falls asleep
[1518-06-23 00:29] falls asleep
[1518-04-19 00:31] wakes up
[1518-07-14 00:43] falls asleep
[1518-08-22 23:50] Guard #863 begins shift
[1518-11-15 00:53] falls asleep
[1518-10-29 00:36] wakes up
[1518-08-11 23:58] Guard #2039 begins shift
[1518-08-27 00:00] Guard #613 begins shift
[1518-10-29 00:59] wakes up
[1518-05-31 00:00] Guard #2039 begins shift
[1518-09-06 00:39] falls asleep
[1518-07-04 23:58] Guard #863 begins shift
[1518-10-20 00:01] falls asleep
[1518-04-17 00:57] falls asleep
[1518-06-21 00:17] falls asleep
[1518-08-26 00:01] Guard #1901 begins shift
[1518-07-17 00:59] wakes up
[1518-07-12 00:55] wakes up
[1518-04-24 00:58] wakes up
[1518-08-08 00:57] falls asleep
[1518-05-22 00:51] wakes up
[1518-10-09 00:57] falls asleep
[1518-06-14 23:56] Guard #3433 begins shift
[1518-10-24 00:16] falls asleep
[1518-07-25 00:55] wakes up
[1518-04-15 00:55] wakes up
[1518-03-09 00:09] falls asleep
[1518-06-07 23:59] Guard #739 begins shift
[1518-10-20 00:59] wakes up
[1518-04-17 00:04] Guard #3229 begins shift
[1518-04-07 00:15] falls asleep
[1518-10-24 00:57] falls asleep
[1518-09-12 00:37] wakes up
[1518-07-17 00:02] Guard #1783 begins shift
[1518-10-19 00:00] Guard #2039 begins shift
[1518-07-09 00:57] falls asleep
[1518-03-07 00:53] wakes up
[1518-10-14 00:00] Guard #1697 begins shift
[1518-09-03 00:46] wakes up
[1518-03-27 23:59] Guard #2003 begins shift
[1518-10-22 00:24] falls asleep
[1518-03-21 00:48] wakes up
[1518-06-12 00:51] wakes up
[1518-10-19 23:50] Guard #1889 begins shift
[1518-03-26 00:04] Guard #2161 begins shift
[1518-11-09 00:12] falls asleep
[1518-09-09 23:58] Guard #1663 begins shift
[1518-07-31 00:42] falls asleep
[1518-05-02 00:54] wakes up
[1518-10-02 00:55] falls asleep
[1518-04-05 00:23] falls asleep
[1518-05-08 00:04] Guard #1097 begins shift
[1518-08-24 00:57] wakes up
[1518-11-08 00:01] falls asleep
[1518-06-03 00:54] falls asleep
[1518-08-19 00:05] wakes up
[1518-09-16 00:45] wakes up
[1518-03-20 00:43] falls asleep
[1518-07-27 00:26] falls asleep
[1518-06-01 00:58] wakes up
[1518-03-17 23:51] Guard #3433 begins shift
[1518-07-19 00:34] wakes up
[1518-06-01 00:57] falls asleep
[1518-05-24 23:59] Guard #2089 begins shift
[1518-10-23 00:58] wakes up
[1518-10-23 00:54] wakes up
[1518-07-19 00:22] falls asleep
[1518-05-27 00:22] falls asleep
[1518-10-29 23:53] Guard #641 begins shift
[1518-07-10 00:50] wakes up
[1518-09-07 00:04] Guard #277 begins shift
[1518-10-15 00:12] wakes up
[1518-03-28 23:54] Guard #641 begins shift
[1518-07-01 00:59] wakes up
[1518-05-11 00:48] wakes up
[1518-11-15 23:47] Guard #3559 begins shift
[1518-04-10 00:25] wakes up
[1518-11-16 23:56] Guard #1097 begins shift
[1518-03-04 00:02] falls asleep
[1518-08-13 00:45] wakes up
[1518-09-02 23:47] Guard #3229 begins shift
[1518-08-09 00:18] falls asleep
[1518-07-28 00:35] wakes up
[1518-08-23 00:53] falls asleep
[1518-07-30 00:32] falls asleep
[1518-03-05 23:58] Guard #1069 begins shift
[1518-07-24 00:49] falls asleep
[1518-04-27 23:56] Guard #2339 begins shift
[1518-03-16 00:00] Guard #613 begins shift
[1518-06-27 00:02] Guard #3433 begins shift
[1518-08-15 00:10] wakes up
[1518-09-27 00:32] falls asleep
[1518-07-14 00:02] wakes up
[1518-11-02 00:35] wakes up
[1518-03-20 00:03] Guard #1783 begins shift
[1518-06-08 00:13] falls asleep
[1518-06-29 00:54] wakes up
[1518-11-20 23:49] Guard #2039 begins shift
[1518-06-30 00:26] falls asleep
[1518-06-06 00:54] falls asleep
[1518-04-30 00:56] wakes up
[1518-06-04 23:57] Guard #1069 begins shift
[1518-09-24 00:03] falls asleep
[1518-06-04 00:01] Guard #3461 begins shift
[1518-06-25 00:02] Guard #641 begins shift
[1518-05-10 00:24] wakes up
[1518-03-31 00:29] falls asleep
[1518-07-02 00:12] falls asleep
[1518-03-14 23:51] Guard #3559 begins shift
[1518-06-02 00:56] wakes up
[1518-10-10 00:00] Guard #1889 begins shift
[1518-05-05 23:56] Guard #3461 begins shift
[1518-11-02 00:09] falls asleep
[1518-03-08 00:12] falls asleep
[1518-04-08 23:57] Guard #2339 begins shift
[1518-03-13 00:34] wakes up
[1518-09-25 00:54] wakes up
[1518-08-22 00:32] wakes up
[1518-11-19 00:57] wakes up
[1518-08-03 00:55] wakes up
[1518-04-13 00:47] wakes up
[1518-09-05 00:01] Guard #2089 begins shift
[1518-06-30 00:32] wakes up
[1518-07-24 00:35] wakes up
[1518-11-09 23:57] Guard #1237 begins shift
[1518-07-16 00:35] wakes up
[1518-11-06 00:57] wakes up
[1518-07-28 00:00] Guard #3229 begins shift
[1518-07-20 23:46] Guard #1901 begins shift
[1518-10-27 00:01] Guard #739 begins shift
[1518-06-30 00:03] Guard #2039 begins shift
[1518-09-18 00:02] Guard #641 begins shift
[1518-06-22 00:47] wakes up
[1518-05-26 00:57] wakes up
[1518-05-15 00:38] wakes up
[1518-08-01 00:56] wakes up
[1518-06-07 00:10] falls asleep
[1518-10-25 00:38] wakes up
[1518-06-09 00:25] wakes up
[1518-09-15 00:04] Guard #613 begins shift
[1518-10-09 00:03] falls asleep
[1518-05-31 00:33] wakes up
[1518-11-13 00:02] falls asleep
[1518-04-11 00:52] wakes up
[1518-08-11 00:54] wakes up
[1518-08-15 00:02] falls asleep
[1518-06-18 00:01] Guard #3229 begins shift
[1518-08-23 00:00] falls asleep
[1518-04-17 00:44] wakes up
[1518-05-30 00:51] falls asleep
[1518-09-28 00:03] Guard #3433 begins shift
[1518-09-22 00:16] wakes up
[1518-03-12 00:06] falls asleep
[1518-10-05 00:09] falls asleep
[1518-10-19 00:06] falls asleep
[1518-10-08 23:50] Guard #1237 begins shift
[1518-07-23 00:19] wakes up
[1518-06-26 00:57] wakes up
[1518-04-03 00:51] wakes up
[1518-07-23 00:57] wakes up
[1518-05-17 00:18] wakes up
[1518-06-28 00:22] falls asleep
[1518-10-20 00:39] wakes up
[1518-05-16 00:04] Guard #1697 begins shift
[1518-08-12 00:25] wakes up
[1518-04-04 00:37] wakes up
[1518-09-02 00:39] falls asleep
[1518-06-02 00:36] wakes up
[1518-06-19 00:00] Guard #2039 begins shift
[1518-07-06 00:20] falls asleep
[1518-05-19 00:59] wakes up
[1518-06-21 00:53] falls asleep
[1518-09-09 00:58] wakes up
[1518-09-26 23:50] Guard #2003 begins shift
[1518-09-17 00:51] falls asleep
[1518-10-23 00:57] falls asleep
[1518-11-15 00:14] falls asleep
[1518-11-20 00:16] falls asleep
[1518-04-28 00:32] falls asleep
[1518-10-28 00:08] falls asleep
[1518-03-04 00:58] wakes up
[1518-07-03 00:01] Guard #1237 begins shift
[1518-06-11 00:00] falls asleep
[1518-10-19 00:54] wakes up
[1518-03-22 00:31] wakes up
[1518-10-31 00:56] wakes up
[1518-08-08 23:46] Guard #1783 begins shift
[1518-10-22 00:01] Guard #1783 begins shift
[1518-10-27 00:50] falls asleep
[1518-07-22 00:27] falls asleep
[1518-08-15 00:51] wakes up
[1518-07-07 00:32] falls asleep
[1518-05-16 00:39] falls asleep
[1518-04-14 00:53] wakes up
[1518-04-03 23:59] Guard #1697 begins shift
[1518-03-11 00:56] wakes up
[1518-05-04 00:11] falls asleep
[1518-09-04 00:37] falls asleep
[1518-08-04 00:34] falls asleep
[1518-10-13 00:49] wakes up
[1518-05-09 00:34] wakes up
[1518-05-22 00:02] Guard #3229 begins shift
[1518-06-22 00:28] falls asleep
[1518-07-05 00:31] falls asleep
[1518-07-28 00:17] wakes up
[1518-06-17 00:28] wakes up
[1518-05-17 00:23] falls asleep
[1518-06-21 00:57] wakes up
[1518-09-09 00:28] falls asleep
[1518-03-21 23:56] Guard #2339 begins shift
[1518-03-18 00:55] wakes up
[1518-05-11 23:48] Guard #3229 begins shift
[1518-04-30 00:23] falls asleep
[1518-10-24 00:53] falls asleep
[1518-03-03 00:39] wakes up
[1518-09-15 23:59] Guard #1901 begins shift
[1518-07-12 00:54] falls asleep
[1518-03-18 23:58] Guard #3433 begins shift
[1518-08-15 00:20] falls asleep
[1518-07-21 00:00] falls asleep
[1518-07-06 23:49] Guard #2003 begins shift
[1518-03-30 00:41] falls asleep
[1518-06-01 00:41] wakes up
[1518-03-15 00:05] falls asleep
[1518-06-28 00:50] wakes up
[1518-04-07 23:57] Guard #739 begins shift
[1518-07-28 00:50] wakes up
[1518-05-04 00:52] falls asleep
[1518-05-03 00:43] wakes up
[1518-03-22 23:58] Guard #2039 begins shift
[1518-08-17 00:01] falls asleep
[1518-06-02 00:19] falls asleep
[1518-08-07 00:23] falls asleep
[1518-08-30 00:26] falls asleep
[1518-10-16 00:53] falls asleep
[1518-04-11 00:55] falls asleep
[1518-11-22 00:48] falls asleep
[1518-10-24 23:53] Guard #1237 begins shift
[1518-09-08 00:11] falls asleep
[1518-11-03 00:56] wakes up
[1518-10-22 00:37] wakes up
[1518-09-02 00:01] Guard #3229 begins shift
[1518-04-13 00:02] Guard #3229 begins shift
[1518-07-28 00:39] falls asleep
[1518-08-24 00:56] falls asleep
[1518-05-04 00:56] wakes up
[1518-04-04 00:17] falls asleep
[1518-05-16 00:53] falls asleep
[1518-09-13 00:08] falls asleep
[1518-08-14 00:03] falls asleep
[1518-04-23 00:54] wakes up
[1518-10-06 00:54] wakes up
[1518-05-13 00:01] falls asleep
[1518-04-24 00:49] wakes up
[1518-10-24 00:30] wakes up
[1518-03-27 00:02] Guard #2089 begins shift
[1518-03-06 00:48] falls asleep
[1518-09-09 00:54] falls asleep
[1518-04-18 00:55] wakes up
[1518-04-01 00:43] falls asleep
[1518-03-24 00:01] Guard #641 begins shift
[1518-10-19 00:25] wakes up
[1518-10-21 00:06] falls asleep
[1518-06-03 00:56] wakes up
[1518-07-16 00:03] Guard #277 begins shift
[1518-05-30 00:58] wakes up
[1518-04-01 00:30] wakes up
[1518-03-04 00:30] falls asleep
[1518-03-29 00:24] falls asleep
[1518-08-28 00:06] falls asleep
[1518-06-06 23:59] Guard #3433 begins shift
[1518-06-16 00:40] wakes up
[1518-07-05 00:41] wakes up
[1518-06-20 00:44] wakes up
[1518-04-24 00:35] wakes up
[1518-07-23 00:00] Guard #1237 begins shift
[1518-10-07 00:30] wakes up
[1518-05-03 00:01] Guard #1097 begins shift
[1518-10-05 23:56] Guard #1901 begins shift
[1518-05-16 00:42] wakes up
[1518-10-20 00:04] wakes up
[1518-07-09 00:04] Guard #2161 begins shift
[1518-10-16 00:04] Guard #1697 begins shift
[1518-10-23 00:48] falls asleep
[1518-05-19 00:57] falls asleep
[1518-06-22 23:57] Guard #1697 begins shift
[1518-03-15 00:40] wakes up
[1518-06-16 00:03] Guard #1069 begins shift
[1518-10-01 00:53] wakes up
[1518-11-22 23:54] Guard #1237 begins shift
[1518-05-08 00:53] wakes up
[1518-05-29 00:56] wakes up
[1518-09-28 00:54] wakes up
[1518-08-10 00:04] Guard #1901 begins shift
[1518-05-03 00:29] falls asleep
[1518-06-13 00:02] Guard #2339 begins shift
[1518-07-01 00:56] falls asleep
[1518-03-26 00:33] wakes up
[1518-07-14 00:00] falls asleep
[1518-03-02 23:58] Guard #3229 begins shift
[1518-07-07 00:55] wakes up
[1518-08-25 00:00] Guard #3433 begins shift
[1518-04-20 00:44] wakes up
[1518-10-15 00:07] falls asleep
[1518-09-13 23:58] Guard #1237 begins shift
[1518-03-13 00:20] falls asleep
[1518-10-14 23:59] Guard #1901 begins shift
[1518-05-23 00:21] falls asleep
[1518-08-05 00:31] falls asleep
[1518-04-08 00:46] wakes up
[1518-10-25 00:02] falls asleep
[1518-05-01 00:03] falls asleep
[1518-05-20 00:37] wakes up
[1518-11-06 23:53] Guard #1237 begins shift
[1518-03-14 00:24] falls asleep
[1518-08-14 23:50] Guard #2003 begins shift
[1518-08-07 00:02] Guard #1069 begins shift
[1518-09-23 00:36] wakes up
[1518-11-14 23:57] Guard #641 begins shift
[1518-03-21 00:57] wakes up
[1518-05-20 00:12] falls asleep
[1518-04-06 00:13] falls asleep
[1518-05-19 00:18] falls asleep
[1518-10-29 00:00] Guard #1697 begins shift
[1518-05-31 00:09] falls asleep
[1518-09-21 00:03] Guard #739 begins shift
[1518-04-02 00:01] Guard #3433 begins shift
[1518-05-18 00:14] wakes up
[1518-03-07 00:03] Guard #277 begins shift
[1518-09-20 00:38] wakes up
[1518-09-25 00:36] wakes up
[1518-04-26 00:02] Guard #2039 begins shift
[1518-09-12 00:12] falls asleep
[1518-05-27 00:01] Guard #739 begins shift
[1518-06-01 00:01] Guard #863 begins shift
[1518-08-02 00:37] wakes up
[1518-06-01 23:59] Guard #1901 begins shift
[1518-04-13 00:13] falls asleep
[1518-10-19 00:52] falls asleep
[1518-03-28 00:13] falls asleep
[1518-07-13 00:55] wakes up
[1518-04-12 00:04] Guard #3229 begins shift
[1518-09-27 00:18] wakes up
[1518-09-04 00:45] wakes up
[1518-07-06 00:45] falls asleep
[1518-03-19 00:41] falls asleep
[1518-06-29 00:09] falls asleep
[1518-07-07 00:24] wakes up
[1518-04-07 00:12] wakes up
[1518-09-11 00:03] falls asleep
[1518-03-15 00:46] falls asleep
[1518-04-07 00:58] wakes up
[1518-11-02 00:42] falls asleep
[1518-04-23 00:00] Guard #1097 begins shift
[1518-11-12 00:57] wakes up
[1518-09-03 00:09] wakes up
[1518-09-22 00:08] falls asleep
[1518-10-28 00:55] wakes up
[1518-07-26 00:31] wakes up
[1518-03-29 00:10] wakes up
[1518-04-14 00:38] falls asleep
[1518-10-02 00:08] falls asleep
[1518-11-14 00:39] falls asleep
[1518-10-17 00:13] falls asleep
[1518-05-15 00:01] Guard #1069 begins shift
[1518-04-13 00:42] wakes up
[1518-09-08 00:56] wakes up
[1518-03-22 00:59] wakes up
[1518-07-05 23:59] Guard #1237 begins shift
[1518-06-30 00:46] falls asleep
[1518-03-23 00:20] falls asleep
[1518-11-03 23:56] Guard #863 begins shift
[1518-06-14 00:53] falls asleep
[1518-05-09 00:29] falls asleep
[1518-04-26 23:59] Guard #947 begins shift
[1518-04-03 00:02] Guard #1069 begins shift
[1518-06-18 00:50] wakes up
[1518-11-03 00:27] falls asleep
[1518-11-12 00:01] Guard #1069 begins shift
[1518-08-19 00:51] falls asleep
[1518-04-06 23:54] Guard #1783 begins shift
[1518-04-18 00:04] Guard #3433 begins shift
[1518-06-09 00:23] falls asleep
[1518-08-02 00:01] Guard #3433 begins shift
[1518-06-11 00:41] wakes up
[1518-06-13 00:54] wakes up
[1518-09-20 00:02] falls asleep
[1518-10-27 00:45] falls asleep
[1518-09-04 00:26] falls asleep
[1518-07-26 00:26] falls asleep
[1518-07-11 00:52] wakes up
[1518-08-18 23:47] Guard #1889 begins shift
[1518-05-27 00:56] wakes up
[1518-07-11 00:44] falls asleep
[1518-09-08 00:28] wakes up
[1518-05-21 00:53] wakes up
[1518-11-19 00:44] wakes up
[1518-03-04 00:41] wakes up
[1518-10-16 00:58] wakes up
[1518-06-16 23:48] Guard #277 begins shift
[1518-11-20 00:02] Guard #613 begins shift
[1518-03-28 00:33] wakes up
[1518-07-01 00:53] wakes up
[1518-10-07 00:25] falls asleep
[1518-11-15 00:56] wakes up
[1518-07-31 00:06] falls asleep
[1518-11-16 00:32] wakes up
[1518-05-26 00:53] falls asleep
[1518-03-29 23:58] Guard #1889 begins shift
[1518-08-04 00:59] wakes up
[1518-09-04 00:53] wakes up
[1518-08-19 00:02] falls asleep
[1518-10-10 00:37] falls asleep
[1518-08-08 00:24] falls asleep
[1518-03-16 00:17] wakes up
[1518-09-18 23:57] Guard #613 begins shift
[1518-04-11 00:56] wakes up
[1518-09-23 00:01] Guard #1697 begins shift
[1518-08-11 00:32] falls asleep
[1518-04-03 00:54] falls asleep
[1518-08-22 00:27] falls asleep
[1518-05-23 00:51] falls asleep
[1518-04-14 00:01] Guard #3433 begins shift
[1518-07-30 00:38] wakes up
[1518-05-31 00:59] wakes up
[1518-06-10 00:03] Guard #3229 begins shift
[1518-10-25 00:57] falls asleep
[1518-09-25 00:52] falls asleep
[1518-06-28 00:41] falls asleep
[1518-03-05 00:56] wakes up
[1518-10-28 00:01] Guard #947 begins shift
[1518-03-23 00:43] wakes up
[1518-03-10 23:58] Guard #739 begins shift
[1518-04-10 00:13] falls asleep
[1518-07-03 23:57] Guard #2003 begins shift
[1518-11-20 00:55] wakes up
[1518-07-20 00:57] wakes up
[1518-03-24 00:23] wakes up
[1518-10-20 00:35] falls asleep
[1518-07-01 23:59] Guard #1237 begins shift
[1518-06-28 23:58] Guard #277 begins shift
[1518-06-08 00:29] falls asleep
[1518-07-09 00:58] wakes up
[1518-05-05 00:59] wakes up
[1518-07-08 00:54] wakes up
[1518-07-12 00:17] falls asleep
[1518-04-29 00:37] wakes up
[1518-09-17 00:01] Guard #2339 begins shift
[1518-03-03 00:18] falls asleep
[1518-05-12 00:04] falls asleep
[1518-07-23 23:57] Guard #2039 begins shift
[1518-05-08 23:57] Guard #3433 begins shift
[1518-10-29 00:52] falls asleep
[1518-11-05 00:00] Guard #2161 begins shift
[1518-03-26 00:47] wakes up
[1518-06-09 00:00] Guard #1237 begins shift
[1518-07-10 00:56] falls asleep
[1518-06-06 00:56] wakes up
[1518-07-29 00:35] wakes up
[1518-03-14 00:57] wakes up
[1518-08-08 00:59] wakes up
[1518-05-04 00:00] Guard #1783 begins shift
[1518-04-15 00:39] wakes up
[1518-08-16 00:17] wakes up
[1518-11-19 00:03] falls asleep
[1518-03-26 00:38] falls asleep
[1518-03-05 00:00] Guard #3229 begins shift
[1518-08-10 00:30] falls asleep
[1518-05-03 00:56] falls asleep
[1518-11-07 00:47] wakes up
[1518-07-29 00:22] falls asleep
[1518-08-27 00:31] falls asleep
[1518-07-31 00:03] Guard #2003 begins shift
[1518-07-18 23:56] Guard #1783 begins shift
[1518-06-17 00:05] falls asleep
[1518-08-19 00:52] wakes up
[1518-11-19 00:53] falls asleep
[1518-05-02 00:02] Guard #641 begins shift
[1518-11-17 00:33] falls asleep
[1518-08-05 00:48] wakes up
[1518-11-06 00:56] falls asleep
[1518-08-16 00:21] falls asleep
[1518-03-17 00:49] wakes up
[1518-09-08 00:32] falls asleep
[1518-08-26 00:56] wakes up
[1518-09-30 00:21] falls asleep
[1518-07-15 00:08] falls asleep
[1518-07-25 00:15] falls asleep
[1518-08-13 00:00] Guard #2161 begins shift
[1518-03-10 00:04] Guard #1783 begins shift
[1518-09-03 23:59] Guard #2003 begins shift
[1518-08-15 23:56] Guard #1237 begins shift
[1518-05-07 00:36] wakes up
[1518-10-26 00:25] falls asleep
[1518-03-22 00:34] falls asleep
[1518-08-13 00:40] falls asleep
[1518-03-24 00:18] falls asleep
[1518-07-22 00:04] Guard #1237 begins shift
[1518-10-14 00:56] falls asleep
[1518-09-26 00:38] falls asleep
[1518-10-26 00:02] Guard #3229 begins shift
[1518-08-21 00:23] falls asleep
[1518-09-15 00:58] wakes up
[1518-08-06 00:34] falls asleep
[1518-06-12 00:03] Guard #1901 begins shift
[1518-11-06 00:01] Guard #641 begins shift
[1518-09-09 00:34] wakes up
[1518-04-21 00:04] Guard #2089 begins shift
[1518-10-01 00:01] Guard #2039 begins shift
[1518-08-17 00:47] falls asleep
[1518-06-08 00:14] wakes up
[1518-05-17 00:55] wakes up
[1518-07-06 00:33] wakes up
[1518-03-18 00:05] falls asleep
[1518-08-01 00:45] falls asleep
[1518-04-20 00:05] falls asleep
[1518-03-29 00:00] falls asleep
[1518-06-18 00:26] falls asleep
[1518-10-03 00:54] wakes up
[1518-07-22 00:37] wakes up
[1518-08-16 00:15] falls asleep
[1518-03-31 00:04] Guard #1097 begins shift
[1518-09-02 00:26] falls asleep
[1518-09-13 00:48] wakes up
[1518-10-27 00:53] wakes up
[1518-10-24 00:01] Guard #947 begins shift
[1518-03-06 00:51] wakes up
[1518-04-24 00:38] falls asleep
[1518-06-21 00:01] Guard #3559 begins shift
[1518-09-10 23:50] Guard #2039 begins shift
[1518-08-16 23:54] Guard #277 begins shift
[1518-06-10 00:48] wakes up
[1518-09-24 00:47] wakes up
