# Created by Ademola Bhadmus at 2020-06-30

Feature: Add Product to Cart
  The features is to test that a product can be added
  to cart and see that the cart content is recorded.



  Scenario: Add a product from Outdoor
    Given I am on the given site

      And I clear the popup

      And I click on the "Outdoor" Category

      And I select a product from "Outdoor" Category

      And I add the product to cart

    When I click to view cart

    Then  The cart icon should show if "outdoor" quantity is added

      And I should see the product from "Outdoor"





