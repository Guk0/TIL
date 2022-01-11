# set current_user

## request_spec
> request spec에서 current_user 정의하기.  

request spec은 rack, controller, routing, view 등을 종합적으로 테스트하기 위한 spec으로  Devise의 sign_in 메서드를 사용한다.

```ruby
# rails_helper.rb
...
config.include Devise::Test::IntegrationHelpers, type: :request
...

# requests/post_specs.rb
let(:current_user) { FactoryGirl.create(:user) }

before do
  sign_in current_user
end
```


[참고1](https://dev.to/kevinluo201/introduce-rspec-request-spec-4pbl)