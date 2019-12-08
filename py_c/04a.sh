#!/bin/bash

sort 4.txt |\
	sed -e 's/Guard #//'|\
	awk '{print $2, $3}' |\
	sed 's/^..://' |\
	tr -d ']'|\
	awk '
		BEGIN {
			startsleep=0;
			id=0;
		}
	 	/falls/ {
			startsleep=$1;
			next;
		}
		/wakes/ {
			endsleep=$1
			sleeptimes[id]+=endsleep-startsleep; 
			if (id==1237) {
#				print startsleep, endsleep; 
				mi=startsleep-0;
				do {
					sleepmins[mi]++;
					mi++;
				} while (mi<endsleep);
			}
			next;
		}
		{
			id=$2;
		}
		END { 
			print "END";
			mt=0;
			for (lid in sleeptimes) {
# print lid, sleeptimes[lid];
				if (sleeptimes[lid]>mt) {
					mt=sleeptimes[lid];
					mlid=lid;
				}
			}
#			print mlid, sleeptimes[mlid];
			mt=0;
			for (mid in sleepmins) {
				print mid, sleepmins[mid];
				if (sleepmins[mid]>mt) {
					mt=sleepmins[mid];
					mlid=mid;
				}
			}
#			print mlid,  sleepmins[mlid];
		}'
		 		
