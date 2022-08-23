
from MainFunctionality import MainFunctionality
from selenium.webdriver.common.by import By

class Web_Tables:

    def __init__(self, driver):
        self.driver = driver
        self.item = None
        self.main = MainFunctionality(self.driver)

    def search_by_name(self, name):
        self.main.click_and_key(".//input[@placeholder='Type to search']", name)

    def nr_elements(self):
        rowCount = 0
        args = [".//div[@class='rt-tr -even']", ".//div[@class='rt-tr -odd']"]
        for xpath in args:
            rowCount += len(self.driver.find_elements(By.XPATH, xpath))
        print(rowCount)

    def search_delete(self):
        self.main.key_delete(".//input[@placeholder='Type to search']")

    def modify_web_table(self, name, **keyword):
        self.main.xpath_click("//div[.//*[text()='" + name + "'] and @class='rt-tr-group']//span[@title='Edit']")

        if all(key in ['First_Name', 'Last_Name', 'Email', 'Age', 'Salary', 'Department'] for key in keyword.keys()):
            self.main.key_delete(".//input[@id='lastName']")
            self.main.click_and_key(".//input[@id='lastName']", keyword['Last_Name'])
            self.main.key_delete(".//input[@id='age']")
            self.main.click_and_key(".//input[@id='age']", keyword['Age'])

        self.main.xpath_click(".//button[@id='submit']")

    def add_web_table(self, first_name, last_name, email, age, salary, department):
        self.main.xpath_click(".//button[@id='addNewRecordButton']")
        self.main.click_and_key(".//input[@id='firstName']", first_name)
        self.main.click_and_key(".//input[@id='lastName']", last_name)
        self.main.click_and_key(".//input[@id='userEmail']", email)
        self.main.click_and_key(".//input[@id='age']", age)
        self.main.click_and_key(".//input[@id='salary']", salary)
        self.main.click_and_key(".//input[@id='department']", department)

        self.main.xpath_click(".//button[@id='submit']")

        # string = "//div[text()='" + first_name + "']"
        # self.main.check_value(string)

    def delete_row(self, name):
        self.main.xpath_click("//div[.//*[text()='" + name + "'] and @class='rt-tr-group']//span[@title='Delete']")
        try:
            self.driver.find_element(By.XPATH, "//div[text()='" + name + "']")
            return
        except:
            return

    def verify_table(self, name):
        string = "//div[text()='" + name + "']"
        self.main.check_value(string)
