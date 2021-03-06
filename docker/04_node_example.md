# Node js example
## nodejs example
Node js에서 앱을 도커 환경에서 실행하려면 먼저 이미지를 생성하고

그 이미지를 이용하여 컨테이너를 실행한 후 그 컨테이너 안에서 Nodejs앱을 실행해야함

<br>

### 왜 베이스 이미지를 노드로 사용하는가?
alpine에는 가장 최소한의 경량화된 파일들이 들어있기 때문에 npm을 위한 파일이 존재하지 않아 RUN 부분에서 npm 인스톨을 할 수 없음.

위 도커파일로 빌드하면? package.json이 없다고 나옴.

NODE 베이스 이미지를 이용하여 임시 컨테이너를 만드는데 컨테이너 안에는 package.json과 server.js가 들어와 있지 않기 때문


위 내용을 해소하기 위해 COPY를 사용해야함.

`COPY package.json ./`

`COPY (로컬에 있는 파일) (도커 컨테이너의 지정된 path에 복사)`

모든 파일 복사?

`COPY ./ ./`

<br>

## 실제 서버를 돌리기 위해서는?

`docker run -p 5000:8080 이미지이름`

위와 같이 커맨드를 입력해야함.

네트워크도 로컬 네트워크에 있던 것을 컨테이너 내부에 있는 네트워크에 연결해줘야 한다.

`5000` : 로컬 `5000`번 포트로 접근

`8080` : 도커 컨테이너 `8080`번 포트로 이동

<br>

## WORKDIR

정의 : 이미지 안에서 어플리케이션 소스코드를 갖고 있을 디렉토리를 생성하는 것.

왜 따로 디렉토리가 존재해야 하는지?

WORKDIR을 사용하지 않으면 COPY를 통해 루트로 들어오게 되는데

1. 베이스 이미지의 폴더, 파일과 이름이 같다면 덮어씌어져 버림.

2. 소스코드 관리를 위해

<br>

## 어플리케이션 소스 변경으로 다시 빌드하는 것의 문제점

어플리케이션을 만들다보면 소스코드를 계속 변경시켜줘야하며 그에 따라 변경된 부분을 확인하며 개발을 해야함

그래서 도커를 이용하여 어떻게 실시간으로 소스가 반영되는지?

`docker run -d guk0/nodejs`
`-d` 옵션 실행후 바로 컨테이너를 빠져나오게 해줌.

첫번째 도커파일의 문제점. package.json 말고 다른 소스코드 수정시, 도커 빌드를 하면 계속 npm install 됨. 굉장히 비효율적.

Package.json 먼저 카피하고 npm 돌리고 파일들을 다시 카피하는 이유?

종속성 부분만 먼저 카피를 하고 이 부분만 npm install을 해줌.

위와 같이 변경하면 소스코드 수정시 다시 npm install하지 않고 반영만 해줌.

<br>

## Docker Volume

소스를 변경할때마다 변경된 소스 부분은 COPY한 후 이미지를 다시 빌드해주고 컨테이너를 다시실행해줘야지 변경된 소스가 화면에 반영된다.

이러한 작업은 너무나 시간 소요가 크고 이미지도 너무나 많이 빌드하게 되어 Volume을 사용한다

로컬 파일을 계속 참조(mapping)함.

`docker run -p 5000:8000 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app <이미지아이디>`

`첫번째 -v` : 호스트 디렉토리에 node_module은 없기에 컨테이너에 매핑을 하지 말라고 하는 것

`두번째 -v` : pwd 경로에 있는 디렉토리 혹은 파일을 /usr/src/app 경로에서 참조

PWD(print working directory) : 현재 작업 중인 디렉토리를 출력
