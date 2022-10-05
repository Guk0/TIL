# String, String buffer, String builder
- (String 불변, StringBuffer, StringBuilder 가변)
- String은 불변하다는 특징을 가지고 있어서 수정을 하게되면 새로운 String 인스턴스가 생성되고 전에 있던 String은 GC에 의해 사라지게 된다.
- StringBuffer는 동기화 키워드를 지원하여 멀티쓰레드 환경에서 안전하다(thread-safe)
  - String도 불변성을 가지기 때문에 마찬가지로 멀티쓰레드 환경에서의 안정성(thread-safe)을 가지고 있다.
- 반대로 StringBuilder는 동기화를 지원하지 않기 때문에 멀티쓰레드 환경에서 사용하는 것은 적합하지 않지만 동기화를 고려하지 않는 만큼 단일쓰레드에서의 성능은 StringBuffer 보다 뛰어나다.

<br>


[참고](https://wookcode.tistory.com/99)