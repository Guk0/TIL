## Event Driven Architecture
- msa 환경에서 노드끼리 통신(HTTP, RPC)을 하다보면 특정 노드에서 에러 발생할 시 다른 노드에 에러가 전파되어 서비스가 마비될 수 있다. 
- api를 이용하여 노드끼리 통신하는 방법 보다는 **메세지 큐** 방식으로 이벤트를 발행하고 해당 이벤트를 구독하고 있는 노드에서 이벤트를 식별하고 작업을 비동기적으로 처리하여 서비스 간 결합도를 낮출 수 있다.
- 이를 **event driven architecture** 라 한다.


<br>


### 서킷브레이커
일반적으로 http나 rpc를 이용한 통신에서는 장애가 전파되지 않도록 서킷브레이커를 걸 수도 있다.
1. 외부 API 통신 시도
2. 외부 통신이 실패함으로써 서킷브레이커 Open
3. Open과 동시에 외부 서버에 요청을 날리지 않고, Fail Fast로 빠른응답 리턴
4. 서킷브레이커가 오픈하면 일정 시간 후에 반오픈(Half-Open) 상태
5. 반오픈 상태에서 다시 외부 서비스를 호출해서 장애를 확인하면 Open, 정상 응답이면 닫힘


<br>

참고  
[https://medium.com/dtevangelist/event-driven-microservice-란-54b4eaf7cc4a](https://medium.com/dtevangelist/event-driven-microservice-%EB%9E%80-54b4eaf7cc4a)  
[https://team.modusign.co.kr/마이크로-서비스-통합-b08979275b59](https://team.modusign.co.kr/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%ED%86%B5%ED%95%A9-b08979275b59)  
[https://velog.io/@hgs-study/CircuitBreaker](https://velog.io/@hgs-study/CircuitBreaker)