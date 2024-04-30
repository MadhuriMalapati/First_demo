import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup():
    driver=webdriver.Chrome()
    driver.get("https://edwheel.com/index.php/flight-reservation-sample-page/")
    yield driver
    print(" program ended")


