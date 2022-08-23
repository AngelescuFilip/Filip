
from MainFunctionality import MainFunctionality
from selenium.webdriver.common.by import By

class Links:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def home(self):
        self.main.id_click('simpleLink')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.main.check_value(".//div[@class='home-content']")

    def initial_page(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

