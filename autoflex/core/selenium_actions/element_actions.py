from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..web_manager import Browser
from ..logger import logger
from ..exceptions import ElementNotFoundError, OperationTimeoutError



class ElementActions:

    @staticmethod
    def find_element(locator, timeout=10):
        driver = Browser.get_driver()
        try:
            logger.info(f"Finding Element: {locator}")
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            logger.error(f"Element Not Found: {locator}")
            raise ElementNotFoundError(f"Element Not Found: {locator}")




    @staticmethod
    def click(locator, timeout=10):
        element = ElementActions.find_element(locator, timeout)
        element.click()
        logger.info(f"Clicked Element: {locator}")




    @staticmethod
    def input_text(locator, text, timeout=10):
        element = ElementActions.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info(f"Input Text '{text}' Into Element: {locator}")




    @staticmethod
    def get_text(locator, timeout=10):
        element = ElementActions.find_element(locator, timeout)
        text = element.text
        logger.info(f"Got Text From Element: {locator} -> {text}")
        return text




    @staticmethod
    def get_attribute(locator, attr_name, timeout=10):
        element = ElementActions.find_element(locator, timeout)
        attr_value = element.get_attribute(attr_name)
        logger.info(f"Got Attribute '{attr_name}' From Element: {locator} -> {attr_value}")
        return attr_value




    @staticmethod
    def is_visible(locator, timeout=10):
        driver = Browser.get_driver()
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element Is Visible: {locator}")
            return True
        except TimeoutException:
            logger.info(f"Element Not Visible: {locator}")
            return False
