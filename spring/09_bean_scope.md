# Bean Scope

### 빈 스코프란?
- 스프링 빈이 스프링 컨테이너의 시작과 함께 생성되어서 스프링 컨테이너가 종료될 때 까지 유지되는 이유는 스프링 빈이 기본적으로 싱글톤 스코프로 생성되기 때문이다. 
  - 스코프 : 빈이 존재할 수 있는 범위

<br>

### 스프링이 지원하는 스코프
- **싱글톤**: 기본 스코프, 스프링 컨테이너의 시작과 종료까지 유지되는 가장 넓은 범위의 스코프이다.
- **프로토타입**: 스프링 컨테이너는 프로토타입 **빈의 생성과 의존관계 주입까지만 관여**하고 더는 관리하지 않는 매우 짧은 범위의 스코프이다.
- **웹 관련 스코프**
  - request
    - HTTP 요청 하나가 들어오고 나갈 때 까지 유지되는 스코프, 각각의 HTTP 요청마다 **별도의 빈 인스턴스**가 생성되고, 관리된다.
  - session
    - HTTP Session과 동일한 생명주기를 가지는 스코프
  - application
    - 서블릿 컨텍스트( ServletContext )와 동일한 생명주기를 가지는 스코프
  - websocket
    - 웹 소켓과 동일한 생명주기를 가지는 스코프


<br>

### 프로토타입 스코프
- 싱글톤 스코프의 빈을 조회하면 스프링 컨테이너는 항상 같은 인스턴스의 스프링 빈을 반환한다.
- 반면에 프로토타입 스코프를 스프링 컨테이너에 조회하면 스프링 컨테이너는 항상 **새로운 인스턴스**를 생성해서 반환한다.

<br>

### 프로토타입 빈
- 스프링 컨테이너에 요청할 때 마다 새로 생성된다.
- 스프링 컨테이너는 프로토타입 빈의 생성과 의존관계 주입 그리고 초기화까지만 관여한다.
- 종료 메서드가 호출되지 않는다.
  - @PreDestroy 같은 종료 메서드가 호출되지 않는다.
- 그래서 프로토타입 빈은 프로토타입 빈을 조회한 클라이언트가 관리해야 한다. 종료 메서드에 대한 호출도 클라이언트가 직접 해야한다.


<br>

### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

**싱글톤 빈에서 프로토타입 빈 사용**
- test.java.hello.core.beanscope.SingletonWithPrototypeTest1 참조
- 프로토타입 빈을 사용하는 싱글톤 빈이 있다 가정.
- 싱글톤 빈은 스프링 빈에 등록되면서 autowired로 프로토타입 빈을 스프링 빈에 요청.
- 싱글톤 빈의 생성시점에 프로토타입 빈이 주입. 그 주입된 프로토타입 빈을 계속 사용.
- 만약 프로토타입 빈을 주입 시점에만 생성하는 것이 아니라 사용할 때 마다 새로 생성하도록 하려면?

<br>

### Provider
**DL이란?**
- 의존관계를 외부에서 주입(DI) 받는게 아니라 직접 필요한 의존관계를 찾는 것을 Dependency Lookup (DL) 의존관계 조회(탐색) 이라한다.

<br>

**ObjectFactory, ObjectProvider**
- 지정한 빈을 컨테이너에서 대신 찾아주는 DL 서비스를 제공하는 것이 바로 ObjectProvider
- prototypeBeanProvider.getObject() 을 통해 항상 새로운 프로토타입 빈이 생성된다.
- ObjectProvider 의 getObject() 를 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환한다. (**DL**)
- 스프링이 제공하는 기능을 사용하지만, 기능이 단순하므로 단위테스트를 만들거나 mock 코드를 만들기는 훨씬 쉬워진다.

<br>

**JSR-330 Provider**
- javax.inject.Provider 라는 JSR-330 자바 표준을 사용하는 방법이다.
- `provider.get()` 을 통해서 항상 새로운 프로토타입 빈이 생성된다
- provider 의 get() 을 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환한다. (**DL**)
- **자바 표준**이고, 기능이 단순하므로 단위테스트를 만들거나 mock 코드를 만들기는 훨씬 쉬워진다.

<br>

## 웹 스코프
### 웹 스코프의 특징
- 웹 스코프는 웹 환경에서만 동작한다.
- 웹 스코프는 프로토타입과 다르게 스프링이 해당 스코프의 종료시점까지 관리한다. 따라서 종료 메서드가 호출된다.

<br>


### request 스코프
참조: (src.main.java.hello.core.common, src.main.java.hello.core.web)

- `Error creating bean with name 'myLogger': Scope 'request' is not active for the current thread;` 에러 발생
- MyLogger는 request scope이므로 client의 요청이 있을 때의 생명주기를 가짐. 그런데 스프링 실행 시점에는 요청이 없으므로 MyLooger를 주입 받을 수 없다.
- Provider 사용해야함.
- `ObjectProvider` 덕분에 `ObjectProvider.getObject()` 를 호출하는 시점까지 request scope **빈의 생성을 지연**할 수 있다.
- `ObjectProvider.getObject()` 를 호출하시는 시점에는 HTTP 요청이 진행중이므로 request scope 빈의 생성이 정상 처리된다.
- `ObjectProvider.getObject()` 를 LogDemoController , LogDemoService 에서 각각 한번씩 따로 호출해도 같은 HTTP 요청이면 같은 스프링 빈이 반환된다.

<br>

### 스코프와 프록시
`@Scope(value = "request", proxyMode = ScopedProxyMode.TARGET_CLASS)`
  - 적용 대상이 클래스면 TARGET_CLASS, 인터페이스면 INTERFACES를 선택
- 이렇게 하면 MyLogger의 가짜 프록시 클래스를 만들어두고 HTTP request와 상관 없이 가짜 프록시 클래스를 다른 빈에 미리 주입해 둘 수 있다.
- @Scope 의 `proxyMode = ScopedProxyMode.TARGET_CLASS)`를 설정하면 스프링 컨테이너는 CGLIB 라는 바이트코드를 조작하는 라이브러리를 사용해서, MyLogger를 상속받은 가짜 프록시 객체를 생성하여 등록한다.
  - 의존관계 주입도 이 가짜 프록시 객체가 주입된다.
  - 클라이언트가 myLogger.logic() 을 호출하면 사실은 가짜 프록시 객체의 메서드를 호출한 것이다.
  - 가짜 프록시 객체는 request 스코프의 진짜 myLogger.logic()를 호출한다.
- 클라이언트 입장에서는 원본인지 가짜인지 모르고 동일하게 사용할 수 있다(다형성)

<br>

Provider를 사용하든, 프록시를 사용하든 핵심은 진짜 객체 조회를 꼭 필요한 시점까지 **지연처리** 한다는 점이다.