#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <string.h>


int main(int argc, const char *argv[]) {
	char *filepath = "link.txt";
	struct stat fileInfo;
	char *update = "hello mmap";
	int fd = open(filepath, O_RDWR, (mode_t)0600); // link.txt를 read, write 권한으로 읽어옴.
	if (fd == -1) {
		printf("can't open file\n");
		exit(EXIT_FAILURE);
	}

	fstat(fd, &fileInfo);  // 파일 정보를 &fileInfo에 넣어주는 함수. 파일 시스템 
	printf("File size is %lld\n", fileInfo.st_size); //fileInfo.st_size : 파일의 사이즈
	
	char *map = mmap(0, fileInfo.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
	if (map == MAP_FAILED) {
		close(fd);
		perror("Error mmapping the file");
		exit(EXIT_FAILURE);
	}
	

	printf("%ld", strlen(update));
	for (size_t i = 0; i < strlen(update); i++) {
		printf("Writing Character %c at %zu\n", update[i], i);
		map[i] = update[i];
	}
	
	if (msync(map, fileInfo.st_size, MS_SYNC) == -1) {
		perror("Could not sync the file to disk");
	}
	
	if (munmap(map, fileInfo.st_size) == -1) {
		close(fd);
		perror("Error un-mmapping the file");
	}
	
}
