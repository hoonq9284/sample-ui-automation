from behave import *

@then("네이버 검색 필드가 표시된다.")
def step_impl(context):
    context.mp.check_search_field()

@then("프로필 영역이 표시된다.")
def step_impl(context):
    context.mp.check_account_container()