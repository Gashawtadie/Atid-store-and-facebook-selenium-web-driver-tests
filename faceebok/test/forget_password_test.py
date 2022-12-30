import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faceebok.base_test.login_forgotten_locator import *


def test_forgot_password():
    # Open Facebook page or application and all necessary fields are present(email,phone, password)
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    #  Test login functionality with enter valid username in username field=example123
    valid_user = driver.find_element(By.XPATH, username_field)
    valid_user.send_keys("0526162719")
    # time.sleep(2)

    # Test login functionality with enter valid password in password field=abc123456
    valid_pass = driver.find_element(By.XPATH, password_field)
    valid_pass.send_keys("123456789")
    # time.sleep(2)

    # Click on login button
    btn_valid = driver.find_element(By.XPATH, btn_locator)
    btn_valid.click()
    # time.sleep(2)

    # Click on the "Forgot password" link.
    forgot = driver.find_element(By.LINK_TEXT, forgot_password)
    forgot.click()
    # time.sleep(2)

    # Click on Not you if the account that display not you
    notyou = driver.find_element(By.XPATH, not_you_locator)
    notyou.click()
    # time.sleep(2)

    # Enter the email address associated with the account
    account = driver.find_element(By.XPATH, account_key_locator)
    account.clear()
    account.send_keys("gashumec@gmail.com")

    # Click the "Send reset email" button
    valid_return = driver.find_element(By.NAME, submit_locator)
    valid_return.click()
    #time.sleep(2)


    # Click the "Search" button
    send_code = driver.find_element(By.XPATH, click_btn_locatr)
    send_code.click()
    #time.sleep(5)

    # Click on continue
    con = driver.find_element(By.TAG_NAME, con_loc)
    con.click()
    #time.sleep(2)

    #Enter code over 6 letters that accept from email address
    not_return = driver.find_element(By.XPATH, enter_loc)
    not_return.clear()
    not_return.send_keys("129102 ")
    #time.sleep(2)


    #Click on last stage inorder to accept confirmation
    last = driver.find_element(By.XPATH, confirm_loc)
    last.click()
    time.sleep(2)

def test_invalid_email():
    # Open Facebook page or application and all necessary fields are present(email,phone, password)
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    #  Test login functionality with enter valid username in username field=example123
    valid_user = driver.find_element(By.XPATH, username_field)
    valid_user.send_keys("0526162719")
    # time.sleep(2)

    # Test login functionality with enter valid password in password field=abc123456
    valid_pass = driver.find_element(By.XPATH, password_field)
    valid_pass.send_keys("123456789")
    # time.sleep(2)

    # Click on login button
    btn_valid = driver.find_element(By.XPATH, btn_locator)
    btn_valid.click()
    # time.sleep(2)

    # Click on the "Forgot password" link.
    forgot = driver.find_element(By.LINK_TEXT, forgot_password)
    forgot.click()
    # time.sleep(2)

    # Click on Not you if the account that display not you
    notyou = driver.find_element(By.XPATH, not_you_locator)
    notyou.click()
    # time.sleep(2)

    # Enter the email address associated with the account
    account = driver.find_element(By.XPATH, account_key_locator)
    account.clear()
    account.send_keys("abcd@gmail.com")

    # Click the "Send reset email" button
    valid_return = driver.find_element(By.NAME, submit_locator)
    valid_return.click()
    #time.sleep(2)

    #incorrect
    incorret = driver.find_element(By.XPATH, incorrect_email_loc)
    incorret.click()
    time.sleep(2)

    #fill email
    fillemail = driver.find_element(By.XPATH, fill_mail_loc)
    fillemail.send_keys("abcd@gmail.com")

    # Error message for email
    # error_message_email = driver.find_element(By.XPATH, "")
    # if error_message_email.is_displayed():
    #     print("")








# Test that the password reset link expires after a certain amount of time (e.g. 24 hours).
# Test that the user is prompted to create a new password when they click the password reset link.
# Test that the user's password is successfully updated when they enter a new password and confirm it.
# Test that the user is redirected to the login page after successfully resetting their password.
# Test that the user is presented with an error message if they enter an email address that is not associated with an account.
# Test that the user is presented with an error message if they try to use an expired password reset link.
# Test that the user is presented with an error message if they enter a new password that does not meet the required complexity (e.g. must contain at least one number and one special character).
# Test that the user is presented with an error message if they enter a new password and confirmation that do not match.
