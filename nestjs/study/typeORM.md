# TypeORM
> typescript로 작성된 ORM 라이브러리  

[nest docs](https://docs.nestjs.com/techniques/database)  
[typeorm docs](https://typeorm.io/)


## ORM
- 객체지향 프로그래밍은 클래스를 사용하고 관계형 데이터베이스는 테이블을 사용.
- 객체 모델과 관계형 모델 간의 불일치를 해소하기 위해 ORM(Object Relational Mapping) 사용.
- 객체와 관계형 데이터베이스의 데이터를 자동으로 변형 및 연결.

``` js
// TypeORM
const boards = Board.find({title: 'Hello', status: 'PUBLIC'})

// Pure js
db.query('SELECT * FROM boards WHERE title = "HELLO" AND status = "PUBLIC', (error, result) => {
  if (err) throw new Error('Error')
  boards = result.rows;
})
```

## 세팅
config 파일 작성 후 아래와 같이 app.module.ts에 설정 추가
```js
...
@Module({
  imports: [TypeOrmModule.forRoot(typeORMConfig), BoardsModule],
})
export class AppModule {}
...
```

## Entity
아래와 같이 Entity 생성.
```ts
@Entity()
export class Board extends BaseEntity {
  @primaryGeneratedColumn()
  id: number;

  @Column()
  title: string;

  @Column()
  description: string;

  @column()
  status: BoardStatus;
}
```

### @Entity()
위 데코레이터 클래스는 Board 클래스가 Entity 임을 나타내는데 사용.

### @primaryGeneratedColumn()
id열이 primary key임을 나타냄.

## Repository
entity 개체와 함께 동작하며 read, insert, update, delete 등을 처리.
```ts
@EntityRepository(Board)
export class BoardRepository extends Repository<Board> {

}
```
- @EntityRepositroy : 클래스를 사용자 정의 저장소로 선언하는데 사용.
- 사용자 정의 저장소란 일부 엔터티를 관리하거나 일반 저장소일 수 있음.
- @InjectableRepository 데코레이터 사용하여 Service에 Repository 넣어주기
``` ts
@Injectable()
export class BoardService {
  constructor(
    @InjectableRepository(BoardRepository)
    private BoardRepository: BoardRepository,
  ) {}
}
```
