# getter, setter

### getter, setter
```ruby
class Food
  def protein # getter
    @protein
  end

  def protein=(value) # setter
    @protein = value
  end
end
```
instance_variable을 get  
instance_variable을 set  

<br>

### attr_accessor, attr_reader ,attr_writer
attr_reader : 위 코드에서 getter를 생성한다.
attr_writer : 위 코드에서 setter를 생성한다.
attr_accessor : getter와 setter 둘 다 생성한다.

<br>

### Get Instance Variable

```ruby
class Node
  def initialize(key, data=nil)
    @key = key
    @data = data
    @children = {}
  end
end

node = Node.new("hihi")
node.key   # NoMethodError (undefined method `key' for #<Node:0x00007fe36bac0160 @key="hihi", @data=nil, @children={}>)
```

위와 같이 instance_variable에 접근시 NoMethodError 발생.

instance_variable에 접근하려면 반드시 `attr_reader :key, :data, :children` 를 사용하든지 아래와 같이 `instance_variable_get("@#{name}")` 을 사용.
- `some_object.instance_variable_get("@#{name}")`

<br>

### Set Instance Variable

```ruby
class Node
  def initialize(key, data=nil)
    @key = key
    @data = data
    @children = {}
  end
end

node = Node.new("hihi")
node.children = {hihi: 444} # NoMethodError (undefined method `children=' for #<Node:0x00007fdb012db278 @key="hihi", @data=nil, @children={}>)
```
