# Transaction 사용시 주의 사항

## Transaction
  - begin query로 시작하여 commit이나 rollback으로 끝남.
  - transaction block 안에 write 연산이 성공적으로 수행되면 commit, 실패하면 rollback.
  
  <img src="https://github.com//Guk0/TIL/blob/master/images/transaction1.png?raw=true" alt="drawing" width="600"/>
  
  - on_destroy나 on_save 콜백이 걸려있는 모델의 경우 해당 모델의 write연산이 성공해도 다른 쿼리의 연산이 실패할 경우 해당 객체에 대한 write 연산은 롤백되지만 콜백은 롤백되지 않는다. 외부 api에 요청을 보내는 경우에는 각별히 주의해서 사용할 필요가 있다. ex) S3로 이미지 업로드나 파일 업로드를 구현한 경우
    
    <br>
    
## sandbox mode
  - sandbox mode에서 write 시 아래와 같이 lock이 걸리게 됨. sandbox 모드 자체가 하나의 Transaction이고 sandbox 모드에서 write 연산 수행시 transaction과 마찬가지로 RowExclusiveLock이 걸리게 됨. console을 종료할때까지 락이 풀리질 않음. 따라서 실서버에서 sandbox 모드를 사용할때는 굉장히 주의해서 사용해야 함.
      - *RowExclusiveLock은 ExclusiveLock 중 하나로 write 연산 시 다른 write 연산은 수행할 수 없도록 Lock을 거는 것을 의미한다.*

  - 해당 table에만 lock이 걸려 write연산을 수행하지 못한다.
  - sandbox mode에서 무조건 lock이 걸리는 것은 아니고 console에서 write연산을 수행했을 때만 lock이 걸림.
  - begin만 있고 commit 쿼리가 없음.

  <img src="https://github.com//Guk0/TIL/blob/master/images/transaction2.png?raw=true" alt="drawing" width="600"/>


<br><br>

[참고1](https://pawelurbanek.com/rails-mistakes-downtime)  
[참고2](https://medium.com/29cm/db-postgresql-lock-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0-57d37ebe057)  
[분산 트랜잭션](https://junhyunny.github.io/msa/design-pattern/distributed-transaction/)