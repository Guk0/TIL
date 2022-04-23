## strip
|character|symbol|
|-----|----|
|null|\x00|  
|horizontal tab|\t|    
|vertical tab|\v|  
|new line|	\n  |
|form feed	|\f  |
|carriage return |	\r  |
|space |	" "  |

문자열 시작과 끝의 whitespace(위 표) 제거하여 return

``` ruby
"\n hihi \n\r\f\t".strip
> "hihi"

"\n hi hi \n\r\f\t".strip
> "hi hi"

"\n hi\nhi \n\r\f\t".strip
> "hi\nhi"

```

## chop
문자열의 마지막 character 제거 후 return. `\r\n`이 문자열의 마지막인 경우 \r\n 둘 다 제거

``` ruby
"hello".chop
> "hell"

"hello\n".chop
> "hello"

"hello\r\n".chop
> "hello"
```


## chomp
문자열의 마지막 `\r\n, \r, \n` 제거 후 return
arg가 있는 경우 마지막에 해당 arg가 있는 경우 해당 charactor 제거

``` ruby
"hello\n".chomp
> "hello"

"hello\r\n".chomp
> "hello"

"hello ".chomp(' ')
> "hello"

"hello e".chomp('e')
> "hello "

"hello".chomp('lo')
> "hel"
```





