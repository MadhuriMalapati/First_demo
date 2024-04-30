from selenium import webdriver


def launch_browser(browser):
    if browser == "chrome":
       driver  = webdriver.Chrome()
    elif browser == "firefox":
        driver =webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Not selected the correct browser.Setting it to default chrome browser")
        driver = webdriver.Chrome()
    return driver
# def open_application(browserdriver,url):
#     browserdriver.get(url)
#     return browserdriver



