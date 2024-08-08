# Created by arshdeepdhillon at 8/7/24
Feature: verify target sign in

  Scenario: Target sign in page
    Given Open target main page
    When user click sign in
    Then user click in right side
    Then verify sign in  form opened