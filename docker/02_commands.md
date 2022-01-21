# Commands
## 기본적인 도커 클라이언트 명령어
`docker run hello-world`  
- docker : 도커 클라이언트 언급  
- run : 컨테이너 생성 및 실행
- hello-world : 이 컨테이너를 위한 이미지

<br>

## 이미지로 컨테이너 생성하는 순서
1. 먼저 파일 스냅샷이 되어 있는 것을 컨테이너의 하드 디스크 부분에 올린다.
2. 시작 커맨드를 이용하여 어플리케이션을 실행한다.
    

`docker run 이미지이름 ls`

- ls : ls 커맨드가 들어가는 자리는 원래 이미지가 가지고 있는 시작명령어를 무시하고 해당 자리에 들어가는 커맨드를 실행하게 함.

`docker ps`
- ps : process status(실행중인 컨테이너 나열)

`docker ps --format 'table{{.Names}}\table{{.Image}}'`
- ps 중 보고 싶은 것만 나열

`docker ps -a`

- 모든 컨테이너 나열

`docker run alpine ping localhost`

- alpine 이미지로 도커 돌리고 localhost에 핑찍기

<br>

## 도커 컨테이너의 생명주기
docker run 은 docker create, docker start가 합쳐진 명령어임.

`docker start hello-world`

- 정보들을 반환하지 않음.

`docker start -a hello-world`

- 정보들을 반환함.

`docker stop hello-world`

- Gracefully하게 중지시킴. 자비롭게 그동안 하던 작업들을 완료하고 컨테이너를 중지시킨다.

`docker kill hello-world`

- Stop과 달리 어떠한 것도 기다리지않고 중지시킨다.
    
    

`docker rm <아이디/이름>`

- 중지된 컨테이너 삭제(docker ps -a)
- 실행중인 컨테이너는 먼저 중지한 후에 삭제 가능

`docker rm <docker ps -a -q>`

- 모든 컨테이너 삭제

`docker rmi <이미지 id>`

- 이미지 삭제

`docker system prune`

- 한번에 컨테이너, 이미지, 네트워크 모두 삭제.

`docker exec <컨테이너 아이디>`

- 이미 실행중인 컨테이너에 명령어를 전달.

</br>

## redis 실행시켜보기
`docker run redis`

- redis 쭉 받아지고
- 레디스가 실행됨.

이상태에서 다른 터미널로 `docker exec -it <컨테이너 아이디> redis-cli`

- -it : it를 붙여줘야 명령어를 실행한 후 계속 명령어를 적을 수 있음.(interactive, terminal flag)

`docker exec -it <컨테이너 아이디> sh`

- sh, bash, zsh, powershell
- 컨테이너를 쉘환경으로 접근