from atid_store.base_test.locatores_paths import *
from atid_store.test.all_functions import *
from faceebok.base_test.register_locator import *
from faceebok.base_test.login_forgotten_locator import *
from faceebok.test.register_test import *
from faceebok.test.loginpage_test import *
from faceebok.test.forget_password_test import *


def app():
    # Atid shopping store
    test_men()
    test_store()
    test_women()
    test_accessories()
    test_search_product()

    test_create_account()
    test_invalid_email()
    test_invalid_password()
    test_email_verification()
    test_error_handling()
    test_already_logedin()

    # login page
    test_positive_login()
    test_invalid_username()
    test_invalid_password()
    test_invalid_user_pass()
    test_both_empty()

    # forgot password
    test_forgot_password()
    test_invalid_email()


app()
