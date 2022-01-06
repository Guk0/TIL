# 데이터 링크 계층과 스위치

## 데이터 링크 계층

### 역할
- OSI 7 Layer의 2계층으로 인접한 네트워크 노드끼리 데이터를 전송하는 기능과 절차를 제공
- 물리계층에서 발생할 수 있는 오류를 감지하고 수정
- 대표적인 프로토콜로는 이더넷이 있으며 장비로는 스위치가 있다.
     

### 2개의 부 계층으로 구성
MAC(Media Access Control)
- 물리적인 부분으로 매체간의 연결 방식을 제어하고 1계층과 연결

LLC(Logical Link Control)
- 논리적인 부분으로 Frame을 만들고 3계층과 연결
    


### MAC 주소

- 명령어 cmd → ipconfig /all 또는 네트워크 설정에서 확인   
- 48bit (6 Bytes)로 6자리로 구성 각 16진수로 표현
- 앞 3자리는 OUI(Organization Unique Identifier) - 회사 지칭
- 나머지 3자리는 제조사 내 일련번호

## 주요 기능
### Framing
- 데이터그램을 캡슐화하여 프레임 단위로 만들고 헤더와 트레일러를 추가
- 헤더는 목적지, 출발지 주소 그리고 데이터 내용을 정의
- 트레일러는 비트 에러를 감지
    

### 회선 제어
- 신호간의 충돌이 발생하지 않도록 제어
- ENQ/ACK 방법
- 전용 전송 링크 1:1
- Polling 방법. 1 : 다
- Select 모드 : 송신자가 나머지 수신자들을 선택하여 전송
- poll 모드 : 수신자에게 데이터 수신 여부를 확인하여 응답을 확인하고 전송(multipoint)
    
### 흐름제어
- 송신자와 수신자의 데이터를 처리하는 속도 차이를 해결하기 위한 제어
- Feedback 방식의 Flow Control이며 상위 계층은 Rate 기반
- **Stop & Wait**
  - 데이터를 보내고 ACK(Acknowledgement) 응답이 올 때까지 기다린다.
  - 간단한 구현, 비효율적
  - ACK이 오지않으면 일정 시간 후 다시 보낸다.
  - Frame을 전달하고 ACK이 회선 문제로 응답하지 않은 경우
  - Frame을 재전송하게 되면 Duplicate frame 문제가 발생할 수 있음
  - **Sequence number**(1bit)를 사용하여 동일 frame인지 구분(중복 데이터인지)하여 상위 계층으로 전달

- **Sliding window**
    - ACK 응답 없이 여러 개의 프레임이 연속으로 전송 가능
    - Window size는 전송과 수신측의 데이터가 저장되는 버퍼의 크기

### 오류제어
- 전송 중에 오류나 손실 발생 시 수신측은 에러를 탐지 및 재전송
- ARQ(Automatic Repeat Request) : 프레임 손상 시 재전송이 수행되는 과정
- **Stop & Wait ARQ**
  - 전송 측에서 NAK를 수신하면 재전송
  - 주어진 시간에 ACK이 안 오면 재전송
- **Go Back n ARQ**
  - 전총 측 Frame 6개 중 수신 측 3번 프레임 문제 발생
  - 수신  측 NAK 3으로 손상 응답
  - 전송 측 3번이 포함된 345 재전ㄴ송
    - 3번만 문제였지만 345를 다버림. 비효율적.
- Selective Repeat ARQ
    - 손상된 Frame만 선별하여 재전송

## 이더넷 프레임 구조

### Ethernet V2

- 데이터 링크 계층에서 MAC(media access control) 통신과 프로토콜의 형식을 정의
- Preamble: 이더넷 프레임의 시작과 동기화
- Dest Addr : 목적지 MAC 주소
- Src Addr : 출발지 MAC 주소
- Type : 캡슐화되어 있는 패킷의 프로토콜 정의
- DATA : 상위 계층의 데이터로 46 ~ 1500바이트의 크기, 46바이트보다 작은 면 뒤에 패딩이 붙는다
- FCS(Frame Check Sequence) : 에러체크

## L2 스위치

### 정의

- 2계층의 대표적인 장비로 MAC 주소 기반 통신
- 허브의 단점 보완
    - Half Duplex → Full duplex(쌍방 통신 가능)
    - 1 Collision Domain → 포트별 Collision Domain(포트별로 나눠서 해당되는 도메인에 대해서만 통신을 하고 불필요한 패킷을 전달하지 않음)
- 라우팅 기능이 있는 스위치를 L3 스위치라고도 부른다.

### 동작 방식

- 목적지 주소를 MAC 주소 테이블에서 확인하여 연결된 포트로 프레임 전달
1. Learning
    - 출발지 주소가 MAC주소 테이블에 없으면 해당 주소를 저장
2. Flooding - Broadcasting
    - 목적지 주소가 MAC 주소 테이블에 없으면 전체 포트로 전달
3. Forwarding
    - 목적지 주소가 MAC 주소 테이블에 있으면 해당 포트로 전달
4. Filtering - Collision Domain
    - 출발지와 목적지가 같은 네트워크 영역이면 다른 네트워크로 전달하지 않음
5. Aging
    - MAC 주소 테이블의 각 주소는 일정 시간 이후에 삭제

### Learning

- 4개의 PC는 스위치에 각 포트에 연결되고 프레임이 스위치에 전달
- 스위치는 해당 포트로 유입된 프레임을 보고 MAC 주소를 테이블에 저장
    
### Flooding

- PC1은 목적지 aa:bb:cc:dd:ee:05 주소로 프레임 전달
- 스위치는 해당 주소가 MAC TABLE에 없어서 전체 포트로 전달
    
    

### Forwarding

- PC1은 목적지  aa:bb:cc:dd:ee:05 주소로 프레임 전달
- 스위치는 해당 주소가 MAC Table에 존재하므로 해당 프레임을 PC5로 전달
    
    

### Filtering

- PC1은 목적지  aa:bb:cc:dd:ee:05 주소로 프레임 전달
- 스위치는 해당 주소가 동일 네트워크 영역임을 확인하여 다른 포트로 전달하지 않음
- 필터링은 각 포트별 Collision Domain을 나누어 효율적인 통신이 가능하다.
    

### Aging

- 스위치의 MAC 주소 테이블은 시간이 지나면 삭제
- 삭제되는 이유는 테이블 저장 공간을 효율적으로 사용
- 해당 포트는 연결된 PC가 다른 포트로 옮겨진 경우도 발생
- 기본 300초(Cisco 기준) 저장. 프레임이 발생되면 다시 카운트
    

### 정리

- 프레임 유입
- 신규라면 출발지 주소 저장(Learning)
- 기존에 있는거라면 Aging 타이머 재시작(refresh)

- 목적지가 Unknown → Flooding
- 목적지가 MAC Table에 존재 → Forwarding
- 목적지가 출발지와 같은 포트에 존재 → Filtering

## ARP

### 역할

- ARP(Address Resolution Protocol)
- IP주소를 통해서 MAC 주소를 알려주는 프로토콜
- 컴퓨터 A가 컴퓨터 B에게 IP통신을 시도하고 통신을 수행하기 위해 목적지 MAC 주소를 알아야 한다.
- 목적지 IP에 해당하는 MAC 주소를 알려주는 역할을 ARP가 해준다.
    

### 동작 과정

1. PC1은 동일 네트워크 대역인 목적지 IP 172.20.10.9로 패킷 전송 시도
    - 목적지 MAC 주소를 알기 위해서 우선 자신의 ARP Cache Table을 확인
2. ARP Cache Table에 있으면 패킷 전송. 없으면 ARP Request 전송 - Broadcasting
    
3. IP 172.20.10.9에서 목적지 MAC 주소를 ARP Reply로 전달
4. 목적지 MAC 주소는 ARP Cache Table에 저장되고 패킷 전송

### ARP 헤더구조

Hardware Type : ARP가 동작하는 네트워크 환경, 이더넷

Protocol Type : 프로토콜 종류, 대부분 IPv4

Hardware & Protocol Length : MAC 주소 6Byte, IP주소 4Byte

Operation : 명령코드, 1 = ARP Request, 2 = ARP Reply

Hardware Address = MAC, Protocol Address = IP

## Looping

### 정의

- 같은 네트워크 대역 대에서 스위치에 연결된 경로 2개 이상인 경우 발생
- PC 브로드캐스팅 패킷을 스위치들에게 전달하고 전달 받은 스위치들은 Flooding을 한다
- 스위치들끼리 Flooding된 프레임이 서로 계속 전달되어 네트워크에 문제를 일으킨다.
- 회선 및 스위치 이중화 또는 증축 등에 의해 발생
- 물리적인 포트 연결의 실수 또는 잘못된 이중화 구성으로 L2에서 가장 빈번히 발생하는 이슈

### 구조
1. PC1은 Switch 1에게 브로드캐스팅 전송
2. Switch 1은 모든 포트에 브로드캐스팅 전송
3. 전달받은 브로드캐스팅 프레임을 Switch 2, 3도 모든 포트에 전송
4. Switch 1은 Switch 2, 3에게 다시 전달 받은 브로드캐스팅을 다시 모든 포트로 전송

## STP(spanning Tree Protocol)

### 정의

- 자동으로 루핑을 막아주는 알고리즘(스패닝 트리 알고리즘)
- Bridge ID
    - 스위치의 우선순위로 0 ~ 65535로 설정, 낮을수록 우선순위가 높다
- Path Cost
    - 링크의 속도(대역폭), 1000/링크 속도로 계산되며 작을수록 우선순위가 높다
    - 1Gbps 속도가 나오면서 계산법이 적합하지 않아 IEEE에서 각 대역폭 별 숫자 정의
    - 10Mbps = 100, 100Mbps = 19, 1Gbps = 4

### 요소
1. Root Bridge : 네트워크당 1개 선출
2. Root Port : Root Bridge가 아닌 스위치들은 1개 포트 선출
3. Designated Port: 각 세그먼트별 1개 포트 지정

### BPDU(Bridge Protocol Data Unit)

- 스패닝 트리 프로토콜에 의해 스위치간 서로 주고받는 제어 프레임
1. Configuration BPDU : 구성관련
    - Root BID : 루트 브릿지로 선출될 스위치 정보
    - Path Cost : 루트 브릿지까지의 경로 비용
    - Bridge ID, Port ID : 나머지 스위치와 포트의 우선순위
2. TCN(Topology Change Notification) BPDU
    - 네트워크 내 구성 변경시 통보

- 우선순위 : 낮은 숫자가 더 높은 Priority를 가진다
    - 누가 더 작은 Root BID?
    - 루트 브릿지까지 더 낮은 Path Cost?
    - 연결된 스위치 중 누가 더 낮은 BID?
    - 연결된 포트 중 누가 더 낮은 Port ID?

### Root Bridge 선출
1. 각 스위치는 고유의 BID를 가진다. 2바이트(우선순위) + 6바이트 MAC 주소
2. 서로 BPDU를 교환하고 가장 낮은 숫자가 루트 브리지가 된다
3. 우선순위 숫자를 명령어로 설정 가능하다.

### Root Port 선출

1. 나머지 스위치들은 루트 브리지와 가장 빠르게 연결되는 루트 포트를 선출한다
2. 루트 포트는 가장 낮은 Root Path Cost 값을 가진다.
3. Switch 2 는 P1 = 4 + 19, Switch 3 는 P0 = 19

### Designated Port 선출


1. 각 세그먼트 별 루트 브릿지와 가장 빠르게 연결되는 포트를 Designated 포트로 선출
2. 우선순위는 루트 브릿지 ID > Path Cost > 브릿지 ID > 포트 ID
3. Switch 1 P0 & P1, 1Gbps 라인에서는 Switch 3 P1이 Designated Port가 됨.

### 상태변화

- 스위치 포트는 스패닝 트리 프로토콜 안에서 5가지 상태로 표현된다.
- Disabled
    - 포트가 Shut Donw인 상태로 데이터 전송 불가, MAC 학습 불가, BPDU 송수신 불가
- Blocking
    - 부팅하거나 Disabled 상태를 Up 했을 때 첫번째 거치는 단계, BPDU만 송수신
- Listening - 15초
    - Blocking 포트가 루트 또는 데지그네이티드 포트로 선정되는 단계, BPDU만 송수신
- Learning - 15초
    - 리스닝 상태에서 특정 시간이 흐른 후 러닝 상태가 됨. MAC 학습 시작. BPDU만 송수신
- Forwarding
    - 러닝 상태에서 특정 시간이 흐른 후 포워딩 상태가 됨. 데이터 전송 시작

## RSTP & MST

### RSTP(Rapid spanning Tree Protocol)

- STP를 적용하면 포워딩 상태까지 30~50초 걸림. 이 컨버전스 타임을 1~2초 내외로 단축
- Learning & Listening 단계가 없음
- 대부분 네트워크 환경은 RSTP로 구축되어 있음.

### MST(Multiple Spanning Tree)

- 네트워크 그룹이 많아지면 STP or RSTP BPDU 프레임이 많아지고 스위치 부하 발생
- 여러개의 STP 그룹들을 묶어 효율적으로 관리

## VLAN

### VLAN(Virtual Local Area Network)

- 물리적 구성이 아닌 논리적인 가상의 LAN을 구성하는 기술
- 불필요한 데이터 차단 : 브로드 캐스트 도메인 별로 나누어 관리
- 관리의 용이성과 보안 : 호스트의 물리적 이동 없이 LAN 그룹 변경이 가능
- 비용 절감 : 새로운 LAN 추가 시 물리적 스위치 구매 필요 없음
    - 스위치 하나로 구성.
    

### 종류

- Port 기반 VLAN
    - 여러개의 VLAN을 설정하고 각각의 LAN에 물리적인 포트를 지정
    - VLAN 변경이 필요한 호스트는 물리적인 포트 또는 스위치의 VLAN 설정을 변경
- MAC 주소 기반 VLAN
    - 각 호스트 또는 네트워크 장비의 MAC 주소를 각각의 VLAN에 정의
    - 호스트가 이동되어도 VLAN 변경 필요 없음. 신규 호스트 연결 시 설정 변경 필요
- IP 주소 기반 VLAN
    - IP 주소 서브넷 기반으로 VLAN을 나누는 방법
    - IP(Internet Protocol) : 3계층에서 사용하는 프로토콜, IP 주소 예) 192.168.10.1
    - 서브넷 : IP 주소의 네트워크 영역의 크기를 나눈 것.

### Port 기반 VLAN
- fe : fast ethernet
- gi : giga bit interface

- VLAN 100(총무팀) : fe0 ~ fe4
- VLAN 200(인사팀) : fe5~fe7
- VLAN 300(영업팀) : fe8~fe9

- 변경시 VLAN 그룹에 매핑되어 있는 포트 설정 정보만 변경 또는 물리적인 케이블을 이동하여 연결.

### MAC 주소 기반 VLAN

- VLAN 100(총무팀) : aa:bb:cc:dd:ee:11~20
- VLAN 200(인사팀) : aa:bb:cc:dd:ee:21~30
- VLAN 300(영업팀) : aa:bb:cc:dd:ee:31~40

- VLAN 변경시 호스트의 MAC주소를 다른 VLAN으로 이동
- 신규 호스트 연결 시 MAC 주소를 확인하여 VLAN 그룹에 소속

### IP 주소 기반 VLAN

- VLAN 100(총무팀) : 192.168.1.0/24
- VLAN 200(인사팀) : 192.168.2.0/24
- VLAN 300(영업팀) : 192.168.3.0/24

- VLAN 변경 시 호스트의 IP 주소를 다른 VLAN으로 이동
- 신규 호스트 연결 시 IP 주소를 확인하여 VLAN 그룹에 소속

## TRUNK

- 물리적 스위치 간 VLAN 연결 시 하나의 물리적 연결로 VLAN 그룹들 공유  
    - 대규모 망에서 스위치의 개수 증가.
    - VLAN 그룹 개수도 증가
    - 물리적 연결 케이블은 복잡
- Trunk 사용시
    - 많은 수의 VLAN 연결도 물리적 연결 케이블 하나로 구성할 수 있다.

### 트렁크 프로토콜

- 이더넷 프레임에 식별용 VLAN ID를 삽입하여 데이터를 구분하여 통신 및 제어 가능
- VLAN Tagging : VLAN ID 정보
    

### Tagged Format

- 이더넷 프레임에 삽입되며 4바이트로 구성    
- TPID(Tag Protocol IDentifier) : 태그되지 않은 프레임과 태깅된 프레임을 구분
- TCI(Tag Control Information) : 태그 제어 정보
    - PCP(Priority Code Point) : 프레임의 우선 순위
    - DEI(Drop Eligible Indicator) : 트래픽 혼잡 시 제거되기 적합한 프레임들을 가리킴.
    - VID(VLAN Identifier) : VLAN이 어느 프레임에 속하는지를 결정

## VLAN 구성

### VLAN 설계

- VLAN 그룹 정의
    - 수도코드 작성
    - 총무팀 vlan 100
    - 인사팀 vlan 200
    - 영업팀 : vlan 300
- VLAN 구성 방법 정의
    - 포트, MAC 주소, IP주소
    - MAC 또는 IP 주소 방식의 경우 미리 사전조사 필요
- 트렁크 포트 정의
    - 대역폭 확인
    - 허가(Tagged)할 프레임 정의, 정의되지 않은 Tag는 통신 불가
    

### VLAN 설정

- VLAN 그룹 설정
    - vlan 100
    - vlan 200
    - vlan 300
- 엑세스 모드 : 사용할 포트에 1개의 VLAN ID 설정
    - interface GigabitEthernet 1/0/1
    - switchport mode access
    - switchport access vlan 100
- 트렁크 모드 : 사용할 포트에 여러개의 VLAN ID 설정
    - interface GigabitEthernet 1/0/2
    - switchport mode trunk
    - switchport access vlan 100, 200, 300
- 다이나믹 모드 : 연결된 포트들의 상태에 따라 액세스 또는 트렁크 모드로 변경되는 모드
    - interface GigabitEthernet 1/0/3
    - switchport mode dynamic desirable 또는 auto