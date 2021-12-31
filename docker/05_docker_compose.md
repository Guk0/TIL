# Docker Compose
## docker compose
다중 컨테이너 도커 어플리케이션을 정의하고 실행하기 위한 도구

## Redis
레디스란?

Redis는 메모리 기반의 키-값 구조 데이터 관리 시스템이며 모든 데이터를 메모리에 저장하고 빠르게 조회할 수 있는 비 관계형 데이터베이스(NoSQL).

메모리에 저장하기 때문에 Mysql같은 데이터베이스에 저장하는 것과 데이터를 불러올 때 훨씬 빠르게 처리할 수 있으며 비록 메모리에 저장하지만 영속적으로도 보관이 가능하다.

그래서 서버를 재부팅해도 데이터를 유지할 수 있는 장점이 있다.

redis 컨테이너와 nodejs 컨테이너간 통신을 위해서는 설정을 추가해줘야함.

`docker run redis`

`docker run guk0/docker-compose`

멀티 컨테이너 상황에서 쉽게 네트워크를 연결해주기 위해 docker compose를 사용한다

## compose

docker-compose.yml 작성 후


`docker-compose up`

**`docker-compose up --build`**

다시 빌드

**`docker-compose up -d --build`**

detach : 백그라운드에서 실행가능.

`docker compose down`

다른 터미널에서 도커 컴포즈를 끌 때