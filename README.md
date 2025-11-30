# ShowMap Utility
A streamlined Python command-line tool designed to open an address directly in your default web browser using **OpenStreetMap**. The utility accepts input from either **command-line arguments** or the **system clipboard**, ensuring fast and efficient map lookups.

### Overview
`showMap.py` enhances productivity by simplifying address searches. With URL encoding, input validation, and clean code structure, it offers a reliable and professional-grade mapping helper for everyday use.

### Features
-   Accepts addresses via command-line or clipboard.
-   Automatically URL-encodes addresses for correct browser     interpretation.
-   Opens results on **OpenStreetMap**.
-   Structured, readable, and maintainable code.
-   Basic error handling for missing or invalid input.

### Prerequisites
#### **Python Version:**
-   Python 3.7 or higher.

#### **Required Packages:**
-   `pyperclip`

Install dependencies with:
``` bash
pip install pyperclip
```

### Usage
#### **1. Provide an Address via Command Line**
``` bash
python showMap.py 1600 Amphitheatre Parkway Mountain View
```
#### **2. Use Your Clipboard**
Copy an address to your clipboard and run:
``` bash
python showMap.py
```
The utility automatically detects clipboard content and opens the corresponding map.
