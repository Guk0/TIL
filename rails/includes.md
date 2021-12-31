## includes
보통 n+1 문제를 해결하기 위해 includes를 많이 사용한다. includes의 기본적인 동작은 preload이지만 특정 조건에서 eager_load와 같은 동작을 한다.

includes는 아래 3가지 조건 중 하나만 만족하면 eager_loading을 아니면 preload와 같이 동작한다.

- *includes한 테이블에 where문을 추가해 필터를한 경우*
- *includes한 association에 joins 메서드나 references 메서드를 호출한 경우*
- *임의의 association에 eager_load를 호출한 경우*

## preload

association의 개수만큼 쿼리를 나눠 날린다. 경험상 pagination을 하거나 데이터 개수가 적을 때는 상관 없지만 많은 양의 데이터 개수를 한번에 불러올 때 preload를 사용하면 쿼리 시간이 굉장히 많이 소요된다. eager_load나 join, left_join으로 변경할 수 있다면 하는게 베스트이다.

### eager_load

left outer join을 하여 association의 개수와 관계없이 쿼리를 한번만 날린다. 

association이 **메모리에 로드**되므로 association에 액세스하려는 경우에만 사용되며, where 절이 지원되거나 모든 association을 단일 쿼리로 가져 오도록 association을 기준으로 레코드를 필터링하려는 경우에 사용된다.

참고  
[https://velog.io/@hyob/Rails-Joins-Preload-Eager-load-and-Includes](https://velog.io/@hyob/Rails-Joins-Preload-Eager-load-and-Includes)

[https://negabaro.github.io/archive/rails-includes-query-detail](https://negabaro.github.io/archive/rails-includes-query-detail)

[https://mznetblog.wordpress.com/2016/04/29/includes-vs-eager_load/](https://mznetblog.wordpress.com/2016/04/29/includes-vs-eager_load/)

[http://blog.ifyouseewendy.com/blog/2015/11/11/preload-eager_load-includes-references-joins/](http://blog.ifyouseewendy.com/blog/2015/11/11/preload-eager_load-includes-references-joins/)

[https://velog.io/@hyob/Rails-Joins-Preload-Eager-load-and-Includes](https://velog.io/@hyob/Rails-Joins-Preload-Eager-load-and-Includes)