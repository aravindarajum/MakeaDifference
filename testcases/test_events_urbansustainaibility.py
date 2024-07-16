import time

import pytest
import softest

from pages.eventregistersuccesspage import EventRegisterConfirmPage
from pages.eventsurbansustainability import EventsPage
from pages.homepage import HomePage
from utils.utilities import Utilities


@pytest.mark.usefixtures("setup")
class TestEventUrbanSustainability(softest.TestCase):
    def test_event_urban_sustainablity_registration(self):
        self.homepage = HomePage(self.driver)
        self.eventurbansustainability = EventsPage(self.driver)
        self.eventregisterconfirm = EventRegisterConfirmPage(self.driver)
        self.utils = Utilities(self.driver)
        self.homepage.click_events_menu()
        self.eventurbansustainability.scroll_to_register_button()
        self.eventurbansustainability.click_register_button()

        for test_data in self.utils.read_data_from_excel('C://Users//Lenovo//PycharmProjects//MakeADifference//testdata//UrbanSustainability_testdata.xlsx','Sheet1'):
            fname,lname,email,phone,address,gender,hobbies = test_data
            self.eventurbansustainability.fill_form(fname,lname,email,phone,address,gender,hobbies)
            # time.sleep(5)
            self.eventurbansustainability.click_submit_button()
            self.eventurbansustainability.wait_register_success_msg()

            self.eventurbansustainability.driver.get('https://aravindaec.wixsite.com/makeadifference/events/panel-paving-the-way-urban-sustainability/form')

