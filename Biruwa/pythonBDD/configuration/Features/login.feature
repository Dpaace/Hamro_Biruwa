Feature: Test the login application


  Scenario: Verify the Home page
    Given Launch the browser
    Then verify the page title
    And close the browser


  Scenario: verify login functionality
   Given Launch the App 
   Then enter the login credentials 
   Then click login
   Then verify the page title
   And close the App
    