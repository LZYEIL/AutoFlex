import pyautogui
from ..logger import logger
from ..exceptions import OperationTimeoutError


class DialogActions:

    @staticmethod
    def show_alert(message, title="AutoFlex Alert"):
        try:
            logger.info(f"Showing alert: {message}")
            pyautogui.alert(message, title)
        except Exception as e:
            logger.error(f"Show alert failed: {e}")
            raise OperationTimeoutError("Show alert failed.")





    @staticmethod
    def show_confirm(message, title="AutoFlex Confirm"):
        try:
            logger.info(f"Showing confirm: {message}")
            result = pyautogui.confirm(message, title)
            return result
        except Exception as e:
            logger.error(f"Show confirm failed: {e}")
            raise OperationTimeoutError("Show confirm failed.")





    @staticmethod
    def show_prompt(message, title="AutoFlex Prompt"):
        try:
            logger.info(f"Showing prompt: {message}")
            result = pyautogui.prompt(message, title)
            return result
        except Exception as e:
            logger.error(f"Show prompt failed: {e}")
            raise OperationTimeoutError("Show prompt failed.")
