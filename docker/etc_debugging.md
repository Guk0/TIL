## m1 이슈
m1에서 mysql사용시 docker-compose.yml에 platform을 명시하여 해결한다

```yaml
# docker-compose.yml

mysql:    
    platform: linux/x86_64
    build:
      dockerfile: Dockerfile
      context: ./mysql     
    restart: unless-stopped
    container_name: app_mysql
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/mysql_data:/var/lib/mysql
      - ./mysql/sqls/:/docker-entrypoint-initdb.d/
    environment:
      MYSQL_ROOT_PASSWORD: *****
      MYSQL_DATABASE: myapp
```

위 방법으로도 해결이 안될때는 mysql의 Dockerfile의 FROM을 아래와 같이 변경한다

```yaml
FROM --platform=linux/x86_64 mysql:8.0
```

<br>

## nodejs 와 mysql 문제

mysql이 정상 시작되기 전에 nodejs가 시작되어 db에 연결할 수 없는 문제 발생.

docker-compose.yml에 depends_on 정의

```yaml
depends_on:
      - mysql
```

하지만 depends_on은 단순히 시작 시점만 바꾸는 것이고 mysql이 ready 상태로 바뀔 때 까지 기다리지 않음.

<br>

## dockerize 사용

``` dockerfile
# backend Dockerfile

... 

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

...

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
```

위와 같이 추가 후 [docker-entrypoint.sh](http://docker-entrypoint.sh) 쉘 스크립트 실행

```bash
echo "wait db server"
dockerize -wait tcp://mysql:3306 -timeout 20s

echo "start node server"
npm run start
```

<br>

## 기타 mysql 에러
### Client does not support authentication protocol requested by server; consider upgrading MySQL client
command: --default-authentication-plugin=mysql_native_password

<br>

### results Error: ER_HOST_NOT_PRIVILEGED: Host '172.19.0.4' is not allowed to connect to this MySQL server

environment에 아래와 같이 root host  env추가.
``` yaml
environment:
  MYSQL_ROOT_HOST: "%"
```