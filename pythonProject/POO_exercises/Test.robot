
*** Settings ***
Library  SeleniumLibrary
Library     C:/Users/Dim/PycharmProjects/pythonProject/POO_exercises/Python_Selenium/MainFunctionality.py
Library     C:/Users/Dim/PycharmProjects/pythonProject/POO_exercises/Python_Selenium/PythonSelenium.py

*** Variables ***
${LOGIN_URL}  https://demoqa.com/
${BROWSER}  Chrome
${ELEMENTS}=     //div[@class="category-cards"]//div[@class="card mt-4 top-card"]//div[@class="card-body"]//h5[text()="Elements"]

*** Test Cases ***
Checking Radio Buttons and Check Boxes
    Open Browser        ${LOGIN_URL}     ${browser}
    Xpath Click      //div[@class="category-cards"]//div[@class="card mt-4 top-card"]//div[@class="card-body"]//h5[text()="Elements"]





*** Keywords ***





