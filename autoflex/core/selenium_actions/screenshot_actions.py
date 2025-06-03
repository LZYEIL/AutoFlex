from ..web_manager import Browser
from ..logger import logger


class ScreenshotActions:

    @staticmethod
    def take_screenshot(file_path):
        driver = Browser.get_driver()
        try:
            driver.save_screenshot(file_path)
            logger.info(f"Screenshot Saved To: {file_path}")
        except Exception as e:
            logger.error(f"Failed To Take Screenshot. Error: {str(e)}")
            raise OperationTimeoutError("Failed to take the screenshot")
