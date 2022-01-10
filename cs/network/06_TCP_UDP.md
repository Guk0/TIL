## Transport 계층

### 역할

- End to End 서비스. 커넥션(연결)을 관리
- Connection-oriented, Reliability, Flow control, Multiplexing
- TCP & UDP, 소켓을 통한 프로세스별 통신
- 5 tuple = Source IP, Source Port, Dest IP, Dest Port, Protocol
    

### Port

- 전송 계층에서 사용되며 특정 프로세스를 구분하는 단위
- 0 ~ 65535
- 0 ~ 1023
    - well-known port
- 1024 ~ 49151
    - registered port
- 49152 ~ 65535
    - dynamic port
- 웹 TCP 80, FTP TCP 21

### 정의

- TCP(Transmission Control Protocol) - 전송 제어 프로토콜
- 인터넷을 구성하는 핵심 프로토콜
- 신뢰성을 기반으로 데이터를 에러 없이 전송. 1:1 통신
- 연결 지향. Connection-oriented. 패킷의 상태 정보를 확인하고 유지
- 에러 발생시 재전송을 요청하고 에러를 복구


### 헤더 포맷
- 20바이트
- 종류
  - Source & Dest port: 소스 포트와 목적지 포트
  - Sequence Number :순서 번호, 패킷 순서화와 중복 패킷 방지
  - Acknowledgement Number :승인번호, 수신측에서 수신 확인하고 다음 송신 데이터 요청
  - HLEN : 20 ~ 60
  - TCP 제어 플래그 : TCP 회선 및 제어 관리
  - Window Size : TCP 흐름 제어, 수신 버퍼의 여유 용량을 통보
  - Checksum  : 데이터 무결성 확인
  - Urgent Pointer : 긴급 데이터를 알림
  - Option & Padding : 옵션, MSS 조절이나 타임스탬프

### TCP 제어 플래그
- 6가지로 구성되며 활성화되는 값을 비트 1로 표현
  - URG: 긴급함을 알림. 긴급 데이터로 우선순위를 높여 먼저 송신
  - ACK: 확인. 수신측에서 송신된 패킷을 정상적으로 받았음을 알림
  - PSH: 버퍼링 되지 않고 바로 송신
  - RST: 비정상 상황에서 연결을 끊음
  - SYN: 연결을 맺기위해 보내는 패킷(000010)
  - FIN : 정상 종료. 송신측에 연결 종료 요청

## UDP

### UDP(User Datagram Protocol)

- 신뢰성은 낮으나 데이터 전송이 빠르다.
- 송신측은 일반적으로 데이터를 보내고 확인 안함. 1:n 통신 가능
- Connectionless. 재전송 불가. 실시간 데이터 전송에 적합
- 스트리밍 서비스의 경우 전송 문제가 발생해도 재전송 보다는 실시간 데이터 전송이 중요.
    

### 헤더포맷
- Source Port : 출발지 포트
- Dest Port : 목적지 포트
- Length : 전체 데이터 길이(header + data)
- Checksum : 데이터 무결성 확인

|  | TCP 20 Byte | UDP 8 Byte |
| --- | --- | --- |
| Protocol ID | 6 | 17 |
| 순서확인 | 가능 | 불가능 |
| 신뢰성 | 높음 | 낮음 |
| 연결성 | Connection-oriented | Connectionless |
| 제어 | 흐름 & 혼잡 제어 가능 | 없다 |
| 속도 | 느리다 | 빠르다 |

## TCP 통신 과정

### 3 way handshake

- TCP는 연결 지향 프로토콜로 두 호스트가 통신하기 전에 연결을 위한 관계를 수립

### 3 way handshake 연결 성립(connection establishment)
1. 클라이언트는 서버에 접속을 요청하는 **SYN(a)** 패킷을 보낸다.
2. 서버는 클라이언트의 요청인 **SYN(a)**을 받고 클라이언트에게 요청을 수락한다는 **ACK(a+1)**와 **SYN(b)**이 설정된 패킷을 발송한다
3. 클라이언트는 서버의 수락 응답인 **ACK(a+1)**와 **SYN(b)** 패킷을 받고 **ACK(b+1)**를 서버로 보내면 연결이 성립된다.
    
### 3 way handshake 연결 해제(connection termination)

1. 클라이언트가 연결을 종료하겠다는 FIN 플래그를 전송
2. 서버는 클라이언트의 요청(FIN)을 받고 알겠다는 확인 메세지로 ACK를 보낸다. 그리고 나서 데이터를 모두 보낼때까지 잠깐 Time out이 된다
3. 데이터를 모두 보내고 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 FIN 플래그를 전송한다.
4. 클라이언트는 FIN메세지를 확인했다는 메세지(ACK)를 보낸다
5. 클라이언트의 ACK 메세지를 받은 서버는 소켓 연결을 close한다.
6. 클라이언트는 아직 서버로부터 받지 못한 데이터가 있을 것을 대비하여 일정 시간 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정을 거친다(TIME_WAIT)
    
### 4 way handshake

- 연결 종료(정상적인 종료)
    

### TCP 타이머(Retransmission)

- 송신 측이 패킷을 매번 전송할 때 카운터
- RTO(Retransmission Timeout) 내 ACK응답이 오지 않으면 재전송
- RTO는 RTT(Round Trip Time)에 따라서 가변적으로 변함
- SRTT(smoothed Round-Trip Time), RTTVAR(Round-Trip Time Variation)
- alpha = 1/8, beta = 1/4, R = 측정된 RTT 값. G = clock granulrity
- RTTVAR = (1-beta) * RTTVAR + beta * |SRTT - R|
- SRTT = (1-alpha) * SRTT + alpha * R
- RTO = SRTT + max(G, 4*RTTVAR)

### TCP 타이머 - Persistence

- 윈도우 사이즈 관련 타이머
- 수신측에서 용량 부족으로 윈도우 사이즈 없음을 보내고 다시 용량에 여유가 생기면 송신측에 요청
- 중간에서 윈도우 사이즈 > 0을 보내는 ACK이 유실되면 서로 통신 간 문제 발생
- 수신측 윈도우 사이즈 > 0을 보낼 경우 Persistence 타이머 가동 - RTO
- Persistence 타이머가 종료되면 Probe(ACK 재전송 요청)를 보내고 타이머 재 가동
- 다시 타이머가 종료되기 전에 ACK를 수신 못하면 시간을 2배로 늘리고 Probe 재전송
- 타이머의 임계치는 60초

### TCP 타이머 - Time waited

- TCP 연결 종료 후에 특정 시간만 연결 유지
- MSL(Maximum Segment Lifetime) = 120초. Time_Wait = 2MSL
- 다른 연결이 맺어진 상태에서 이전 연결의 지연/중복 패킷도착으로 인한 문제 발생

### TCP 타이머 - Keepalive

- TCP 연결 유지 타이머
- TCP 연결을 맺고 수신측에서 2시간 동안 송신하는 패킷이 없으면 수신측은 75초 단위로 Probe 전송
- Probe 9개를 보내고 응답이 없으면 연결 종료
- Probe 9개 이전에 응답이 있으면 타이머는 재 설정됨.

## 흐름제어

### Flow Control

- 송신과 수신측의 데이터 처리 속도 차이를 해결
- Sliding Window 기법. Window = 데이터 전송을 위한 버퍼
    - 버퍼 사이즈 중 Window = 4
    - TCP 데이터 중 1을 프로세스에서 Read 처리
    - Window Size = 5, 송신 측에서 Size 확인 후 데이터 전송
- 윈도우 사이즈 = 마지막 수신한 데이터 - 프로세스가 처리한 데이터

### 혼잡제어(Congestion Control)

- 수신측으로 유입되는 트래픽의 양이 정해진 대역폭을 넘어가지 않도록 제어
- AIMD(Additive Increase/Multiplicative Decrease)
    - 패킷 전송시 문제 없으면 Window size 1씩 증가. 타임아웃 또는 loss 시 패킷 속도 1/2 감소.
    - 초기에 높은 대역폭 사용 불가. 미리 혼잡 상태 감지 불가
- Slow Start
    - 패킷 전송시 문제 없으면 Window size 2배씩 증가. 혼잡 상태 발생시 1로 변경
    - 사전 혼잡 상태를 기록하고 Window size 절반까지 2배씩 증가 후 1씩 증가
- Fast Retransmit - TCP Tahoe / Fast Recovery - TCP Reno
    - 수신측에서 먼저 와야 하는 패킷이 오지 않고 다음 패킷이 오게 되어도 송신측에 ACK를 보냄
    - 송신 측은 타임아웃 시간을 기다리지 않고 중복된 순번의 패킷을 3개 받으면 재전송
- 개선된 Fast Retransmit / Fast Recovery
    - TCP New Reno, SACK(TCP Tahoe + Selective Retransmit)

## 공인 IP & 사설 IP

### 공인 IP

- ICANN(Internet Corporattion for Assigned Names and Numbers)
- 공인기관에서 인정하는 IP주소이며 인터넷을 통한 외부망에서 식별되고 통신 가능한 IP

### 사설 IP

- 내부망에서 사용 및 식별 가능한 IP, IPv4개수의 한계
- 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- WAN 에서 사용하는 IP : 공인 IP
- LAN 에서 사용하는 IP: 사설 IP

## NAT 개요

### NAT(Network Address Translation)

- 네트워크 주소 변환
- 사설 IP 네트워크를 인터넷으로 연결 → 라우팅 가능한 공인 IP로 변환
- 보완 : 내부 IP주소를 외부에 공개하지 않음
- 유연성
    - 공인 IP대역은 영향을 주지 않고 내부 네트워크 구성 변경 가능
    - 기존 사용하던 외부에 공개된 공인 IP 주소는 변경되지 않으나 내부 IP만 변경
- 비용
    - 공인 할당 비용 감소
- L3 이상의 장비 또는 방화벽에서 NAT 가능

### Static NAT
- 예시
  - 1:1 NAT, 정적 NAT
  - 사설 IP 1개를 공인 IP 1개로 매핑하며 주로 외부 공개형 서버에 구성
  - 외부에서 211.103.1.100으로 접속 시도
  - 외부 → 211.203.1.100, 패킷이 eth0에 도달
  - 211.203.1.100 to 192.168.1.100로 1:1 NAT됨을 확인
  - 192.168.1.x 대역인 eth1로 전달
  - 외부 → 192.168.1.100, 패킷은 Server에 도착

### Dynamic NAT
- 예시
  - 내부 IP 주소와 외부 IP 주소가 범위 내에서 맵핑
  - 내부 PC들은 외부로 통신 시 공인 IP 대역 Pool에서 할당 받는다
  - 내부 192.168.1.0/24 대역의 내부 PC 20대는 웹사이트 접속 시도
  - eth1에 패킷 도달, NAT 테이블의 공인 IP 대역 Pool을 확인하고 매핑
  - eth0에서 매핑된 공인 IP 주소 211.203.1.x로 변환되어 외부로 통신 시도
  - 나머지 PC들도 NAT Pool을 확인하고 동일한 방식으로 매핑

### PAT(Port Address Translation)
- 예시
  - 1:N NAT, 여러개의 내부 사설 IP들이 1개의 공인 IP로 변환
  - 공개형 서버가 아닌 내부 → 외부 접속이 필요한 PC들이 사용
  - IP가 중복되기 때문에 Port로 세션 구분
  - 내부 192.168.1.0/24 대역의 내부 PC 20대는 웹사이트 접속 시도
  - eth1에 패킷 도달, NAT 테이블의 PAT 대표 공인 IP:Port를 확인하고 매핑
  - eth0에서 매핑된 공인 IP주소 211.203.1.x로 변환되어 외부로 통신 시도
  - 나머지 PC들도 동일한 방식으로 매핑 - 공인 IP는 동일, Port 번호는 다름

### Port Forwarding

- 공인 IP 1개로 여러대의 사실 IP를 Port로 구분하여 연결
- 공인 IP 1개로 여러대의 공개형 서비스를 구축할 때 사용
- 예시
  - 외부에서 211.203.1.100으로 웹 접속 시도
  - 외부 → 211.203.1.100, 패킷이 eth0에 도달
  - 211.203.1.100:80 to 192.168.1.100:80로 포트 포워딩됨을 확인
  - 192.168.1.x 대역인 eth1로 전달되고 패킷은 웹서버에 도착
  - 외부에서 211.203.1.100으로 이메일 접속 시도
  - 외부 → 211.203.1.100 패킷이 eth0에 도달
  - 211.203.1.100:25 to 192.168.1.100:25로 포트 포워딩 됨을 확인
  - 192.168.1.x 대역인 eth1로 전달되고 패킷은 이메일 서버에 도착

## Hairpin NAT

### NAT 이슈
- 동일 사설 네트워크 내 공인 IP로 목적지 서버에 접속하는 경우
  - 외부에서 211.203.1.100으로 웹 접속 시도
  - NAT 테이블에서 211.203.1.200은 192.168.1.200으로 매핑됨을 확인
  - 192.168.1.x 대역인 eth1로 전달되고 패킷은 웹서버에 도착
  - 웹서버는 응답 패킷을 전달 시도. 192.168.1.200 → 192.168.1.100
  - 목적지 PC는 동일 대역대 IP로 확인되고 PC에게 바로 응답 패킷 전달
      - PC입장에서 기존 커넥션이 아닌 신규 패킷으로 판단되어서 통신 불가

### 해결책

- Hairpin Nat해결책NAT 장비에서 출발지 IP를 NAT장비 IP로 변경
- 예시
  - PC는 211.203.1.200으로 웹 접속 시도
  - NAT테이블에서 211.203.1.200은 192.168.1.200으로 맵핑됨을 확인
  - 192.168.1.x 대역인 eth1로 전달 되고 패킷은 웹 서버에 도착
  - 웹 서버는 응답 패킷을 전달 시도, 192.168.1.200 -> 192.168.1.1
  - 192.168.1.00 : 192.169.1.11 맵핑 정보를 확인하고 PC에게 응답 패킷 전달
  - 소켓 프로그래밍 작성시 사설 IP & 공인 IP의 Flow를 확인 못하여 빈번한 장애 발생

# TELNET

### 역할
- 원격지 호스트 컴퓨터에 접속하기 위해 사용되는 프로토콜
- 장비 관리 또는 서버 접속 시 사용 - Shell - Command Line Interface
- 클라이언트 소프트웨어인 경우, 포트 테스트 용도로 많이 사용
- `telnet[naver.com](http://naver.com) 80`
- 해당 도메인 또는 IP 주소에 서비스 포트(서비스)가 열려 있는지 확인 가능

### 기능

- NVT(Network Virtual Terminals)지원
    - 데이터 변환 가상 장치
- 협상 가능한 옵션
- 프로세스와 터미널의 1:1 sysmmetric 관계
  

### Negotiation Commands
- WILL : 옵션 활성화를 원한다
- WON'T : 옵션 활성화를 원하지 않는다
- DO : 옵션 활성화를 요청한다
- DON'T : 옵션 활성화를 요청하지 않는다
    
### 접속 및 옵션 ID협상 확인
- 원격지 IP
    - Port로 접속 시도 → ID : Password 입력 → 원격지 서버에 연결
- 윈도우 CMD 또는 리눅스 터미널에서 접속 가능
- 무료 오픈소스인 Putty프로그램을 많이 사용

# SSH

### 역할
- Secure Shell
- TELNET을 대체하기 위해 개발
- 원격지에 있는 컴퓨터를 명령어를 통해서 제어
- 강력한 인증 방법 및 암호화 통신을 제공, TCP 22
- SSHv1, SSHv2

### 특징
- 인증(Authentication)
    - 사용자가 서버 접속시 패스워드 또는 공개키 기반의 인증 방식을 지원
- 암호화(Encryption)
    - 대칭키 방식 사용 - AES, Blowfish, 3DES
- 무결성(Integrity)
    - 데이터 위변조 방지 - MAC(Message Authentication Code)
- 압축(Compression), 다중화 통신
- 대칭키
    - 동일한 키로 암복호화를 동시에 할 수 있는 방식
- 공개키(공개키 + 개인키) 방식
    - 공개키 암호화 -> 데이터 보안, 서버의 공개키로 데이터를 암호화 -> 서버의 개인키로 복호화
    - 개인키 암호화 -> 인증 보안, 개인키 소유자가 개인키로 암호화 하고 공개키를 함께 전달 -> 함호화 데이터 + 공개키로 신원 확인 -> 전자서명 방법

### 통신 과정

- TCP Connection Established
- SSH veresion string exchange
- Key exchange
- Alorithm negotiation
- DH Key exchange
    - 대칭키 공유 → 상대방의 공개키와 자신의 개인키를 사용(이산 로그 방식 이용) → 비밀키 생성 → 데이터 암호화
- Data Exchange