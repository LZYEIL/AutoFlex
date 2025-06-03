from selenium.webdriver.common.action_chains import ActionChains
from ..web_manager import Browser
from .element_actions import ElementActions
from ..logger import logger


class MouseActions:

    @staticmethod
    def move_to_element(locator):
        driver = Browser.get_driver()
        element = ElementActions.find_element(locator)
        ActionChains(driver).move_to_element(element).perform()
        logger.info(f"Moved To Element: {locator}")




    @staticmethod
    def double_click(locator):
        driver = Browser.get_driver()
        element = ElementActions.find_element(locator)
        ActionChains(driver).double_click(element).perform()
        logger.info(f"Double Clicked: {locator}")




    @staticmethod
    def right_click(locator):
        driver = Browser.get_driver()
        element = ElementActions.find_element(locator)
        ActionChains(driver).context_click(element).perform()
        logger.info(f"Right Clicked: {locator}")



        

    @staticmethod
    def drag_and_drop(source_locator, target_locator):
        driver = Browser.get_driver()
        source = ElementActions.find_element(source_locator)
        target = ElementActions.find_element(target_locator)
        ActionChains(driver).drag_and_drop(source, target).perform()
        logger.info(f"Dragged Element {source_locator} To {target_locator}")
