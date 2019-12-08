#include <stdio.h>
#include <string.h>

#define MAXX 400
#define MAXY 400
// #define MAXX 12
// #define MAXY 12

void print_field(char field[MAXX][MAXY]) {
	for (int y=0; y<MAXY; y++) {
		for (int x=0; x<MAXX; x++) {
			printf("% 2d ", field[x][y]);
		}
		printf("\n");
	}
	printf("\n");
}

void test_and_remove(char field[MAXX][MAXY], int id) {
	if (id<=0)
		return;
	for (int x=1; x<MAXX-1; x++) {
		for (int y=1; y<MAXY-1; y++) {
			if (field[x][y]==id) {
				field[x][y]=0;
			}
		}
	}
}

int count_ids(char field[MAXX][MAXY], int id) {
	int counter=0;
	for (int x=1; x<MAXX-1; x++) {
		for (int y=1; y<MAXY-1; y++) {
			if (field[x][y]==id) {
				counter++;
			}
		}
	}
	return counter;
}

int main() {
	char inbuf[256];
	char field[MAXX][MAXY];
	char field_new[MAXX][MAXY];
	int x, y;
	int not_filled;
	int tmpid, id;

	memset(field, 0, sizeof(field));

	id=1;
	FILE *infile=fopen("6.txt", "r");
	while (fgets(inbuf, sizeof(inbuf), infile)) {
		sscanf(inbuf, "%d %d\n", &x, &y);
		field[x][y]=id;
		id++;
	}
	fclose(infile);
	memcpy(field_new, field, sizeof(field));

	not_filled=1;
	while (not_filled>0) {
//		print_field(field);
		not_filled=0;
		for (x=1; x<MAXX-1; x++) {
			for (y=1; y<MAXY-1; y++) {
				if (field[x][y]!=0) {
					continue;
				}
				not_filled++;
				tmpid=0;
				if (field[x+1][y]>0) tmpid=field[x+1][y];
				if (field[x-1][y]>0) {
					if ( (tmpid>0) && (tmpid!=field[x-1][y]) ) {
						field_new[x][y]=-1;
						continue;
					} else {
						tmpid=field[x-1][y];
					}
				}
				if (field[x][y-1]>0) {
					if ( (tmpid>0) && (tmpid!=field[x][y-1]) ) {
						field_new[x][y]=-1;
						continue;
					} else {
						tmpid=field[x][y-1];
					}
				}
				if (field[x][y+1]>0) {
					if ( (tmpid>0) && (tmpid!=field[x][y+1]) ) {
						field_new[x][y]=-1;
						continue;
					} else {
						tmpid=field[x][y+1];
					}
				}
				if (tmpid>0) {
					field_new[x][y]=tmpid;
				}
			}
		}
		memcpy(field, field_new, sizeof(field));
	}
//	print_field(field);
	for (x=1; x<MAXX-1; x++) {
		test_and_remove(field, field[x][1]);
		test_and_remove(field, field[x][MAXY-2]);
	}
	for (y=1; y<MAXY-1; y++) {
		test_and_remove(field, field[1][y]);
		test_and_remove(field, field[MAXX-2][y]);
	}

//	print_field(field);
	for (id=1; id<=50; id++) {
		printf("% 2d %d\n", id, count_ids(field, id));
	}

	return 0;
}

	
