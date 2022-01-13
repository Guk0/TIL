# Basic

## describe / it / expect
```ruby
  RSpec.describe  "설명" do
    it '더하기' do
      expect(1 + 1).to eq 2
    end
    it '빼기' do
      expect(2 - 1).to eq 1
    end
  end
```
- describe
    - 테스트 그룹화 선언.
- it
    - 하나의 테스트 케이스
    - example라는 단위로 정리 역할.
    - 기대값(2)과 실제값(1+1)이 eq(matcher)을 만족하여 모두 통과하면 example는 통과한 것으로 간주.
- expect(1+1).to eq 2
    - 1+1이 2가 되는 것을 기대하는 테스트
- RSpec 2.10 이전 버전에서는 should로 expectaion을 했다.    
    ```ruby
    (1 + 2).should eq 3
    (1 + 2).shourl == 3
    ```
    
    - should는 메타 프로그래밍을 사용하고 있어 드물게 불일치가 발생하였다. 그래서 expect가 사용되어 진다.
- describe 중 복수의 example(it ... do ... end)를 사용할 수 있다.


<br/>  

## 복수 개의 example
```ruby
	it '사칙연산' do
		expect(10 - 3).to eq 7
		expect(5 - 1).to not_eq 1
		expect(3 - 1).to eq 2
		expect(2 - 1).to eq 1
	end
```
- 1개의 example(it)에서 여러개의 expectation을 사용할 수 있다.
- 다만 테스트가 실패하였을 때 어느 expectation이 통과하였는지 알 수 없다.
- 1개의 example에는 1개의 expectation을 사용하는 것이 원칙이다.

<br/>  

## nested describe
```ruby
RSpec.describe  "설명" do
	describe '더하기' do
		it '덧셈이 2와 동일한지?' do
			expect(1 + 1).to eq 2
		end
	end
	
	describe '빼기' do
		it '뺄셈이 1과 동일한지?' do
			expect(2 - 1).to eq 1
		end
	end
end
```
- 가장  상위의 describe외의 다른 describe에서는 RSpec. 생략 가능

<br/>  

## before
before은 describe나 context 에서 사용 가능하다. 

```ruby
RSpec.describe  "설명" do
	describe '더하기' do
		before do
			# do something			
		end

		context "context1" do
			before do
				# do something			
			end

			it '덧셈이 2와 동일한지?' do
				expect(1 + 1).to eq 2
			end
		end

		context "context2" do
			it '덧셈이 2와 동일한지?' do
				expect(1 + 1).to eq 2
			end
		end

	end
end
```

<br/>  

## let
```ruby
before do 
	@params = { name: 123 }
end
```
- 위와 같이 before do block에 인스턴스 변수로 선언하여 describe와 context 내에서 사용이 가능하지만 let을 선언하여 인스턴스 변수처럼 사용하는 것이 가능하다.

```ruby
let(:params) {{name: 123}}
```
- 블럭으로도 사용 가능하다

```ruby
let(:params) do
  hash = {}
  hash[:name] = 123
  hash
end
```

<br/>  

## change by
```ruby
  expect { delete post_url(mock_post) }.to change(Post, :count).by(-1)
```
- expect 블럭과 change 함수 두 개로 나눠 생각하면 됨. 
- expect 블럭과 change 함수의 인자 Post.count가 몇개가 차이 날지를 테스트하는 함수. by(-1)이므로 expect block(0개) - Post.count(1개) = -1
  
<br/>  
    
## let vs before
- let : let 블럭안에 있는 식을 호출되는 시점에 실행한다. 정의된 코드 순서는 상관없다.
- before : example이 실행되기 전에 실행된다.

<br/>  

## subject

```ruby
it 'has a title' do
  post.title = ""
  post.body = "a valid body"
  # this test will be fail
  expect(post).to_not be_valid
  post.title = "Has a title"
  expect(post).to be_valid
end

it 'has a body' do
  post.title = "a valid title"
  post.body = ""

  expect(post).to_not be_valid
  post.body = "Has a body"
  expect(post).to be_valid
end
```
expect 메서드에 들어가는 인자가 동일할때 subject로 뺄 수 있음.

```ruby
subject { post }

it 'has a title' do
  post.title = ""
  post.body = "a valid body"
  # this test will be fail
  is_expected.to_not be_valid
  post.title = "Has a title"
  is_expected.to be_valid
end

it 'has a body' do
  post.title = "a valid title"
  post.body = ""

  is_expected.to_not be_valid
  post.body = "Has a body"
  is_expected.to be_valid
end
```

<br/>  

## example, specify
it의 ailas. 자연스러운 영문화를 위해 사용한다.

```ruby
it 'has a body' do
  post.body = "Has a body"
  is_expected.to be_valid
end

specify 'has a body' do
  post.body = "Has a body"
  is_expected.to be_valid
end

example 'has a body' do
  post.body = "Has a body"
  is_expected.to be_valid
end
```


<br/>  

## shared_examples  / it_behaves_like
- example block을 shared_examples로 정의하여 여러 곳에서 사용 가능.

```ruby
...
	let(:post) { Post.new(title: "", body: "", user: current_user, views: 0) }
  subject { post }

  shared_examples 'be_valid' do
    it { is_expected.to be_valid }
  end

	context '0살의 경우' do
		it_behaves_like 'be_valid'
  end
...

```
<br/>  

## let!
```ruby
let(:post) { Post.create(title: 'rspec', content: 'test') }
```

let으로 사용할 경우 아래 it 블럭에서 test가 fail 한다. let(:post)가 호출되기 전 Post.first를 찍었기 때문. before 구문으로 let(:post)를 미리 호출할 수도 있지만 let!을 사용하면 쉽게 해결 가능하다. example이 실행되기 전에 let을 호출한다.

```ruby
RSpec.describe Post do
  let!(:post) { Post.create(title: 'rspec', content: 'test') }
  
  it 'eq to first post' do
    expect(Post.first).to eq post
  end
end
```

<br/>  

## pending

```ruby
pending "add some examples to (or delete) #{__FILE__}"
```
- 보류. 실행을 중단하는 것이 아니라 실행을 그대로 이어 나감.

<br/>  

## skip
- 보류와는 반대로 skip아래부터 실행을 중단함.

<br/>  

## xit
```ruby
RSpec.describe Post do
  let!(:post) { Post.create(title: 'rspec', content: 'test') }
  
  xit 'eq to first post' do
    expect(Post.first).to eq post
  end
end
```
- example 전체를 skip

<br/>  

## xdescribe / xcontext

```ruby
xdescribe 'post' do
  it 'eq to first post' do
    expect(Post.first).to eq post
  end
  it 'not eq to first post' do
    expect(Post.first).not_to eq post
  end
end

xcontext 'post' do
  it 'eq to first post' do
    expect(Post.first).to eq post
  end
  it 'not eq to first post' do
    expect(Post.first).not_to eq post
  end
end

```
- describe 혹은 context 전체를 스킵

<br/>  

## it

```ruby
RSpec.describe Post do
  let!(:post) { Post.create(title: 'rspec', content: 'test') }
  
  it 'pending....'
end
```
- do end 블럭 없이 it을 사용시 pending의 역할을 함.