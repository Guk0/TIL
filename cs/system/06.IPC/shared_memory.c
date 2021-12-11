#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
	int shmid, pid;
	char *shmaddr_parent, *shmaddr_child;
	shmid = shmget((key_t)1234, 10, IPC_CREAT|0644);
	if (shmid == -1) { // 안 만들어졌을때
		perror("shmget error\n");
		exit(1);
	}
	pid = fork(); // fork
	if (pid > 0) { // parent process
		wait(0);
		shmaddr_parent = (char *)shmat(shmid, (char *)NULL, 0);
		printf("%s\n", shmaddr_parent);
		shmdt((char *)shmaddr_parent);
	}
	else { //child process
		shmaddr_child = (char *)shmat(shmid, (char *)NULL, 0);
		strcpy((char *)shmaddr_child, "Hello Parent");
		shmdt((char *)shmaddr_child); // 해제해도 위에 텍스트는 남아있음
		exit(0);
	}
	shmctl(shmid, IPC_RMID, (struct shmid_ds *)NULL); // 메모리 삭제
	return 0;
}

