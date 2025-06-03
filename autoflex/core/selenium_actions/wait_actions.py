from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..web_manager import Browser
from ..logger import logger
from ..exceptions import OperationTimeoutError


class WaitActions:


    @staticmethod
    def wait_for_element_visible(locator, timeout=10):
        driver = Browser.get_driver()
        try:
            logger.info(f"Waiting For Element Visible: {locator}")
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Timeout Waiting For Element Visible: {locator}")
            raise OperationTimeoutError(f"Timeout Waiting For Element Visible: {locator}")




    @staticmethod
    def wait_for_element_clickable(locator, timeout=10):
        driver = Browser.get_driver()
        try:
            logger.info(f"Waiting For Element Clickable: {locator}")
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Timeout Waiting For Element Clickable: {locator}")
            raise OperationTimeoutError(f"Timeout Waiting For Element Clickable: {locator}")
