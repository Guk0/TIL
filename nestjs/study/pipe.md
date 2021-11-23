
# Pipe

Pipe는 @Injectable () 데코레이터로 주석이 달린 클래스.
client ->(요청) -> Pipe -> 엔드포인트 ->(응답) client
Pipe는 data transformation과 data validation을 담당.
파이파는 메서드 호출 직전 작동하여 인수에 대해 변환할 데이터가 있다면 변환하고 유효성 체크 진행.

## Data transformation
입력 데이터를 원하는 형식으로 변환. 숫자를 number type으로 받고 싶은데 string으로 오는 경우 이를 number type으로 변경.

## Data validation
입력 데이터가 유효한지 판단. 그렇지 않으면 예외 발생.
만약 text의 길이가 10자 이하로 제한하였는데 10자 이상이 되면 에러 발생.

## Pipe의 종류
Handler level Pipes
Parameter level Pipes
Global level Pipes

### Handler level Pipes
``` typescript
@Post()
@UsePipes(pipe)
createBoard(
  @Body('title') title,
  @Body('description') description,
) {}
```

### Parameter level Pipes
``` typescript
@Post()
createBoard(
  @Body('title', ParameterPipe) title,
  @Body('description') description,
) {}
```

### Global level Pipes
``` typescript
// main.ts
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(GlobalPipes);
  await app.listen(3000);
}
bootstrap();
```
* 모든 요청에 적용.


### Built-in Pipes
nest js의 기본적인 6가지 파이프
 - ValidationPipe
 - ParseIntPipe
 - ParseBoolPipe
 - ParseArrayPipe
 - ParseUUIDPipe
 - DefaultValuePipe

ParseIntPipe
``` typescript
@Get(':id')
findOne(@Param('id', ParseIntPipe) id: number) {
  return;
}
```
* :id 해당하는 id 값 path는 항상 string 으로 오기 때문에 ParseIntPipe를 사용하여 number 타입으로 변경.

### 필요한 패키지
[class-validator](https://github.com/typestack/class-validator)
[class-transformer](https://github.com/typestack/class-transformer)

### 필수 값 지정
```typescript
// controller
  @Post()
  @UsePipes(ValidationPipe)
  createBoard(@Body() createBoardDto: CreateBoardDto): Board {
    return this.boardsService.createBoard(createBoardDto);
  }

```

```typescript
// dto
export class CreateBoardDto {
  @IsNotEmpty()
  title: string;

  @IsNotEmpty()
  description: string;
}
```



### 404 not found exception

``` typescript
// service
getBoardById(id: string): Board {
  const board = this.boards.find((board) => board.id === id);
  if (!board) throw new NotFoundException();
  return board;
}
```




### Custom Pipe
custom pipe 선언시 반드시 PipeTransform을 implement 해줘야함. 모든 파이프는 transfrom() 메서드를 필요로 함.

>transform() 메서드   
두개의 인자를 전달해야함.  
첫번째는 처리가 된 인자의 값(value)  
두번째는 인자에 대한 메타 데이터를 포함한 객체  
리턴된 값은 Route 핸들러로 전달됨.   
예외가 발생하면 바로 클리어언트에 전달.
```js
//다음과 board의 status를 validation하는 pipe 정의 후
export class BoardStatusValidationPipe implements PipeTransform {
  readonly StatusOptions = [BoardStatus.PRIVATE, BoardStatus.PUBLIC];

  transform(value: any, metadata: ArgumentMetadata) {
    value = value.toUpperCase();

    if (!this.isStatusValid(value)) {
      throw new BadRequestException(`${value} isn't in the status options`);
    }
    return value;
  }

  private isStatusValid(status: any) {
    const index = this.StatusOptions.indexOf(status);
    return index !== -1;
  }
}

...
//컨트롤러에서 사용. Body에 넣어준다.
@Patch('/:id/status')
updateboardStatus(
  @Param('id') id: string,
  @Body('status', BoardStatusValidationPipe) status: BoardStatus,
) {
  return this.boardsService.updateBoardStatus(id, status);
}

```