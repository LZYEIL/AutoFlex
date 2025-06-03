from ..web_manager import Browser
from ..logger import logger


class ScriptActions:

    @staticmethod
    def execute_script(script):
        driver = Browser.get_driver()
        try:
            result = driver.execute_script(script)
            logger.info(f"Executed Script: {script}")
            return result
        except Exception as e:
            logger.error(f"Failed To Execute Script: {script}. Error: {str(e)}")
            raise OperationTimeoutError("Execute script failed.")





    @staticmethod
    def execute_async_script(script):
        driver = Browser.get_driver()
        try:
            result = driver.execute_async_script(script)
            logger.info(f"Executed Async Script: {script}")
            return result
        except Exception as e:
            logger.error(f"Failed To Execute Async Script: {script}. Error: {str(e)}")
            raise OperationTimeoutError("Execute script failed.")
