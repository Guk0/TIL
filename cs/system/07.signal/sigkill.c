#include <sys/types.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>


int main(int argc, char **argv) 
{
	int pid, result;
	int sig_num;
	if (argc != 3) {
		printf("usage %s [pid][signum]\n", argv[0]);
		exit(1);
	}
	pid = atoi(argv[1]);
	sig_num = atoi(argv[2]);
	result = kill(pid, sig_num);
	if (result < 0) {
		perror("To send Signal is failed\n");
		exit(1);
	}
	return 0;
}

// ps로 위 SIGINT 코드 pid 확인 후 위 main 함수에 인자로 넣어줌. 2는 시그널 넘버(kill -l 로 확인)
// ./sigkill 20393 2
// 하면 죽일 수 없다고 나옴. 왜냐하면 막아놨으니
