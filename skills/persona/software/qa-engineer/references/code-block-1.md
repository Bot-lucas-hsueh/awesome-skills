# gherkin Example

```
# features/user_login.feature
Feature: User Authentication
  As a registered user
  I want to log into the application
  So that I can access my account

  Background:
    Given the application is running
    And a user exists with email "user@example.com" and password "SecurePass123!"

  Scenario: Successful login with valid credentials
    When I submit login with email "user@example.com" and password "SecurePass123!"
    Then I should be redirected to the dashboard
    And I should see my username in the header

  Scenario: Failed login with incorrect password
    When I submit login with email "user@example.com" and password "WrongPassword"
    Then I should see the error message "Invalid email or password"
    And I should remain on the login page

  Scenario Outline: Account lockout after failed attempts
    When I submit <attempts> failed login attempts for "user@example.com"
    Then the account should be locked
    And I should see the message "Account temporarily locked"

    Examples:
      | attempts |
      | 5        |
      | 10       |
```
