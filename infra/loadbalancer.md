## L4 VS L7 로드밸런서
클라우드에서는 이 둘을 구분하는데 AWS의 **NLB**(network load balancer)는 L4이고, **ALB**(application load balancer)는 L7입니다.

<br>

## L4 로드 밸런싱(Layer 4 - 전송계층)
- L4 로드 밸런서는 **네트워크 계층(IP, IPX)이나 전송 계층(TCP, UDP)의 정보**(IP주소, 포트번호, MAC주소, 전송 프로토콜)를 바탕으로 로드를 분산한다.
- 최근의 로드 밸런서는 L4, L7의 기능을 모두 지원하므로 L4 기능만 전용으로 제공하는 로드 밸런서 장비는 찾기 어려워졌고 어떻게 설정했는지, 무슨 정보를 사용하는지에 따라 4계층 정보로만 분산처리를 할 경우 L4 로드 밸런서라고 합니다. 단순히 443 포트냐, 80 포트냐만을 본다면 L4 로드 밸런서입니다.

<br>

## L7 로드 밸런싱(Layer 7 - 응용계층)
- L7 로드 밸런서는 HTTP, FTP, SMTP와 같은 프로토콜을 기반으로 로드밸런싱합니다.
    - 그러니까, HTTP의 헤더나 url 주소를 기반으로 연결한 서버를 분기한다면 그건 L7 로드 밸런서라는 겁니다.
- 이러한 로드 밸런서를 **ADC**(Application Delivery  Controller)라고 부릅니다.

<br>

## vs API Gateway
주로 MSA환경에서 많이 사용. 라우팅을 통해 MSA의 여러 서비스들을 하나의 도메인으로 관리할 수 있다. 
장점
- 클라이언트에서 어느 마이크로서비스 인스턴스로 요청을 보낼지 고민하지 않아도 된다.
- 백엔드 마이크로서비스의 복잡도를 숨길 수 있다.
- 클라이언트 입장에서 여러 개의 서비스를 하나의 서비스로 취급하거나, 반대로 한 개의 서비스를 여러 서비스로 취급하여 처리할 수 있다.
- 요청에 대한 공통 관심사를 중앙에서 처리할 수 있다. (Security, Routing, Rate Limiting, Monitoring etc)


[참고](https://darrengwon.tistory.com/1329)
