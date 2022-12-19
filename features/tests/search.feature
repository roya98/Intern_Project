# Created by roya at 12/18/22
Feature: Main Page Search
  # Enter feature description here

  Scenario: User can access search
     Given Open main page
     When From page footer, click Search
     Then Verify search page opened