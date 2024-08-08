import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    ser = Service(ChromeDriverManager().install())
    op = webdriver.ChromeOptions()
    op.add_argument("--no-first-run")
    op.add_argument("--no-default-browser-check")
    op.add_argument("--disable-extensions")
    op.add_argument("--incognito")
    op.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(service=ser, options=op)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("Setting up webdriver")
    yield driver
    driver.quit()


def test_black_white_car_image(driver):
    driver.get("https://buggy.justtestit.org/")
    image = driver.find_element(By.XPATH, '//img[@src="/img/header-car.gif"]')

    assert image.is_displayed(), "The black and white car image is not displayed"

    image.click()
    print("Page title: " + driver.title)
