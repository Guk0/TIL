## 커버링 인덱스 란?
- 즉, 실제 데이터의 접근이 없이 인덱스의 컬럼만으로 쿼리를 완성하는 것
- 원래는 select 문 안의 칼럼들을 가져오기 위해 index table 서치 후에 디스크 탐색(db)을 실행해야함. 커버링 인덱스를 이용하면 디스크 탐색 시간을 없앨 수 있어 쿼리 성능이 비약적으로 빨라짐.


[참고1](https://icarus8050.tistory.com/44)   
[참고2](https://jojoldu.tistory.com/476)