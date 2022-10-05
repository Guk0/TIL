# Component Scan
### 컴포넌트 스캔
- 클래스에 `@Component` 를 붙여주면 Config에서 `@ComponentScan`을 통해 찾아와 Bean에 등록함.
- 생성자에 `@Autowired`를 붙여주면 의존관계를 자동으로 주입해줌.
  - 마치 `ac.getBean(MemberRepository.class)` 와 같이 동작
    
<br>

### @ComponentScan
- @ComponentScan 은 @Component 가 붙은 모든 클래스를 스프링 빈으로 등록한다.
- 이때 스프링 빈의 기본 이름은 클래스명을 사용하되 맨 앞글자만 소문자를 사용한다.
    - **빈 이름 기본 전략:** MemberServiceImpl 클래스 memberServiceImpl
    - **빈 이름 직접 지정:** 만약 스프링 빈의 이름을 직접 지정하고 싶으면`@Component("memberService2")` 이런식으로 이름을 부여하면 된다.
    
<br>

### @Autowired 의존관계 자동 주입
- 생성자에 @Autowired 를 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입한다.
- 이때 기본 조회 전략은 타입이 같은 빈을 찾아서 주입한다.
    - getBean(MemberRepository.class) 와 동일하다고 이해하면 된다.

<br>

### 탐색할 패키지의 시작 위치 지정
모든 자바 클래스를 다 컴포넌트 스캔하면 시간이 오래 걸린다. 그래서 꼭 필요한 위치부터 탐색하도록 시작
위치를 지정할 수 있다.
```java
@ComponentScan(
    basePackages = "hello.core",
)

```
- basePackages : 탐색할 패키지의 시작 위치를 지정한다. 이 패키지를 포함해서 하위 패키지를 모두 탐색한다.
    - `basePackages = {"hello.core", "hello.service"}` 이렇게 여러 시작 위치를 지정할 수도 있다.
- basePackageClasses : 지정한 클래스의 패키지를 탐색 시작 위치로 지정한다.
- 만약 지정하지 않으면 `@ComponentScan` 이 붙은 설정 정보 클래스의 패키지가 시작 위치가 된다.

<br>

### 권장하는 방법
- 패키지 위치를 지정하지 않고 설정 정보 클래스의 위치를 프로젝트 최상단에 둔다. 최근 스프링 부트도 이 방법을 기본으로 제공한다.
- 예를 들어서 프로젝트가 다음과 같이 구조가 되어 있으면
```
com.hello
com.hello.serivce
com.hello.repository

```
- com.hello 프로젝트 시작 루트, 여기에 AppConfig 같은 메인 설정 정보를 두고,
@ComponentScan 어노테이션을 붙이고, basePackages 지정은 생략한다.