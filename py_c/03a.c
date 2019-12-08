#include <stdio.h>
#include <string.h>

#define BUFLEN 256

int main(int argc, char *argv[]) {
	unsigned char fabric[1000][1000];
	char inbuf[BUFLEN];
	int claim_id, x, y, width, height;
	int overlapped=0;

	memset(fabric, 0, sizeof(fabric));

	while (fgets(inbuf, BUFLEN, stdin)) {
		sscanf(inbuf, "#%d @ %d,%d: %dx%d\n", &claim_id, &x, &y, &width, &height);
//		printf("#%d %d %d %d %d : %s", claim_id, x, y, width, height, s);
		for (int xi=x; xi<x+width; xi++) {
			for (int yi=y; yi<y+height; yi++) {
				if (fabric[xi][yi]<255) {
					fabric[xi][yi]++;
				}
			}
		}
	}

	for (int xi=0; xi<1000; xi++) {
		for (int yi=0; yi<1000; yi++) {
			if (fabric[xi][yi]>1) {
				overlapped++;
			}
		}
	}

	printf("overlapped: %d\n", overlapped);
}

