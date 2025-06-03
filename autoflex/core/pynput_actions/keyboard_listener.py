from pynput import keyboard
from ..logger import logger
from ..exceptions import OperationTimeoutError


class KeyboardListener:


    @staticmethod
    def start_listener(on_press_func):
        """Listening the keyboard"""
        try:
            logger.info("Starting keyboard listener")
            listener = keyboard.Listener(on_press=on_press_func)
            listener.start()
            return listener
        except Exception as e:
            logger.error(f"Keyboard listener failed: {e}")
            raise OperationTimeoutError("Failed to start keyboard listener.")
