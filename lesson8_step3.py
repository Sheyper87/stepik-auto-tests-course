from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

e1 = browser.find_element_by_id('num1')
e2 = browser.find_element_by_id('num2')
val1 = int(e1.text)
val2 = int(e2.text)
sum = str(val1 + val2)


select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum) # ищем элемент с текстом "Python"

option3 = browser.find_element_by_class_name('btn.btn-default')
option3.click()
