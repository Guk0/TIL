#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>



int main(void) {
	void exithandling(void);
	void goodbyemessage(void);
	int ret;
	
	ret = atexit(exithandling);
	if (ret != 0) perror("Error in atexit\n");
	ret = atexit(goodbyemessage);
	if (ret != 0) perror("Error in atexit\n");
	exit(EXIT_SUCCESS);
}

void exithandling(void) {
	printf("exit handling\n");
}

void goodbyemessage(void) {
	printf("see you again!\n");
}

// see you again!
// exit handling
// 순으로 출력
