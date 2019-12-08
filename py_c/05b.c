#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFLEN 100000

int react(char *instr) {
	char c0, c1;
	char *tmpbuf=(char*)malloc(BUFLEN);
	int rv;

	strncpy(tmpbuf, instr, BUFLEN);

	int i=0;
	while (i<strlen(tmpbuf)-1) {
		c0=tmpbuf[i];
		c1=tmpbuf[i+1];
		if ( ((c0<='z') && (c0-'a'+'A'==c1)) ||
			 ((c0>='A') && (c0-'A'+'a'==c1)) ) {
			memmove(tmpbuf+i, tmpbuf+i+2, strlen(tmpbuf)-i-2+1);
			if (i>0) {
				i--;
			}
			continue;
		}
		i++;
	}
	rv=strlen(tmpbuf)-1;
	free(tmpbuf);
	return rv;
}

int remove_react(char *instr, char c) {
	int rv;
	char *tmpbuf=(char*)malloc(BUFLEN);

	strncpy(tmpbuf, instr, BUFLEN);

	int i=0;
	while (i<strlen(tmpbuf)) {
		if ( (tmpbuf[i]==c) || (tmpbuf[i]==c-'a'+'A') ) {
			memmove(tmpbuf+i, tmpbuf+i+1, strlen(tmpbuf)-i-1+1);
			continue;
		}
		i++;
	}
	rv=react(tmpbuf);
	free(tmpbuf);
	return rv;
}

int main() {
	char *inbuf;

	inbuf=(char*)malloc(BUFLEN);

	FILE *infile=fopen("5.txt", "r");
	fread(inbuf, BUFLEN, sizeof(char), infile);
	fclose(infile);

	for (char x='a'; x<='z'; x++) {
		printf("%c %d\n", x, remove_react(inbuf, x));
	}
	return 0;
}

	
