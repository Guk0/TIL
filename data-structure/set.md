## set

### 특징
- 데이터를 비순차적(unordered)으로 저장할 수 있는 순열  자료구조(collection)
- 삽입 순서대로 저장되지 않고 특정한 순서를 기대할 수 없는 자료구조
- 수정가능(mutable)
- 동일한 값 여러 번 삽입 불가(동일 값을 여러번 넣을 경우 하나의 값만 저장). 중복 값 x
- Fast Lookup(특정 값을 포함하고 있는지 확인)이 필요할 때 주로 사용

### 구조
- 저장 순서
  - 저장할 데이터의 hash 값 구하기
  - 해시값에 해당하는 공간(bucket)에 값 저장
- 저장하고자하는 값의 해시값에 해당하는 bucket에 값을 저장하기 때문에 순서가 없음(index도 없다)
- 해시값 기반의 bucket에 저장하여 중복된 값을 저장할 수 없음
- 해시값 기반으로 저장하여 lookup이 빠름
  - Set의 총 길이와 상관없이 단순히 해시값 계산 후 해당 bucket을 확인하면 됨.

<br>

참고  
[https://kim-mj.tistory.com/255](https://kim-mj.tistory.com/255)  
[https://velog.io/@taeha7b/datastructure-set](https://velog.io/@taeha7b/datastructure-set)