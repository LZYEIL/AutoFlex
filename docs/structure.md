---
title: Framework Structure
layout: default
nav_order: 3
permalink: /frme-structure
---

## Framework Structure

<br>

### AutoFlex:

![Project Structure1](https://raw.githubusercontent.com/lzyeil/AutoFlex/main/docs/assets/structure1.png)

- **`.github/workflows/`**
   Contains CI/CD workflows powered by GitHub Actions. For example, `pages.yml` automates deployment of this documentation website.
- **`autoflex/`**
   This is the main package where AutoFlex's functionality lives—utilities, and core framework modules.
- **`docs/`**
   Markdown-based documentation files rendered by Just the Docs. This directory powers the GitHub Pages site. 
- **`logs/`**
   (Optional) For storing logs generated during runtime or debugging. Helpful for tracking issues or reviewing system behavior.
- **`LICENSE`**
   Specifies the open-source license for the project, clarifying usage and distribution rights.
- **`README.md`**
   The main entry point when visiting the GitHub repository. Typically includes an overview, installation guide, and quick usage instructions.



<br>

<br>

### autoflex:

![Project Structure2](https://raw.githubusercontent.com/lzyeil/AutoFlex/main/docs/assets/structure2.png)

- **`__pycache__/`**
   Automatically generated directory that stores compiled `.pyc` files for faster module loading.

- **`config/`**
   Contains configuration-related code. 

- **`core/`**
   The heart of the framework. Includes the main algorithm or workflow engine.

- **`tests/`**
   Tests that validate the correctness of the library.

- **`__init__.py`**
   Marks this directory as a Python package.

- **`pyproject.toml`**
   A modern Python configuration file standardized by [PEP 518](https://www.python.org/dev/peps/pep-0518/).

- **`setup.py`**
   Traditional script used to define package metadata and entry points.



<br>

<br>

### core:

![Project Structure3](https://raw.githubusercontent.com/lzyeil/AutoFlex/main/docs/assets/structure3.png)

- **`pyautogui_actions/`**
   Contains automation logic (*Not Comprehensive*) built with [`PyAutoGUI`](https://pyautogui.readthedocs.io/en/latest/), a library that simulates mouse and keyboard actions on the screen.

- **`pynput_actions/`**
   Contains automation modules (*Not Comprehensive*) that use [`pynput`](https://pynput.readthedocs.io/en/latest/), a library for controlling and monitoring keyboard/mouse events at a lower level.

- **`selenium_actions/`**
   Includes actions implemented (*Not Comprehensive*) using [`Selenium`](https://www.selenium.dev/), a browser automation framework.

- **`actions.py`**
   Acts as a **dispatcher** to unify the various action modules (`pyautogui`, `pynput`, `selenium`). **This is the file you may find most useful.**

- **`config_loader.py`**
   Responsible for loading and validating configuration files.

- **`exceptions.py`**
   Defines custom error classes specific to your framework.

- **`logger.py`**
   Sets up the logging system.

- **`web_manager.py`**
   Handles browser session management using Selenium.



---

© 2025 AutoFlex. Built by Zhiyuan Li
