# Created by roya at 12/15/22
Feature: Search Result
  # Enter feature description here

  Scenario: Correct Search Results for Cure
    Given Open Search Result for Cure
    Then Verify 23 results


  Scenario: Search results UI for CURE is correct
    Given Open Search Result for Cure
    Then Verify first results have name, image, and price


  Scenario: Top logo takes to the main page
    Given Open Search Result for Cure
    When Click on CureSkin logo in the header
    Then Verify user is taken to the main page

