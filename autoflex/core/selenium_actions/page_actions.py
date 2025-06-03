from ..web_manager import Browser
from ..logger import logger
from ..exceptions import OperationTimeoutError
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class PageActions:


    @staticmethod
    def switch_to_window(window_name):
        driver = Browser.get_driver()
        try:
            driver.switch_to.window(window_name)
            logger.info(f"Switched To Window: {window_name}")
        except Exception as e:
            logger.error(f"Failed To Switch To Window: {window_name}. Error: {str(e)}")
            raise OperationTimeoutError("Failed to switch to window.")





    @staticmethod
    def switch_to_frame(locator):
        driver = Browser.get_driver()
        try:
            element = driver.find_element(*locator)
            driver.switch_to.frame(element)
            logger.info(f"Switched To Frame: {locator}")
        except Exception as e:
            logger.error(f"Failed To Switch To Frame: {locator}. Error: {str(e)}")
            raise OperationTimeoutError("Failed to switch to frame.")





    @staticmethod
    def switch_to_default_content():
        driver = Browser.get_driver()
        driver.switch_to.default_content()
        logger.info("Switched To Default Content")




    @staticmethod
    def accept_alert():
        driver = Browser.get_driver()
        try:
            driver.switch_to.alert.accept()
            logger.info("Accepted Alert")
        except NoAlertPresentException:
            logger.error("No Alert Present To Accept")
            raise OperationTimeoutError("Failed to accept the alert.")





    @staticmethod
    def dismiss_alert():
        driver = Browser.get_driver()
        try:
            driver.switch_to.alert.dismiss()
            logger.info("Dismissed Alert")
        except NoAlertPresentException:
            logger.error("No Alert Present To Dismiss")
            raise OperationTimeoutError("Failed to dismiss the alert.")
