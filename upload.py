import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators import Locators
from user import UserClass
import os
from selenium.webdriver.common.keys import Keys

""" Upload photos to instagram"""

class BasePostGenerator():

    def __init__(self, driver):

        self.driver = driver

    @staticmethod
    def time_execution():

        time.sleep(1.5)

    def start_connection(self, executable_path):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(Locators.MOBILE_ARGUMENT)
        self.driver = webdriver.Chrome(f'{executable_path}', options=chrome_options)

    def get_website(self, url):

        self.driver.get(f'{url}')

    def click_element(self, element, form=None):

        self.time_execution()

        if form == 'xpath' or form == None:

            element_xpath = self.driver.find_element_by_xpath(element)
            element_xpath.click()

        self.time_execution()
            

    def send_keys_to_element(self, element, keys, form=None):

        self.time_execution()

        if form == 'xpath' or form == None:

            element_xpath = self.driver.find_element_by_xpath(element)
            element_xpath.send_keys(keys)


    def send_file_to_element(self, element, file):

        self.driver.find_element_by_xpath(element).send_keys('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Ft Project\\images\\{}.jpg'.format(file))

    def get_rid_of_popup(self):

        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    @staticmethod
    def wait_upload_to_complete():

        time.sleep(8)

class PostGenerator(BasePostGenerator):

    def __init__(self, driver):

        super().__init__(driver)

    def upload_photo(self, file_name, phrase):

        self.start_connection(self.driver)

        self.get_website(Locators.MAIN_PAGE)

        self.click_element(Locators.MAIN_PAGE_ENTER_BUTTON)

        user = UserClass()

        username, password = user.get_user_and_password()

        self.send_keys_to_element(Locators.USERNAME_INPUT, username)

        self.send_keys_to_element(Locators.PASSWORD_INPUT, password)

        self.driver.maximize_window()

        self.click_element(Locators.CLOSE_BLACK_BAR)

        self.click_element(Locators.ENTER_BUTTON_LOGIN)

        self.click_element(Locators.NOT_NOW)

        self.click_element(Locators.DONT_INITIAL_PAGE)

        self.click_element(Locators.CLOSE_BLACK_BAR)

        self.click_element(Locators.BUTTON_TO_UPLOAD_A_FILE)

        self.send_file_to_element(Locators.SEND_FILE, f'{file_name}')

        self.click_element(Locators.ADVANCE_BUTTON)

        self.send_keys_to_element(Locators.LEGEND_INPUT, f'{phrase}')

        self.click_element(Locators.SHARE_BUTTON)

        self.wait_upload_to_complete()

        self.driver.close()