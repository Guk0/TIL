# Transaction 사용시 주의 사항

## Transaction
  - 함께 수행해야할 작업의 논리적 단위.
  - DB write 연산(create, update, destroy)를 하나의 코드 블럭으로 묶어 연산이 하나라도 실패하면 나머지 연산들은 rollback하여 연산 이전 상태로 돌아가는 기능
  - begin query로 시작하여 commit이나 rollback으로 끝난다.
  - transaction block 안에 write 연산이 성공적으로 수행되면 commit, 실패하면 rollback.
  
  <img src="https://github.com//Guk0/TIL/blob/master/images/transaction1.png?raw=true" alt="drawing" width="600"/>
  
  - on_destroy나 on_save 콜백이 걸려있는 모델의 경우 해당 모델의 write연산이 성공해도 다른 쿼리의 연산이 실패할 경우 해당 객체에 대한 write 연산은 롤백되지만 콜백은 롤백되지 않는다. 외부 api에 요청을 보내는 경우에는 각별히 주의해서 사용할 필요가 있다. ex) S3로 이미지 업로드나 파일 업로드를 구현한 경우
  - transaction 블럭 안의 write 연산이 실행되면 해당 데이터의 write 연산은 수행하지 못하도록 Lock을 건다. 
  - 이 Lock은 실제 운영 환경에서 다양한 문제를 초래할 수 있기 때문에 주의가 필요하다.

    <br>


## isolation level
 read uncommitted, read commit, repeatable reads, serializable

- postgresql에서는 read commit이 defualt.
- active record transaction 메서드의 default isolation level은 db의 default isolation level을 따라감.
  - mysql: repeatable_read.
  - postgresql: read_committed.


<br>

## console sandbox mode
  - sandbox 모드 자체가 하나의 Transaction이고 sandbox 모드에서 write 연산 수행시 transaction과 마찬가지로 RowExclusiveLock이 걸리게 된다.
    - *RowExclusiveLock은 ExclusiveLock 중 하나로 write 연산 시 다른 write 연산은 수행할 수 없도록 Lock을 거는 것을 의미한다.*
  - 이 Lock은 콘솔을 종료하여 rollback될 때까지 풀리지 않는다. 콘솔을 종료할 때까지 Lock이 걸린 테이블에 대한 연산을 실행할 수 없게 된다. 따라서 실서버에서 sandbox 모드를 사용할때는 굉장히 주의해서 사용해야 한다.
    - ex) sandbox 모드 console에서 `User.first.update(name: "123")` 을 실행하면 해당 콘솔이 종료될 때까지 첫번째 user에 대한 write 연산(로그인 시간 및 횟수를 기록하는 경우 로그인, 사용자 수정, 삭제 등)은 대기하게 된다.
    - 따라서 실수로 연산 수행 후 console을 계속 켜놓는 경우 실제 운영하고 있는 서버에서 Lock이 걸린 데이터에 대한 연산을 수행하지 못하게 되어 장애를 초래한다.
  - sandbox mode에서 무조건 lock이 걸리는 것은 아니고 console에서 write 연산을 수행했을 때만 lock이 걸린다.
  - begin만 있고 commit 쿼리가 없고 console을 종료하면 rollback 쿼리를 날린다.

  <img src="https://github.com//Guk0/TIL/blob/master/images/transaction2.png?raw=true" alt="drawing" width="600"/>


<br><br>

[참고1](https://pawelurbanek.com/rails-mistakes-downtime)  
[참고2](https://medium.com/29cm/db-postgresql-lock-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0-57d37ebe057)  
[분산 트랜잭션](https://junhyunny.github.io/msa/design-pattern/distributed-transaction/)