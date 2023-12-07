*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}          https://the-internet.herokuapp.com/login
${browser}      chrome
${username}     tomsmith
${password}     SuperSecretPassword!
*** Test Cases ***
Login
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    logintoapplication
    sleep   5
    close browser
*** Keywords ***
logintoapplication
    input text  id:username   ${username}
    input text  id:password  ${password}
    click element   xpath://*[@class='fa fa-2x fa-sign-in']