from behave import *
from playwright.sync_api import expect


@given('username and pwd password')
def input_creds(context):
    context.page.goto('http://uitestingplayground.com/sampleapp')

    context.page.get_by_placeholder('User Name').fill('name')
    context.page.get_by_placeholder('********').fill('pwd')


@when('Log In button clicked')
def click_login(context):
    context.page.get_by_role('button', name='Log In').click()


@then('Show welcome message')
def expect_welcome_message(context):
    message = context.page.locator('label#loginstatus')
    expect(message). to_have_text('Welcome, name!')
