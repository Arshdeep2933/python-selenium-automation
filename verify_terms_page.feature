# Created by arshdeepdhillon at 8/12/24
Feature: Verify_terms_conditions

  Scenario: Verify Terms and Conditions page
     Given Open target main page
     When user click sign in
     Then user click in right side
     Then verify sign in  form opened
     When Store original window
     Then Click on Target terms and conditions link
     When Switch to the newly opened window
     Then Verify Terms and Conditions page is opened
     Then User can close new window
     Then switch back to original window