#!/bin/bash

if [ -z $1 ]||[ -z $2 ]; then
	echo usage: $0 sourcedir targetdir  # $1과 $2이 없다면 사용법을 보여 주고 끝냄.
else
	SRCDIR=$1
	DSTDIR=$2
	BACKUPFILE=backup.$(date +%y%m%d%H%M%S).tar.gz
	if [ -d $DSTDIR ]; then # $DSTDIR이 있다면 해당 경러에 압축파일을 넣고
		tar -cvzf $DSTDIR/$BACKUPFILE $SRCDIR
	else # $DSTDIR이 없다면 디렉토리 생성 후 넣는다.
		mkdir $DSTDIR
		tar -cvzf $DSTDIR/$BACKUPFILE $SRCDIR
	fi
fi
	
