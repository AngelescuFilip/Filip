
from MainFunctionality import MainFunctionality

class Radio_Button:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def press_radio_button(self, name):
        lname = name.lower()
        string = ".//label[@class='custom-control-label' and @for='" + lname + "Radio']"
        self.main.xpath_click(string)

    def check_radio_value(self, name):
        lname = name.lower()
        string = "//div[@id='result']//span[text()='" + lname + "']"
        self.main.check_value(string)

    def check_radio_button_status(self, name):
        lname = name.lower()
        string = ".//input[@type='radio' and @id='" + lname + "Radio']"
        self.main.check_status(string)