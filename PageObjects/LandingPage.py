from selenium.webdriver.common.by import By


class LandingPage:

    def __init__(self, driver):
        self.driver = driver
        self.blackWhiteCarImage = '//img[@src="/img/header-car.gif"]'

    def getBlackWhiteCarImage(self):
        return self.driver.find_element(By.XPATH, self.blackWhiteCarImage)
