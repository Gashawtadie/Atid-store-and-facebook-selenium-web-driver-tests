import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faceebok.base_test.login_forgotten_locator import *


def test_positive_login():
    # Open Facebook page or application and all necessary fields are present(email,phone, password)
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    # (Enter correct username)
    #  Test login functionality with enter valid username in username field=example123
    valid_user = driver.find_element(By.XPATH, username_field)
    valid_user.send_keys("0526162719")
    time.sleep(2)

    # Test login functionality with enter valid password in password field=abc123456
    valid_pass = driver.find_element(By.XPATH, password_field)
    valid_pass.send_keys("Gasaki86")
    time.sleep(2)

    # Click on login button
    btn_valid = driver.find_element(By.XPATH, btn_locator)
    btn_valid.click()
    time.sleep(2)

    # Ensure the data are connect the exact account
    well_locator = driver.find_element(By.XPATH, "//span[contains(text(),'Welcome to Facebook, Gashu')]")
    well_come = well_locator.text
    assert well_come == "Welcome to Facebook, Gashu"


def test_invalid_username():
    # Open Facebook page or application and all necessary fields are present(email,phone, password)
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    # Test login username incorrect User into Username field
    invalid_username = driver.find_element(By.XPATH, username_field)
    invalid_username.send_keys("0123456789")

    # Test login password correct into Password field password = abc123456
    valid_pass = driver.find_element(By.XPATH, password_field)
    valid_pass.send_keys("Gasaki86")

    # Click Login button
    btn = driver.find_element(By.XPATH, btn_locator)
    btn.click()
    # time.sleep(2)

    # Ensure the data are connect the exact account
    nextpage = driver.find_element(By.XPATH, "//div[contains(text(),'Continue as Gashu?')]")
    page = nextpage.text
    assert page == "Continue as Gashu?"

    # Select optional choose if you are not select Not you
    choose_notyou = driver.find_element(By.CSS_SELECTOR, invalid_username_notyou_cssselector)
    choose_notyou.click()
    time.sleep(2)

    # # Verify error message is displayed
    error_message_locator = driver.find_element(By.CSS_SELECTOR, error_message_locator_invalidusername)
    if error_message_locator.is_displayed():
        print("The email address or mobile number you entered isn't connected to an account. Find your account and log "
              "in. ")


def test_invalid_password():
    # Open page
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    # Test login valid username = abcdefg
    login_corect = driver.find_element(By.XPATH, username_field)
    login_corect.send_keys("0501234567")

    # Test login invalid password = incorrect password
    incorrect_login = driver.find_element(By.XPATH, password_field)
    incorrect_login.send_keys("123456abc")

    # Click login button
    lo_btn = driver.find_element(By.XPATH, btn_locator)
    lo_btn.click()

    # error message displayed
    error_message = driver.find_element(By.CSS_SELECTOR, error_message_invalipassword)
    assert error_message.is_displayed(), "Error message is not displayed, but it should be display cause of wrong " \
                                         "password "

    # Verify error message displayed when error password entered
    error_pass = error_message.text
    assert error_pass == "The password that you've entered is incorrect. Forgotten password?"


def test_invalid_user_pass():
    # Open page
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    # Test login invalid username = abcdefg
    login_corect = driver.find_element(By.XPATH, username_field)
    login_corect.send_keys("incorrect")

    # Test login invalid password = incorrect password
    incorrect_login = driver.find_element(By.XPATH, password_field)
    incorrect_login.send_keys("incorrect")

    # Click login button
    lo_btn = driver.find_element(By.XPATH, btn_locator)
    lo_btn.click()

    # error message displayed
    error_message = driver.find_element(By.CSS_SELECTOR, test_invalid_user_pass_error_locator)
    if error_message.is_displayed():
        print("The password that you've entered is incorrect. ")
    driver.quit()


def test_both_empty():
    # Open page
    driver = webdriver.Chrome()
    driver.get(home_page_fb)

    # Test login empty username
    login_corect = driver.find_element(By.XPATH, username_field)
    login_corect.send_keys(" ")

    # Test login empty password
    incorrect_login = driver.find_element(By.XPATH, password_field)
    incorrect_login.send_keys(" ")

    # Click login button
    lo_btn = driver.find_element(By.XPATH, btn_locator)
    lo_btn.click()
    # time.sleep(2)

    # Error message displayed
    error_message = driver.find_element(By.CSS_SELECTOR, error_message_locator_invalidusername)
    if error_message.is_displayed():
        print("Invalid username or password detected")
    driver.quit()
