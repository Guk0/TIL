# cors

[https://inpa.tistory.com/entry/WEB-📚-CORS-💯-정리-해결-방법-👏](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)

<br>

## 요약
CORS란 교차 출처 리소스 공유를 의미합니다. 즉, 서로 다른 origin간의 리소스를 공유할 수 있도록 하는 정책입니다. 원래 웹에는 Same Origin Policy라는 정책이 존재합니다. 이 SOP 정책은 같은 출처에서만 리소스를 공유할 수 있다는 정책인데요. 서로 다른 Origin에서 리소스를 공유하는 것을 일부 허용하기 위해 CORS 정책을 이용합니다.

주로 서버 response에 access-control-allow-origin이라는 헤더를 추가하고 이 헤더에 교차 출처를 허용하는 origin을 명시합니다. 브라우저에서는 request 의 origin과 response의 헤더에 담긴 origin을 비교하여 다르다면 응답을 사용하지 않고 버립니다.

- same origin이라고 판단하는 기준은 무엇일까?
  - 프로토콜, 호스트, 포트가 동일하면 동일한 origin이라고 판단합니다. 셋 중 하나라도 일치하지 않으면 cross origin이라고 판단합니다.


<br>

## same origin policy(**SOP**)
  - **같은 출처에서만 리소스를 공유할 수 있다**는 정책
  - 프로토콜, 호스트, 포트가 동일하면 같은 출처라고 확인. 하나라도 일치하지 않으면 cross origin이라고 함.
  - 출처를 비교하는 로직은 서버에 구현된 스펙이 아닌 브라우저에 구현된 스펙이다.

<br>

## 교차 출처 리소스 공유(Cross-Origin Resource Sharing, CORS)
  - **추가 HTTP 헤더**를 사용하여, 한 출처에서 실행 중인 서버가 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 **브라우저에 알려주는 체제**다.
  - 추가 HTTP 헤더는 서버측에서 response header로 부여한다(**Access-Control-Allow-Origin**)
  - 서버측에서 허용할 오리진이 이 헤더에 담긴다.
  - 브라우저에서 서버 측 response와 클라이언트 측 origin을 체크하여 다르면 응답을 사용하지 않고 버린다.
  - CORS 정책 위반을 판단하는 주체는 브라우저다.

- preflight와 preflight 생략
    - 서버는 이 preflight(예비요청)에 대한 응답으로 어떤 것을 허용하고 어떤것을 금지하고 있는지에 대한 정보를 담아서 브라우저로 다시 보내준다.
    - preflight
        - **PUT DELETE일때 preflight를 날린다.** 서버측에서는 이 preflight의 응답에 allow-origin 헤더(위의 헤더)를 붙여서 응답한다.
        - 브라우저에서 cors 체크 후 본 요청을 다시 날린다.
    - non-preflight
        - **GET POST일때 preflight를 날리지 않는다.** 다만 이외에도 충족해야할 요건이 많은데 이는 블로그 참조
        - 본 요청에 대한 응답에 헤더를 붙여 브라우저에서 same-origin을 판단하게 한다.