# 구조

app.module.ts에서 각 모듈들을 import.  
각 모듈들은 controller와 provider를 호출. provider는 보통 service.

rails에서 service layer를 사용하는 것과 같은 맥락이라고 보면 될 듯. 

controller는 엔드포인트(액션)들로 구성되어 있고 각 엔드포인트에서 서비스에 정의된 메서드들을 호출하여 사용.
