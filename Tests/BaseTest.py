from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        ser = Service("C:\workspace\drivers\chromedriver-win64\chromedriver.exe")
        op = webdriver.ChromeOptions()
        op.add_argument("--no-first-run")
        op.add_argument("--no-default-browser-check")
        op.add_argument("--disable-extensions")
        op.add_argument("--incognito")
        op.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Setting up webdriver")

    def tearDown(self):
        driver = self.driver
        driver.quit()
