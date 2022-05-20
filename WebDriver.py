import os
from selenium import webdriver

def set_chrome_options(chromeBinaryPath):
    options = webdriver.ChromeOptions()
    options.binary_location = chromeBinaryPath
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-gp")

    return options


def create_webdriver(chromeBinaryPath):
    # Get current dir + chromedriver name
    chrome_driver_path = os.path.dirname(
        os.path.abspath(__file__)) + r"\chromedriver.exe"

    return webdriver.Chrome(chrome_driver_path, chrome_options=set_chrome_options(chromeBinaryPath))