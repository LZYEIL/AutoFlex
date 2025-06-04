---
title: Use Case
layout: default
nav_order: 2
permalink: /use-case
---

## Use Case

For those of you who are new and could not understand the functionalities of AutoFlex described in the *Overview*, here is a detailed version of what it means and what it can do:

**AutoFlex** is purpose-built for scenarios where traditional web automation frameworks fall short, or where system-level interactions must complement browser-based work flows. Below are common cases where AutoFlex delivers unique value:

<br>

### Automating Non-Standard Web Elements
Modern web applications often include custom UI components such as:
- `canvas`-based drawing areas
- `span` elements styled to behave like input fields
- Modal dialogs without standard HTML controls
- Drag-and-drop interfaces

In these cases, Selenium alone is insufficient. AutoFlex seamlessly integrates PyAutoGUI to simulate precise mouse and keyboard interactions at specific screen positions, bypassing DOM limitations.

<br>



### Handling Native System Dialogs

When a web application triggers native OS dialogs like file pickers or alert boxes, Selenium has no access to those system windows. AutoFlex bridges this gap with PyAutoGUI and Pynput, enabling:
- Automated file uploads/download confirmations
- System pop-up dismissal
- Automated screenshots on specific triggers



<br>

### Combining Web and Desktop Automation

AutoFlex shines in hybrid work flows that involve both browser and desktop application control. Examples:
- Taking screenshots of both browser content and desktop apps
- Automating desktop testing tools alongside browser-based dashboards

<br>

### Global Keyboard and Mouse Event Monitoring

For automation scenarios requiring:
- Global hotkey triggers (e.g. `Ctrl+Shift+Q` to terminate a test)
- Real-time mouse click monitoring
- Background keyboard activity logging

AutoFlex leverages Pynput to provide lightweight, reliable event listeners independent of browser context.



<br>

## Summary

Whether you're dealing with complex web UIs, hybrid desktop + web workflows, or system-level interactions beyond browser boundaries, **AutoFlex simplifies the entire process with a clean, integrated API** — no separate tools, no redundant code, no fuss.

---

© 2025 AutoFlex. Built by Zhiyuan Li