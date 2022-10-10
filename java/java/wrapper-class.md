# Wrapper Class
### Wrapper 클래스란?
- 자바의 자료형은 크게 원시 자료형(primitive type)과 참조 타입(reference type)으로 나뉜다.
- 대표적으로 원시 자료형 타입은 char, int, float, double, boolean 등이 있고 참조 타입은 class, interface 등이 있다.
- 원시 자료형(primitive type)을 객체로 다루기 위해서 사용하는 클래스들을 wrapper class라 하고 자바의 모든 원시자료형(primitive type)에 대응하는 wrapper class가 존재한다.
- 래퍼 클래스로 감싸고 있는 기본 타입 값은 외부에서 변경할 수 없다. String과 같이 새로 생성해야한다.

<br>

### 종류
| 원시자료형 | Wrapper 클래스 |
| --- | --- |
| byte | Byte |
| char | Character |
| int | Integer |
| float | Float |
| double | Double |
| boolean | Boolean |
| long | Long |
| short | Short |

- Wrapper 클래스는 Java.lang 에 포함.
- 모든 Wrapper 클래스의 최종 부모 클래스는 Object이다. 숫자를 다루는 클래스의 부모는 Number 클래스이고 Number 클래스의 부모 클래스가 Object 클래스이다.

<br>

### 박싱과 언박싱

```java
Integer num = new Integer(1); // 박싱
int n = num.intValue(); // 언박싱
```
- 박싱 : 원시 자료형을 wrapper class로 만드는 과정
- 언박싱 :  wrapper class에서 원시 자료형을 얻어내는 과정

<br>

### 자동 박싱, 자동 언박싱
```java
Integer num = 17; // 자동 박싱
int n = num; // 자동 언박싱
```
- 컴파일러가 자동으로 박싱, 언박싱 해준다.
- 자동 박싱 : 원시자료형을 wrapper class 타입의 변수에 대입하는 경우
- 자동 언박싱 : wrapper class 타입의 값을 원시자료형에 대입하는 경우

<br>

### 형변환
- 대부분의 wrapper class는 parseInt, parseFloat, parseBoolean, parseByte과 같이 형변환 메서드를 가지고 있다. 문자열을 받아 원시자료형으로 변환한다.

<br>

### 주의
- wrapper 객체는 내부 값을 비교하기 위해 동등 연산자(==)를 사용할 수 없다.
    - 동등 연산자는 내부의 값을 비교하는 것이 아닌 wrapper 객체의 참조 주소를 비교한다.
    - `equals()` 메서드를 사용해야 한다. 매개변수로 wrapper 객체가 올수도 있고 원시자료형이 와도 된다.
- 원시자료형과 wrapper 객체는 메모리차이가 심하다.
    - int와 Integer의 경우 Integer이 5배정도 더 많이 차지한다.
    - wrapper 객체와 원시자료형 둘 다 사용할 수 있다면 원시자료형을 사용하는 것이 더 낫다.
- null 값을 가질 수 있다.
    - wrapper class는 null 값을 가질 수 있고 원시자료형은 null 값을 가질 수 없다.
- wrapper 객체는 어쨌든 객체이기 때문에 heap 영역에 값을 저장하고 stack에 주소를 저장한다.
    - GC 해야할 대상이 많아진다.
- 가능하면 원시자료형을 사용하고 collections를 사용하는 경우에만 wrapper class를 사용한다.

```java
List<Integer> num1;
List<int> num2;  // 에러
```

<br><br>

참조  
[https://includestdio.tistory.com/1](https://includestdio.tistory.com/1)  
[https://velog.io/@skyepodium/자바-박싱-언박싱은-낯설어서](https://velog.io/@skyepodium/%EC%9E%90%EB%B0%94-%EB%B0%95%EC%8B%B1-%EC%96%B8%EB%B0%95%EC%8B%B1%EC%9D%80-%EB%82%AF%EC%84%A4%EC%96%B4%EC%84%9C)  
[https://coding-factory.tistory.com/547](https://coding-factory.tistory.com/547)
