#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/msg.h>

typedef struct msgbuf {
	long type;
	char text[50];
} MsgBuf;


int main(void) {
	int msgid, len;
	MsgBuf msg;
	key_t key = 1234;
	msgid = msgget(key, IPC_CREAT|0644); //메세지큐 생성
	if (msgid == -1) {
		perror("msgget");
		exit(1);
	}
	msg.type = 1;
	strcpy(msg.text, "hello message queue\n");
	if (msgsnd(msgid, (void *)&msg, 50, IPC_NOWAIT == -1)) {
		perror("msgsnd");
		exit(1);
	}
	len = msgrcv(msgid, &msg, 50, 0, 0);
	printf("Received Message is '%s' [%d]\n", msg.text, len);
	msgctl(msgid, IPC_RMID, 0); // IPC_RMID + 인자 0 =  메세지큐 삭제
	return 0;
}
