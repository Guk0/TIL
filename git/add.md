# 특정 파일 혹은 파일 내 특정 부분만 커밋하고 싶을 때

## 특정 파일 

`git add <file1> <fil2>`

<br>

## 특정 부분
hunk 단위로 add가 가능하다. 

`git add -p`

```
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
g - select a hunk to go to
/ - search for a hunk matching the given regex
j - leave this hunk undecided, see next undecided hunk
J - leave this hunk undecided, see next hunk
k - leave this hunk undecided, see previous undecided hunk
K - leave this hunk undecided, see previous hunk
s - split the current hunk into smaller hunks
e - manually edit the current hunk
? - print help
```
### 자주 사용하는 키워드
- y, n, q, s, e
  - y, n 는 해당 hunk를 stage 할지 안할지 결정
  - q는 종료. 종료하기 이전에 y만 반영
  - s는 hunk를 split. 떨어져 있는 수정사항만 split 가능. 이어져있는 5줄의 수정사항은 split 불가능.
  - e는 hunk 수정

### hunk edit 후 Your edited hunk does not apply 에러 발생시
  - hunk는 '+', '-', ''(blank)로 구성
    - '+' 사인은 추가될 라인
    - '-' 사인은 삭제될 라인
    - '' 사인은 참고용
  - hunk edit에서 아래와 같은 사항을 위반할 경우 not apply 에러 발생
    - '+' 사인이 있는 라인에 새 수정사항을 추가한 경우(공백 포함). 
      - 추가될 라인('+' 사인)을 제거한 후 새로운 줄을 추가해서는 안된다. 
    - '-' 사인이 있는 라인을 지운 경우
      - 제거될 라인('-')을 변경하려면 해당 라인을 지우면 안되고 '-' 사인만 지워야 한다.



### References
[참고1](https://velog.io/@swhan9404/Git-에서-특정파일-임시로-commit-에서-제외시키기)  
[참고2](https://salferrarello.com/your-edited-hunk-does-not-apply/)