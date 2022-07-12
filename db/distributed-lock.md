# 분산락

## 요약
- 분산된 서버에서 동일한 자원을 접근할때 락을 걸기 위해 사용(ex. 재고 수량 등)
- redis를 이용하여 구현하고(single-thread 라는 특징. or 다양한 자료구조 지원) 락의 획득과 해지 기능을 레디스로 구현한다.
- 락을 획득하는 방식은 스핀락(루프를 돌며 공유자원에 접근 가능한지 체크)을 사용할 수도 있고 redis pub/sub을 이용하여 구현할 수도 있다.

<br>

## 분산락이란?
- 서버가 여러 대인 상황에서 동일한 데이터에 대한 동기화를 보장하기 위해 사용
- 서버들 간에 동기화된 처리가 필요하고, 여러 서버에 공통된 락을 적용해야 하기 때문에 redis 를 이용하여 분산락을 이용한다.
- redis를 이용하여 자원이 사용중인지 확인하기 때문에 전체 서버에 동기화된 처리가 가능 하다.

- 분산락의 구현 방법 중 하나가 스핀락.
  - 스핀락 : 루프를 돌면서 공유자원에 접근 가능한지 체크.

<br>

## redlock.rb 동작
[https://github.com/leandromoreira/redlock-rb/blob/5e8aece723e516f39a91b52a0282d890b4b01473/lib/redlock/client.rb#L226-L239](https://github.com/leandromoreira/redlock-rb/blob/5e8aece723e516f39a91b52a0282d890b4b01473/lib/redlock/client.rb#L226-L239)

```ruby
def try_lock_instances(resource, ttl, options)
    retry_count = options[:retry_count] || @retry_count
    tries = options[:extend] ? 1 : (retry_count + 1)

    tries.times do |attempt_number|
      # Wait a random delay before retrying.
      sleep(attempt_retry_delay(attempt_number, options)) if attempt_number > 0

      lock_info = lock_instances(resource, ttl, options)
      return lock_info if lock_info
    end

    false
  end
```

- 다른 락이 점유하고 있으면 지정된 횟수만큼 sleep하여 대기한다.
- 스핀락으로 구현.

<br>

## redisson(java 진영) 에서의 동작
- 스핀락을 사용하지 않고 redis의 pub/sub 활용함. 락 해제 시 대기 중인 프로세스에 메시지를 보내(pub/sub) 락이 풀렸음을 전달. 
- waitTime,  leaseTime 두개의 매개변수로 락을 대기하는 시간(이미 락이 있을때)과 락을 풀어주는 제한 시간(락을 소유하고 있을 때)을 설정할 수 있다.

<br>

## mysql의 named lock 사용

<br>

## 참고
- [https://soyeon207.github.io/db/2021/08/29/distributed-lock.html](https://soyeon207.github.io/db/2021/08/29/distributed-lock.html)
- [https://happyer16.tistory.com/entry/레디스와-분산락](https://happyer16.tistory.com/entry/%EB%A0%88%EB%94%94%EC%8A%A4%EC%99%80-%EB%B6%84%EC%82%B0%EB%9D%BD)
- [https://www.korecmblog.com/redis-dlm/단일 인스턴스로 구성된 레디스에서의 분산 락 구현/](https://www.korecmblog.com/redis-dlm/%EB%8B%A8%EC%9D%BC%20%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4%EB%A1%9C%20%EA%B5%AC%EC%84%B1%EB%90%9C%20%EB%A0%88%EB%94%94%EC%8A%A4%EC%97%90%EC%84%9C%EC%9D%98%20%EB%B6%84%EC%82%B0%20%EB%9D%BD%20%EA%B5%AC%ED%98%84/)
- [https://velog.io/@hgs-study/redisson-distributed-lock](https://velog.io/@hgs-study/redisson-distributed-lock)
- [https://redis.io/docs/reference/patterns/distributed-locks/](https://redis.io/docs/reference/patterns/distributed-locks/)
- [https://blog.eomsh.com/138](https://blog.eomsh.com/138)