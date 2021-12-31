# IPC
### 공유메모리(shared memory)
- 커널영역에 메모리를 만들고 해당 공간을 변수처럼 사용
- 공유메모리 **key**를 가지고 여러 프로세스가 접근 가능
- shmget, shmat, shmdt, shmctl

 