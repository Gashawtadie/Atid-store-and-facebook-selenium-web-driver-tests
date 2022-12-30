import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

home_page_fb = "https://www.facebook.com/login/"
username_field = "//input[@id='email']"
password_field = "//input[@id='pass']"
btn_locator = "//button[@id='loginbutton']"
username_errormessage_locator = "//body/div[@id='u_0_0_/b']/div[@id='globalContainer']/div[""@id='content']/div[1]/div[2]/div[" \
                                "2]/form[1]/div[1]/div[1]/div[2] "
password_errormessage_locator = "//body/div[@id='u_0_0_/b']/div[@id='globalContainer']/div[""@id='content']/div[" \
                                "1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2] "

invalid_username_notyou_cssselector = "body.fbIndex.UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5" \
                                      ".Locale_en_GB.cores-gte4._19_u:nth-child(2) " \
                                      "div._10._9lv3.uiLayer._4-hy._3qw:nth-child(25) div._59s7._9l2g div._4t2a " \
                                      "div:nth-child(1) div._4-i2._pig._9kpl._50f4 div._9kpp:nth-child(6) span._9kpq " \
                                      "> a._39g9 "

error_message_locator_invalidusername = "body._39il._97vt._97vz._97v-._97v_._97w2._97w0._9ax-._9ax_._9ay1" \
                                        ".UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5.Locale_en_GB" \
                                        ".cores-gte4._19_u:nth-child(2) div._li:nth-child(2) " \
                                        "div.uiContextualLayerParent:nth-child(1) div.fb_content.clearfix:nth-child(" \
                                        "1) div._4-u5._30ny div._4-u2._1w1t._4-u8._52jv div.login_form_container " \
                                        "form:nth-child(1) div:nth-child(4) div.clearfix._5466._44mg:nth-child(11) > " \
                                        "div._9ay7 "

error_message_invalipassword = "body._39il._97vt._97vz._97v-._97v_._97w2._97w0._9ax-._9ax_._9ay1" \
                               ".UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5" \
                               ".Locale_en_GB.cores-gte4._19_u:nth-child(2) div._li:nth-child(2) " \
                               "div.uiContextualLayerParent:nth-child(1) " \
                               "div.fb_content.clearfix:nth-child(1) div._4-u5._30ny " \
                               "div._4-u2._1w1t._4-u8._52jv div.login_form_container " \
                               "form:nth-child(1) div:nth-child(4) " \
                               "div.clearfix._5466._44mg:nth-child(12) > div._9ay7:nth-child(2)"

both_empty_locator = "//body/div[@id='u_0_0_R+']/div[@id='globalContainer']/div[""@id='content']/div[1]/div[2]/div[" \
                     "2]/form[1]/div[1]/div[1]/div[2] "

test_invalid_user_pass_error_locator = "body._39il._97vt._97vz._97v-._97v_._97w2._97w0._9ax-._9ax_" \
                                       "._9ay1.UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome" \
                                       ".webkit.win.x1-5.Locale_en_GB.cores-gte4._19_u:nth-child(2) " \
                                       "div._li:nth-child(2) div.uiContextualLayerParent:nth-child(" \
                                       "1) div.fb_content.clearfix:nth-child(1) div._4-u5._30ny " \
                                       "div._4-u2._1w1t._4-u8._52jv div.login_form_container " \
                                       "form:nth-child(1) div:nth-child(4) " \
                                       "div.clearfix._5466._44mg:nth-child(12) > " \
                                       "div._9ay7:nth-child(2)"

# ************************************* Forgot password **********************************************

forgot_password = "Forgotten password?"
not_you_locator = "//a[contains(text(),'Not you?')]"
account_key_locator = "//input[@id='identify_email']"
submit_locator = "did_submit"
click_btn_locatr = "//button[@id='did_submit']"
con_loc = "button"
enter_loc =  "//input[@id='recovery_code_entry']"
confirm_loc = "//button[contains(text(),'Continue')]"
incorrect_email_loc = "//a[contains(text(),'Not you?')]"
fill_mail_loc = "//input[@id='identify_email']"