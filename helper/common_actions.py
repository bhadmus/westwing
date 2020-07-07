from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class CommonAction:
    """This creates the class file to collect
        all common events (actions) on the site
    """

    def click_an_element(self, product):
        """
                This method is to help select any product
                on the westwing site
                :param product:
                :return:
                """
        WebDriverWait(self.site.driver, 30) \
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, product)))
        self.site.driver.find_element_by_css_selector(product).click()

