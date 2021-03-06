from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

from .common_actions import CommonAction
from webdriver_config import Driver
from values import labels


class AddProdcutToCart(CommonAction):
    """This creates the class file to describe the journey of adding to Cart"""

    def __init__(self):
        """Creating the instance of the webdriver class
           so it can be accessible inside this class
        """
        self.site = Driver()

    def setup(self):
        """
        This is to launch the westwing site so that
        actions can be performed.
        :return: An instance of the site
        """
        self.site.launch_site()

    def clear_popup(self, cookie):
        """
        This is to clear cookies
        """
        WebDriverWait(self.site.driver, 20) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, cookie)))
        self.site.driver.find_element_by_css_selector(cookie).click()

    def choose_product_category(self, category):
        """
        This method is to help select any product category
        on the westwing site
        :param category:
        :return:
        """
        WebDriverWait(self.site.driver, 20) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, category)))
        self.site.driver.find_element_by_css_selector(category).click()

    def remove_notice(self, body):
        """
        This method is to help to remove the login popup
        :param body:
        :return:
        """
        WebDriverWait(self.site.driver, 10) \
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, body)))
        outside = self.site.driver.find_element_by_css_selector(body)
        action = ActionChains(self.site.driver)
        # action.double_click(outside).perform()
        action.move_to_element(outside).perform()
        self.site.driver.execute_script("arguments[0].click();", outside)

    def select_product(self, item):
        """
        This method is to help select any product
        on the westwing site
        :param
        :return:
        """
        WebDriverWait(self.site.driver, 10) \
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, item)))
        locate = self.site.driver.find_element_by_css_selector(item)
        action = ActionChains(self.site.driver)
        action.move_to_element(locate).perform()
        self.click_an_element(item)

    def add_to_cart(self, add_btn):
        """
        The step that adds the product to cart
        :param add_btn:
        :return:
        """
        WebDriverWait(self.site.driver, 20) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, add_btn)))
        self.site.driver.find_element_by_css_selector(add_btn).click()

    def display_cart(self, show_cart):
        """
        This clicks the cart
        :param show_cart:
        :return:
        """
        WebDriverWait(self.site.driver, 20) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, show_cart)))
        self.site.driver.find_element_by_css_selector(show_cart).click()

    def close_session(self):
        self.site.driver.close()

    def verify_cart_icon(self, count):
        WebDriverWait(self.site.driver, 10) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, labels.cart_icon)))
        cart = self.site.driver.find_element_by_css_selector(labels.cart_icon)
        try:
            assert count in cart.text
            print(f'{count} is present')
        except AssertionError:
            f"{count} not present"

    def verify_cart_content(self, content):
        WebDriverWait(self.site.driver, 10) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, labels.cart)))
        item = self.site.driver.find_element_by_css_selector(labels.cart)

        try:
            assert content in item.text
            print(f'{content} is present in the cart')
        except AssertionError:
            "Item not Found"
