# intelliJ 단축키

### *command + n*
- directory에서 패키지 혹은 클래스 만들때 사용.
- 클래서 내에서 constructure나 getter, setter 만들 때 사용.
    - 옵션 중 메서드 오버라이딩을 통해 toString 같은 메서드도 오버라이딩 가능

<br>

### *option + enter*
- 인터페이스 구현시 사용. 
  - `public class MemoryMemberRepository implements MemberRepository` 와 같이 implements를 작성하고 `MemberRepository` 에 option + enter를 누르면 메서드 자동 구현.
- import되지 않은 class를 import 할 때 사용.
- static import
    - `Assertions.assertThat()` 에 Assertions에 위 단축키 입력시 static import가 됨.
    - 클래스의 static method를 보다 편하게 import하여 사용할 수 있게 해줌.
    - 정적 메서드 뿐만 아니라 정적 멤버 변수도 static import 의 대상이 됨.
    - 클래스 내의 동일한 메서드가 존재할 경우 해당 메서드의 우선순위가 더 높음.
    
<br>

### *command + shift + t*
- 클래스(서비스, 폴리시)에서 위 단축키를 입력하면 자동으로 테스트를 만들어줌. JUnit5, 이름 디폴트로 놓고 생성.

<br>

### *control + shift + r*
- 소스코드 실행.
- 메서드 내에서 입력하면 해당 메서드만 실행(JUnit)
- 클래스 선언부 내에 커서를 두고 입력하면 해당 클래스 전체 실행. 파일에 놓아도 마찬가지.
- 패키지에 놓으면 해당 패키지 전체 실행.

<br>

### *command + e + enter*
- 바로 이전 파일로 돌아감.
- `command + e` 는 파일 히스토리. 맨 처음 파일이 바로 이전 파일

<br>

### *command + option + m*

```java
public MemberService memberService() {
    return new MemberServiceImpl(new MemberRepository());
}
```
- `new MemberRepository()` 에 블록을 잡은 후 위 커맨드를 입력하면 아래와 같이 변경 가능

```java
public MemberService memberService() {
    return new MemberServiceImpl(memberRepository());
}

private MemberRepository memberRepository() {
    return new MemoryMemberRepository();
}
```

<br>

### *command + d*
- 코드를 블록잡고 위 커맨드를 입력하면 아래에 동일한 코드가 복사됨.