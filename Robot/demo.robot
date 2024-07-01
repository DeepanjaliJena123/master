*** Settings ***
Documentation    - validate login funtionality
Library    SeleniumLibrary
Force Tags    Regrassion


*** Variables ***
#scalar variable
${Browser}     Chrome
${URL}     https://www.google.com/

#list variable
@{crd}    admin     admin123

#dictionary variable
&{login_data}     username=Admin     password=admin123

*** Test Cases ***
Verify login
     Open Browser     ${URL}     ${Browser}

*** Keywords ***
