## Factory Bot


```ruby
gem "factory_bot_rails
```

```ruby
require 'rspec/core'

RSpec.configure do |config|
	...
  config.include FactoryBot::Syntax::Methods
	...
end
```

```ruby
# spec/factories.rb

FactoryBot.define do
  factory :user do
    password { "password" }
    password_confirmation { "password" }

    sequence(:email) { |n| "email#{n}@factory.com" }
  end

  factory :post do
    title { "Test" }
    body { "12345" }
    user { User.first }
    views { 0 }
  end
end
```
위와 같이 정의 후 아래와 같이 사용

`let(:post) { build(:post, title: "", body: "", user: current_user) }`  
`let(:post) { create(:post, title: "", body: "", user: current_user) }`


<br>

## database_cleaner

TODO

```ruby
# spec/rails_helper.rb

RSpec.configure do |config|
	config.before(:suite) { DatabaseCleaner.clean_with(:truncation) }
	config.before(:each) { DatabaseCleaner.strategy = :transaction }
	config.before(:each, js: true) { DatabaseCleaner.strategy = :truncation }
	config.before(:each) { DatabaseCleaner.start }
	config.before(:each) { DatabaseCleaner.clean }
end
```

<br>


## fuubar

test 실행 시 progress bar 기능 지원

```ruby
# .rspec

--require spec_helper
--format Fuubar
--color
```

```ruby
# spec/rails_helper.rb

...
require 'fuubar'
...

RSpec.configure do |config|
	...
	config.fuubar_progress_bar_options = { format: 'Completed Tests <%B> %p%% %a' }
	...
end
```

<br>

## guard, guard-rspec

guard console 을 키면 file system을 listening하여 저장시 자동으로 테스트 진행함.   
model, routing, request 파일 별로 저장한 해당 파일만 테스트를 진행하며 model, controller 등 app 파일 수정시에도 해당 spec에 맞는 테스트 진행.

```ruby
# Gemfile

group :development, :test do
	...
  gem 'guard'
  gem 'guard-rspec'
	...
end
```

`bundle exec guard init`

후

`bundle exec guard`

<br>

### simplecov

테스트 커버리지를 수치화하여 html파일로 generate 해주는 gem

```ruby
# Gemfile

group :test do
	...
  gem 'simplecov', require: false
	...
end
```

```ruby
# spec/spec_helper.rb

require 'simplecov'
SimpleCov.start

...
```

```ruby
# .simplecov

require 'simplecov'

SimpleCov.start do
  add_filter 'spec/rails_helper.rb'
end
```