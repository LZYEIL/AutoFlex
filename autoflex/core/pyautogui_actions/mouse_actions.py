import pyautogui
from ..logger import logger
from ..exceptions import OperationTimeoutError


class MouseActions:


    @staticmethod
    def click_at(x, y):
        try:
            logger.info(f"Clicking at ({x}, {y})")
            pyautogui.click(x, y)
        except Exception as e:
            logger.error(f"Click at ({x}, {y}) failed: {e}")
            raise OperationTimeoutError(f"Click at ({x}, {y}) failed.")





    @staticmethod
    def double_click_at(x, y):
        try:
            logger.info(f"Double clicking at ({x}, {y})")
            pyautogui.doubleClick(x, y)
        except Exception as e:
            logger.error(f"Double click at ({x}, {y}) failed: {e}")
            raise OperationTimeoutError(f"Double click at ({x}, {y}) failed.")



    @staticmethod
    def right_click_at(x, y):
        try:
            logger.info(f"Right clicking at ({x}, {y})")
            pyautogui.rightClick(x, y)
        except Exception as e:
            logger.error(f"Right click at ({x}, {y}) failed: {e}")
            raise OperationTimeoutError(f"Right click at ({x}, {y}) failed.")




    @staticmethod
    def move_to(x, y, duration=0.5):
        try:
            logger.info(f"Moving mouse to ({x}, {y}) over {duration}s")
            pyautogui.moveTo(x, y, duration=duration)
        except Exception as e:
            logger.error(f"Move to ({x}, {y}) failed: {e}")
            raise OperationTimeoutError(f"Move to ({x}, {y}) failed.")



    @staticmethod
    def drag_to(x, y, duration=0.5):
        try:
            logger.info(f"Dragging to ({x}, {y}) over {duration}s")
            pyautogui.dragTo(x, y, duration=duration)
        except Exception as e:
            logger.error(f"Drag to ({x}, {y}) failed: {e}")
            raise OperationTimeoutError(f"Drag to ({x}, {y}) failed.")




    @staticmethod
    def scroll(amount):
        try:
            logger.info(f"Scrolling {amount} units")
            pyautogui.scroll(amount)
        except Exception as e:
            logger.error(f"Scroll {amount} failed: {e}")
            raise OperationTimeoutError(f"Scroll {amount} failed.")




    @staticmethod
    def get_position():
        try:
            pos = pyautogui.position()
            logger.info(f"Mouse position: {pos}")
            return pos
        except Exception as e:
            logger.error(f"Get mouse position failed: {e}")
            raise OperationTimeoutError("Get mouse position failed.")
