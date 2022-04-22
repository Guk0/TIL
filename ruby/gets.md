## gets.chomp() vs STDIN.gets.chomp()
`gets.chomp()`는 main 함수에 인자인 ARGV를 먼저 read하고 다음 input을 read 함.
`STDIN.gets.chomp()`는 ARGV를 확인하지 않고 input을 read 함.

따라서 둘 중 STDIN.gets.chomp()를 사용하는 것이 성능적으로 유리함.
