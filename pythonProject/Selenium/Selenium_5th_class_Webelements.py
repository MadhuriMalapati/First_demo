import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Selenium.Selenium_class1 import launch_browser

driver=launch_browser("chrome")
driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()
title=driver.title
print(title)
#cookie handling
time.sleep(10)
reject_all=driver.find_element(By.XPATH,"(//button[contains(text(), 'Reject All')])[1]")
reject_all.click()
print("Reject button clicked")
driver.find_element(By.ID,"name").send_keys("Neerus")
driver.find_element(By.ID,"email").send_keys("vithika@gmail.com")
#handling drop down in 3 ways
dropdownobejct=driver.find_element(By.ID,"dropdown")
select_dropdwon=Select(dropdownobejct)
#1
select_dropdwon.select_by_index(1)
#2
select_dropdwon.select_by_value("DPValue1")
#3
select_dropdwon.select_by_visible_text("DPValue 3")
#handling check boxes
driver.find_element(By.ID,"chbValue1").click()
#handling button
driver.find_element(By.ID,"resetButton").click()
list_selecion=driver.find_element(By.ID,"listbox")
selected1=Select(list_selecion)
selected1.select_by_value("list1")
selected1.select_by_index(3)
selected1.select_by_visible_text("List 3")
#handling radio button
driver.find_element(By.ID,"radio1").click()
#handling auto-suggestion text box
driver.find_element(By.ID,"countrySuggestion").send_keys("Australia")
# to read a value from any label or webelement
# .text method will not work for dynamic values

elements=driver.find_element(By.ID,"countrySuggestion").text
print("text",elements)
auto_suggest_text1 = driver.find_element(By.ID, "countrySuggestion").get_attribute("value")
print("text from getattribute is: ", auto_suggest_text1)
#using css selector
driver.find_element(By.CSS_SELECTOR,"#countries>option:nth-child(2)").click()
countries=driver.find_element(By.CSS_SELECTOR,"#countries>option")
length=len(countries)
print("Total countires:",len(countries))
