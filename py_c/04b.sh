#!/bin/bash

sort 4.txt |\
sed -e 's/Guard #//'|\
awk '{print $2, $3}' |\
sed 's/^..://' |\
tr -d ']'|\
awk '
	BEGIN {
		startsleep=0;
		guard_id=0;
	}
	/falls/ {
		startsleep=$1;
		next;
	}
	/wakes/ {
		endsleep=$1
		sleeptimes[guard_id]+=endsleep-startsleep; 
		mi=startsleep-0;
		do {
			sleepmins[guard_id][mi]++;
			mi++;
		} while (mi<endsleep);
		next;
	}
	{
		guard_id=$2;
	}
	END { 
		max_time=0;
		for (guard_id in sleepmins) {
			for (minute in sleepmins[guard_id]) {
				print guard_id, minute, sleepmins[guard_id][minute];
				if (sleepmins[guard_id][minute]>max_time) {
					max_time=sleepmins[guard_id][minute];
					max_guard_id=guard_id;
					max_minute=minute;
				}
			}
		}
		print max_guard_id, max_minute, sleepmins[max_guard_id][max_minute], max_guard_id*max_minute;
	}'
		 		
