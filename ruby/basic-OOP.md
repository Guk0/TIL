## OOP 기초

- 모든 객체(클래스 인스턴스)는 고유한 객체 아이디(object identifier(ID))를 가진다. 
- 클래스의 메서드는 객체에 메시지를 보내 호출할 수 있다. 메시지에는 메서드 이름과 메서드에 필요한 매개 변수들이 포함된다. 객체가 메시지를 받으면, 자신의 클래스에서 해당 메서드를 찾는다.
- class 의 method 안에서 다른 메서드 사용시에는 self 나 class 명을 붙이지 않고 바로 사용 가능하다.
- gets나 puts 같이 Kernel에 정의된 메서드를 Kernel을 명시하지 안하도 호출할 수 있는 것이 바로 위 설명의 연장선이다. 

<br>

## 진정한 객체제향 언어 루비.
- 자바에서는 abs 메서드를 사용하기 위해 다음과 같이 abs 메서드의 매개변수로 num을 넘겨준다.
`num = Math.abs(num)`
- 루비에서는 num 자체를 객체로 보아 해당 객체의 method인 abs를 호출한다.
- 다른 언어에서 nil(null)은 `아무 객체도 아님`을 의미 하지만 루비에서는 nil은 `‘아무것도 아님'을 표현하는 하나의 객체`이다.

<br>

## 객체 초기화(initializing) 과정
새로운 객체를 만들기 위해 Book.new를 호출하면 루비는 초기화되지 않은 객체를 메모리에 할당하고 new의 매개변수를 이용해 그 객체의 initialize 메서드를 호출하여 객체를 초기화한다.


puts vs p   && to_s

```ruby
class Book
	def initialize(name)
		@name = name
	end
end

b1 = Book.new("hihi")

p b1      # #<Book:0x00007fa3d8aba850 @name="hihi">
puts b1    # #<Book:0x00007fa3d8aba850>

```

puts은 단순히 프로그램의 표준 출력에 문자열을 출력할 뿐이다. 가장 간단한 방법인 to_s를 붙여 출력한다. 따라서 클래스 내부에 to_s 메서드를 재정의한다면 아래와 같은 출력 포맷을 만들 수 있다.

```ruby
class Book
	def initialize(name)
		@name = name
	end

	def to_s
		"name: #{@name}"
	end
end

b1 = Book.new("hihi")

p b1      # #<Book:0x00007fa3d8aba850 @name="hihi">
puts b1    # name: hihi
```

<br>

## 객체의 attribute
- 객체의 내부 상태는 각 객체 내부에 저장된 정보로 다른 객체에서는 이 정보에 접근할 수 없다. 이는 객체의 일관성을 지키기 위한 책임이 하나의 객체에 전적으로 맡겨진다는 것을 의미한다.
- 하지만 일반적으로 객체 외부에서 객체 상태에 접근하거나 조작하는 메서드를 별도로 정의하여 외부에서도 객체 상태에 접근 가능하도록 만들어 준다.
- 이렇듯 객체의 내부가 외부에 노출되는 부분을 객체의 속성(attribute)라고 부른다.
- 루비에서는 접근자 메서드(getter)를 attr_reader를 통해 쉽게 제공한다. 다만 오해하면 안될 것이 인스턴스 변수와 접근자 메서드는 완전 다른 것이다. 접근자 메서드를 정의하였더라도 인스턴스 변수는 따로 정의해줘야 한다.

<br>

## getter
```ruby
....
def price
	@price
end
...

book.price # 100000
```
- getter를 정의하지 않는다면 *NoMethodError (undefined method `price' for #<Book...>)* 에러 발생
- `instance_variable_get("@#{name}")` 메서드를 사용할 수도 있다. `book.instance_variable_get("@price")`


## setter

```ruby
....
def price=(new_price)
	@price = new_price
end
...

book.price = book.price * 0.75
```
- 다음과 같이 setter를 정의할 수 있다.
- 또 다른 방법으로는 attr_writer 대입 메서드를 사용한다.
- attr_reader와 attr_writer를 동시에 정의하는 attr_accessor를 제공한다.
- setter를 정의하지 않는다면 *# NoMethodError (undefined method `price=' for #<Book....>) 에러 발생*

<br>

## 가상속성

```ruby
...
def price_in_cents=(cents)
	@price = cents / 100.0
end
...

book.price_in_cents = 100
```
- 밖에서 보면 price_in_cents라는 인스턴스 변수가 있는 것 처럼 보인다. 하지만 메서드 내부를 보면 단지 price 인스턴스 변수를 set하는 코드이다. 
- 가상 속성 값을 통해 인스턴스 변수에 매핑하기도 한다.
- 단일접근원칙이라고도 한다. 우리가 만든 수백줄만줄의 코드에 영향을 주지 않으면서 내부 구현을 바꿀 수 있다.

<br>

## Attribute 심화
- attribute는 단순히 메서드일 뿐이다. 인스턴스 변수의 값을 반환하고 객체의 상태를 바꾸는 용도로 사용한다.
- attribute을 일반 메서드와 구분 짓는 차이는? 그런건 없다. 그냥 취향이다.
- **내부 상태는 인스턴스 변수에 저장하고 외부에 보이는 상태는 attribute라고 부르는 메서드를 통해서만 해야한다. 여기서 formatting이라든지 하는 부분이 달라질 수 있다.**
- initialize 메서드는 객체의 환경을 초기화하여 이를 사용 가능한 상태로 만들어 두어야 한다. 다른 메서드에서는 이 상태를 사용한다.

<br>

## 접근제어
- 클래스를 외부에 어디까지 노출할 지를 결정하는 것이 클래스 인터페이스를 설계할 때 중요하다. 너무 깊이 접근하도록 허용하면 각 요소간 결합도(coupling)이 높아질 우려가 있다. 이는 유지보수를 힘들게 한다.
- coupling과 decoupling

- public  
- protected   
  - 해당 메서드는 그 객체를 정의한 클래스와 하위 클래스에서만 호출할 수 있다.  
- private  
  - 수신자를 지정하여 호출할 수 없다. 이 메서드의 수신자는 오로지 self이다. 다른 객체는 private 메서드에 접근할 수 없다.

- 루비의 protected와 private은 다른 언어와 좀 다르다.
- 루비에서는 접근제어가 동적으로, 프로그램이 실행될때 결정되지만 다른 객체지향 언어는 그렇지 않다. 접근 제한된 메서드를 실제로 호출한 그 순간에만 exception이 발생하게 된다.
- 보통 클래스 내부에서 세가지 접근 제어 함수 아래의 메서드들이 해당 접근 제한 단계로 결정된다.

```ruby
private
def hihi
	puts "123"
end
```

또는 접근제어 함수 뒤 인자로 메서드 이름을 쓰는 방법도 있다.

```ruby
private :hihi, :hihi2
public :byebye
protected :hi

def hihi
	puts "123"
end
```