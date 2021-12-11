#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// sig loop. SIGINT 재정의 함. 계속 루프 돌려서 안죽음

static void signal_handler (int signo) {
	printf("Catch SIGINT!, but no stop\n");
}

int main (void) {
	if (signal (SIGINT, signal_handler) == SIG_ERR) {
		printf("Can't catch SIGINT!\n");
		exit(1);
	}
	for (;;)
		pause();
	return 0;
}
