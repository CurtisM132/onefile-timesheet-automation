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
        sleep(1)


def create_journal_entry(driver, title, desc, category, dateStr):
    print("Creating learning journal entry ({0})".format(dateStr))
    print("Note that you must manually input the date and learning criteria")

    driver.get("https://learning.onefile.co.uk/")
    sleep(1)

    # Click the new journal entry button/div
    driver.find_element_by_xpath("//*[contains(text(),'add a new journal entry')]").click()
    sleep(0.5)

    # Title
    titleEl = driver.switch_to.active_element
    titleEl.send_keys(title)

    # Description (aka Reflection)
    descEl = driver.find_element_by_class_name("creation-input")
    descEl.click()
    descEl.clear()
    descEl.send_keys(desc)

    # Date
    # timeInputsContainer = driver.find_element_by_class_name(
    #     "date-time-picker-block")
    # timeInputs = timeInputsContainer.find_elements_by_tag_name("input")
    # # Date
    # timeInputs[0].send_keys(dateStr)

    # Start Time
    timeEl = driver.find_elements_by_class_name("ngb-tp-hour")
    hourInputEl = timeEl[0].find_element_by_tag_name("input")
    hourInputEl.click()
    hourInputEl.send_keys("09")
    timeEl = driver.find_elements_by_class_name("ngb-tp-minute")
    minuteInputEl = timeEl[0].find_element_by_tag_name("input")
    minuteInputEl.click()
    minuteInputEl.send_keys("0")

    # Duration
    timeEl = driver.find_elements_by_class_name("ngb-tp-hour")
    hourInputEl = timeEl[1].find_element_by_tag_name("input")
    hourInputEl.click()
    hourInputEl.send_keys("8")
    timeEl = driver.find_elements_by_class_name("ngb-tp-minute")
    minuteInputEl = timeEl[1].find_element_by_tag_name("input")
    minuteInputEl.click()
    minuteInputEl.send_keys("0")

    # Timesheet Category
    driver.find_element_by_tag_name("mat-select").click()
    driver.find_element_by_xpath("//*[contains(text(),'{0}')]".format(category)).click()


if __name__ == "__main__":
    date = date.today().strftime("%d/%m/%Y")
    if len(sys.argv) >= 2:
        try:
            datetime.strptime(sys.argv[1], '%d/%m/%Y')
            date = sys.argv[1]
        except ValueError:
            print("Incorrect date format, should be DD/MM/YYYY. Using {0} instead".format(date))

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

    print("Creating web driver")
    driver = create_webdriver(formDetails.get_chrome_binary_path(), headless=False)

    # Navigate to the OneFile website
    print("Navigating to: https://live.onefile.co.uk")
    driver.get("https://live.onefile.co.uk")

    sign_in(driver, username, password)
    open_portfolio(driver)
    
    while True:
        create_journal_entry(
            driver, 
            formDetails.get_title(), 
            formDetails.get_description(),
            formDetails.get_category(),
            date
        )
        input()

    # print("Finished, closing web driver")
    # driver.close()
    
    # print("Exiting")
    # sys.exit()