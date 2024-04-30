import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Selenium.Selenium_class1 import launch_browser

driver = launch_browser("chrome")

driver.maximize_window()
driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()
print("Title of open page is: ", driver.title)
# driver.implicitly_wait(10)
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located(By.ID, "name"))
#handling cookie information
time.sleep(10)
try:
    reject_all_button = driver.find_element(By.XPATH, "(//button[contains(text(), 'Reject All')])[1]")
    reject_all_button.click()
    print("Clicked 'Reject ALL' button in privacy pop-up")
except Exception as e:
    print(f"error: {e}")
