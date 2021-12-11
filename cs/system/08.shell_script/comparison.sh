#/bin/bash

if [ $1 -gt $2 ]
then
	echo "$1 is higher than $2"   # 문자열안에 $1 기호를 써도 동작한다.
	exit
fi
