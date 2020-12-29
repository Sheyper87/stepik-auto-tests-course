from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)
option1 = browser.find_element_by_id('robotCheckbox')
option1.click()
option2 = browser.find_element_by_id('robotsRule')
option2.click()
option3 = browser.find_element_by_class_name('btn.btn-primary')
option3.click()




