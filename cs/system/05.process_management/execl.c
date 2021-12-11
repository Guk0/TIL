#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>


int main()
{
	printf("execute ls\n");
	execl("/bin/ls", "ls", "-l", NULL);
	perror("execl is faild\n");
	exit(1);
}
