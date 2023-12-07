*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
Login
    Open Browser    https://the-internet.herokuapp.com/login    chrome
    input text  id:username   tomsmith
    input text  id:password  SuperSecretPassword!
    click element   xpath://*[@class='fa fa-2x fa-sign-in']

*** Keywords ***
