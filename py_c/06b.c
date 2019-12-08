#include <stdio.h>
#include <string.h>

#define MAXX 400
#define MAXY 400

#define NUM_IDS 100
#define MAX_DST 10000

#define abs(x) (x>=0?(x):(-(x)))

typedef struct {int x; int y;} coords_t;

// #define MAXX 12
// #define MAXY 12

int manhattan_distance(coords_t c1, coords_t c2) {
	return abs(c1.x-c2.x)+abs(c1.y-c2.y);
}


int main() {
	char inbuf[256];
	int x, y;
	int id;
	int num_safe;
	int num_ids;
	coords_t coords[NUM_IDS+1];
	int sum_dst;


	id=0;
	FILE *infile=fopen("6.txt", "r");
	while (fgets(inbuf, sizeof(inbuf), infile)) {
		sscanf(inbuf, "%d %d\n", &x, &y);
		coords[id] = (coords_t){x, y};
		id++;
	}
	num_ids=id;
	printf("Num ids: %d\n", num_ids);

	fclose(infile);

	num_safe=0;
	for (x=0; x<MAXX; x++) {
		for (y=0; y<MAXY; y++) {
			sum_dst=0;
			for (int id=0; id<num_ids; id++) {
				int md=manhattan_distance(coords[id], (coords_t){x, y});
				sum_dst+=md;
				if (sum_dst>=MAX_DST) {
					break;
				}
			}
			if (sum_dst<MAX_DST) {
				printf("% 4d,%-4d %d\n", x, y, sum_dst);
				num_safe++;
			}
		}
	}

	printf("num safe: %d\n", num_safe);

	return 0;
}

	
