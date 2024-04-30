import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import variables

import common_methods as em

from the_internet_herokapp.object_repository import checkboxes_link, checkboxselect_click, checkbox_heading, \
    context_menu_link, context_menu_heading,  disapper_elemtns_link

driver = em.launch_browser(variables.browserName)

driver.maximize_window()
driver.get(variables.appURL)

def abtesting():
    driver.find_element(By.LINK_TEXT, "A/B Testing").click()
    headertext = driver.find_element(By.TAG_NAME, "h3").text

    print("Header text is: ", headertext)
    pageContent = driver.find_element(By.XPATH, "//p[contains(text(),'split')]").text
    print("Page content is: ", pageContent)
    driver.back()


def addRemoveElement():
    add_remove_elements_link = driver.find_element(By.LINK_TEXT, "Add/Remove Elements")
    add_remove_elements_link.click()
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()
    print("Added an element!")
    time.sleep(1)
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_button.click()
    print("Deleted the element!")
    time.sleep(1)
    driver.back()

def basic_auth():
    basic_auth_link=driver.find_element(By.LINK_TEXT,"Basic Auth")
    basic_auth_link.click()
    time.sleep(2)
    user="admin"
    password="admin"
    authentic_url="https://admin:admin@the-internet.herokuapp.com/basic_auth"
    driver.get(authentic_url)
    #auth_url = f"https://{username}:{password}@{url.split('//')[1]}"
    time.sleep(2)
    if "Congratulations! You must have the proper credentials." in driver.page_source:
        print("Authentication Successful! You have access to the page.")
    else:
        print("Error in the credentials")

    driver.back()
    time.sleep(5)

def Broken_images():
    driver.get(variables.appURL)
    broken_images_link=driver.find_element(By.LINK_TEXT,"Broken Images")
    broken_images_link.click()
    print("broken images link opened successfullly")

    driver.back()


def challenging_dom():
    challenging_dom_link=driver.find_element(By.LINK_TEXT,"Challenging DOM")
    challenging_dom_link.click()
    dom_header_text=driver.find_element(By.TAG_NAME,"h3").text
    print(dom_header_text)
    dom_paragraph=driver.find_element(By.XPATH,"//p[contains(text(),'automated')]").text
    first_button_click=driver.find_element(By.XPATH,"(//a)[2]").click()
    time.sleep(5)
    first_button_text=driver.find_element(By.XPATH,"(//a)[2]").text
    print(first_button_text)
    element_selection=driver.find_element(By.CSS_SELECTOR,".large-10 table tbody tr:nth-child(1) td:nth-child(1)").text
    print(element_selection)
    driver.back()
def check_boxes():
    driver.find_element(By.LINK_TEXT,checkboxes_link).click()
    time.sleep(5)
    heading=driver.find_element(By.TAG_NAME,checkbox_heading).text
    print(heading)
    driver.find_element(By.XPATH,checkboxselect_click).click()
    driver.back()

def context_menu():
    driver.find_element(By.XPATH,context_menu_link).click()
    heading_context=driver.find_element(By.TAG_NAME,context_menu_heading).text
    print(heading_context)
    context_menu_paragraph=driver.find_element(By.XPATH,"(//p)[1]").text
    print(context_menu_paragraph)
    action = ActionChains(driver)
    action.context_click(driver.find_element(By.CSS_SELECTOR,"#hot-spot")).perform()
    print("right click done succesffully")
    alert_box=driver.switch_to.alert
    alert_text=alert_box.text
    alert_box.accept()
    print("allert box clicked sucessfully")
    time.sleep(5)
    action.send_keys(Keys.ESCAPE).perform()




def Digest_authentication():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"Digest Authentication").click()
    driver.refresh()
    time.sleep(5)

    print("diegst opend succesffuly")
    driver.back()

def disapper_elements():
    driver.find_element(By.LINK_TEXT,disapper_elemtns_link).click()
    driver.refresh()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.back()

def drag_drop():
    driver.find_element(By.LINK_TEXT,"Drag and Drop").click()
    # time.sleep(10)
    # print("drag and drop opned")
    drag_from=driver.find_element(By.CSS_SELECTOR,"#column-a")
    drag_to=driver.find_element(By.CSS_SELECTOR,"#column-b")
    action=ActionChains(driver)
    action.drag_and_drop(drag_from,drag_to).perform()
    time.sleep(5)
    driver.back()

def drop_down():
    driver.find_element(By.LINK_TEXT,"Dropdown").click()
    drop_down=driver.find_element(By.ID,"dropdown")
    select_dropdown=Select(drop_down)
    select_dropdown.select_by_index(1)
    select_dropdown.select_by_value("2")
    time.sleep(5)
    driver.back()

def dynamic_content():
    driver.find_element(By.LINK_TEXT,"Dynamic Content").click()
    driver.refresh()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    #to make the content static
    driver.find_element(By.LINK_TEXT,"click here").click()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    # driver.refresh()
    # time.sleep(5)
    driver.back()


def dynamic_control():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"Dynamic Controls").click()
    #enable and disable
    dynamic_enable_disable=driver.find_element(By.XPATH,"//button[text()='Enable' or text()='disable']").click()
    time.sleep(10)
    dynamic_text_msg=driver.find_element(By.XPATH,"//p[@id='message']").text
    print(dynamic_text_msg)
    dynamic_enable_add_remove=driver.find_element(By.XPATH,"//button[text()='add' or text()='Remove']").click()
    time.sleep(5)
    driver.back()

def dynamic_loading():
    driver.find_element(By.LINK_TEXT,"Dynamic Loading").click()
    example1_link=driver.find_element(By.LINK_TEXT,"Example 1: Element on page that is hidden").click()
    start_link=driver.find_element(By.XPATH,"//button[text()='Start']").click()
    hidden_element=driver.find_element(By.XPATH,"//div[@id='finish']/h4").get_property("h4")
    print(hidden_element)
    time.sleep(5)
    driver.back()

def entry_ad():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"Entry Ad").click()
    model_heading=driver.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text
    print(model_heading)
    #time.sleep(5)
    wait=WebDriverWait(driver,10)
    element=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[text()='Close']")))
    element.click()
    time.sleep(5)
    #driver.find_element(By.CSS_SELECTOR,"div[class='modal-footer'] p").click()
    #re-enable the pop up
    driver.find_element(By.XPATH,"//a[text()='click here']").click()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.back()

def exit_intent():
    driver.find_element(By.LINK_TEXT,"Exit Intent").click()
    time.sleep(5)
    driver.back()

def file_download():
    driver.find_element(By.LINK_TEXT,"File Download").click()
    heading_filedownload=driver.find_element(By.TAG_NAME,"h3").text
    print(heading_filedownload)
    #download_file=driver.find_element(By.XPATH,"//a[text()='logo.jpg']")
    download_file=driver.find_element(By.XPATH,"(//div[@class='example']/a)[2]")
    download_file.click()
    time.sleep(5)
    driver.back()

def file_upload():
    driver.find_element(By.LINK_TEXT,"File Upload").click()
    time.sleep(5)
    choose_file=driver.find_element(By.ID,"file-upload")
    choose_file.send_keys("C:\\Users\\madhu\\Downloads\\logo.jpg")
    driver.find_element(By.ID,"file-submit").click()
    time.sleep(5)
    driver.back()

def floating_menu():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"Floating Menu").click()
    driver.execute_script("window.scrollTo(0,5000);")
    time.sleep(5)
    driver.back()

def forgot_pwd():
    driver.find_element(By.LINK_TEXT,"Forgot Password").click()
    time.sleep(2)
    driver.find_element(By.ID,"email").send_keys("Spport@gmail.com")
    driver.find_element(By.ID,"form_submit").click()
    time.sleep(5)
    driver.back()

def form_authentication():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"Form Authentication").click()
    authentication_heading=driver.find_element(By.TAG_NAME,"h2").text
    print(authentication_heading)
    time.sleep(10)
    #login page
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, ".radius").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".button ").click()
    time.sleep(5)




def status_codes():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT, "Status Codes").click()
    driver.find_element(By.XPATH, "(//ul/li/a)[2]").click()
    time.sleep(5)
    textcode_forcodes = driver.find_element(By.XPATH, "//p").text
    print(textcode_forcodes)
    driver.find_element(By.XPATH, "//a[text()='here']").click()
    time.sleep(5)
    driver.back()

def hovers():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT, "Hovers").click()
    action = ActionChains(driver)
    element_to_hover = (driver.find_element(By.XPATH, "(//img[@src='/img/avatar-blank.jpg'])[3]"))
    action.move_to_element(element_to_hover).perform()
    time.sleep(5)
    element_text = driver.find_element(By.XPATH, "(//h5)[3]").text
    print(element_text)
    driver.back()

def notifications_msg():
    driver.find_element(By.LINK_TEXT,"Notification Messages").click()
    time.sleep(3)
    # msg_text=driver.find_element(By.CSS_SELECTOR,"#flash").text()
    driver.find_element(By.CSS_SELECTOR,".close").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[text()='Click here']").click()
    time.sleep(5)
    driver.back()

def multiple_windows():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,".example a").click()
    driver.switch_to.window(driver.window_handles[1])

    print(driver.title)
    driver.switch_to.window(driver.window_handles[0])
    driver.back()

def securefile_downlaod():

    driver.find_element(By.LINK_TEXT, "Secure File Download").click()
    user = "admin"
    password = "admin"
    secred_url = "https://admin:admin@the-internet.herokuapp.com/download_secure"
    driver.get(secred_url)

    # auth_url = f"https://{username}:{password}@{url.split('//')[1]}"

    time.sleep(5)
    if "download_secure" in driver.current_url:
            # print("Authentication Successful! You have access to the page.")
        download_securefile = driver.find_element(By.XPATH, "(//div[@class='example']/a)[2]")
        download_securefile.click()
    else:
        print("Error in the credentials")
    driver.back()

def javascript_alerts():
    driver.get(variables.appURL)
    driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert_box = driver.switch_to.alert
        # alert_botext=driver.find_element(By.CSS_SELECTOR,"#result").get_attribute("h4")
    alert_box.accept()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert_box.dismiss()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert_box.send_keys("1234rtfb")
    time.sleep(3)
    alert_box.accept()
    time.sleep(3)
    driver.back()


    # Confirm deletion by checking if the "Delete" button is no longer present
    #assert not driver.find_elements(By.XPATH, "//button[text()='Delete']"), "Element deletion failed!"

    #print("Automation successful!")




# TC1 - A/B Testing
abtesting()

#TC2 - Add Remove Elements
addRemoveElement()

#TC3 - basic-auth
basic_auth()

#Tc4
Broken_images()

#Tc5
challenging_dom()
#Tc6
check_boxes()

#Tc7
context_menu()

#Tc8
Digest_authentication()

#Tc9
disapper_elements()

#Tc10
drag_drop()

#Tc11
drop_down()

#Tc12
dynamic_content()

#Tc13
dynamic_control()

#Tc14
dynamic_loading()

#Tc15
entry_ad()

#Tc16
exit_intent()

#Tc17
file_download()

#Tc18
file_upload()

#Tc19
floating_menu()

#Tc20
forgot_pwd()

#Tc 21
form_authentication()


#Tc 22
status_codes()

#Tc 23
hovers()

#Tc 24
notifications_msg()

#Tc 25
multiple_windows()

#Tc 26
securefile_downlaod()

#Tc 27
javascript_alerts()

#Tc 28
