from pages.basedriver import BaseDriver
from selenium.webdriver.common.by import By

from utils.utilities import Utilities


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()

        self.event_menu = (By.XPATH, "//*[@id='comp-izp8qiib3label']")

    def click_events_menu(self):
        try:
            self.click_element(self.event_menu)
            self.log.info(f"Events menu found {self.event_menu}")
        except Exception:
            self.log.error(f"Events menu not found {self.event_menu}")
