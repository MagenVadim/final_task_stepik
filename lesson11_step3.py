import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get(link)
button = driver.find_element(By.ID, "verify")
button.click()
message = driver.find_element(By.ID, "verify_message")

assert "successful" in message.text
