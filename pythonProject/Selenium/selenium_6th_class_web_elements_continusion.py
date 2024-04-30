import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Selenium.Selenium_class1 import launch_browser

driver=launch_browser("chrome")
driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()
#handling switch button
driver.find_element(By.ID,"switchWindowButton").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
#swicth tab button
driver.find_element(By.ID,"switchTabButton").click()
#driver.switch_to.window(driver.window_handles)
#handling alerts
driver.find_element(By.CSS_SELECTOR,"#nameTextbox").send_keys("Ambalika")
driver.find_element(By.XPATH,"//button[text()='Alert']").click()


alert_box=driver.switch_to.alert
alert_box_text=alert_box.text
print(alert_box_text)
#when alert box has ok buttton
alert_box.accept()
# if alert box has cancel button
# alert_box.dismiss()
# if alert box has cancel button
# alert_box.dismiss()
# Handling mouse hovers
# using Action class - Advanced user Interactions
action=ActionChains(driver)
action.click_and_hold(driver.find_element(By.ID,"mouseHoverButton")).perform()
action.context_click(driver.find_element(By.ID,"mouseHoverButton")).perform()
#action.drag_and_drop(driver.find_element(By.ID, "mouseHoverButton")).perform()
#handling iframe
driver.find_element(By.ID,"toggleIframeButton").click()
time.sleep(5)
driver.switch_to.frame("exampleIframe")
time.sleep(10)
#hide and show button
driver.find_element(By.ID, "hideShowButton").click()
time.sleep(5)
