# Transaction

## Isolation level
동시성과 데이터 무결성은 같이 갈 수 없고 적당히 조정이 필요함.   
동시성을 높이면 데이터 무결성은 떨어지고 데이터 무결성을 높이면 동시성은 낮아짐.

<br>

### Read Uncommitted
  - 커밋되지 않은 데이터 read 허용
  - 트랜잭션에서 write 쿼리로 데이터를 수정한 후 commit하지 않았는데도 다른 트랜잭션에서 해당 데이터를 읽을 때 수정된 데이터로 read.
  - DB의 일관성을 유지하는 것이 불가능.
  - 데이터 정합성에 문제가 생김
  - Dirty Read 문제.
      - 트랜잭션이 완료되지 않았는데도 수정된 데이터를 볼 수 있다.
      - 수정된 데이터로 로직 처리 중에 데이터 롤백 시 문제가 발생.

<br>

### Read Committed
  - 커밋된 데이터만 read 허용
  - 트랜잭션에서 write 쿼리로 수정한 후 commit하여야 다른 트랜잭션에서 수정 후 데이터를 read할 수 있음.
  - 수정 후 커밋 전까지 해당 데이터에 shared lock이 걸리게 되어 다른 트랜잭션에서 해당 데이터를 write 할 수 없음.
  - 동일 데이터에 write 연산 시 순차적으로 처리.
  - Non-repeatable read 문제
      - 트랜잭션 A에서 데이터를 read.
      - 트랜잭션 B에서 해당 데이터를 write
      - 트랜잭션 A에서 다시 해당 데이터를 read하면 변경된 데이터 조회.
      - 트랜잭션 A 내에서 read한 데이터가 변화. 데이터 일관성 문제.

<br>

### Repeatable Read
  - 수정 후 커밋 전까지 해당 데이터에 shared lock이 걸리게 되어 다른 트랜잭션에서 해당 데이터를 write 할 수 없음.
  - 트랜잭션 내에서 read를 여러번 할 때 다른 트랜잭션에서 데이터가 update되어도 undo 영역에서 데이터를 read하여 데이터 일관성 문제 해결.
      - 자신의 트랜잭션 번호보다 낮은 트랜잭션 번호에서 변경된 데이터만 보게 됨.
      - undo 영역에 백업된 레코드는 변경을 발생시킨 트랜잭션 번호를 포함.
  - phantom read 문제.
      - update, destroy한 데이터는 undo 영역에서 가져오지만 새로 create된 데이터는 제대로 가져올 수 있음.
      - 따라서 트랜잭션 내에서 새로운 데이터가 조회되는 문제 발생.


  <img src="https://github.com//Guk0/TIL/blob/master/images/transactionDB.png?raw=true" alt="drawing" width="600"/>

<br>

### Serializable
  - phantom read 문제 해결
  - 트랜잭션들이 동시에 일어나지 않고 순차적으로 실행되는 것처럼 동작.
  - 성능 저하 이슈 존재





[참고1](https://brownbears.tistory.com/272)  
[참고2](https://dar0m.tistory.com/225)
