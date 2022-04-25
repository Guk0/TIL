# Object

### Basic Object instance methods
- :equal?
- :!
- :==
- :instance_exec
- :!=
- :instance_eval
- :`__id__`, :`__send__`

### Object instance methods
BasciObject를 상속 받는다. 
<i>Object.instance_methods 로 instance_methods 확인 가능</i>


- :instance_of?
- :kind_of?
- :is_a?
- :nil?
- :to_s
- :send
- :eql?
- :respond_to?
- :dup
- :clone
- :equal?
- :!
- :==
- :!=

위 메서드들은 자료형 인스턴스(String, Array, Numeric, Hash 등)에 관계없이 사용할 수 있음. `자료형 클래스는 모두 Object 클래스를 상속 받기 때문.`

<br>

Object 클래스는 모든 자료형의 parent class이며 사용자가 별다른 상속없이 정의하는 모든 클래스의 parent이다.

<br>

상수 혹은 메서드를 top level programming scope에 정의 시 해당 상수, 메서드는 Object의 상수, 메서드로 정의된다.

<br>

Object를 상속 받는 자료형
- String, Array, Numeric, Hash, NilClass, FalseClass, TrueClass