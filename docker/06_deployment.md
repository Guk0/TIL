# Deployment
## 배포
docker 파일은 dev, prod 등 개발환경에 따라 나눠 작성한다. dev 환경에서는 Dockerfile.dev와 같이 .dev파일로 생성한다.

Dockerfile.dev로 dockerfile을 생성하고 빌드하면 아래와 같은 오류가 발생한다.

unable to evaluate symlink... 

이 에러는 원래 이미지를 빌드할때 해당 디렉토리만 정해주면 dockerfile을 자동으로 찾아 빌드하는데 현재는 dockerfile.dev 밖에 없으니 에러가 발생한다. 

임의로 build할때 어떤 파일을 참조할 것인지를 옵션으로 준다.

`docker build -f Dockerfile.dev .`

`docker build -f Dockerfile.dev -t guk0/docker-react-app .`

노드 모듈은 사실 카피를 할 필요가 없음. 불필요한 프로세스를 진행하는 것. 노드 모듈 지워주고 빌드하자.

<br>

## 포트 매핑
띄어놓은 리액트 앱을 로컬에서 실행하려면 포트 매핑을 해줘야함. 

`docker run -it -p 3000:3000 guk0/docker-react-app` 

리액트 쪽 변경사항으로 -it 옵션을 주지 않으면 매핑이 안됨.
- i : 상호 입출력
- p : tty를 활성화하여 bash 쉘을 사용

<br>

## VOLUME
COPY 대신 VOLUME을 이용하여 소스를 변경하였을때 다시 이미지를 빌드하지 않아도 변경한 소스 부분이 어플리케이션에 반영하도록 함.

**소스코드 지속적으로 변경!**

`docker run -it -p 3000:3000-v /usr/src/app/node_modules-v $(pwd):/usr/src/app<이미지 아이디>`

- -v /usr/src/app/node_modules : 호스트 디렉토리에 node_modules는 없기에 컨테이너에 매핑하지 말라고 하는 것.

- -v $(pwd):/usr/src/app : pwd 경로에 있는 디렉터리 혹은 파일을 /usr/src/app 경로에서 참조

<br>

## Docker-compose

위 명령어를 치는게 너무 불편함! 이를 docker-compose로 처리한다.

docker-compose.yml

```yaml
# docker-compose.yml
version: "3"
services:
  react:
    build: 
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - /usr/src/app/node_modules
      - ./:/usr/src/app
    stdin_open: true
```


### 테스트

`docker build -f dockerfile.dev .
docker run -it 이미지이름 npm run test`

docker-compose를 통해 소스가 변경될때마다 자동으로 테스트코드 돌도록 설정 가능.



```yaml
# docker-compose.yml
...

tests: 
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - /usr/src/app/node_modules
      - ./:/usr/src/app
    command: ["npm", "run", "test"]
```

## nginx

prod 환경에서는 nginx가 필요함.

1단계 : 빌드파일들을 생성

2단계 : nginx를 가동하고 첫번째 단계에서 생성한 빌드폴더의 파일들을 웹브라우저의 요청에 따라 제공해준다.

```dockerfile
FROM node:alpine as builder
```

FROM 부터 다음 FROM 까지는 빌드 스테이지라는 것을 명시.

```dockerfile
COPY --from=builder /usr/src/app/build /usr/share/nginx/html
```

-  --from=builder
    - 다른 stage에 있는 파일을 복사할때 다른 Stage 이름을 명시

- /usr/src/app/build /usr/share/nginx/html
  - build stage에서 생성된 파일들은 /usr/src/app/build에 들어가게 되며 그곳에 저장된 파일들을 /usr/share/nginx/html로 복사를 하여 nginx가 웹 브라우저의 http 요청이 올때마다 알맞은 파일을 전해 줄 수 있게 만듦.

- /usr/share/nginx/html
  - 이 장소로 build 파일들을 복사시켜주는 이유는 이 장소로 파일을 넣어 두면 nginx가 알아서 client 요청이 올때마다 알맞은 정적 파일들을 제공해줌. 이 장소는 설정을 통해 바꿀수도 있음.

```dockerfile
FROM node:alpine as builder
WORKDIR '/usr/src/app'
COPY package.json .
RUN npm install
COPY ./ ./
CMD ["npm", "run", "build"]

FROM nginx
COPY --from=builder /usr/src/app/build /usr/share/nginx/html
```

build 및 실행

`docker build .`