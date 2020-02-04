*** Variables ***
${BROWSER}       chrome
${ROOT}          http://172.17.0.1/core/
${PLATFORM}      linux
${VERSION}       latest
${SELENIUM_URL}  http://localhost:4444
${ADMIN_USERNAME}  admin
${ADMIN_PASSWORD}  admin

*** Settings ***
Library    SeleniumLibrary
Library    PageObjectLibrary
Library    Provisioning.py  ${ADMIN_USERNAME}  ${ADMIN_PASSWORD}  ${ROOT}
Library    LoginContext.py
Library    listener.py

Suite Setup  set log level  DEBUG

Test Setup     Open test browser
Test Teardown  Close all test browsers

*** Test Cases ***
Valid Login
    Given a user has been created with username jasmine and password jasmine
    And Go To Page  LoginPage
    When User Logs In With Username jasmine And Password jasmine
    Then The current page should be  FilesPage

*** Keywords ***
Open test browser
	Open browser  ${ROOT}  ${BROWSER}
	...  remote_url=${SELENIUM_URL}/wd/hub
	...  desired_capabilities=browserName:${BROWSER},version:${VERSION},platform:${PLATFORM}

Close all test browsers
    Close all browsers
    Delete All Created Users