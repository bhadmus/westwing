# Created by sanguine at 2020-07-28
Feature: Add Product to Cart
  The features is to test that a product can be added
  to cart and see that the cart content is recorded.

  Scenario: Add a product from Nursery

    Given I am on the given site

      And I click on the "Nursery" Category

      And I select a product from "Nursery" Category

      And I add the product to cart

    When I click to view cart

    Then  The cart icon should show if "nursery" quantity is added

      And I should see the product from "Nursery"

    Then I close the page
