#include <stdio.h>
#include <string.h>
#include <stdint.h>


uint64_t run_program(int reg0, uint64_t max_iters) {
	int r[6];
	uint64_t iter_no=0;

	memset(r, 0, sizeof(r));
	r[0] = reg0;

	// Instruction pointer: 4
	//#ip 4
	//  0. seti 123 0 5
	r[5] = 123;							iter_no++;
	//  1. bani 5 456 5
	r[5] = r[5] & 456;					iter_no++;
	//  2. eqri 5 72 5
	r[5] = (r[5] == 72)?1:0;			iter_no++;
	//  3. addr 5 4 4
	if (r[5] != 1) {
	//  4. seti 0 0 4
		printf("Endless loop detected, abort\n");
		return 0;
	}
	//  5. seti 0 9 5
	r[5] = 0;							iter_no++;
label6:
	//  6. bori 5 65536 3
	r[3] = r[5] | 65536;				iter_no++;
	//  7. seti 10828530 0 5
	r[5] = 10828530;					iter_no++;
label8:
	if (iter_no > max_iters) {
		printf("Over maxiters, r0: %d, iters: %lu\n", reg0, iter_no);
		return 0;
	}
	/*
	if (iter_no % 100000000 < 10000) {
		printf("r0: %d iter: %lu\n", reg0, iter_no);
	}
	*/
	//  8. bani 3 255 2
	r[2] = r[3] & 255;					iter_no++;
	//  9. addr 5 2 5
	r[5] = r[5] + r[2];					iter_no++;
	// 10. bani 5 16777215 5
	r[5] = r[5] & 16777215;				iter_no++; // 0xFFFFFF
	// 11. muli 5 65899 5
	r[5] = r[5] * 65899;				iter_no++;
	// 12. bani 5 16777215 5
	r[5] = r[5] & 16777215;				iter_no++; // 0xFFFFFF
	// 13. gtir 256 3 2
	r[2] = (256>r[3])?1:0;				iter_no++;
	// 14. addr 2 4 4
	if (r[2]>0) {
		iter_no++;
		goto label16;
	}
	// 15. addi 4 1 4
	iter_no++;
	goto label17;
label16:
	// 16. seti 27 4 4
	iter_no++;
	goto label28;
label17:
	// 17. seti 0 4 2
	r[2] = 0;							iter_no++;
label18:
	// 18. addi 2 1 1
	r[1] = r[2] + 1;					iter_no++;
	// 19. muli 1 256 1
	r[1] = r[1] * 256;					iter_no++;
	// 20. gtrr 1 3 1
	r[1] = (r[1]>r[3])?1:0;				iter_no++;
	// 21. addr 1 4 4
	if (r[1]>0) {
		iter_no++;
		goto label23;
	}
	// 22. addi 4 1 4
	iter_no++;
	goto label24;
label23:
	// 23. seti 25 9 4
	iter_no++;
	goto label26;
label24:
	// 24. addi 2 1 2
	r[2] = r[2] + 1;					iter_no++;
	// 25. seti 17 9 4
	iter_no++;
	goto label18;
label26:
	// 26. setr 2 8 3
	r[3] = r[2];						iter_no++;
	// 27. seti 7 9 4
	iter_no++;
	goto label8;
label28:
	// 28. eqrr 5 0 2
	r[2] = (r[5] == r[0])?1:0;			iter_no++;
	// 29. addr 2 4 4
	if (r[2]>0) {
		printf("Instruction pointer overflow, r0: %d, iters: %lu\n", reg0, iter_no);
		return iter_no;
	}
	// 30. seti 5 5 4
	iter_no++;
	goto label6;
}

int main() {
	char inbuf[256];
	int r0;
	uint64_t max_iter = 0;
	uint64_t act_iter = 0;
	int max_r0=0;

	run_program(202209, 20000000000);
//	run_program(1, 20000000000);
	FILE *infile = fopen("21x2.out", "r");
	while (fgets(inbuf, sizeof(inbuf), infile)) {
		sscanf(inbuf, "%d\n", &r0);
		act_iter = run_program(r0, 20000000000);
		if (act_iter>max_iter) {
			printf("New maxiter, reg0: %d, iters: %lu\n", r0, act_iter);
			max_iter = act_iter;
			max_r0 = r0;
		}
	}
	printf("max r0: %d\n", max_r0);
	return 0;
}

