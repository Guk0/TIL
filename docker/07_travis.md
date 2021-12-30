## travis ci란?

깃헙 레포에 있는 프로젝트를 특정 이벤트에 따라 자동으로 테스트, 빌드하거나 배포할 수 있다. private은 유료
1. 로컬 깃에 있는 소스를 깃헙 저장소에 푸시

2. github master 저장소에 있는 소스가 push되면 travis ci에게 소스가 push 이벤트 트리거

3. travis ci는 업데이트 된 소스를 github에서 가지고 온다.

4. 깃헙에서 가져온 소스의 테스트 코드를 실행해봅니다.

5. 테스트 코드 실행 후 테스트가 성공하면 AWS같은 호스팅 사이트로 보내서 배포를 한다.

## Travis ci

깃헙에 소스를 올렷을때 Travis CI에서 그 소스를 트래킹 해야하기 때문에 깃헙과 travis ci가 연결되어 있어야 함.

travis ci에 가입 후 레포지토리 싱크를 완료하면 해당 소스를 어떻게 travis ci에 전달하며 전달 받은 소스를 어떻게 테스트하며 그 테스트가 성공하였을때 어떻게 AWS에 전달하여 배포할 것인지를 설정해줘야함. 

해당 설정은 travis.yml 파일에 작성함.

## travis.yml

```yaml
sudo: required

language: generic

services:
  - docker

before_install:
  - echo "start creating an image with dockerfile"
  - docker build -t guk0/docker-react-app -f Dockerfile.dev .

script:
  - docker run -e CI=true guk0/docker-react-app npm run test -- --coverage

after_success:
  - echo "Test Success"
```

## EB(Elastic BeanStalk)

Apache, Nginx 같은 서버에서 Java, NET, PHP, Node.js, Python, ruby 및 Docker과 함께 개발된 웹 응용프로그램 및 서비스를 배포하고 확장하기 쉬운 서비스.

EB안에 여러 AWS 리소스들을 구성할 수 있음.

## deploy

```yaml
sudo: required

language: generic

services:
  - docker

before_install:
  - echo "start creating an image with dockerfile"
  - docker build -t guk0/docker-react-app -f Dockerfile.dev .

script:
  - docker run -e CI=true guk0/docker-react-app npm run test -- --coverage

deploy: 
  provider: elasticbeanstalk
  region: "ap-northeast-2"
  app: "docker-react-app"
  env: "Dockerreactapp-env"
  bucket_name: "elasticbeanstalk-ap-northeast-2-957930470982"
  bucket_path: "docker-react-app"
  on: 
    branch: master
```

- Dockerfile.dev 로 배포하는 이유?
    - EB에서는 운영환경을 Docker로 배포했기 때문에 알아서 Dockerfile을 찾아 돌림.
    - Dockerfile.dev는 travis-ci를 위한 파일이라고 보면 됨.

## 소스 파일을 전달하기 위한 접근 요건
인증을 위해 api key 필요

IAM USER 생성

AdministratorAccess-AWSElasticBeanstalk 권한 주고 생성

access key 와 secret key는 travis dashboard에 넣어줌.

넣어주고 .yml 파일에서 환경변수로 가져다 씀.

```yaml
....

deploy: 
  provider: elasticbeanstalk
  region: "ap-northeast-2"
  app: "docker-react-app"
  env: "Dockerreactapp-env"
  bucket_name: "elasticbeanstalk-ap-northeast-2-957930470982"
  bucket_path: "docker-react-app"
  on: 
    branch: master
access_key_id: $AWS_ACCESS_KEY
access_secret_key: $AWS_SECRET_ACCESS_KEY
```