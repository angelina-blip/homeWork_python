from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_locator = "input[id='username']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_locator1 = "input[id='password']"
search_input1 = driver.find_element(By.CSS_SELECTOR, search_locator1)
search_input.send_keys("tomsmith")
search_input1.send_keys("SuperSecretPassword!")

sleep(2)

button = driver.find_element(By.CSS_SELECTOR, ".fa-sign-in")
button.click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text.strip())

driver.quit()