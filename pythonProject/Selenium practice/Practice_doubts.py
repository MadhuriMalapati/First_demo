import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium.Selenium_class1 import launch_browser

# driver=launch_browser("chrome")
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT,"Form Authentication").click()
# Username = "tomsmith"
# Password = "SuperSecretPassword!"
# auth_url = "https://tomsmith:SuperSecretPassword!@the-internet.herokuapp.com/login"
# driver.get(auth_url)
# time.sleep(10)
# driver.find_element(By.XPATH,"//button[@class='radius']").click()
#     # auth_url = f"https://{username}:{password}@{url.split('//')[1]}"
# time.sleep(2)
# if "secure" in driver.current_url:
#     print("Login and Logout successful")
# else:
#     print("invalid credentials")
#     time.sleep(5)


# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Status Codes").click()
# elements=driver.find_element(By.CSS_SELECTOR,".example ul li")
# for element in elements:
#     new_element=driver.find_element(element)
#     print(new_element)
#     # time.sleep(5)
# ------------
# def jquery_ui():
#     driver.find_element(By.LINK_TEXT,"JQuery UI Menus").click()
#     #link
#     driver.find_element(By.XPATH,"//p/a[text()='JQuery UI Menus']").click()
#     time.sleep(3)
#     driver.back()
#     enabled=driver.find_element(By.XPATH,"(//ul[@id='menu']/li[2]/a)")
#     enabled.click()
#     driver.implicitly_wait(5)
#     #downlaods option code
#     # downloads=driver.find_element(By.XPATH,"//li[@id='ui-id-4'] /a[text()='Downloads']")
#     # downloads.click()
#     # driver.implicitly_wait(5)
#     # file_click=driver.find_element(By.XPATH,"//a[contains(text(),'Excel')]")
#     # file_click.click()
#     #jquey option code
#     driver.find_element(By.XPATH,"//a[text()='Back to JQuery UI']").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH,"//a[text()='JQuery UI']").click()
#     time.sleep(3)
#     driver.back()
#     driver.find_element(By.XPATH,"//a[text()='Menu']").click()
#     time.sleep(5)
#
# jquery_ui()


# def challenging_dom():
#     challenging_dom_link=driver.find_element(By.LINK_TEXT,"Challenging DOM")
#     challenging_dom_link.click()
#     dom_header_text=driver.find_element(By.TAG_NAME,"h3").text
#     print(dom_header_text)
#     dom_paragraph=driver.find_element(By.XPATH,"//p[contains(text(),'automated')]").text
#     first_button_click=driver.find_element(By.XPATH,"(//a)[2]").click()
#     time.sleep(10)
#     first_button_text=driver.find_element(By.XPATH,"(//a)[2]").text
#     print(first_button_text)
#     element_selection=driver.find_element(By.CSS_SELECTOR,".large-10 table tbody tr:nth-child(1) td:nth-child(1)").text
#     print(element_selection)
#     driver.back()
#
# challenging_dom()

def key_presses():
    driver.find_element(By.LINK_TEXT,"Key Presses").click()
    time.sleep(5)
    key_elements=driver.find_element(By.CSS_SELECTOR,"#target")
    #TAB
    key_elements.send_keys(Keys.ESCAPE)

    key_elements.send_keys(Keys.ENTER)

    key_elements.send_keys(Keys.ALT)


    # text_sene=driver.find_element(By.XPATH,"//p[@id='result']").text
    # print(text_sene)
    #
    # print(text_sene)

key_presses()
