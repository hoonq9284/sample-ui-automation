# Repository 소개
- behave를 사용한 자동화 스크립트를 관리하는 레포지토리 입니다.

# Use Tool
- Language
  - Python
  - Gherkin
- Framework
  - Selenium
- BDD
  - behave
- Design Pattern
  - Page Object Model

# 실행 구조 및 방법
- 커맨드라인에서 아래 명령어를 통해 실행할 수 있습니다.
  - behave features/{추가 하위 디렉토리.feature}
  - 추가 하위 디렉토리를 입력하면 해당 feature 파일만 실행하고, beahve features/ 를 입력하면 모든 feature 파일을 실행하는 구조
- behave 시나리오는 steps/Steps.py 파일에 있는 함수를 순차적으로 실행합니다. 또한 feature 파일 내에 있는 given, when, then 시나리오를 순차적으로 실행하고, 구현되지 않은 시나리오는 NotImplmentedError 를 발생시킵니다.
