# conditional check

루비에서는 `0, "", [], {}`은  조건절에서 false로 보지 않는다. 오로지 `nil`만 false로 본다. 

따라서 조건절에 `0, "", [], {}` 사용시에는 .zero?, .empty?, .length?를 사용해야 한다.

```ruby
0.zero? # true
"".empty? # true
[].empty? # true
{}.empty? # true

if 0
	puts 1
end
# expect to print nothing. but it print 1
```