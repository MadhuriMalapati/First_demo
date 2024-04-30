import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# @pytest.mark.usefixtures("setup")
def test_sampleflightbook(setup):
    print("website opened")
    title_of_page = setup.title
    print(title_of_page)
    setup.maximize_window()
    setup.find_element(By.ID,"from").send_keys("Delhi")
    setup.find_element(By.ID,"to").send_keys("Mumbai")
    setup.find_element(By.ID,"departureDate").send_keys("20-05-2024")
    setup.find_element(By.ID,"returnDate").send_keys("23-05-2024")
    drop_down_currency=setup.find_element(By.ID,"currency")
    select_currency=Select(drop_down_currency)
    select_currency.select_by_value("EUR")
    drop_down_passenger=setup.find_element(By.ID,"passengerCount")
    select_passenger=Select(drop_down_passenger)
    select_passenger.select_by_index(2)
    setup.find_element(By.ID,"seniorCitizen").click()
    time.sleep(5)
    setup.find_element(By.XPATH,"//button[text()='Reserve Flight']").click()
    time.sleep(5)


