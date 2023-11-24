from behave import *

@then('네이버 검색 필드가 표시된다.')
def step_impl(context):
    context.mp.check_search_field()

@then('프로필 영역이 표시된다.')
def step_impl(context):
    context.mp.check_account_container()

@then('로그인 안내 문구가 표시된다.')
def step_impl(context):
    context.mp.check_login_info_text()

@then('로그인 버튼이 표시된다.')
def step_impl(context):
    context.mp.check_login_button()

@then('"아이디 찾기" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_find_id_text()

@then('"비밀번호 찾기" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_find_password_text()

@then('"회원가입" 링크 텍스트가 표시된다.')
def step_impl(context):
    context.mp.check_register_text()