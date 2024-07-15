# Created by arshdeepdhillon at 7/15/24
Feature: Target main page search tests

  Scenario: user can search for a product on target
    Given Open target main page
    When Search for Product
    Then Verify search worked