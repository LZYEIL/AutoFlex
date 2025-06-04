---
title: Project Structure
layout: default
nav_order: 3
permalink: /get-started
---

## Project Structure

![Project Structure1](\assets\structure1.png)

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
