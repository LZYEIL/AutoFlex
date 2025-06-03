from pynput.keyboard import Controller, Key
from ..logger import logger
from ..exceptions import OperationTimeoutError
from time import sleep


class KeyboardController:
    kb = Controller()

    @staticmethod
    def press_key(key):
        """Press a single key"""
        try:
            logger.info(f"Pressing key: {key}")
            KeyboardController.kb.press(getattr(Key, key) if hasattr(Key, key) else key)
        except Exception as e:
            logger.error(f"Press key {key} failed: {e}")
            raise OperationTimeoutError(f"Press key {key} failed.")





    @staticmethod
    def release_key(key):
        """Release a single key"""
        try:
            logger.info(f"Releasing key: {key}")
            KeyboardController.kb.release(getattr(Key, key) if hasattr(Key, key) else key)
        except Exception as e:
            logger.error(f"Release key {key} failed: {e}")
            raise OperationTimeoutError(f"Release key {key} failed.")





    @staticmethod
    def press_and_hold(keys, hold_time=0.5):
        """Press multiple keys and wait for release"""
        try:
            logger.info(f"Holding keys: {keys} for {hold_time}s")
            for k in keys:
                KeyboardController.kb.press(getattr(Key, k) if hasattr(Key, k) else k)
            sleep(hold_time)
            for k in reversed(keys):
                KeyboardController.kb.release(getattr(Key, k) if hasattr(Key, k) else k)
            logger.info(f"Released keys: {keys}")
        except Exception as e:
            logger.error(f"Hold and release keys {keys} failed: {e}")
            raise OperationTimeoutError(f"Hold and release keys {keys} failed.")
