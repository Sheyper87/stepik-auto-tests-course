from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)



input1 = browser.find_element_by_class_name('trollface.btn.btn-primary')
input1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_element = browser.find_element_by_css_selector('.form-group>label>.nowrap:nth-child(2)')
x = x_element.text
y = calc(x)

input2 = browser.find_element_by_id('answer')
input2.send_keys(y)

input3 = browser.find_element_by_tag_name('button')
input3.click()


