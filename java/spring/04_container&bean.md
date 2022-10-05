# spring container and spring bean

### 스프링 컨테이너 생성
```java
//스프링 컨테이너 생성
ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);

```
- ApplicationContext 를 스프링 컨테이너라 하고 인터페이스이다.
- 스프링 컨테이너는 XML을 기반으로 만들 수 있고, **애노테이션 기반**의 자바 설정 클래스로 만들 수 있다.
- 직전에 AppConfig 를 사용했던 방식이 애노테이션 기반의 자바 설정 클래스로 스프링 컨테이너를 만든 것이다.
- AnnotationConfigApplicationContext 는 자바 설정 클래스를 기반의 스프링 컨테이너( ApplicationContext ) 구현체이다. 
- 참고
    - 스프링 컨테이너를 지칭할 때 BeanFactory , ApplicationContext 로 구분한다.
    - BeanFactory 를 직접 사용하는 경우는 거의 없으므로 일반적으로 ApplicationContext 를 스프링 컨테이너라 한다.
    
<br>

### 빈 이름
- 빈 이름은 메서드 이름을 사용한다.
- 빈 이름을 직접 부여할 수 도 있다.
    - `@Bean(name="memberService2")`
- **주의**
    - **빈 이름은 항상 다른 이름을 부여**해야 한다. 같은 이름을 부여하면, 다른 빈이 무시되거나, 기존 빈을 덮어버리거나 설정에 따라 오류가 발생한다.

<br>    

### 스프링 빈 상속관계
- 부모 타입으로 조회하면 자식 타입도 함께 조회한다.
- 모든 자바 객체의 최고 부모 객체인 Object 타입으로 조회하면 모든 스프링 빈을 조회한다.

<br>

## Bean Factory와 ApplicationContext
### BeanFactory
- 스프링 컨테이너의 최상위 인터페이스다.
- **스프링 빈을 관리하고 조회**하는 역할을 담당한다.
- getBean()을 제공

<br>

### ApplicationContext
- BeanFactory 상속 받음
- ApplicationContext가 제공하는 **부가 기능**
    - **메시지소스를 활용한 국제화 기능**
        - 예를 들어서 한국에서 들어오면 한국어로, 영어권에서 들어오면 영어로 출력
    - **환경변수**
        - 로컬, 개발, 운영 등을 구분해서 처리
    - **애플리케이션 이벤트**
        - 이벤트를 발행하고 구독하는 모델을 편리하게 지원
    - **편리한 리소스 조회**
        - 파일, 클래스패스, 외부 등에서 리소스를 편리하게 조회
- BeanFactory를 직접 사용할 일은 거의 없다. 부가기능이 포함된 ApplicationContext를 사용한다.
- BeanFactory나 ApplicationContext를 스프링 컨테이너라 한다.

<br>

### 다양한 설정 형식 지원
- 스프링 컨테이너와 스프링 빈을 이용하는 방법에는 설정 자바파일에 어노테이션을 사용하는 것과 XML을 사용하는 방법이 있다.

<br>

### 스프링 빈 설정 메타 정보
- 스프링은 **`BeanDefinition`** 이라는 추상화를 통해 다양한 설정 형식(자바 코드, XML 등)을 제공한다.
    - **역할과 구현을 개념적으로 나눔**
    - XML, 혹은 자바 코드를 읽고 BeanDefinition을 만든다.
    - 스프링 컨테이너는 자바 코드인지, XML인지 몰라도 된다. 오직 BeanDefinition만 알면 된다.
    - 스프링은 BeanDefinition에만 의존한다. BeanDefinition는 인터페이스
- BeanDefinition 을 빈 설정 메타정보라 한다.
    - @Bean , <bean> 당 각각 하나씩 메타 정보가 생성된다.
- 스프링 컨테이너는 이 메타정보를 기반으로 스프링 빈을 생성한다.