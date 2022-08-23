
#from PythonSelenium import MyClass
from MainFunctionality import MainFunctionality

class Check_Box:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def check_the_box(self, name):
        string = "//span[.//*[text()='" + name + "'] and @class='rct-text']//span[contains(@class, 'rct-checkbox')]"
        self.main.xpath_click(string)

    def dropdown(self, name):
        string = "//span[.//*[text()='" + name + "'] and @class='rct-text']//button[contains(@class, 'collapse')]"
        self.main.xpath_click(string)

    def check_box_value(self, name):
        lname = name.lower()
        string = ".//div[@id='result']//span[text()='" + lname + "']"
        self.main.check_value(string)