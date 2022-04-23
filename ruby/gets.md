## gets vs STDIN.gets
`gets`는 Kernel object에 정의되어있는 메서드로 command line arguments인 ARGV를 먼저 read하고 다음 input을 read 함.

`STDIN.gets`는 ARGV를 확인하지 않고 input을 read 함.

따라서 둘 중 STDIN.gets를 사용하는 것이 성능적으로 유리함.


</br>



## ARGV 활용 예시
https://guides.rubyonrails.org/initialization.html#rails-commands-rb

rails s, rails g, rails d 명령어들은 모두 ARGV로 받아 동작한다.
``` ruby
# in rails source    railties/lib/rails/command.rb

require "rails/command"

aliases = {
  "g"  => "generate",
  "d"  => "destroy",
  "c"  => "console",
  "s"  => "server",
  "db" => "dbconsole",
  "r"  => "runner",
  "t"  => "test"
}

command = ARGV.shift
command = aliases[command] || command

Rails::Command.invoke command, ARGV

```