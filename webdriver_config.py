from selenium import webdriver

class Driver:
    """
    The driver class is to help create the webdriver class needed
    in such a way that it can be resused anywhere within the project
     """

    def __init__(self):
        self.driver = webdriver.Chrome() # Chrome driver must set to PATH before this step

    def launch_site(self):
        self.driver.get("https://www.westwingnow.de/")
