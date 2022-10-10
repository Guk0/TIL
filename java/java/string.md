# String
## String, String buffer, String builder
- (String 불변, StringBuffer, StringBuilder 가변)
- String은 불변하다는 특징을 가지고 있어서 수정을 하게되면 새로운 String 인스턴스가 생성되고 전에 있던 String은 GC에 의해 사라지게 된다.
- StringBuffer는 동기화 키워드를 지원하여 멀티쓰레드 환경에서 안전하다(thread-safe)
  - String도 불변성을 가지기 때문에 마찬가지로 멀티쓰레드 환경에서의 안정성(thread-safe)을 가지고 있다.
- 반대로 StringBuilder는 동기화를 지원하지 않기 때문에 멀티쓰레드 환경에서 사용하는 것은 적합하지 않지만 동기화를 고려하지 않는 만큼 단일쓰레드에서의 성능은 StringBuffer 보다 뛰어나다.

<br>

[참고](https://wookcode.tistory.com/99)

<br>

## StringTokenizer
``` java
import java.util.StringTokenizer;

...
String str = "1 2 3 4 5"
StringTokenizer st = new StringTokenizer(str, " ");

int a = Integer.parseInt(st.nextToken()); // 1
int b = Integer.parseInt(st.nextToken()); // 2
st.countTokens() // 3
st.hasMoreTokens() // true
```

### Class
- StringTokenizer는 필드로 currentPosition, maxPosition를 가지고 있고 `nextToken` 메서드 사용시 currentPosition를 +1 한다.
- `countTokens`나 `hasMoreTokens` 메서드 사용시 현재 포인터를 기준으로 남아있는 토큰을 판단한다.

### methods
- `Object nextElement(), String nextToken()`
  - 다음의 토큰을 반환. nextElement는 Object를, nextToken은 String을 반환한다.  
- `int countTokens()`
  -  남아있는 token의 개수를 반환. 현재 남아있는 token 개수.
- `boolean hasMoreElements(), boolean hasMoreTokens()`
  - 토큰이 남아있는지 판단.





<br>

[참고](https://reakwon.tistory.com/90)