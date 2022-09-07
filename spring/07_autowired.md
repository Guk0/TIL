# Autowired
### 의존관계 주입 방법
- 생성자 주입
- 수정자 주입(setter 주입)
- 필드 주입
- 일반 메서드 주입

<br>

### 생성자 주입
- 생성자를 통해서 의존 관계를 주입 받는 방법이다.
- 특징
    - 생성자 호출시점에 딱 1번만 호출되는 것이 보장된다.
    - **불변, 필수** 의존관계에 사용
        - 불변 : 딱 한번만 호출. 바뀌지 않는 값. 생성자만 사용하고 setter를 사용하지 말아야함.
        - 필수 : `final` 값이 무조건 있어야 함.
- **생성자가 딱 1개만 있으면 @Autowired를 생략해도 자동 주입된다.**

<br>

### 수정자 주입(setter 주입)
- setter를 통해서 의존관계를 주입하는 방법이다.
- 특징
    - **선택, 변경** 가능성이 있는 의존관계에 사용
    - 자바빈 프로퍼티 규약의 수정자 메서드 방식을 사용하는 방법이다.
- 참고: `@Autowired` 의 기본 동작은 주입할 대상이 없으면 오류가 발생한다. 주입할 대상이 없어도 동작하게 하려면 `@Autowired(required = false)` 로 지정하면 된다.

<br>

### 필드주입
- 필드에 바로 주입하는 방법이다.
    
    ```java
    @Component
    public class OrderServiceImpl implements OrderService {
    	  @Autowired
    	  private MemberRepository memberRepository;
    	  @Autowired
    	  private DiscountPolicy discountPolicy;
    }
    ```
- 특징
    - 코드가 간결해서 많은 개발자들을 유혹하지만 외부에서 변경이 불가능해서 **테스트 하기 힘들다**는 치명적인 단점이 있다.
    - DI 프레임워크가 없으면 아무것도 할 수 없다. 순수한 자바코드로 테스트 불가능.
    - setter를 사용해야한다. setter를 사용할바엔 setter에 @Autowired를 거는게 낫다.
- 아래의 경우가 아니면 사용하지 않는 것이 좋다.
    - 애플리케이션의 실제 코드와 관계 없는 테스트 코드에서는 사용할 수도 있다.
    - 스프링 설정을 목적으로 하는 `@Configuration` 같은 곳에서만 특별한 용도로 사용

<br>    

### 일반 메서드 주입
- setter가 아닌 일반 메서드를 통해서 주입 받을 수 있다.
- 특징
    - 한번에 여러 필드를 주입 받을 수 있다.
    - 일반적으로 잘 사용하지 않는다.

<br>

### 옵션처리
- 주입할 스프링 빈이 없어도 동작해야 할 때가 있다.
- 그런데 `@Autowired` 만 사용하면 required 옵션의 기본값이 true 로 되어 있어서 자동 주입 대상이 없으면 오류가 발생한다.

- 자동 주입 대상을 옵션으로 처리하는 방법은 다음과 같다.
    - `@Autowired(required=false)` : 자동 주입할 대상이 없으면 수정자 메서드 자체가 호출 안됨.
    - `org.springframework.lang.@Nullable` : 자동 주입할 대상이 없으면 null이 입력된다. 호출은 된다.
    - `Optional<>` : 자동 주입할 대상이 없으면 `Optional.empty` 가 입력된다.
    - test.java.hello.core.autowired에 테스트 코드 참고

<br>

### 생성자 주입을 선택해야하는 이유
과거에는 수정자 주입과 필드 주입을 많이 사용했지만, 최근에는 스프링을 포함한 DI 프레임워크 대부분이 생성자 주입을 권장한다. 그 이유는 다음과 같다.

**불변**
- 대부분의 의존관계 주입은 한번 일어나면 애플리케이션 종료시점까지 의존관계를 변경할 일이 없다. 오히려 대부분의 의존관계는 애플리케이션 종료 전까지 변하면 안된다.(**불변해야 한다.**)
- 수정자 주입을 사용하면, setXxx 메서드를 public으로 열어두어야 한다.
- 누군가 실수로 변경할 수 도 있고, 변경하면 안되는 메서드를 열어두는 것은 좋은 설계 방법이 아니다.
- 생성자 주입은 객체를 생성할 때 딱 1번만 호출되므로 이후에 호출되는 일이 없다. 따라서 불변하게 설계할 수 있다.

**누락**
- 프레임워크 없이 순수한 자바 코드를 단위 테스트 하는 경우에 다음과 같이 수정자 의존관계인 경우
- `@Autowired` 가 프레임워크 안에서 동작할 때는 의존관계가 없으면 오류가 발생하지만, 지금은 프레임워크 없이 순수한 자바 코드로만 단위 테스트를 수행하고 있다.

**final 키워드**
- 생성자 주입을 사용하면 필드에 final 키워드를 사용할 수 있다.
- 그래서 생성자에서 혹시라도 값이 설정되지 않는 오류를 컴파일 시점에 막아준다.

**정리**
- 생성자 주입 방식을 선택하는 이유는 여러가지가 있지만, 프레임워크에 의존하지 않고, 순수한 자바 언어의 특징을 잘 살리는 방법이기도 하다.
- 기본으로 생성자 주입을 사용하고, 필수 값이 아닌 경우에는 수정자 주입 방식을 옵션으로 부여하면 된다.
- 생성자 주입과 수정자 주입을 동시에 사용할 수 있다.
- 항상 생성자 주입을 선택해라! 그리고 가끔 옵션이 필요하면 수정자 주입을 선택해라. 필드 주입은 사용하지 않는게 좋다.

<br>

### 롬복과 최신 트랜드
- 대부분이 다 불변이고, 그래서 필드에 final 키워드를 사용하게 된다.
- 그런데 생성자도 만들어야 하고, 주입 받은 값을 대입하는 코드도 만들어야 하고...
- 이를 롬복을 통해 최적화할 수 있다.
- 롬복의 `@Getter`, `@Setter` 어노테이션을 이용하여 getter와 setter를 정의하지 않고도 사용할 수 있다.
    - `@ToString` 어노테이션도 있다.
- `@RequiredArgsConstructor`
    - 필드 중 final이 붙은 필드를 생성자로 만들어줌.
    - 많이 사용함. OrderServiceImpl 참조
    

<br>

### 조회 빈이 2개 이상
- @Autowired 는 타입(Type)으로 조회한다.
- 타입으로 조회하기 때문에, 마치 다음 코드와 유사하게 동작한다. (실제로는 더 많은 기능을 제공한다.)
    - `ac.getBean(DiscountPolicy.class)`
- 타입으로 조회하면 선택된 빈이 2개 이상일 때 문제가 발생한다.
- DiscountPolicy 의 하위 타입인 FixDiscountPolicy , RateDiscountPolicy 둘다 스프링 빈으로 선언해보자.
    - expected single matching bean but found 2: fixDiscountPolicy,rateDiscountPolicy
        - 위와 같은 오류 발생.
    - OrderServiceImple 생성자에서 문제 발생.
    - 이때 하위 타입으로 지정할 수 도 있지만, 하위 타입으로 지정하는 것은 DIP를 위배하고 유연성이 떨어진다.
    - 그리고 이름만 다르고, 완전히 똑같은 타입의 스프링 빈이 2개 있을 때 해결이 안된다.
    - 스프링 빈을 수동 등록해서 문제를 해결해도 되지만, 의존 관계 자동 주입에서 해결하는 여러 방법이 있다.

<br>

### @Autowired 필드 명, @Qualifier, @Primary
조회 대상 빈이 2개 이상일 때 해결 방법
- @Autowired 필드 명 매칭
    ```java
    @Autowired
    private DiscountPolicy rateDiscountPolicy
    ```
- @Qualifier → @Qualifier끼리 매칭 → 빈 이름 매칭
    - @Qualifier 는 추가 구분자를 붙여주는 방법이다. 주입시 추가적인 방법을 제공하는 것이지 빈 이름을 변경하는 것은 아니다.
    
    ```java
    @Component
    @Qualifier("mainDiscountPolicy")
    public class RateDiscountPolicy implements DiscountPolicy {}
    ```
    
    ```java
    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, @Qualifier("mainDiscountPolicy") DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
    ```
    - `@Qualifier` 는 `@Qualifier` 를 찾는 용도로만 사용하는게 명확하고 좋다.
    - 매칭 순서
        - 1. @Qualifier끼리 매칭
        - 2. 빈 이름 매칭
        - 3. NoSuchBeanDefinitionException 예외 발생
- @Primary 사용
    - `@Primary` 는 우선순위를 정하는 방법이다. `@Autowired` 시에 여러 빈이 매칭되면 `@Primary` 가 우선권을 가진다.
    - `@Qualifier` 의 단점은 주입 받을 때 다음과 같이 모든 코드에 `@Qualifier` 를 붙여주어야 한다. 반면 `@Primary`는 모든 코드에 붙일 필요 없다.
        - 둘 다 사용할때는 `@Qualifier`가 우선 순위가 높다.

<br>

### 어노테이션 직접 만들기
- `@Qualifier("mainDiscountPolicy")` 이렇게 문자를 적으면 컴파일시 타입 체크가 안된다.
- 애노테이션을 직접 만들어서 문제를 해결할 수 있다.

<br>

### 조회한 빈이 모두 필요할 때. List, Map
- 의도적으로 정말 해당 타입의 스프링 빈이 다 필요한 경우도 있다.
- 예를 들어서 할인 서비스를 제공하는데, 클라이언트가 할인의 종류(rate, fix)를 선택할 수 있다고 가정해보자. 스프링을 사용하면 소위 말하는 전략 패턴을 매우 간단하게 구현할 수 있다.
- [test.java.hello.core.autowired.AllBeanTest.java](http://test.java.hello.core.autowired.AllBeanTest.java) 참조

<br>

### 자동, 수동의 올바른 실무 운영 기준
- 점점 자동을 선호하는 추세
- 스프링은 @Component 뿐만 아니라 @Controller , @Service , @Repository 처럼 계층에 맞추어 일반적인 애플리케이션 로직을 자동으로 스캔할 수 있도록 지원한다.
- 거기에 더해서 최근 스프링 부트는 컴포넌트 스캔을 기본으로 사용하고, 스프링 부트의 다양한 스프링 빈들도 조건이 맞으면 자동으로 등록하도록 설계했다.

<br>

### 수동 빈은 언제 사용하면 좋을까?
- **업무 로직 빈:** 웹을 지원하는 **컨트롤러**, 핵심 비즈니스 로직이 있는 **서비스**, 데이터 계층의 로직을 처리하는
**리포지토리** 등이 모두 업무 로직이다. 보통 비즈니스 요구사항을 개발할 때 추가되거나 변경된다.
    - 업무 로직은 숫자도 매우 많고, 한번 개발해야 하면 컨트롤러, 서비스, 리포지토리 처럼 어느정도 유사한 패턴이 있다. 이런 경우 **자동 기능을 적극 사용하는 것이 좋다**. 보통 문제가 발생해도 어떤 곳에서 문제가 발생했는지 명확하게 파악하기 쉽다.
- **기술 지원 빈:** 기술적인 문제나 공통 관심사(AOP)를 처리할 때 주로 사용된다. 데이터베이스 연결이나,
공통 로그 처리 처럼 업무 로직을 지원하기 위한 하부 기술이나 공통 기술들이다.
    - 기술 지원 로직은 업무 로직과 비교해서 그 수가 매우 적고, 보통 애플리케이션 전반에 걸쳐서 광범위하게 영향을 미친다. 그리고 업무 로직은 문제가 발생했을 때 어디가 문제인지 명확하게 잘 드러나지만, 기술 지원 로직은 적용이 잘 되고 있는지 아닌지 조차 파악하기 어려운 경우가 많다. 그래서 이런 기술 지원 로직들은 가급적 수동 빈 등록을 사용해서 명확하게 드러내는 것이 좋다.