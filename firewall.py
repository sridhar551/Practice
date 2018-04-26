from calendar import weekday

import openpyxl
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver = '/home/sree/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)


browser.get('http://172.16.0.1/corporate/webpages/login.jsp')
browser.implicitly_wait(10)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("admin")
password.send_keys("@elsmkpng4600")

browser.find_element_by_name("loginbutton").click()
browser.find_element_by_id("vrReports").click()