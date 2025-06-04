# AutoFlex

[![PyPI version](https://img.shields.io/pypi/v/autoflex.svg)](https://pypi.org/project/autoflex/) [![Python Versions](https://img.shields.io/pypi/pyversions/autoflex.svg)](https://pypi.org/project/autoflex/) [![License](https://img.shields.io/pypi/l/autoflex.svg)](LICENSE)

<br>

## Overview

**AutoFlex** is a comprehensive automation framework integrating Selenium, PyAutoGUI, and Pynput to enable flexible web and system-level automation. Designed for ease of use and extensibility, AutoFlex provides unified APIs to perform browser automation, GUI interaction, and advanced input control, empowering developers and testers to build robust automation workflows effortlessly.

<br>


## Features

- Seamless integration of Selenium for browser automation  
- System-level input automation using PyAutoGUI  
- Advanced keyboard and mouse control with Pynput  
- Unified and consistent API design  
- Support for complex automation scenarios beyond browser scope  
- Configurable logging, wait strategies, and error handling  
- Easy to extend and customize for different automation needs

<br>

## Installation

Install the latest stable version from PyPI:

```bash
pip install autoflex
```

<br>

## Quick Start

Here is a basic example to get started with AutoFlex:

```python
from autoflex.web_manager import Browser
from autoflex.actions import Actions

# Start browser
driver = Browser.start(browser_type="chrome")

# Open a webpage
driver.get("https://www.example.com")

# Perform actions using unified APIs
Actions.click(locator="//*[@id='submit-button']")
Actions.input_text(locator="//*[@id='username']", text="test_user")

# Close browser
Browser.quit()
```
For detailed usage, please refer to the [official documentation](https://lzyeil.github.io/AutoFlex/).

<br>

## Contributing
Contributions are welcome! Please follow the guidelines below:

1. Fork the repository

2. Create a new feature branch (```git checkout -b feature-name```)

3. Commit your changes (```git commit -m 'Add feature'```)

4. Push to the branch (```git push origin feature-name```)

5. Open a Pull Request

*Please ensure all tests pass and the code style is consistent.*

<br>

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit) - see the [LICENSE file](https://github.com/LZYEIL/AutoFlex/blob/main/LICENSE) for details.

<br>

## Disclaimer
AutoFlex is provided “as is” without warranty of any kind. Use at your own risk.
