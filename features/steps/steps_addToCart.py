from behave import *


from helper.page_objects import AddProdcutToCart


from values import labels


use_step_matcher("parse")
driver = AddProdcutToCart()


@given('I am on the given site')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.setup()


@step('I clear the popup')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.clear_popup(labels.cookies)


@step(u'I click on the "{text}" Category')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "Outdoor":
        driver.choose_product_category(labels.outdoor)
    elif text == "Decoration":
        driver.choose_product_category(labels.decor)
    else:
        driver.choose_product_category(labels.nursery)


@step(u'I select a product from "{text}" Category')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "Outdoor":
        driver.remove_notice(labels.body)
        driver.select_product(labels.item)
    elif text == "Decoration":
        driver.select_product(labels.item)
    else:
        driver.select_product(labels.item)


@step('I add the product to cart')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.add_to_cart(labels.add_btn)


@when('I click to view cart')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.display_cart(labels.show_cart)


@then('The cart icon should show if "{count}" quantity is added')
def step_impl(context, count):
    """
    :type context: behave.runner.Context
    """

    if count == "outdoor":
        driver.verify_cart_icon(labels.value_1)
    elif count == "decor":
        driver.verify_cart_icon(labels.value_2)
    else:
        driver.verify_cart_icon(labels.value_3)


@step(u'I should see the product from "{item}"')
def step_impl(context, item):
    """
    :type context: behave.runner.Context
    """
    if item == "Nursery":
        driver.verify_cart_content(labels.crate)
    elif item == "Decor":
        driver.verify_cart_content(labels.candle)
    else:
        driver.verify_cart_content(labels.chair)


@then("I close the page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.close_session()
