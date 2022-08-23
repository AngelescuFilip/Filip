
from selenium.webdriver import ActionChains
from MainFunctionality import MainFunctionality
from selenium.webdriver.common.by import By

class Buttons:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def double_click(self):
        source = self.driver.find_element(By.ID, 'doubleClickBtn')
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        self.main.check_value(".//p[@id='doubleClickMessage']")

    def right_click(self):
        source = self.driver.find_element(By.ID, 'rightClickBtn')
        action = ActionChains(self.driver)
        action.context_click(source).perform()
        self.main.check_value(".//p[@id='rightClickMessage']")

    def click(self):
        self.main.xpath_click("//button[text()='Click Me']")
        self.main.check_value(".//p[@id='dynamicClickMessage']")
