
from Check_Box import Check_Box
from MainFunctionality import MainFunctionality
from Radio_Button import Radio_Button
from Web_Tables import Web_Tables
from Buttons import Buttons
from Links import Links
from Upload_and_Download import Upload_and_Download

class MyClass:

    def __init__(self):
        self.main = MainFunctionality()
        self.checkbox = Check_Box(self.main.driver)
        self.radio = Radio_Button(self.main.driver)
        self.tables = Web_Tables(self.main.driver)
        self.buttons = Buttons(self.main.driver)
        self.links = Links(self.main.driver)
        self.upload_and_download = Upload_and_Download(self.main.driver)


demoq_element_xpath = '//div[@class="category-cards"]//div[@class="card mt-4 top-card"]//div[@class="card-body"]//h5[text()="Elements"]'

textbox_element_xpath = '//span[text()="Text Box"]'

username_xpath = '//div[@id="userName-wrapper"]//div[contains(@class, "col-md-9")]//input[@id="userName"]'
email_xpath = '//div[@id="userEmail-wrapper"]//div[contains(@class, "col-md-9")]//input[@id="userEmail"]'
current_address_xpath = '//div[@id="currentAddress-wrapper"]//div[contains(@class, "col-md-9")]//textarea[@id="currentAddress"]'
permanent_address_xpath = '//div[@id="permanentAddress-wrapper"]//div[contains(@class, "col-md-9")]//textarea[@id="permanentAddress"]'

submit_id = 'submit'


#username_input = driver.find_element(By.XPATH, '//div[@id="userName-wrapper"]//div[contains(@class, "col-md-9")]//input[@id="userName"]')
#username_input.click()
#username_input.send_keys('yes')
#username_input.send_keys(Keys.RETURN)

#//*[@id="tree-node"]/ol/li/span/button/svg/path
# //div[@class="check-box-tree-wrapper"]//span[@class="rct-text"]

d = MyClass()
d.main.start_server('https://demoqa.com')
# d.main.xpath_click(demoq_element_xpath)

## Exercitiu A  - CHECK BOX
# d.main.xpath_click('//span[text()="Check Box"]')
# d.checkbox.dropdown('Home')
# d.checkbox.dropdown('Documents')
# d.checkbox.dropdown('Office')
# d.checkbox.check_the_box('Private')
# d.checkbox.check_box_value('Private')
#
# d.checkbox.check_the_box('Private')
# d.checkbox.check_box_value('Private')
#
# d.checkbox.check_the_box('Classified')
# d.checkbox.check_the_box('General')
# d.checkbox.check_the_box('Public')

## Exercitiu B  -  RADIO BUTTON
# d.main.xpath_click("//span[text()='Radio Button']")
# d.main.check_title('Radio Button')
# d.radio.press_radio_button('Impressive')
# d.radio.check_radio_value('Impressive')
# d.radio.press_radio_button('Yes')
# d.radio.check_radio_value('Yes')
# d.radio.check_radio_button_status('No')

## Exercitiu C  -  WEB TABLES
# d.main.xpath_click('//span[text()="Web Tables"]')
# d.main.check_title('Web Tables')
# d.tables.search_by_name('Kierra')
# d.tables.nr_elements()
# d.tables.search_delete()
# d.tables.modify_web_table('Alden', Last_Name='Grigorescu', Age=21)
# d.tables.verify_table('Alden')
# d.tables.delete_row('Cierra')
# d.tables.verify_table('Cierra')
# d.tables.add_web_table('Chuck', 'Wills', 'cuckwills@test.com', '33', '5000', 'IT')
# d.tables.verify_table('Chuck')

## Exercitiu D - Buttons
# d.main.xpath_click('//span[text()="Buttons"]')
# d.main.check_title('Buttons')
# time.sleep(1)
# d.buttons.double_click()
# time.sleep(1)
# d.buttons.right_click()
# time.sleep(1)
# d.buttons.click()

## Exercitiu E - Links
# d.main.xpath_click('//span[text()="Links"]')
# d.main.check_title('Links')
# d.links.home()
# time.sleep(1)
# d.links.initial_page()

## Exercitiu F - Upload and Download
# d.main.xpath_click('//span[text()="Upload and Download"]')
# d.main.check_title('Upload and Download')
# d.upload_and_download.download()















#d.xpath_click(textbox_element_xpath)
#d.click_and_key(username_xpath, 'Filip')
#d.click_and_key(email_xpath, 'Filip@yahoo.com')
#d.click_and_key(current_address_xpath, 'Str Delinesti')
#d.click_and_key(permanent_address_xpath, 'Str Pascani')
#d.id_click(submit_id)

