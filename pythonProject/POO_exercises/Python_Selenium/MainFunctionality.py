
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainFunctionality:

    def __init__(self):
        self.driver = None
        self.website = None
        self.item = None

    def start_server(self, website):
        self.website = website
        s = Service(r'C:/Users/Dim/PycharmProjects/webdrivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(self.website)

    def xpath_click(self, xpath):
        self.item = self.driver.find_element(By.XPATH, xpath)
        self.item.click()

    def id_click(self, id):
        self.item = self.driver.find_element(By.ID, id)
        self.item.click()

    def css_click(self, css):
        self.item = self.driver.find_element(By.CSS_SELECTOR, css)
        self.item.click()

    def click_and_key(self, xpath, name):
        self.xpath_click(xpath)
        self.item.send_keys(name)

    def key_delete(self, xpath):
        self.xpath_click(xpath)
        self.item.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def check_value(self, xpath):
        try:
            self.item = self.driver.find_element(By.XPATH, xpath)
            print(self.item.is_displayed())
        except:
            print('False')

    def check_title(self, name):

        string = ".//div[text()='" + name + "']"
        try:
            self.item = self.driver.find_element(By.XPATH, string)
            return print('Title is correct')
        except:
            return print('Title is wrong')

    def check_status(self, xpath):
        self.item = self.driver.find_element(By.XPATH, xpath)
        if self.item.is_enabled():
            return print('Enabled')
        else:
            return print('Disabled')