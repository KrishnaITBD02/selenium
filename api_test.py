import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("URL Check")
@allure.title("Check if URL is accessible")
def test_check_url():
    # Initialize WebDriver (choose appropriate WebDriver, e.g., ChromeDriver, GeckoDriver)
    driver = webdriver.Chrome()  # Change this line to select the appropriate WebDriver

    # Maximize the window (optional)
    driver.maximize_window()

    # Set up allure report steps
    with allure.step("Open URL"):
        driver.get("https://itbd-dev-frontend.team-gps.net/login")

    with allure.step("Check URL status"):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            )
            assert "Login" in driver.title  # You can modify this validation as per your requirements
            allure.attach(driver.get_screenshot_as_png(), name="URL_Screenshot", attachment_type=allure.attachment_type.PNG)
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="URL_Error_Screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("URL did not load properly")
        finally:
            # Close the browser window
            driver.quit()

if __name__ == "__main__":
    pytest.main(['-s', '-v', '--alluredir=allure-results'])
