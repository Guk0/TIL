#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

void *t_function(void *ptr) {
	char *message;
	message = (char *)ptr;
	printf("%s start \n", message);
	sleep(5);
	printf("%s end\n", message);
	return 0;
}

int main() {
	pthread_t thread1, thread2;
	const char *message1 = "Thread1";
	const char *message2 = "Thread2";
	int ret, status;

	ret = pthread_create(&thread1, NULL, t_function, (void *)message1);
	if (ret < 0) {
		perror("thread create error");
	}
	pthread_join(thread1, (void **)&status);
	//pthread_detach(thread1);

	printf("thread1 returns: %d\n", status);
	
	ret = pthread_create(&thread2, NULL, t_function, (void *)message2);
	if (ret < 0) {
		perror("thread create error");
	}
	pthread_join(thread2, (void **)&satus);
	//pthread_detach(thread2);

	sleep(10);
	return 0;
}
