import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from datetime import date


def set_chrome_options():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--start-maximized")

    return options


def create_webdriver():
    # Get current dir + chromedriver name
    chrome_driver_path = os.path.dirname(
        os.path.abspath(__file__)) + r"\chromedriver.exe"

    return webdriver.Chrome(chrome_driver_path, chrome_options=set_chrome_options())


def sign_in(driver):
    driver.find_element_by_xpath("//input[@id='Username']").send_keys("curtis.martin@warwick.ac.uk")
    driver.find_element_by_xpath("//input[@id='Password']").send_keys("D8iL*_#bwnyTgJ#")

    driver.find_element_by_xpath("//input[@type='submit']").submit()


def open_portfolio(driver):
    portfolios = driver.find_elements_by_class_name(
        "account-list-item-details")
    if len(portfolios) > 0:
        portfolios[0].click()


def create_timesheet_for_today(driver):
    sleep(0.5)
    driver.get("https://live.onefile.co.uk/timesheet/")
    sleep(0.5)

    # Click the new timesheet button
    driver.find_element_by_xpath("//input[@type='submit']").click()
    sleep(0.5)

    # Timesheet Description
    entryInput = driver.find_element_by_xpath("//textarea[@class='formtext']")
    entryInput.click()
    entryInput.clear()
    entryInput.send_keys("Study Day")

    # Timesheet Category
    driver.find_element_by_tag_name("select").click()
    driver.find_element_by_xpath("//option[text()='Assignment preparation & writing']").click()

    timeInputsContainer = driver.find_element_by_class_name(
        "date-time-picker-block")
    timeInputs = timeInputsContainer.find_elements_by_tag_name("input")
    # Date
    timeInputs[0].send_keys(date.today().strftime("%d/%m/%Y"))
    # Start Time
    timeInputs[1].send_keys("09:00")

    # Duration
    timeInputsContainer = driver.find_element_by_xpath(
        "//fieldset[@class='control-grouping']")
    timeInputs = timeInputsContainer.find_elements_by_tag_name("input")
    # Hours
    timeInputs[0].send_keys("5")
    # Minutes
    timeInputs[1].send_keys("0")

    # Save
    driver.find_element_by_xpath("//input[@value='Save']").click()


if __name__ == "__main__":
    driver = create_webdriver()

    # Navigate to the OneFile website
    driver.get("https://live.onefile.co.uk")

    sign_in(driver)
    open_portfolio(driver)
    create_timesheet_for_today(driver)
