from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
search_locator = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Sky")

sleep(3)

search_input.clear()
search_input.send_keys("Pro")
driver.quit()