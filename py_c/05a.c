#include <stdio.h>
#include <string.h>

#define BUFLEN 100000

int main() {
	char *inbuf;
	char c0, c1;

	inbuf=(char*)malloc(BUFLEN);

	FILE *infile=fopen("5.txt", "r");
	fread(inbuf, BUFLEN, sizeof(char), infile);
	fclose(infile);

	int i=0;
	while (i<strlen(inbuf)-1) {
		c0=inbuf[i];
		c1=inbuf[i+1];
		if ( ((c0<='z') && (c0-'a'+'A'==c1)) ||
			 ((c0>='A') && (c0-'A'+'a'==c1)) ) {
			memmove(inbuf+i, inbuf+i+2, strlen(inbuf)-i-2+1);
			if (i>0) {
				i--;
			}
			continue;
		}
		i++;
	}
	printf("%ld %s\n", strlen(inbuf)-1, inbuf);
	return 0;
}

	
