Feature: MainPage

# feature 초기화 작업
Background: 초기화
    Given Chrome Browser로 NAVER URL에 접속한다.
    And 테스트 수행에 필요한 초기화를 한다.
    And 창을 최대화한다.

Scenario: 메인 페이지 접속 확인하기
    Then 네이버 검색 필드가 표시된다.

Scenario: 프로필 영역 확인하기
    Then 프로필 영역이 표시된다.
