import pyautogui
from ..logger import logger
from ..exceptions import OperationTimeoutError


class ScreenActions:

    @staticmethod
    def take_screenshot(file_path):
        try:
            pyautogui.screenshot(file_path)
            logger.info(f"Screenshot saved to {file_path}")
        except Exception as e:
            logger.error(f"Take screenshot failed: {e}")
            raise OperationTimeoutError("Take screenshot failed.")



    @staticmethod
    def get_pixel_color(x, y):
        try:
            color = pyautogui.pixel(x, y)
            logger.info(f"Pixel color at ({x}, {y}): {color}")
            return color
        except Exception as e:
            logger.error(f"Get pixel color at ({x}, {y}) failed: {e}")
            raise OperationTimeoutError("Get pixel color failed.")




    @staticmethod
    def pixel_matches_color(x, y, color):
        try:
            result = pyautogui.pixelMatchesColor(x, y, color)
            logger.info(f"Pixel at ({x}, {y}) matches {color}: {result}")
            return result
        except Exception as e:
            logger.error(f"Pixel match check failed at ({x}, {y}): {e}")
            raise OperationTimeoutError("Pixel match check failed.")




    @staticmethod
    def locate_image_on_screen(image_path, confidence=0.9):
        try:
            pos = pyautogui.locateOnScreen(image_path, confidence=confidence)
            logger.info(f"Locate image {image_path}: {pos}")
            return pos
        except Exception as e:
            logger.error(f"Locate image {image_path} failed: {e}")
            raise OperationTimeoutError("Locate image on screen failed.")
