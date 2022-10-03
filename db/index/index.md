# index란?
## index
인덱스(index)의 원래 뜻은 색인. 데이터베이스에서 조회 및 검색을 더 빠르게 할 수 있는 방법/기술, 혹은 이에 쓰이는 자료구조 자체를 의미하기도 함

<br>

## 동작
- Index Table에서 `where`에 포함된 값을 검색
- 해당 값의 table_id PK를 획득
- 가져온 table_id PK값으로 원본 테이블에서 값을 조회

<br>

## B+tree 알고리즘
- DBMS는 인덱스를 다양한 알고리즘으로 관리를 하고 있는데 일반적으로 사용되는 알고리즘은 B+ Tree 알고리즘이다.
- 구조
  - 실제 데이터가 저장된 리프노드(Leaf nodes)
  - 리프노드까지의 경로 역할을 하는 논리프노드(Non-leaf nodes)
  - 경로의 출발점이 되는 루트 노드(Root node)
- B+tree는 리프노드에 이르기까지에 대한 자식 노드에 포인터가 저장되어 있다. 즉, B+트리의 검색은 루트노드에서 어떤 리프 노드에 이르는 한 개의 경로만 검색하면 되므로 매우 효율적이다.

<br>

## B+tree vs hash table
- 쿼리에는 보통 부등호 연산(<>)도 포함
- hash table은 동등 연산에 특화된 자료구조이기 때문에 부등호 연산 사용 시 문제 발생

<br>

## 주의할 점
- 인덱스는 따로 테이블의 형태로 관리가 된다. 자원을 소모한다는 의미. 때문에 무분별한 인덱스의 사용은 성능에 부정적인 영향을 미칠 수 있다.
- 또한 인덱스는 이진트리를 사용하기 때문에 기본적으로 정렬되어 있다. 이로인해 검색과 조회의 속도를 향상시킬 수 있지만 잦은 데이터의 변경(삽입, 수정 삭제)가 된다면 인덱스 데이블을 변경과 정렬에 드는 오버헤드 때문에 오히려 성능 저하가 일어날 수 있다.
    - INSERT : 테이블에는 입력 순서대로 저장되지만, 인덱스 테이블에는 정렬하여 저장하기 때문에 성능 저하 발생
    - DELETE : 테이블에서만 삭제되고 인덱스 테이블에는 남아있어 쿼리 수행 속도 저하
    - UPDATE : 인덱스에는 UPDATE가 없기 때문에 DELETE, INSERT 두 작업 수행하여 부하 발생
- 데이터의 중복이 높은 컬럼(카디널리티가 낮은 컬럼)은 인덱스로 만들어도 무용지물 (예: 성별)
- 다중 컬럼 인덱싱할 때 카디널리티가 높은 컬럼->낮은 컬럼 순으로 인덱싱해야 효율적
- join이 잦은 작업에 쓰는게 좋음.
- index도 결국 데이터다보니 DB 내 공간을 차지한다.
- 데이터의 양이 너무 적으면 오히려 성능이 떨어질 수도 있다.

<br>

## 인덱스를 타지 않는 경우

인덱스 컬럼절을 변형한 경우
```sql
/* 인덱스를 타지 않는 예 */
SELECT column_name FROM table_name WHERE TO_CHAR(column_name, 'YYYYMMDD') = '20130909';

/* 인덱스를 타는 예 */
SELECT column_name FROM table_name WHERE column_name = TO_DATE('20130909', 'YYYYMMDD');
```

내부적으로 데이터 형 변환이 일어난 경우
``` sql
/* 인덱스를 타지 않는 예  DATE 타입의 column */
SELECT column_name FROM table_name WHERE column_name  = '20130909'; 

/* 인덱스를 타는 예 */
SELECT column_name FROM table_name WHERE column_name = TO_DATE('20130909', 'YYYYMMDD');
```
조건절에 NULL 또는 NOT NULL을 사용하는 경우
``` sql
/* 인덱스를 타지 않는 예 */
FROM table_name WHERE column_name IS NULL;
SELECT column_name FROM table_name WHERE column_name IS NOT NULL;

/* 인덱스를 타는 예 */
SELECT column_name FROM table_name WHERE column_name > '';
SELECT column_name FROM table_name WHERE column_name >= 0;
```
부정형으로 조건을 사용한 경우
``` sql
/* 인덱스를 타지 않는 예 */
SELECT column_name FROM table_name WHERE column_name != 30;

/* 인덱스를 타는 예 */
SELECT column_name FROM table_name WHERE column_name < 30 AND column_name > 30;
SELECT column_name FROM table_name WHERE NOT EXISTS (SELECT column_name FROM table_name WHERE column_name = 30);
```
LIKE 연산자를 사용하는 경우
``` sql
/* 인덱스를 타지 않는 예 */
SELECT column_name FROM table_name WHERE column_name LIKE '%S%';
SELECT column_name FROM table_name WHERE column_name LIKE '%S';

/* 인덱스를 타는 예 */
SELECT column_name FROM table_name WHERE column_name LIKE 'S%';
```
OR 조건을 사용하는 경우
``` sql
/* 인덱스를 타지 않는 예 */
SELECT * FROM table_name  WHERE column_name = 'yunseop' or name = 'song';

/* 인덱스를 타는 예 */
SELECT * FROM table_name  WHERE column_name = 'yunseop';
UNION ALL 
SELECT * FROM table_name  WHERE column_name = 'song';
```

[참고](http://dbcafe.co.kr/wiki/index.php/%EC%98%A4%EB%9D%BC%ED%81%B4_%EC%9D%B8%EB%8D%B1%EC%8A%A4_%ED%83%80%EC%A7%80_%EC%95%8A%EB%8A%94_%EA%B2%BD%EC%9A%B0)