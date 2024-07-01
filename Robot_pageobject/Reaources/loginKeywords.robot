*** Settings ***
Library    SeleniumLibrary
Variables    ../Robot_pageobject/pageobject/locators.py

*** Keywords ***
open browser
    [Arguments]    ${url}   ${browser}
    open browser    ${url}   ${browser}
    maximize browser window

username
    [Arguments]    ${username}
    input text    txt_loginusername     ${username}
Enter password  ${password}
    [Arguments]    text_loginpassword     ${password}

Click signin
    click button    text_signin

Verify successful login
    title should be    Login: Mercury Tours

Close my browser
    close all browsers