#include <stdio.h>
#include <string.h>

#define BUFLEN 256

int main(int argc, char *argv[]) {
	unsigned char fabric[1000][1000];
	char inbuf[BUFLEN];
	char *s;
	int id=0, x, y, w, h;
	int overlap_found=0;
	FILE *infile;

	memset(fabric, 0, sizeof(fabric));

	infile=fopen("3.txt", "r");
	if (!infile) return 1;

	while ( (id!=1409) && ((s=fgets(inbuf, BUFLEN, infile))) ) {
		sscanf(s, "#%d @ %d,%d: %dx%d\n", &id, &x, &y, &w, &h);
		for (int xi=x; xi<x+w; xi++) {
			for (int yi=y; yi<y+h; yi++) {
				if (fabric[xi][yi]<255) {
					fabric[xi][yi]++;
				}
			}
		}
	}

	rewind(infile);
	while ((s=fgets(inbuf, BUFLEN, infile))) {
		sscanf(s, "#%d @ %d,%d: %dx%d\n", &id, &x, &y, &w, &h);
//		printf("#%d %d %d %d %d : %s", id, x, y, w, h, s);
		overlap_found=0;
		for (int xi=x; xi<x+w; xi++) {
			for (int yi=y; yi<y+h; yi++) {
				if (fabric[xi][yi]>1) {
					overlap_found=1;
					break;
				}
			}
			if (overlap_found) 
				break;
		}
		if (!overlap_found) {
			printf("id: #%d\n", id);
			break;
		}
	}
}

