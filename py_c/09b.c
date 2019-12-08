#include <stdio.h>
#include <string.h>
#include <stdint.h>

// #define NUM_PLAYERS 9
// #define MAX_MARBLE 25

// #define NUM_PLAYERS 10
// #define MAX_MARBLE 1618
// #define DEBUG 1

#define NUM_PLAYERS 462
#define MAX_MARBLE 7193800

int marble_circle[MAX_MARBLE+2];
int circle_len = 1;

int add_new_marble(int act_id, int new_id) {
	int insert_point = act_id + 2;
	if (insert_point>circle_len) {
		insert_point -= circle_len;
	}
	if (insert_point != circle_len) {
		// memmove(marble_circle+insert_point+1, marble_circle+insert_point, sizeof(int)*(circle_len-insert_point+1));
	}
	marble_circle[insert_point] = new_id;
	circle_len++;
	return insert_point;
}

void remove_marble_7(int *act_id, int *seven_score) {
	int remove_point = *act_id - 7;
	if (remove_point<0) {
		remove_point += circle_len;
	}
	*seven_score = marble_circle[remove_point];
	*act_id = remove_point;
	// memmove(marble_circle+remove_point, marble_circle+remove_point+1, sizeof(int)*(circle_len-remove_point+1));
	circle_len--;
}

int main() {
	int act_marble = 0;
	int marble_id = 1;
	int player_id = 1;
	int score = 0;
	uint64_t max_score = 0;
	uint64_t player_score[NUM_PLAYERS+2];

	memset(marble_circle, 0, sizeof(marble_circle));
	memset(player_score, 0, sizeof(player_score));

	while (marble_id<=MAX_MARBLE) {
		if (marble_id%10000==0) {
			printf("%d\n", marble_id);
		}
		if (marble_id%23 == 0) {
			remove_marble_7(&act_marble, &score);
			player_score[player_id] += marble_id+score;
		} else {
			act_marble = add_new_marble(act_marble, marble_id);
		}

#ifdef DEBUG
		printf("n: % 3d p: % 2d a: % 3d m:", marble_id, player_id, act_marble);
		for (int i=0; i<circle_len; i++) {
			printf("% 5d", marble_circle[i]);
		}
		printf("\n");
#endif

		player_id++;
		if (player_id>NUM_PLAYERS) {
			player_id = 1;
		}
		marble_id++;
	}
	for (int i=1; i<=NUM_PLAYERS; i++) {
		if (player_score[i]>max_score) {
			max_score = player_score[i];
		}
		printf("% 3d %ld\n", i, player_score[i]);
	}
	printf("max score: %ld\n", max_score);
	return 0;
}



