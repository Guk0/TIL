# 애플리케이션 계층
## 애플리케이션 계층
### 역할
- TCP/IP 모델에서 최상위 계층으로 사용자와 가장 가까운 소프트웨어
- 여러 프로토콜 개체들의 서비스에 대한 사용자 인터페이스 제공
- HTTP, DNS, SMTP, SSH, BGP, BHCP 등이 이 범주에 속함
    

### DNS(Domain Name Service)
- 호스트(도메인) 이름을 IP주소로 변환 - Port53
- 웹사이트 접속 또는 이메일 전송시 *.google.com등의 도메인 이름으로 접속
- 사람이 좀 더 기억하기 쉬운 문자 형태의 도메인 개발 - 반면 컴퓨터는 IP로 통신 - 서로의 변환 필요
    

### 계층적 구조
- top : kr, com, org
- second : naver, googlle
- sub : www, mail


### 쿼리 과정
- Recusive Query: Local DNS 서버가 재귀적으로 여러 서버에게 질의하여 응답을 받음
- Iterative Query: Local DNS 서버가 반복적으로 질의

## Resource Records
- DNS 레코드, DNS 서버가 가지고 있는 IP 매핑 정보 테이블
- 4 tuple: {Name, Value, Type, TTL} 로 구성되어 있다
- Type
    - A: 호스트, IP - www.fastcampus.co.kr, A 레코드, 1.1.1.1에 매핑되어 있다
    - NS: 네임서버 - fastcampus.co.kr, NS, ns.fastcampus.co.kr
    - CName: 별칭 - ftp.fastcampus.co.kr, CNAME, fastcampus.co.kr
    - MX: 메일서버 - mail.fastcampus.co.kr, MX, 2.2.2.2
- 리눅스머신에서 확인 가능
- dig @168.126.63.1 www.naver.com

### DNS 메시지 - 쿼리와 응답으로 구분
- Query: 2개
    - Header + Question
- Response: 5개
    - Header + Question + Answer + Authority + Additional
- Identifier : 쿼리와 응답 구분
- Flag : DNS 쿼리의 속성
- Questions : 질의
- Answers : 응답(Resource Records)
- Authorities : 책임(Resource Records)
- Additional : 추가(Resource Records)

## Hosts.txt
- 호스트 이름과 IP주소가 맵핑되어 저장된 파일
- Local DNS로 쿼리 전에 우선 참조하는 파일
    

### DNS 캐시 테이블
- 기존에 응답 받은 DNS 정보를 일정시간(TTL) 저장하고 동일한 질의 시 응답
    
    

## DNS 동작 과정
- PC -> 웹사이트 접속(www.daum.net)
  1. PC 네트워크 환경 확인 - Primary DNS 8.8.8.8로 설정
  2. hosts.txt 파일 참조 - 해당 도메인(www.daum.net)이 설정된 경우 맵핑된 IP로 응답
  3. dns cache table참조 - 해당 도메인(www.daum.net)이 저장된 경우 저장된 IP로 응답
  4. hosts.txt & cache table에 없으므로 Local DNS(8.8.8.8)에게 쿼리
  5. Local DNS(8.8.8.8)에서 응답

## HTTP 개요

### 정의
- HTTP(HyperText Transfer Protocol)
- WWW 상에서 정보를 공유하는 프로토콜 - Port80 - HTML
- WWW(World Wide Web)
- HTML(HyperText Markup Language)

### URL(Uniform Resource Locator)
- 웹 페이지를 찾기 위한 주소
    
    

## HTTP Request

### Client가 Server에게 특정 Method를 사용하여 요청
- Head(+Start Line), Body로 구성
- Start LineHTTP Method / Request target / HTTP Version
- HTTP Method: 요청의 목적 - GET, POST, PUT, HEAD, DELETE
    - GET: 리소스 요청
    - POST: 내용 전송
    - PUT: 내용 갱신
    - HEAD: 리소스에 대한 정보만 요청
    - DELETE: 리소스 제거
- Request target: 리소스 경로
- HTTP version : HTTP1.1 or HTTP/2

### Head
- Accept : 클라이언트가 허용 가능한 파일 형식
- User-Agent : 클라이언트의 OS, 브라우저 정보
- Host : 서버의 도메인 네임

## HTTP Response

### Client 요청에 따른 Server의 응답

- Head + Body
- Version / Status / Status Message
    - Version: HTTP 버전
    - Status: 상태
    - Status Message: 상태 메시지
- Date, Content-location, etag: 캐시 정보 업데이트
- Last-modified: 요청한 데이터의 최종 수정일Content-Length: 요청한 데이터 길이

## Status Code

주요 응답 코드

- 2** Success - 200 OK
- 3** Redirection - 307 Temporary Redirect
- 4** Client Error -
    - 400 Bad Request
    - 401 Unauthorized
    - 404 Not Found
- 5** Server Error
    - 500 Internal Server Error
    - 502 Bad Gateway
    - 503 Service Unavailable
    

## HTTP 속성

## Stateless

- HTTP는 통신이 끝나면 상태 정보를 유지하지 않는다
- 서버는 HTTP 요청에 대한 응답을 보내고 접속을 끊어 커넥션 리소스 비용을 줄인다
- 단순 페이지 또는 문서 정보 열람은 가능
- 하지만 클라이언트가 새로운 페이지를 접속할 때마다 서버는 신원을 알 수 없다
- 예를 들어, 인터넷 쇼핑몰의 경우 페이지 마다 어떤 회원인지 인증이 필요
- 회원 정보 식별, 로그인 여부, 결제 정보 및 장바구니 등
- 해결책 = Cookie & Session
- Stateful: 상태 정보 유지

## HTTP Cookie

### 정의
- 클라이언트 웹 브라우저 로컬에 저장되는 키와 값이 들어 있는 파일
- 이름, 값, 도메인, 만료일, 경로 - 일정 시간 정보 저장 -> 로그인, 장바구니


### Session
- 서버는 일정 시간 같은 웹브라우저의 요청이 들어오면 하나의 상태로 유지
- 서버는 클라이언트에 대한 세션ID 발급 및 보유 -> 쿠키로 전달 -> 동일 세션ID로 접속 -> 정보 확인

- Cookie는 사용자 로컬에 정보가 저장 - 유출 또는 조작 가능
- Session은 서버에 정보를 저장(안전) - 인증에 세션을 사용 - 세션 하이재킹? - HTTPS - SSL/TLS

## SSL/TLS

### 정의
- SSL(Secure Socket layer) / TLS(Transport Layer Security)
- TCP / IP 네트워크 통신 간 보안을 제공하는 프로토콜
- HTTPS : HTTP over TLS (http를 TLS로 감쌈)

### 기능
- 인증 - Client to Server 통신 간 상태방에 대한 인증
    - RSA, DSS 알고리즘
- 무결성
    - 메시지 인증 코드로 제공 HMAC - MD5, SHA-2
- 기밀성 - 데이터 암호
    - 3DES, RC4

### 프로토콜 구성
- 상위
    - HandShake: 키 교환 방식, 암호화 방식, HAMC방식, 압축 방식 등을 협상
    - Change Cipher Spec: 협상 정보가 적용됨을 알림
    - Alert: 협상 과정에서 제시한 암호화 방식을 지원 못하는 경우 알림
- 하위 (알고리즘 협상하고 암호화 시켜서 보냄)
    - Record: 데이터 교환, 메시지를 전송

### TLS Stack
- TLS 계층은 상위 3개 프로토콜, 하위 Record 프로토콜로 구분
- 상위 계층에서 협상 후 Record 프로토콜에서 Application 데이터를 분할, 압축, 암호화해서 전달

### 동작과정
1. 클라이언트 지원 가능한 cipher suite 전달
2. 서버는 자신이 지원하는 cipher suite 전달
3. Certificate: 서버 인증서 전달  
    ServerKeyExchange: DH 키교환 - 키 전달  
    CertificateRequest: 인증서 요청  
    ServerHelloDone: 모든 메시지 전달 완료
    
4. Ceriticate: 클라이언트 인증서 전달      
    ClientKeyExchange: DH, 클라이언트 키 교환   
    CertificateVerify: 인증서 확인   
    버전, cipher suite결정, 상대방 신원 확인 완료
    
5. ChangeCipherSpec Finished  
    TLSCiphertxt 전송, 협상된 키가 맞는지 검증
    

## 메일 서비스

## SMTP(Simple Mail Transfer Protocol)

- 전자 메일 전송을 위한 표준 프로토콜
- 클라이언트 - 서버 통신
- SMTP 명령어
    - HELO: 인사, 세션 초기화
    - MAIL: 메일 전송 시작, 송신자 이름
    - RCPT: 수신자, 수신자 이름
    - DATA: 데이터 전송 시작
    - QUIT: 세션 종료
- SMTP 응답
    - 220 세션 준비
    - 221 세션 종료
    - 250 요청한 명령이 정상적으로 수행
    - 421 서비스 불가
    - 450 다른 프로세스에 의해 접근 불가
    - 500 명령이 잘못됨
    - 551 잘못된 사용자 요청

### SMPT 통신 예제
- `telnet localhost 25`

### POP3(Post Office Protocol Version3)

- 수신서버의 메일 박스에서 메일을 가져오고 삭제하는 프로토콜
- 아웃룩 같은 메일 클라이언트 프로그램에서 사용
- POP3 명령어
    - USER: 사용자
    - IDPASS: 사용자
    - PasswordSTAT: 서버 상태
    - LIST: 메시지 리스트와 크기 확인
    - DELE: 메시지 삭제
    - QUIT: 연결 종료
- POP3 응답
    - + OK: 정상
    - - ERR: 에러

### IMAP4(Internet Message Access Protocol4)

- 메일서버로 접속하여 메일을 읽거나 삭제하는 프로토콜
- IMAP4는 원하는 메일 메시지만 전송, 다중 접속 가능, 메일 보관함 연동
- 메일 서버의 자원 사용률이 높아짐
- IMAP4 명령어
    - LOGIN: 사용자 접속
    - SLECT INBOX: 메일 박스 선택
    - FETCHl: 리스브 보기
    - UID FETCH: 메시지 가져오기
    - STATUS: 메일 박스의 상태 정보 확인
    

### 동작 과정

메일 서버, 메일 클라이언트

- 메일 서버: MTA(Mail Transfer Agent): 메일 전송
- 메일 클라이언트: MTU(Mail User Agent): 메일 송수신 프로그램
- MDA(Mail Delivery Agent): MTA가 수신한 메일을 수신자 우편함에 기록
- MRA(Mail REtrieval Agent): 리모트 서버의 우편함에서 사용자에게 메일을 가져오는 프로그램

### A 메일 서버 to B 메일 서버로 메일 전송

- A: MUA에서 SMTP를 통해서 메일 송신 - MTA - MDA (큐에 저장하고 순서대로 전송)
- B: MTA에서 메일 수신 - MDA - 지정된 메일박스로 전달 - MRA(POP3 or IMAP4)가 mail-box에서 메일 찾아옴 - MUA