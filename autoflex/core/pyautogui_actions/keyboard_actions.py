import pyautogui
from pynput.keyboard import Controller, Key
from ..logger import logger
from ..exceptions import OperationTimeoutError
from time import sleep


class KeyboardActions:

    @staticmethod
    def type_text(text, interval=0.05):
        try:
            logger.info(f"Typing text: {text}")
            pyautogui.typewrite(text, interval=interval)
        except Exception as e:
            logger.error(f"Type text failed: {e}")
            raise OperationTimeoutError("Type text failed.")




    @staticmethod
    def press_key(key):
        try:
            logger.info(f"Pressing key: {key}")
            pyautogui.press(key)
        except Exception as e:
            logger.error(f"Press key {key} failed: {e}")
            raise OperationTimeoutError(f"Press key {key} failed.")





    @staticmethod
    def press_hotkey(*keys):
        try:
            logger.info(f"Pressing hotkey: {' + '.join(keys)}")
            pyautogui.hotkey(*keys)
        except Exception as e:
            logger.error(f"Press hotkey {keys} failed: {e}")
            raise OperationTimeoutError(f"Press hotkey {keys} failed.")





    @staticmethod
    def hold_and_release(keys, hold_time=0.5):
        try:
            logger.info(f"Holding keys: {keys} for {hold_time}s")
            kb = Controller()
            for k in keys:
                kb.press(getattr(Key, k) if hasattr(Key, k) else k)
            sleep(hold_time)
            for k in reversed(keys):
                kb.release(getattr(Key, k) if hasattr(Key, k) else k)
        except Exception as e:
            logger.error(f"Hold and release keys {keys} failed: {e}")
            raise OperationTimeoutError(f"Hold and release {keys} failed.")
