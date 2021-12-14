import os
import sys
from datetime import date, datetime, timedelta
from time import sleep

from WebDriver import create_webdriver
from FormDetails import JSONFormDetails


def sign_in(driver, username, password):
    driver.find_element_by_xpath("//input[@id='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='Password']").send_keys(password)

    driver.find_element_by_xpath("//input[@type='submit']").submit()


def open_portfolio(driver):
    portfolios = driver.find_elements_by_class_name(
        "account-list-item-details")
    if len(portfolios) > 0:
        portfolios[0].click()


def create_timesheet(driver, timesheetDescription, timesheetCategory, dateStr):
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

    # Time Inputs
    timeInputsContainer = driver.find_element_by_class_name(
        "date-time-picker-block")
    timeInputs = timeInputsContainer.find_elements_by_tag_name("input")
    # Date
    timeInputs[0].send_keys(dateStr)
    # Start Time
    timeInputs[1].send_keys("09:00")

    # Duration Inputs
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
    currentDate = date.today().strftime("%d/%m/%Y")
    if len(sys.argv) >= 2:
        try:
            datetime.strptime(sys.argv[1], '%d/%m/%Y')
            currentDate = sys.argv[1]
        except ValueError:
            print("Incorrect date format, should be DD/MM/YYYY. Using {0} instead".format(currentDate))

    formDetails = JSONFormDetails()
    formDetails.load_json_details()
        
    # Get sign in details
    username = formDetails.get_username()
    if username == "":
        print("No Username, execution terminated")
        exit()

    password = formDetails.get_password()
    if password == "":
        print("No Password, execution terminated")
        exit()

    timesheetDescription = formDetails.get_timesheet_description()
    timesheetCategory = formDetails.get_timesheet_category()

    driver = create_webdriver()

    # Navigate to the OneFile website
    driver.get("https://live.onefile.co.uk")

    sign_in(driver, username, password)
    open_portfolio(driver)
    create_timesheet(driver, timesheetDescription, timesheetCategory, currentDate)

    driver.close()
