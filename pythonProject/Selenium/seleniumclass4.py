import time

from selenium.webdriver.common.by import By

from Selenium.Selenium_class1 import launch_browser
driver = launch_browser("chrome")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/challenging_dom")
print("Title of open page is: ", driver.title)
print(driver.find_element(By.CSS_SELECTOR,"#page-footer a").text)
