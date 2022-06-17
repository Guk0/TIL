# git-flow


## git flow init
- git init 과 유사하다. git init과 같이 저장소를 초기화 한다.
- git flow init으로 생성되는 브랜치는 6종류다
  - master : 사용자에게 배포되는 Stable 브랜치
  - develop : 다음 릴리즈를 위해 기능들을 모으는 최신 브랜치
  - feature : develop base. 특정 기능 개발을 위한 브랜치
  - release : develop 작업 사항 이전. 릴리즈를 위해 버그 픽스(Bug fix)를 모으는 브랜치 / 이번 출시 버전을 준비하는 브랜치
  - hotfix : master base. 긴급 버그 픽스를 위한 브랜치
  - support : 버전 호환성 문제를 위한 브랜치
- '-d' 옵션을 주면 브랜치 이름을 지정하지 않아도 된다.
<br>

## feature
- `git flow feature start <feature name>`
  - 위 명령어로 develop을 base로 한 feature 브랜치를 만든다.
  - 생성된 브랜치 명에는 'feature/' prefix가 붙는다. 즉, 브랜치명은 `feature/<feature name>`이 된다.
  - prefix를 바꾸려면 위 명령어에서 feature를 수정하면 된다.
- `git flow feature finish <feature name>`
  - feature 브랜치에서 작업이 완료되었다면 위 명령어를 통해 develop에 merge한다.
  - git-flow는 develop으로 checkout 한뒤 feature 브랜치의 커밋 내용을 merge한 뒤 브랜치를 삭제한다.
- `git flow feature publish <feature name>`
  - origin(원격 저장소)로 브랜치를 push 한다.
- `git flow feature pull origin <feature name>`
  - origin(원격 저장소)에서 브랜치를 pull 한다.

## release
- `git flow release start <version>`
  - develop 브랜치를 기반으로 release 브랜치 생성
- `git flow release publish <version>`
  - origin(원격 저장소)로 브랜치를 push 한다.
- `git flow release track <version>`
  - pull. feature와는 다르게 pull 명령어 대신 track 명령어를 사용한다.
- `git flow release finish <version>`
  - release 브랜치를 master에 merge 하고 release 버전을 태그로 생성.
  - git flow init 할 때 명시한 Version tag prefix 문자열이 release 버전 앞에 추가되어 태그로 생성된다.
  - release 브랜치를 develop에 merge 후 release 브랜치 삭제

## hotfix
- `git flow hotfix start <version>`
  - 핫픽스 브랜치 생성
- `git flow hotfix finish <version>`
  - hotfix 브랜치를 master에 merge 하고 hotfix 버전을 태그로 생성.
  - git flow init 할 때 명시한 Version tag prefix 문자열이 hotfix 버전 앞에 추가되어 태그로 생성된다.
  - hotfix 브랜치를 develop에 merge 후 hotfix 브랜치 삭제


[참고](https://soft.plusblog.co.kr/20)