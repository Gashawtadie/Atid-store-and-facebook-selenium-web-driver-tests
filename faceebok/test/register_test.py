import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from faceebok.base_test.register_locator import *


def test_create_account():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(home_page_fb)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, sign_up_locator)
    new_acc.click()
    # time.sleep(2)

    # Insert correct name in first name field
    name = driver.find_element(By.NAME, name_field_locator)
    name.send_keys("Name")
    # time.sleep(2)

    # Insert correct sure name in sure name field
    sure_name = driver.find_element(By.NAME, sure_name_locator)
    sure_name.send_keys("SureName")
    # time.sleep(2)

    # Insert correct email address or phone number
    email = driver.find_element(By.NAME, email_phone_locator)
    email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Enter confirmation emai address
    confrm_email = driver.find_element(By.NAME, confrirmation_email_locator)
    confrm_email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Insert password for email
    pas_email = driver.find_element(By.XPATH, insert_password_locator)
    pas_email.send_keys("Abcde123456")
    # time.sleep(2)

    # Select date
    date = Select(driver.find_element(By.XPATH, select_date_locat))
    date.select_by_visible_text("7")
    # time.sleep(1)
    # select month
    month = Select(driver.find_element(By.NAME, month_selector))
    month.select_by_visible_text("Jan")
    # ime.sleep(2)

    # select year
    year = Select(driver.find_element(By.NAME, year_selector))
    year.select_by_visible_text("1992")
    # time.sleep(2)

    # Select gender
    male = driver.find_element(By.XPATH, gender_selector)
    male.click()
    # time.sleep(2)

    # Click sigh up button
    sign_up = driver.find_element(By.TAG_NAME, button_selector)
    sign_up.click()



def test_invalid_email():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(home_page_fb)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, sign_up_locator)
    new_acc.click()
    # time.sleep(2)

    # Insert correct name in first name field
    name = driver.find_element(By.NAME, name_field_locator)
    name.send_keys("Correct-First")
    # time.sleep(2)

    # Insert correct sure name in sure name field
    sure_name = driver.find_element(By.NAME, sure_name_locator)
    sure_name.send_keys("Correct-Last")
    # time.sleep(2)

    # Verify that register with an invalid email address (e.g. missing "@" symbol).
    email = driver.find_element(By.NAME, email_phone_locator)
    email.send_keys("Abcdef12345@gmail.com")
    # time.sleep(2)

    # Enter confirmation emai address
    confrm_email = driver.find_element(By.NAME, confrirmation_email_locator)
    confrm_email.send_keys("Abcdef12345@gmail.com")
    # time.sleep(2)

    # Insert password for email
    pas_email = driver.find_element(By.XPATH, insert_password_locator)
    pas_email.send_keys("Abcd1236")
    # time.sleep(2)

    # Select date
    date = Select(driver.find_element(By.XPATH, select_date_locat))
    date.select_by_visible_text("7")
    # time.sleep(1)
    # select month
    month = Select(driver.find_element(By.NAME, month_selector))
    month.select_by_visible_text("Jan")
    # ime.sleep(2)
    # select year
    year = Select(driver.find_element(By.NAME, year_selector))
    year.select_by_visible_text("2015")
    # time.sleep(2)

    # Select gender
    male = driver.find_element(By.XPATH, gender_selector)
    male.click()
    # time.sleep(2)

    # Click sigh up button
    sign_up = driver.find_element(By.TAG_NAME, button_selector)
    sign_up.click()

    # Check if the wrong email input is working well
    send_email = driver.find_element(By.TAG_NAME, wrong_email_select)
    if send_email.is_displayed():
        print("Sorry, we are not able to process your registration.")
    time.sleep(5)


def test_invalid_password():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(home_page_fb)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, sign_up_locator)
    new_acc.click()
    # time.sleep(2)

    # Insert correct name in first name field
    name = driver.find_element(By.NAME, name_field_locator)
    name.send_keys("Correct-First")
    # time.sleep(2)

    # Insert correct sure name in sure name field
    sure_name = driver.find_element(By.NAME, sure_name_locator)
    sure_name.send_keys("Correct-Last")
    # time.sleep(2)

    # Verify that register with an invalid email address (e.g. missing "@" symbol).
    email = driver.find_element(By.NAME, email_phone_locator)
    email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Enter confirmation email address
    confrm_email = driver.find_element(By.NAME, confrirmation_email_locator)
    confrm_email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Test that the user cannot register with a password that is too short.
    pas_email = driver.find_element(By.XPATH, insert_password_locator)
    pas_email.send_keys("Ab")
    # time.sleep(2)

    # Select date
    date = Select(driver.find_element(By.XPATH, select_date_locat))
    date.select_by_visible_text("7")
    # time.sleep(1)
    # select month
    month = Select(driver.find_element(By.NAME, month_selector))
    month.select_by_visible_text("Jan")
    # ime.sleep(2)
    # select year
    year = Select(driver.find_element(By.NAME, year_selector))
    year.select_by_visible_text("2015")
    # time.sleep(2)

    # Select gender
    male = driver.find_element(By.XPATH, gender_selector)
    male.click()
    # time.sleep(2)

    # Click sigh up button
    sign_up = driver.find_element(By.TAG_NAME, button_selector )
    sign_up.click()
    time.sleep(2)

    # display error message when short password enter
    error_meassage = driver.find_element(By.TAG_NAME, error_message_password)
    if error_meassage.is_displayed():
        print("Sorry, we are not able to process your registration.")


def test_email_verification():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(home_page_fb)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, sign_up_locator )
    new_acc.click()
    # time.sleep(2)

    # Insert correct name in first name field
    name = driver.find_element(By.NAME, name_field_locator)
    name.send_keys("Correct-First")
    # time.sleep(2)

    # Insert correct sure name in sure name field
    sure_name = driver.find_element(By.NAME, sure_name_locator)
    sure_name.send_keys("Correct-Last")
    # time.sleep(2)

    # Verify that register with valid email address
    email = driver.find_element(By.NAME, email_phone_locator)
    email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Enter confirmation emai address
    confrm_email = driver.find_element(By.NAME, confrirmation_email_locator)
    confrm_email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Insert password for email
    pas_email = driver.find_element(By.XPATH, insert_password_locator)
    pas_email.send_keys("Abcd1236")
    # time.sleep(2)

    # Select date
    date = Select(driver.find_element(By.XPATH, select_date_locat))
    date.select_by_visible_text("7")
    # time.sleep(1)
    # select month
    month = Select(driver.find_element(By.NAME, month_selector))
    month.select_by_visible_text("Jan")
    # ime.sleep(2)
    # select year
    year = Select(driver.find_element(By.NAME, year_selector))
    year.select_by_visible_text("2015")
    # time.sleep(2)

    # Select sex
    male = driver.find_element(By.XPATH, gender_selector)
    male.click()
    # time.sleep(2)

    # Click sigh up button
    sign_up = driver.find_element(By.TAG_NAME, button_selector)
    sign_up.click()

    # Enter the code from your email
    confrm = driver.find_element(By.XPATH, error_message_code)
    confrm.send_keys("12922")
    time.sleep(1)

    # Test that the user receives a verification email after registering.
    send_email = driver.find_element(By.XPATH, send_email_selector)
    send_email.click()
    time.sleep(5)


def test_error_handling():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(error_handling_locator)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, signup_error_handling)
    new_acc.click()
    # time.sleep(2)

    # # Test that the user sees an error message if they try to register with an email that is already in use.
    name = driver.find_element(By.XPATH, email_already_use)
    if name.is_displayed():
        print("Already have an account?")
    time.sleep(2)


def test_already_logedin():
    # Open Facebook page or application
    driver = webdriver.Chrome()
    driver.get(home_page_fb)
    driver.implicitly_wait(10)

    # Click on Sign up facebook
    new_acc = driver.find_element(By.XPATH, test_already_newaccount)
    new_acc.click()
    # time.sleep(2)

    # Insert correct name in first name field
    name = driver.find_element(By.NAME, name_field_locator)
    name.send_keys("firstname")
    # time.sleep(2)

    # Insert correct sure name in sure name field
    sure_name = driver.find_element(By.NAME, sure_name_locator)
    sure_name.send_keys("lastname")
    # time.sleep(2)

    # Insert correct email address or phone number
    email = driver.find_element(By.NAME, email_phone_locator )
    email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Enter confirmation emai address
    confrm_email = driver.find_element(By.NAME, confrirmation_email_locator)
    confrm_email.send_keys("Example@gmail.com")
    # time.sleep(2)

    # Insert password for email
    pas_email = driver.find_element(By.XPATH, insert_password_locator )
    pas_email.send_keys("Abcde123456")
    # time.sleep(2)

    # Select date
    date = Select(driver.find_element(By.XPATH, select_date_locat))
    date.select_by_visible_text("7")
    # time.sleep(1)
    # select month
    month = Select(driver.find_element(By.NAME, month_selector))
    month.select_by_visible_text("Jan")
    # ime.sleep(2)
    # select year
    year = Select(driver.find_element(By.NAME, year_selector))
    year.select_by_visible_text("1992")
    # time.sleep(2)

    # Select gender
    male = driver.find_element(By.XPATH, gender_selector)
    male.click()
    # time.sleep(2)

    # Click sigh up button
    sign_up = driver.find_element(By.TAG_NAME, button_selector)
    sign_up.click()

    # Test that the user sees an error message if they try to register while they are already logged in.
    alreadu_use = driver.find_element(By.XPATH, email_already_use)
    if alreadu_use.is_displayed():
        print("That number was used too recently")
    time.sleep(1)
