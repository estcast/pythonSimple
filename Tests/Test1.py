from BaseTest import BaseTest
from PageObjects.LandingPage import LandingPage
import unittest


class BuggyCar(BaseTest):

    def test_validateImage(self):
        driver = self.driver
        driver.get("https://buggy.justtestit.org/")
        landing = LandingPage(driver)
        image = landing.getBlackWhiteCarImage()
        self.assertTrue(image.is_displayed())
        image.click()
        print(driver.title)


if __name__ == '__main__':
    unittest.main()
