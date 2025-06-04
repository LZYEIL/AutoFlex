---
title: Everything You Need
layout: default
nav_order: 5
permalink: /all-functions
---

## Everything You Need

<br>

### Selenium-Based Actions

### `find_element(locator, timeout=10)`

**Description:**  
Find a web element on the current page using Selenium.

**Parameters:**

- `locator` (`str`): XPath locator string for the target element.
- `timeout` (`int`, optional): Maximum wait time in seconds (default is `10`).

**Returns:**  
`WebElement` object if found.

**Raises:**  
- `OperationTimeoutError` if element cannot be found within timeout.

---

### `click(locator=None, x=None, y=None, timeout=10)`

**Description:**  
Click an element on the page via Selenium (if `locator` is given), or click a specific position on the screen using PyAutoGUI.

**Parameters:**
- `locator` (`str`, optional): XPath locator of the element.
- `x` (`int`, optional): X-coordinate for screen click.
- `y` (`int`, optional): Y-coordinate for screen click.
- `timeout` (`int`, optional): Timeout for element search (default `10`).

**Returns:**  
`None`

**Raises:**  
- `OperationTimeoutError` if both Selenium and PyAutoGUI clicks fail.

---

### `input_text(locator, text, timeout=10)`

**Description:**  
Input text into a web element using Selenium.

**Parameters:**
- `locator` (`str`): XPath locator.
- `text` (`str`): Text to input.
- `timeout` (`int`, optional): Timeout in seconds.

**Returns:**  
`None`

**Raises:**  
- `OperationTimeoutError` if action fails.

---

### `get_text(locator, timeout=10)`

**Description:**  
Retrieve the text content of a web element.

**Parameters:**
- `locator` (`str`): XPath locator.
- `timeout` (`int`, optional): Timeout in seconds.

**Returns:**  
`str` — Text content.

**Raises:**  
- `OperationTimeoutError` if element is not found.

---

### `get_attribute(locator, attr, timeout=10)`

**Description:**  
Get a specific attribute value from a web element.

**Parameters:**
- `locator` (`str`): XPath locator.
- `attr` (`str`): Attribute name.
- `timeout` (`int`, optional): Timeout in seconds.

**Returns:**  
`str` — Attribute value.

**Raises:**  
- `OperationTimeoutError` if operation fails.

---

### `is_visible(locator, timeout=10)`

**Description:**  
Check if an element is visible.

**Parameters:**
- `locator` (`str`): XPath locator.
- `timeout` (`int`, optional): Timeout in seconds.

**Returns:**  
`bool`

---

### `move_to_element(locator, timeout=10)`

**Description:**
 Move the mouse cursor to a specific web element using Selenium.

**Parameters:**

- `locator` (`str`): XPath locator of the target element.
- `timeout` (`int`, optional): Timeout in seconds (default `10`).

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError` if action fails.

------

### `double_click(locator=None, x=None, y=None, timeout=10)`

**Description:**
 Perform a double click via Selenium (on an element) or via PyAutoGUI (on screen position).

**Parameters:**

- `locator` (`str`, optional): XPath locator of the element.
- `x` (`int`, optional): X-coordinate for screen double-click.
- `y` (`int`, optional): Y-coordinate for screen double-click.
- `timeout` (`int`, optional): Timeout for Selenium action.

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError` if both attempts fail.

------

### `right_click(locator=None, x=None, y=None, timeout=10)`

**Description:**
 Perform a right-click via Selenium or PyAutoGUI.

**Parameters:**
 (same as `double_click`)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError` if both attempts fail.

------

### `drag_and_drop(source_locator, target_locator, timeout=10)`

**Description:**
 Drag an element from source to target using Selenium.

**Parameters:**

- `source_locator` (`str`): XPath of source element.
- `target_locator` (`str`): XPath of target element.
- `timeout` (`int`, optional)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `select_by_visible_text(locator, text, timeout=10)`

**Description:**
 Select an option from a dropdown by visible text.

**Parameters:**

- `locator` (`str`)
- `text` (`str`)
- `timeout` (`int`)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `select_by_value(locator, value, timeout=10)`

**Description:**
 Select an option from a dropdown by `value` attribute.

**Parameters:**
 (same as above, `value` instead of `text`)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `select_by_index(locator, index, timeout=10)`

**Description:**
 Select an option from a dropdown by its index.

**Parameters:**
 (same as above, `index` is `int`)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `switch_to_window(window_name)`

**Description:**
 Switch to a browser window by name or handle.

**Parameters:**

- `window_name` (`str`)

**Returns:**
 `None`

------

### `switch_to_frame(frame_reference)`

**Description:**
 Switch focus to a frame.

**Parameters:**

- `frame_reference` (`str | WebElement | int`)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `switch_to_default_content()`

**Description:**
 Switch focus back to the default page content.

**Parameters:**
 *None*

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `accept_alert()`

**Description:**
 Accept a browser alert popup.

**Parameters:**
 *None*

**Returns:**
 `None`

------

### `dismiss_alert()`

**Description:**
 Dismiss a browser alert popup.

**Parameters:**
 *None*

**Returns:**
 `None`

------

### `take_screenshot(file_path)`

**Description:**
 Take a screenshot via Selenium or fallback to PyAutoGUI.

**Parameters:**

- `file_path` (`str`): File path to save the screenshot.

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `execute_script(script)`

**Description:**
 Execute JavaScript synchronously in browser context.

**Parameters:**

- `script` (`str`)

**Returns:**
 `any` — The result of the script.

------

### `execute_async_script(script)`

**Description:**
 Execute JavaScript asynchronously.

**Parameters:**
 (same as above)

**Returns:**
 `any`

------

### `wait_for_element_visible(locator, timeout=10)`

**Description:**
 Wait until an element is visible.

**Parameters:**
 (same as earlier)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

------

### `wait_for_element_clickable(locator, timeout=10)`

**Description:**
 Wait until an element is clickable.

**Parameters:**
 (same as earlier)

**Returns:**
 `None`

**Raises:**

- `OperationTimeoutError`

<br>

### PyAutoGUI Dialog Actions

### `show_alert(message)`

**Description:**
 Show an alert dialog box.

**Parameters:**

- `message` (`str`)

**Returns:**
 `None`

------

### `show_confirm(message)`

**Description:**
 Show a confirm dialog box.

**Parameters:**
 (same as above)

**Returns:**
 `bool` — User’s choice.

------

### `show_prompt(message)`

**Description:**
 Show a prompt dialog to accept text input.

**Parameters:**
 (same)

**Returns:**
 `str` — User input.

<br>

### PyAutoGUI Keyboard Actions

### `press_key(key)`

**Description:**
 Simulate pressing a single key.

**Parameters:**

- `key` (`str`)

------

### `press_hotkey(*keys)`

**Description:**
 Simulate pressing a key combination.

**Parameters:**

- `*keys` (`str`): Any number of keys.

------

### `hold_and_release(keys, hold_time=0.5)`

**Description:**
 Hold keys for a specified time.

**Parameters:**

- `keys` (`list[str]`)
- `hold_time` (`float`)

------

### `type_text(text, interval=0.05)`

**Description:**
 Simulate typing text.

**Parameters:**

- `text` (`str`)
- `interval` (`float`)

<br>

### PyAutoGUI Mouse Actions

### `move_to(x, y, duration=0.5)`

Move the mouse cursor to a screen coordinate.

- Parameters:
  - x (int): X coordinate
  - y (int): Y coordinate
  - duration (float, optional): Movement duration in seconds. Default: 0.5
- Returns: None

------

### `drag_to(x, y, duration=0.5)`

Drag the mouse from current position to target.

- Parameters:
  - x (int): Target X
  - y (int): Target Y
  - duration (float): Duration of drag
- Returns: None

------

### `scroll(amount)`

Scroll the mouse vertically.

- Parameters:
  - amount (int): Positive = up, negative = down
- Returns: None

------

### `get_mouse_position()`

Returns the current mouse position.

- Returns: Tuple[int, int] — (x, y)

<br>

### PyAutoGUI Screen Pixel & Image Actions

### `get_pixel_color(x, y)`

Get RGB color of pixel at (x, y).

- Parameters:
  - x (int)
  - y (int)
- Returns: Tuple[int, int, int] — RGB

------

### `pixel_matches_color(x, y, expected_color)`

Check if pixel at (x, y) matches given color.

- Parameters:
  - x (int)
  - y (int)
  - expected_color (tuple[int, int, int])
- Returns: bool

------

### `locate_image_on_screen(image_path, confidence=0.9)`

Find image on screen using template matching.

- Parameters:
  - image_path (str): Path to template image
  - confidence (float): Match threshold (0–1)
- Returns: Tuple[int, int] — Center of match or None

<br>

### Pynput Keyboard & Mouse Listener Actions

### `press_key_pynput(key)`

Press a key using pynput.

- Parameters:
  - key (str)
- Returns: None

------

### `release_key_pynput(key)`

Release a key using pynput.

- Parameters:
  - key (str)
- Returns: None

------

### `press_and_hold_pynput(keys, hold_time=0.5)`

Hold down keys and release after time.

- Parameters:
  - keys (list[str])
  - hold_time (float)
- Returns: None

------

### `start_keyboard_listener(on_press_func)`

Start a background keyboard listener.

- Parameters:
  - on_press_func (Callable): Function to call on key press
- Returns: pynput.keyboard.Listener

------

### `start_mouse_listener(on_click_func)`

Start a background mouse click listener.

- Parameters:
  - on_click_func (Callable): Function to call on mouse click
- Returns: pynput.mouse.Listener

<br>

### Class: Browser

Located in: autoflex/web_manager.py

------

### `start(browser_type='chrome', remote_url=None, config_path=None)`

Start a Selenium WebDriver session.

- Parameters:
  - browser_type (str): "chrome" | "firefox" | "edge"
  - remote_url (str, optional): Remote WebDriver address
  - config_path (str, optional): Path to JSON config
- Returns: webdriver instance

------

### `get_driver()`

Return the current active WebDriver.

- Returns: webdriver instance

------

### `quit()`

Terminate WebDriver session.

- Returns: None

---

© 2025 AutoFlex. Built by Zhiyuan Li