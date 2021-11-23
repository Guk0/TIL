# DTO(DATA TRANSFER OBJECT)

``` typescript
// controller
  @Post()
  createBoard(@Body() createBoardDto: CreateBoardDto): Board {
    return this.boardsService.createBoard(createBoardDto);
  }
```

@Body로 파라미터를 받을 때 
``` typescript
@Body('title') title: string,
@Body('description') description: string,
```

  위와 같은 방식으로 정의하면 나중에 많은 양의 key, value 값이 파라미터로 넘어오면 유지보수 측면에서 매우 비효율적인 코드가 됨.  
  dto.ts에 CreateBoardDto에 파라미터들을 정의.
  
  ``` ts
  export class CreateBoardDto {
    title: string;
    description: string;
  }
  ```