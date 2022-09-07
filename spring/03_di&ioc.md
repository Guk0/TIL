# di & ioc

```java
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    // private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    // private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
    private DiscountPolicy discountPolicy;
    // 누군가가 discountPolicy의 구현객체를 대신 생성하고 주입해줘야함.

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice); // db에 따로 저장하지 않는다.
    }
}
```

- `OrderServiceImpl`은 `MemberRepository` 인터페이스에도 의존하고 `MemoryMemberRepository` 에도 의존하게 된다. DIP 원칙 위배. OCP 원칙도 위배.

<br>

관심사의 분리
- 애플리케이션이 하나의 공연이고 각각의 인터페이스를 배역(배우 역할)이라 가정.
    - 배역 맞는 배우를 선택하는 것은 누가 하는가?
- 배역을 정하는 것은 배우들이 정하는게 아니다. 이전 코드는 마치 로미오 역할(인터페이스)을 하는 레오나르도 디카프리오(구현체, 배우)가 줄리엣 역할(인터페이스)을 하는 여자 주인공(구현체, 배우)을 직접 초빙하는 것과 같다. 디카프리오는 공연도 해야하고 동시에 여자 주인공도 공연에 직접 초빙해야 하는 **다양한 책임**을 가지고 있다

<br>

### AppConfig
- 위 배역을 결정하는 역할. 공연 기획자. 배우와 공연 기획자의 책임을 확실히 분리
- AppConfig는 애플리케이션의 실제 동작에 필요한 **구현 객체를 생성**한다.
    - MemberServiceImpl
    - MemoryMemberRepository
    - OrderServiceImpl
    - FixDiscountPolicy
- AppConfig는 생성한 객체 인스턴스의 참조(레퍼런스)를 **생성자를 통해서 주입(연결)**해준다.
    - MemberServiceImpl MemoryMemberRepository
    - OrderServiceImpl MemoryMemberRepository , FixDiscountPolicy

<br>

```java
public class AppConfig {
    public MemberService memberService() {
        return new MemberServiceImpl(new MemoryMemberRepository());
    }

    public OrderService orderService() {
				return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }
}
```
- MemberServiceImpl의 생성자를 통해 MemberRepository의 구현체를 주입함.
    - 생성자 주입.
- OrderApp 혹은 MemberApp에서 MemberService, OrderService를 가져와 사용.

<br>

```java
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice); // db에 따로 저장하지 않는다.
    }
}
```
- 이렇게 된다면 철저하게 DIP를 지키고 있다고 볼 수 있음.
    - 인터페이스에만 의존하고 있음.
- appConfig 객체는 memoryMemberRepository 객체를 생성하고 그 참조값을 memberServiceImpl 을 생성하면서 생성자로 전달한다.
- 클라이언트인 memberServiceImpl 입장에서 보면 의존관계를 마치 외부에서 주입해주는 것 같다고 해서  DI(Dependency Injection) 우리말로 **의존관계 주입** 또는 **의존성 주입**이라 한다.
- 설계 변경으로 OrderServiceImpl 은 FixDiscountPolicy 를 의존하지 않는다!
- 단지 DiscountPolicy 인터페이스만 의존한다.
- OrderServiceImpl 입장에서 생성자를 통해 어떤 구현 객체가 들어올지(주입될지)는 알 수 없다.
- OrderServiceImpl 의 생성자를 통해서 어떤 구현 객체을 주입할지는 오직 외부( AppConfig )에서 결정한다.
- OrderServiceImpl 은 이제부터 실행에만 집중하면 된다.
- 결국 AppConfig를 사용하는 것은 사용 영역의 코드를 수정하지 않고 구성 영역의 코드만 수정하도록 하는 것.

<br>

## 좋은 객체 지향 설계의 5가지 원칙의 적용
여기서 3가지 SRP, DIP, OCP 적용

### SRP
- 단일 책임 원칙한 클래스는 하나의 책임만 가져야 한다.
- 클라이언트 객체는 직접 구현 객체를 생성하고, 연결하고, 실행하는 다양한 책임을 가지고 있음
- SRP 단일 책임 원칙을 따르면서 관심사를 분리함
- 구현 객체를 생성하고 연결하는 책임은 `AppConfig`가 담당
- 클라이언트 객체는 실행하는 책임만 담당

<br>

### DIP 의존관계 역전 원칙
- 프로그래머는 “추상화에 의존해야지, 구체화에 의존하면 안된다.” 의존성 주입은 이 원칙을 따르는 방법 중 하나다.
- 새로운 할인 정책을 개발하고, 적용하려고 하니 클라이언트 코드도 함께 변경해야 했다. 왜냐하면 기존 클라이언트 코드( `OrderServiceImpl` )는 DIP를 지키며 `DiscountPolicy` 추상화 인터페이스에 의존하는 것 같았지만, `FixDiscountPolicy` 구체화 구현 클래스에도 함께 의존했다.
- AppConfig가 `FixDiscountPolicy` 객체 인스턴스를 클라이언트 코드 대신 생성해서 클라이언트 코드에 의존관계를 주입했다. 이렇게해서 DIP 원칙을 따르면서 문제도 해결했다.

<br>

### OCP
- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다
- 애플리케이션을 사용 영역과 구성 영역으로 나눔
- AppConfig가 의존관계를 `FixDiscountPolicy`  → `RateDiscountPolicy` 로 변경해서 클라이언트 코드에 주입하므로 클라이언트 코드는 변경하지 않아도 됨

<br>

## IoC, DI, 그리고 컨테이너
### 제어의 역전 IoC(Inversion of Control)
- AppConfig 도입 전에는 클라이언트 구현 객체가 스스로 필요한 서버 구현 객체를 **생성**하고, **연결**하고, **실행**했다.
    - → 구현 객체가 프로그램의 제어 흐름을 스스로 조종했다.
- 반면에 AppConfig가 등장한 이후에 구현 객체는 **자신의 로직을 실행하는 역할만 담당**한다. **프로그램의 제어 흐름**은 이제 AppConfig가 가져간다. OrderServiceImpl 은 필요한 인터페이스들을 호출하지만 어떤 구현 객체들이 실행될지 모른다.
- **프로그램에 대한 제어 흐름**에 대한 권한은 모두 AppConfig가 가지고 있다. 심지어 OrderServiceImpl도 AppConfig가 생성한다. 그리고 AppConfig는 OrderServiceImpl 이 아닌 OrderService 인터페이스의 다른 구현 객체를 생성하고 실행할 수 도 있다. OrderServiceImpl 은 묵묵히 자신의 로직만 실행할 뿐이다.
- 이렇듯 프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는 것을 제어의 역전(IoC)이라 한다.
    - 객체가 갖는 의존성을 외부에서 결정시키는 것. 외부라 함은 프레임워크가 될 수도 있고 개발자가 정의한 계층(AppConfig와 같은 클래스)일 수도 있다.

<br>

### 프레임워크 vs 라이브러리
- 프레임워크가 내가 작성한 코드를 제어하고, 대신 실행하면 그것은 프레임워크가 맞다. (JUnit)
    - **작성한 코드의** 제어권**이 나에게 없다면 프레임워크.**
    - JUnit은 작성한 테스트 코드를 호출하는 부분이 없음. JUnit이 그것을 실행하므로 프레임워크다.
- 반면에 내가 작성한 코드가 직접 제어의 흐름을 담당한다면 그것은 프레임워크가 아니라 라이브러리다.

<br>

### 의존관계 주입 DI(Dependency Injection)
- OrderServiceImpl 은 DiscountPolicy 인터페이스에 의존한다. 실제 어떤 구현 객체가 사용될지는 모른다.
- 의존관계는 **정적인 클래스 의존 관계와, 실행 시점에 결정되는 동적인 객체(인스턴스) 의존 관계** 둘을 분리해서 생각해야 한다.

<br>

### 정적인 클래스 의존관계
- 클래스가 사용하는 import 코드만 보고 의존관계를 쉽게 판단할 수 있다.
- 그런데 이러한 클래스 의존관계 만으로는 실제 어떤 객체가 OrderServiceImpl 에 주입 될지 알 수 없다.

<br>

### 동적인 객체 인스턴스 의존 관계
애플리케이션 **실행 시점**에 실제 생성된 객체 인스턴스의 참조가 연결된 의존 관계다.
- 애플리케이션 **실행 시점(런타임)** 에 외부에서 실제 구현 객체를 생성하고 클라이언트에 전달해서 클라이언트와 서버의 실제 의존관계가 연결 되는 것을 **의존관계 주입** 이라 한다.
    - 객체 인스턴스를 생성하고 그 참조값을 전달해서 연결된다.
- 의존관계 주입을 사용하면 클라이언트 코드를 변경하지 않고, 클라이언트가 호출하는 대상의 타입 인스턴스를 변경할 수 있다.
- 의존관계 주입을 사용하면 정적인 클래스 의존관계를 변경하지 않고, 동적인 객체 인스턴스 의존관계를 쉽게 변경할 수 있다.
    - 정적인 클래스 의존관계 변경 x.   →   애플리케이션 코드를 손대지 않는다.

<br>

### IoC 컨테이너, DI 컨테이너
- AppConfig 처럼 객체를 생성하고 관리하면서 의존관계를 연결해 주는 것을 IoC 컨테이너 또는 **DI 컨테이너**라 한다.
    - 의존관계 주입에 초점을 맞추어 최근에는 주로 DI 컨테이너라 한다.
    - 또는 어샘블러, 오브젝트 팩토리 등으로 불리기도 한다.

<br>

### 스프링 빈 컨테이너 사용
- AppConfig에 `@Configuration` 어노테이션 적용.
- 각 메서드에 `@Bean` 어노테이션 적용.
- MemberApp에 아래와 같이 코드 적용

```java
ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
MemberService memberService = applicationContext.getBean("memberService", MemberService.class);
```

<br>

### **스프링 컨테이너**

- `ApplicationContext` 를 스프링 컨테이너라 한다.
- 기존에는 개발자가 AppConfig 를 사용해서 직접 객체를 생성하고 DI를 했지만, 이제부터는 스프링 컨테이너를 통해서 사용한다.
- 스프링 컨테이너는 `@Configuration` 이 붙은 AppConfig 를 설정(구성) 정보로 사용한다. 여기서 `@Bean` 이라 적힌 메서드를 모두 호출해서 반환된 객체를 스프링 컨테이너에 등록한다. 이렇게 스프링 컨테이너에 등록된 객체를 스프링 빈이라 한다.
- 스프링 빈은 `@Bean` 이 붙은 메서드의 명을 스프링 빈의 이름으로 사용한다. ( memberService , orderService )
- 빈으로 등록된 객체는 `applicationContext.getBean()` 메서드를 사용해서 찾을 수 있다.
- 순수 자바 코드가 아닌 스프링 컨테이너에 객체를 스프링 빈으로 등록하고, 스프링 컨테이너에서 스프링 빈을 찾아서 사용하도록 변경되었다.

<br>

스프링 컨테이너
- 빈을 등록하는 공간

스프링 빈
- 스프링 컨테이너에 등록된 객체