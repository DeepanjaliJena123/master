## main purpose page object model::to acheive the reusability and to avoide the duplication




*** Settings ***
Library    SeleniumLibrary
Resource    ../Robot_pageobject/Reaources/loginKeywords.robot

*** Variables ***
${browser}  Chrome
${url}  https://demo.guru99.com/test/newtours/login_sucess.php
${username} tutorial
${password} tutorial

*** Test Cases ***
Login page
    Open my browser     ${url}     ${browser}
    Enter user name     ${username}
    Enter password   ${password}
    Click signin
    Verify successful login
    Close my browser






