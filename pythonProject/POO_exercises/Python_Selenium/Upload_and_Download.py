
from MainFunctionality import MainFunctionality
from selenium.webdriver.common.by import By

class Upload_and_Download:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def download(self):
        self.main.xpath_click("//a[text()='Download']")
