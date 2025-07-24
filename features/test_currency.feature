Feature: REST Countries Currency API

  Scenario: Happy Path - Valid currency returns 200 and country name
    Given I have a valid currency code "KES"
    When I send a request to the API
    Then the response status code should be 200
    And I should get at least one country name in the response

  Scenario: Unhappy Path - Invalid currency returns error
    Given I have an invalid currency code "XYZ"
    When I send a request to the API
    Then the response status code should not be 200
    And I should get an error message or empty response
