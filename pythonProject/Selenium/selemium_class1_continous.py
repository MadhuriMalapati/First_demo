import time

from selenium.webdriver.common.by import By

from Selenium.Selenium_class1 import launch_browser

chrome_browser=launch_browser("chrome")
chrome_browser.get("https://edwheel.com/index.php/selenium-practice/")
chrome_browser.maximize_window()
print("The title of the url is :",chrome_browser.title)


# Locators in any test automation
# generic locators in Selenium - ID, Name, ClassName, Linktext, partial linktext, tag
# special locators - css selectors, xpaths
chrome_browser.find_element(By.ID,"name").send_keys("Manasi")
chrome_browser.find_element(By.NAME,"name").clear()
chrome_browser.find_element(By.NAME,"name").send_keys("lovely")


header_text=chrome_browser.find_element(By.CLASS_NAME,"title-post").text
print(header_text)
chrome_browser.find_element(By.LINK_TEXT,"Sample Link").click()
chrome_browser.find_element(By.PARTIAL_LINK_TEXT,"Sample").click()
time.sleep(5)

#Css selectors
# 1 - using css selector to locate an element by id
button =chrome_browser.find_element(By.CSS_SELECTOR,"#resetButton").text
print(button)
# 2 - using css selector to locate an element by class
hidden_text=chrome_browser.find_element(By.CSS_SELECTOR,".entry-title").text
print(hidden_text)
# 3. using css selector by tag and class; syntax = tag.class value
new=chrome_browser.find_element(By.CSS_SELECTOR,"h1.entry-title").text
print(new)
#4.using css selector to locate an element by tag and attribute; syntax = tag[attribute=value]
new_one=chrome_browser.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys("Abs@gmail.com")
time.sleep(5)
chrome_browser.close()