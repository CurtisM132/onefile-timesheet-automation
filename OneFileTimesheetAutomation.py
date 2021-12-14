import json
import os
from datetime import date
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


def get_json_details():
    with open('details.json') as json_file:
        return json.load(json_file)


def set_chrome_options():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

    return options


def create_webdriver():
    # Get current dir + chromedriver name
    chrome_driver_path = os.path.dirname(
        os.path.abspath(__file__)) + r"\chromedriver.exe"

    return webdriver.Chrome(chrome_driver_path, chrome_options=set_chrome_options())


def sign_in(driver, username, password):
    driver.find_element_by_xpath("//input[@id='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='Password']").send_keys(password)

    driver.find_element_by_xpath("//input[@type='submit']").submit()


def open_portfolio(driver):
    portfolios = driver.find_elements_by_class_name(
        "account-list-item-details")
    if len(portfolios) > 0:
        portfolios[0].click()


def create_timesheet_for_today(driver, timesheetDescription, timesheetCategory):
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
    entryInput.send_keys(timesheetDescription)

    # Timesheet Category
    driver.find_element_by_tag_name("select").click()
    driver.find_element_by_xpath("//option[text()='{0}']".format(timesheetCategory)).click()

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
    data = get_json_details()

    driver = create_webdriver()

    # Navigate to the OneFile website
    driver.get("https://live.onefile.co.uk")

    try:
        sign_in(driver, data["username"], data["password"])
    except KeyError:
        print("No Username or Password, execution terminated")
        exit()

    open_portfolio(driver)

    timesheetDescription = "Study Day"
    try:
        timesheetDescription = data["timesheetDescription"]
    except KeyError:
        print("No Timesheet Description, using default of {0}".format(timesheetDescription))

    timesheetCategory = "Assignment preparation & writing"
    try:
        timesheetCategory = data["timesheetCategory"]
    except KeyError:
        print("No Timesheet Category, using default of {0}".format(timesheetCategory))

    create_timesheet_for_today(driver, timesheetDescription, timesheetCategory)

    driver.close()
