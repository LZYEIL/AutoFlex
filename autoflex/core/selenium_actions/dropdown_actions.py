from selenium.webdriver.support.ui import Select
from ..web_manager import Browser
from .element_actions import ElementActions
from ..logger import logger


class DropdownActions:

    @staticmethod
    def select_by_visible_text(locator, text):
        element = ElementActions.find_element(locator)
        Select(element).select_by_visible_text(text)
        logger.info(f"Selected Dropdown Value By Visible Text: {text}")




    @staticmethod
    def select_by_value(locator, value):
        element = ElementActions.find_element(locator)
        Select(element).select_by_value(value)
        logger.info(f"Selected Dropdown Value By Value: {value}")





    @staticmethod
    def select_by_index(locator, index):
        element = ElementActions.find_element(locator)
        Select(element).select_by_index(index)
        logger.info(f"Selected Dropdown Value By Index: {index}")
