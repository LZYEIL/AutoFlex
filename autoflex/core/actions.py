from .selenium_actions import (
    element_actions as selenium_element,
    dropdown_actions as selenium_dropdown,
    page_actions as selenium_page,
    mouse_actions as selenium_mouse,
    wait_actions as selenium_wait,
    script_actions as selenium_script,
    screenshot_actions as selenium_screenshot
)
from .pyautogui_actions import (
    mouse_actions as pyauto_mouse,
    keyboard_actions as pyauto_keyboard,
    screen_actions as pyauto_screen,
    dialog_actions as pyauto_dialog
)
from .pynput_actions import (
    keyboard_controller as pynput_keyboard,
    keyboard_listener as pynput_kb_listener,
    mouse_listener as pynput_mouse_listener
)
from .logger import logger
from .exceptions import OperationTimeoutError




class Actions:


    # Here are the functions from the Selenium:
    @staticmethod
    def find_element(locator, timeout=10):
        element = selenium_element.ElementActions.find_element(locator, timeout)
        return element




    # Click: Supports switching to PyAutoGUI
    @staticmethod
    def click(locator=None, x=None, y=None, timeout=10):
        if locator:
            try:
                selenium_element.ElementActions.click(locator, timeout)
                logger.info(f"Click via Selenium: {locator}")
                return
            except Exception as e:
                logger.warning(f"Selenium click failed: {e}, fallback to PyAutoGUI.")
        if x is not None and y is not None:
            try:
                pyauto_mouse.MouseActions.click_at(x, y)
                logger.info(f"Click at ({x},{y}) via PyAutoGUI")
                return
            except Exception as e:
                logger.error(f"PyAutoGUI click failed: {e}")
        raise OperationTimeoutError("Click failed.")




    @staticmethod
    def input_text(locator, text, timeout=10):
        try:
            selenium_element.ElementActions.input_text(locator, text, timeout)
            logger.info(f"Input text via Selenium on {locator}: {text}")
        except Exception as e:
            logger.error(f"Input text on {locator} failed: {e}")
            raise OperationTimeoutError("Input text failed.")




    @staticmethod
    def get_text(locator, timeout=10):
        try:
            text = selenium_element.ElementActions.get_text(locator, timeout)
            logger.info(f"Get text via Selenium from {locator}: {text}")
            return text
        except Exception as e:
            logger.error(f"Get text from {locator} failed: {e}")
            raise OperationTimeoutError("Get text failed.")




    @staticmethod
    def get_attribute(locator, attr, timeout=10):
        try:
            value = selenium_element.ElementActions.get_attribute(locator, attr, timeout)
            logger.info(f"Get attribute '{attr}' from {locator}: {value}")
            return value
        except Exception as e:
            logger.error(f"Get attribute {attr} from {locator} failed: {e}")
            raise OperationTimeoutError("Get attribute failed.")




    @staticmethod
    def is_visible(locator, timeout=10):
        visible = selenium_element.ElementActions.is_visible(locator, timeout)
        return visible




    @staticmethod
    def move_to_element(locator, timeout=10):
        try:
            selenium_mouse.MouseActions.move_to_element(locator, timeout)
            logger.info(f"Moved to element via Selenium: {locator}")
        except Exception as e:
            logger.error(f"Move to {locator} failed: {e}")
            raise OperationTimeoutError("Move to element failed.")




    # double_click supports switching to PyAutoGUI
    @staticmethod
    def double_click(locator=None, x=None, y=None, timeout=10):
        if locator:
            try:
                selenium_mouse.MouseActions.double_click(locator, timeout)
                logger.info(f"Double click via Selenium: {locator}")
                return
            except Exception as e:
                logger.warning(f"Selenium double click failed: {e}, fallback.")
        if x is not None and y is not None:
            try:
                pyauto_mouse.MouseActions.double_click_at(x, y)
                logger.info(f"Double click at ({x},{y}) via PyAutoGUI")
                return
            except Exception as e:
                logger.error(f"PyAutoGUI double click failed: {e}")
        raise OperationTimeoutError("Double click failed.")




    # right_click supports switching to PyAutoGUI
    @staticmethod
    def right_click(locator=None, x=None, y=None, timeout=10):
        if locator:
            try:
                selenium_mouse.MouseActions.right_click(locator, timeout)
                logger.info(f"Right click via Selenium: {locator}")
                return
            except Exception as e:
                logger.warning(f"Selenium right click failed: {e}, fallback to PyAutoGUI.")
        if x is not None and y is not None:
            try:
                pyauto_mouse.MouseActions.right_click_at(x, y)
                logger.info(f"Right click at ({x},{y}) via PyAutoGUI")
                return
            except Exception as e:
                logger.error(f"PyAutoGUI right click failed: {e}")
        raise OperationTimeoutError("Right click action failed.")





    @staticmethod
    def drag_and_drop(source_locator, target_locator, timeout=10):
        try:
            selenium_mouse.MouseActions.drag_and_drop(source_locator, target_locator, timeout)
        except Exception as e:
            logger.error(f"Drag and drop from {source_locator} to {target_locator} failed: {e}")
            raise OperationTimeoutError("Drag and drop failed.")



    @staticmethod
    def select_by_visible_text(locator, text, timeout=10):
        try:
            selenium_dropdown.DropdownActions.select_by_visible_text(locator, text, timeout)
        except Exception as e:
            logger.error(f"Select by text in {locator} failed: {e}")
            raise OperationTimeoutError("Select by visible text failed.")




    @staticmethod
    def select_by_value(locator, value, timeout=10):
        try:
            selenium_dropdown.DropdownActions.select_by_value(locator, value, timeout)
        except Exception as e:
            logger.error(f"Select by value in {locator} failed: {e}")
            raise OperationTimeoutError("Select by value failed.")




    @staticmethod
    def select_by_index(locator, index, timeout=10):
        try:
            selenium_dropdown.DropdownActions.select_by_index(locator, index, timeout)
        except Exception as e:
            logger.error(f"Select by index in {locator} failed: {e}")
            raise OperationTimeoutError("Select by index failed.")




    @staticmethod
    def switch_to_window(window_name):
        selenium_page.PageActions.switch_to_window(window_name)




    @staticmethod
    def switch_to_frame(frame_reference):
        selenium_page.PageActions.switch_to_frame(frame_reference)




    @staticmethod
    def switch_to_default_content():
        try:
            selenium_page.PageActions.switch_to_default_content()
        except Exception as e:
            logger.error(f"Switch to default content failed: {e}")
            raise OperationTimeoutError("Switch to default content failed.")




    @staticmethod
    def accept_alert():
        selenium_page.PageActions.accept_alert()




    @staticmethod
    def dismiss_alert():
        selenium_page.PageActions.dismiss_alert()




    # take_screenshot supports switching to PyAutoGUI
    @staticmethod
    def take_screenshot(file_path):
        try:
            selenium_screenshot.ScreenshotActions.take_screenshot(file_path)
            logger.info(f"Screenshot via Selenium saved to {file_path}")
            return
        except Exception as e:
            logger.warning(f"Selenium screenshot failed: {e}, fallback to PyAutoGUI.")
        try:
            pyauto_screen.ScreenActions.take_screenshot(file_path)
            logger.info(f"Screenshot via PyAutoGUI saved to {file_path}")
        except Exception as e:
            logger.error(f"PyAutoGUI screenshot failed: {e}")
            raise OperationTimeoutError("Screenshot action failed.")




    @staticmethod
    def execute_script(script):
        result = selenium_script.ScriptActions.execute_script(script)
        return result




    @staticmethod
    def execute_async_script(script):
        result = selenium_script.ScriptActions.execute_async_script(script)
        return result




    @staticmethod
    def wait_for_element_visible(locator, timeout=10):
        try:
            selenium_wait.WaitActions.wait_for_element_visible(locator, timeout)
            logger.info(f"Element {locator} is visible.")
        except Exception as e:
            logger.error(f"Wait for element {locator} visible failed: {e}")
            raise OperationTimeoutError("Wait for element visible failed.")




    @staticmethod
    def wait_for_element_clickable(locator, timeout=10):
        try:
            selenium_wait.WaitActions.wait_for_element_clickable(locator, timeout)
            logger.info(f"Element {locator} is clickable.")
        except Exception as e:
            logger.error(f"Wait for element {locator} clickable failed: {e}")
            raise OperationTimeoutError("Wait for element clickable failed.")

    


    # Below are the functions from the PyAutogGUI:
    # Dialog Actions:
    @staticmethod
    def show_alert(message):
        pyauto_dialog.DialogActions.show_alert(message)

  


    
    @staticmethod
    def show_confirm(message):
        result = pyauto_dialog.DialogActions.show_confirm(message)
        return result

    


    @staticmethod
    def show_prompt(message):
        result = pyauto_dialog.DialogActions.show_prompt(message)
        return result


    # Keyboard Actions:
    @staticmethod
    def press_key(key):
        pyauto_keyboard.KeyboardActions.press_key(key)

    

    @staticmethod
    def press_hotkey(*keys):
        pyauto_keyboard.KeyboardActions.press_hotkey(*keys)



    @staticmethod
    def hold_and_release(keys, hold_time=0.5):
        pyauto_keyboard.KeyboardActions.hold_and_release(keys, hold_time)

    

    @staticmethod
    def type_text(text, interval=0.05):
        pyauto_keyboard.KeyboardActions.type_text(text, interval)

    
    # Mouse Actions:
    @staticmethod
    def move_to(x, y, duration=0.5):
        pyauto_mouse.MouseActions.move_to(x, y, duration)


    
    @staticmethod
    def drag_to(x, y, duration=0.5):
        pyauto_mouse.MouseActions.drag_to(x, y, duration)



    @staticmethod
    def scroll(amount):
        pyauto_mouse.MouseActions.scroll(amount)

    

    @staticmethod
    def get_mouse_position():
        pos = pyauto_mouse.MouseActions.get_position()
        return pos



    # Screen Actions:
    @staticmethod
    def get_pixel_color(x, y):
        color = pyauto_screen.ScreenActions.get_pixel_color(x, y)
        return color


    
    @staticmethod
    def pixel_matches_color(x, y, expected_color):
        match = pyauto_screen.ScreenActions.pixel_matches_color(x, y, expected_color)
        return match


    

    @staticmethod
    def locate_image_on_screen(image_path, confidence=0.9):
        pos = pyauto_screen.ScreenActions.locate_image_on_screen(image_path, confidence)
        return pos


    
    # Below are the functions from the PynPut:
    @staticmethod
    def press_key_pynput(key):
        pynput_keyboard.KeyboardController.press_key(key)


    

    @staticmethod
    def release_key_pynput(key):
        pynput_keyboard.KeyboardController.release_key(key)

    


    @staticmethod
    def press_and_hold_pynput(keys, hold_time=0.5):
        pynput_keyboard.KeyboardController.press_and_hold(keys, hold_time)




    @staticmethod
    def start_keyboard_listener(on_press_func):
        try:
            pynput_kb_listener.KeyboardListener.start_listener(on_press_func)
            logger.info(f"Pynput keyboard listener started.")
        except Exception as e:
            logger.error(f"Pynput keyboard listener failed: {e}")
            raise OperationTimeoutError("Pynput keyboard listener failed.")




    @staticmethod
    def start_mouse_listener(on_click_func):
        try:
            pynput_mouse_listener.MouseListener.start_listener(on_click_func)
            logger.info(f"Pynput mouse listener started.")
        except Exception as e:
            logger.error(f"Pynput mouse listener failed: {e}")
            raise OperationTimeoutError("Pynput mouse listener failed.")


    
