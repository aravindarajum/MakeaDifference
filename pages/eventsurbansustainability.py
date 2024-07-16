import time

from pages.basedriver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.utilities import Utilities
from selenium.webdriver.support import expected_conditions as EC


class EventsPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()
        self.wait = WebDriverWait(driver,10)
        self.register_button_div = (By.XPATH,"//*[@id='wix-events-widget']/div/div/ul/li[1]/div")
        self.register_button = (By.XPATH,"//*[@id='wix-events-widget']/div/div/ul/li[1]/div/div[2]/div/div/a")
        self.first_name = (By.XPATH,"//*[@id='firstName']")
        self.last_name = (By.XPATH,"//*[@id='lastName']")
        self.email = (By.XPATH,"//*[@id='email']")
        self.phone = (By.XPATH,"//*[@id='phone']")
        self.address = (By.XPATH,"//*[@id='address-0']")
        self.submit_button = (By.XPATH,"//button[normalize-space()='SUBMIT']")
        self.register_success_msg = (By.XPATH,"//h2[text()='Thank you! See you soon']")
        self.gender_male = (By.XPATH,"//div[contains(text(),'Male')]")
        self.gender_female = (By.XPATH,"//div[contains(text(),'Female')]")
        self.music_hobby = (By.XPATH,"//div[text()='Music']")
        self.chess_hobby = (By.XPATH,"//div[text()='Chess']")
        self.crafts_hobby = (By.XPATH,"//div[text()='Crafts']")


    def scroll_to_register_button(self):
        self.wait.until(EC.presence_of_element_located(self.register_button_div))
        self.scroll_to_element(self.register_button_div)
    def click_register_button(self):
        self.click_element(self.register_button)

    def click_submit_button(self):
        self.click_element(self.submit_button)
        time.sleep(3)

    def click_male_radio_button(self):
        self.click_element(self.gender_male)

    def click_female_radio_button(self):
        self.click_element(self.gender_female)

    def wait_register_success_msg(self):
        self.wait_until_element_present(self.register_success_msg)

    def fill_form(self,first_name,last_name,email,phone_num,address,gender,hobbies):
        self.wait.until(EC.presence_of_element_located(self.first_name))

        fname = self.fill_form_element(self.first_name)
        fname.send_keys(first_name)

        lname = self.fill_form_element(self.last_name)
        lname.send_keys(last_name)
        e_mail = self.fill_form_element(self.email)
        e_mail.send_keys(email)
        phone_number = self.fill_form_element(self.phone)
        phone_number.send_keys(phone_num)
        house_address = self.fill_form_element(self.address)
        house_address.send_keys(address)

        if gender == "Male":
            male_radio_button = self.fill_form_element(self.gender_male)
            self.click_element(self.gender_male)
            time.sleep(3)
        elif gender == "Female":
            female_radio_button = self.fill_form_element(self.gender_female)
            self.click_element(self.gender_female)
            time.sleep(3)

        # for hobby in hobbies:
        if hobbies == 'Music':
            hobby_music = self.fill_form_element(self.music_hobby)
            self.click_element(self.music_hobby)

        if hobbies == 'Chess':
            hobby_chess = self.fill_form_element(self.chess_hobby)
            self.click_element(self.chess_hobby)

        if hobbies == 'Crafts':
            hobby_crafts = self.fill_form_element(self.crafts_hobby)
            self.click_element(self.crafts_hobby)












