import time

from pages.basedriver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.utilities import Utilities
from selenium.webdriver.support import expected_conditions as EC

class EventRegisterConfirmPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        self.register_success_msg = (By.XPATH,"//h2[text()='Thank you! See you soon']")

    def wait_register_success_msg(self):
        self.wait_until_element_present(self.register_success_msg)
