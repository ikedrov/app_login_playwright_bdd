Feature: Login
    Identify the visitor

Scenario: Successful Login
    Given username and pwd password
    When Log In button clicked
    Then Show welcome message
