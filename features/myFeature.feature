Feature: Orange HRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on the page
    And close browser

# to run this feature in terminal run  --> behave features/myFeature.feature