import time

from selenium.webdriver.common.by import By

from Selenium.Selenium_class1 import launch_browser

driver=launch_browser("chrome")
driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Neeru")
driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@name='email']").clear()

# 1. Node Selection:
# /: selects from the root node (absolute path)
# //: selects nodes anywhere in the document (Relative xpath)

# 2. Element selection:
# tagname: selects all elements witht he specified tag name
print("The count of elemnets is",driver.find_element(By.XPATH,"//input"))
# 3. *: selects any element
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("meena")
# 4. Attribute selection:
# [@attibute = 'value'] : selects element with a specific attribute and its value
driver.find_element(By.XPATH, "//input[@id='name']").clear()
# 5. Indexing:
driver.find_element(By.XPATH,"//input[6]").send_keys("abc@gmail.com")
time.sleep(5)


# 6. Conditions (and, or)
driver.find_element(By.XPATH, "//button[text()='Alert' or text()='Reset']").click()

# selecting by text:
# text() - selects element with exact text
# contain(text(),"sub") - selects elements containing the text part

driver.find_element(By.XPATH, "//button[contains(text(),'Ale')]").click()

time.sleep(5)
