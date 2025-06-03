from pynput import mouse
from ..logger import logger
from ..exceptions import OperationTimeoutError


class MouseListener:

    @staticmethod
    def start_listener(on_click_func):
        """Starting the mouse listening"""
        try:
            logger.info("Starting mouse listener")
            listener = mouse.Listener(on_click=on_click_func)
            listener.start()
            return listener
        except Exception as e:
            logger.error(f"Mouse listener failed: {e}")
            raise OperationTimeoutError("Failed to start mouse listener.")
