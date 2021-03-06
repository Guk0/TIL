# 물리계층 장비 & 케이블
## 물리계층 장비

### 허브와 리피터
- 허브는 전기신호를 증폭하여 포트에 연결된 PC들끼리 통신이 가능하게 한다
- 리피터는 현재 거의 쓰지 않는 장비로 신호의 세기를 증폭하여 좀 더 먼거리까지 통신이 가능
    

### 허브의 동작방식
- 단순 중계기의 역할로 허브에 연결된 PC1이 다른 PC2에게 데이터를 보내려 하면 허브에 연결된 모든 PC들에게 그 데이터를 전달하게 된다.
- 브로드캐스팅 통신 1 :  all
- 유니캐스팅 통신 1 : 1
- 멀티캐스트 통신 1 : N

### CSMA/CD
- Carrier sense multiple access/collision detection
- 송신 노드는 데이터를 전송하고 다음 채널에서 다른 노드의 데이터 충돌 발생을 계속 감지
- 충돌 발생시에는 모든 노드에게 충돌 발생을 통지하고 재전송을 시도
    - Carrier Sensing : 데이터를 보내기 전에 다른 노드에서 데이터를 보내는 중인지 확인
    - Multiple Access : 데이터를 보내는 곳이 없다면 전송 시작
    - Collision Detection : 동 시간대에 데이터를 보내게 되면 충돌이 일어나고 정지
    - 그 이후 특정 시간이 지나면 다시 첫번째 단계로 반복
- Half Duplex : 반이중 전송방식

### 전송 방식
1. Simplex : 단방향 통신으로 수신측은 송신측에 응답 불가
2. Half Duplex : 반이중 전송방식으로 양방향 통신이나 송수신 시간은 정해짐(무전기)
3. Full Duplex : 전이중 전송방식으로 동시 양방향 통신이 가능(전화기)

## 케이블과 커넥터

### 종류
- 전송 장치에 신호를 전달하는 통로로 주요 케이블로는 TP, 동축, Fiber 등이 있다.

### TP(Twisted Pair)
- 총 8가닥의 선으로 구성되며 두개의 선을 서로 꼬아놓는다.
- 선을 꼬아놓는 이유는 자기장 간섭을 최소화하여 성능(속도와 거리)를 향상
- STP는 UTP보다 성능이 더 좋지만 현실적인 이유로 UTP를 더 광범위하게 사용.
- 가운데 RJ-45 커넥터

### 동축(Coaxial)
- 선 중앙에 심선이 있으며 그 주위를 절연물과 외부 도체를 감싸고 있다.
- 전화 또는 회선망 등 광범위하게 사용
    

### 광(Fiber)

- 전기신호의 자기장이 없는 빛으로 통신하기 때문에 장거리 고속 통신이 가능
- 2개의 모드(Single, Multi)와 주요 커넥터 타입(LC, SC)이 있다.
    

### 광 트랜시버
- 광통신에 사용되는 네트워크 인터페이스 모듈 커넥터로 SFP, GBIC이 있다.
- SFP(Small Form-Factor Pluggable transceiver), GBIC(Gigabit Interface Connector)
    

## 단위와 성능

### bit & Byte
- bit는 2진수로 Binary 0, 1로 이루어지며 True & False 등 신호를 표현
- 1Byte = 8bit
- bit는 일반적으로 회선 Speed, Byte는 Data Size에 쓰인다.
- 100Mbps = 100 Mega bit per second. SSD 500GB = 50 Giga Byte

### Performance
- Bandwidth(대역폭) : 주어진 시간대에 네트워크를 통해 이동할 수 있는 정보의 양
- Throughput(처리량) : 단위 시간당 디지털 데이터 전송으로 처리하는 양
- 대역폭이 8차선 도로라면 처리량은 그 도로를 달리는 자동차의 숫자(양)와 같다.
- BackPlane : 네트워크 장비가 최대로 처리할 수 있는 데이터 용량
- CPS(Connection Per Second) : 초당 커넥션 연결수(L4)
- CC(Concurent Connections) : 최대 수용가능한 커넥션
- TPS(Transactions Per Seconds) : 초당 트랜잭션 연결수(L7). 주로 HTTP 성능

### 예시
FW : 방화벽
쓰루풋 :  데이터가 커지면 쓰루풋은 커지고 작아지면 작아짐
백본은 내부 모든 통신을 계산하기 때문에 굉장히 큼.

## UTP 케이블이란?

### 정의
- Unshielded Twisted Pair. 주로 근거리 통신망(LAN)에서 사용되는 케이블.
- 이더넷 망 구성시 가장 많이 보게되는 케이블
- 알렉산더 그레이엄 벨이 AT&T에서 발명
    
## 코드배열

### 8P8C

- 8개의 선 배열에 따라 다이렉트 또는 크로스 케이블로 구성한다.
- Direct Cable(568B-568B) : PC to Hub → DTE to DCE
- Cross Cable(568A-568B) : PC to PC, Hub to Hub → DTE to DTE, DCE to DCE
- DTE(Data Terminal Equipment), DCE(Data Communication Equipment)

### Auto MDI-X

- Automatic Medium Dependent Interface Crossover)
- 어떤 노드의 연결인지에 따라서 다이렉트와 크로스 케이블을 선택 → 불편
- 케이블 타입에 관계없이 노드 상호간 자동으로 통신이 가능하게 하는 기술
- MDI 포트 → DTE & MDIX 포트 → DCE, 송신과 수신의 관계
    

## UTP 카테고리

### 정의
- UTP 케이블의 전송 가능한 대역폭을 기준으로 분류
    

### Wi-Fi란?
### 정의
- 비영리 기구인 Wi-Fi Aliance의 상표로 전자기기들이 무선랜에 연결할 수 있게 하는 기술
- 1999년 몇몇 회사들이 브랜드에 상관 없이 무선 네트워킹 기술의 발전을 위해 협회 결성

## 무선랜 구성
인터넷 - ISP - 라우터 - WIPS - AP - 컴퓨터

WIPS(wireless IPS)와 AP(Access Point)가 있어야 무선랜 구성 가능

## WireShark란?

### 정의
- 오픈소스 패킷 분석 프로그램
- 예전에는 이더리얼로 불렸다가 상표권 문제로 와이어샤크로 변경
- 리눅스 TCPDUMP와 함께 네트워크 분석에 널리 쓰이는 도구