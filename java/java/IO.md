# Scanner vs BufferedReader
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