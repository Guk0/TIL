# IO

### Stream이란?

- 한 곳에서 다른 곳으로의 데이터 흐름
    - 파일 데이터, HTTP 응답 데이터, 키보드 입력
- 단방향. 입력과 출력이 동시에 발생할 수 없다.
    - 입력스트림(InputStream), 출력스트림(OutputStream)으로 나뉨.

<br>

### System.in.read()

- System.in은 InputStream 타입의 필드임.
    - `InputStream is = System.in;`
- InputStream의 read() 메서드는 입력받은 데이터를 int형으로 저장함.
    - 운영체제의 인코딩 형식(UTF-8)의 10진수로 변수에 저장됨.
- 1byte 씩 읽는다.
    - 일반적인 ascii 코드에 해당하는 문자열은 잘 읽음.
    - 한글은 3byte 혹은 2byte에 해당하므로 제대로 읽어오지 못한다.

<br>

### InputStreamReader

- InputStream의 read() 메서드가 1byte만 읽는 것을 보완하기 위한 클래스.

```java
import java.io.InputStream;
import java.io.InputStreamReader;

...

InputStream inputstream = System.in;
InputStreamReader sr = new InputStreamReader(inputstream);
```

<br>

### Scanner
- 버퍼보다 속도가 느리다.
    - 데이터를 입력 받을 경우 즉시 사용자에게 전송. 매번 전송하기 때문에 많은 양의 데이터를 입력 받는 경우 버퍼보다 느림.
    - 내부적으로 입력 데이터를 처리할 때 정규식 사용.
- 입력받을 때  `nextInt`, `nextDouble`과 같이 데이터형을 지정하여 입력받을 수 있음.
- 예외 처리를 하지 않아도 된다.
- 동기화 처리를 따로 해줘야한다.

```java
import java.util.Scanner;

String string1;
int age;
double height;

Scanner sc = new Scanner(System.in);

hihi = sc.next();  // 한 단어
hihi = sc.nextLine();  // 한 줄

age = sc.nextInt(); // int
height = sc.nextDouble(); // double
```

<br>

### BufferedReader
- 버퍼라는 저장 공간에 하나씩 채우다가 버퍼가 가득 차거나 개행 문자를 만날 경우 버퍼의 내용을 사용자에게 전송.
- 입력을 한 줄 단위로 받고 모든 입력 데이터를 String으로 인식. 추가적인 형변환이 필요하다.
- try-catch 혹은 throws로 직접 예외 처리를 해줘야한다.
- 내부적으로 동기화를 지원해준다. 멀티스레딩 환경에서 유용


``` java
import java.io.BufferedReader;
import java.io.InputStreamReader;

... 

public static void main(String args[] ) throws Exception {
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  String s = br.readLine();
  br.close();

  int intNum = Integer.parseInt(s);
  long longNum = Long.parseLong(s);
}

...

```

<br>

[참고](https://sorjfkrh5078.tistory.com/93)