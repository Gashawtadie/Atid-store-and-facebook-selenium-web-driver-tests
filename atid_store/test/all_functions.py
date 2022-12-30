import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from atid_store.base_test.locatores_paths import *


def test_store():
    driver = webdriver.Chrome()
    driver.get(home_path)

    click_store = driver.find_element(By.XPATH, hm_str_pth)
    click_store.click()
    # time.sleep(2)

    men_pro = driver.find_element(By.XPATH, str_pro_path)
    men_pro.click()

    product_name_store = driver.find_element(By.XPATH, pro_name_path)
    actual_text = product_name_store.text
    expected_result = "ATID Yellow Shoes"

    assert actual_text == expected_result, f"expected product name{expected_result}, but got {product_name_store}"

    # time.sleep(2)
    add_btn = driver.find_element(By.XPATH, str_btn_path)
    add_btn.click()
    # time.sleep(2)

    price_black_yellow_shoes = driver.find_element(By.XPATH, price_str_path)
    price = price_black_yellow_shoes.text
    assert price == '120.00 ₪'
    time.sleep(2)

    cart_store = driver.find_element(By.XPATH, cpn_str_path)
    cart_store.click()
    copon = driver.find_element(By.XPATH, store_cpn_field)
    copon.clear()
    copon.send_keys(By.NAME, "123456kl")
    apply_cop = driver.find_element(By.XPATH, store_apply_path)
    apply_cop.click()
    time.sleep(5)


def test_men():
    driver = webdriver.Chrome()
    driver.get(home_path_men)

    home_men = driver.find_element(By.XPATH, hm_men_pth)
    home_men.click()
    # time.sleep(2)

    pro_men = driver.find_element(By.XPATH, men_pro_path)
    pro_men.click()
    # time.sleep(2)

    product_name_category = driver.find_element(By.XPATH, pro_name_men_path)
    category_product = product_name_category.text
    expected_result = "ATID Green Tshirt"
    assert category_product == expected_result, f"expected result name {expected_result} but got{category_product}"

    add_men = driver.find_element(By.XPATH, men_btn_path)
    add_men.click()
    # time.sleep(2)
    price_men = driver.find_element(By.XPATH, price_men_path)
    price = price_men.text
    assert price == "190.00 ₪"
    time.sleep(2)

    cart_store = driver.find_element(By.XPATH, cpn_men_path)
    cart_store.click()
    copon = driver.find_element(By.XPATH, men_cpn_field)
    copon.clear()
    copon.send_keys(By.NAME, "123456kl")
    apply_cop = driver.find_element(By.XPATH, men_apply_path)
    apply_cop.click()
    time.sleep(5)


def test_women():
    driver = webdriver.Chrome()
    driver.get(home_path_wmn)
    home_womn = driver.find_element(By.XPATH, hm_wmn_pth)
    home_womn.click()
    # time.sleep(2)

    pro_womn = driver.find_element(By.XPATH, mwn_pro_path)
    pro_womn.click()
    # time.sleep(2)

    product_name_women = driver.find_element(By.XPATH, pro_name_path_wmn)
    women_product_name = product_name_women.text
    expect = "Blue Denim Shorts"
    assert women_product_name == expect

    add_womn = driver.find_element(By.XPATH, str_btn_path_wmn)
    add_womn.click()
    # ime.sleep(2)
    price_women = driver.find_element(By.XPATH, price_wmn_path)
    price = price_women.text
    assert price == "130.00 ₪"
    time.sleep(2)

    cart_store = driver.find_element(By.XPATH, cpn_wmn_crt_path)
    cart_store.click()
    copon = driver.find_element(By.XPATH, wmn_cpn_field)
    copon.clear()
    copon.send_keys(By.NAME, "123456kl")
    apply_cop = driver.find_element(By.XPATH, wmn_apply_path)
    apply_cop.click()
    time.sleep(5)


def test_accessories():
    driver = webdriver.Chrome()
    driver.get(home_path_acc)
    cate_home = driver.find_element(By.XPATH, hm_acc_pth)
    cate_home.click()
    # time.sleep(2)

    pro_cate = driver.find_element(By.XPATH, acc_pro_path)
    pro_cate.click()

    product_name_category = driver.find_element(By.XPATH, pro_name_path_acc)
    category_product = product_name_category.text
    expected_result = "Boho Bangle Bracelet"
    assert category_product == expected_result
    # time.sleep(2)

    add_cate = driver.find_element(By.XPATH, str_btn_path_acc)
    add_cate.click()

    price_black_yellow_shoes = driver.find_element(By.XPATH, price_acc_path)
    price = price_black_yellow_shoes.text
    assert price == "45.00 ₪"
    time.sleep(2)

    cart_store = driver.find_element(By.XPATH, cpn_acc_crt_path)
    cart_store.click()
    copon = driver.find_element(By.XPATH, acc_cpn_field)
    copon.clear()
    copon.send_keys(By.NAME, "123456kl")
    apply_cop = driver.find_element(By.XPATH, acc_apply_path)
    apply_cop.click()
    time.sleep(5)


def test_search_product():
    driver = webdriver.Chrome()
    driver.get(home_path)
    src = driver.find_element(By.XPATH, search_btn_locator)
    src.click()
    enter_pro = driver.find_element(By.TAG_NAME, Insert_product_locator)
    enter_pro.clear()
    enter_pro.send_keys("Anchor Bracelet")
    time.sleep(2)
    search_btn = driver.find_element(By.XPATH, search_product_locator)
    search_btn.click()
    check_name = driver.find_element(By.XPATH, check_locator)
    check = check_name.text
    assert check == "Anchor Bracelet"


