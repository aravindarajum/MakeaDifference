import os
import time
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from utils.utilities import Utilities


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()

    def scroll_to_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info(f"Scrolled to the element {locator}")
            time.sleep(2)  # Wait to ensure the page has finished scrolling
        except Exception:
            self.log.error(f"Element NOT found, NOT scrolled to element {locator}")

    def click_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            element.click()
            self.log.info(f"Clicked on the element {locator}")
        except Exception:
            self.log.error(f"Element could not me clicked {locator}")

    def wait_until_element_present(self,locator):
        try:
            element = self.driver.find_element(*locator)
            self.log.info(f"Element found {locator}")
        except Exception:
            self.log.error(f"Element NOT found {locator}")

    def fill_form_element(self,locator):
        try:
            element = self.driver.find_element(*locator)
            self.log.info(f"Value filled in {locator}")
            return element
        except Exception:
            self.log.error(f"Element could not me clicked {locator}")

    def capture_screenshot(self,name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshots/{name}_{timestamp}.png"
        os.makedirs(os.path.dirname(screenshot_name), exist_ok=True)
        self.driver.save_screenshot(screenshot_name)
        self.log.info(f"Screenshot captured: {screenshot_name}")
