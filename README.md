# TIHLR Distribution Plotter

This Python script generates the Probability Density Function (PDF) and Cumulative Distribution Function (CDF) for the Type I Half Logistic Rayleigh (TIHLR) distribution, based on user-provided parameters.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)

---

## Installation

### 1. Install Python
1. Download the latest version of Python from the official [Python website](https://www.python.org/downloads/).
2. Run the installer and **check the box** that says **“Add Python to PATH”** during installation.
3. Verify the installation by opening a terminal/command prompt and typing:
    ```bash
    python --version
    ```

### 2. Install Required Libraries
The script uses two Python libraries, **NumPy** and **Matplotlib**. These can be installed using `pip`.

1. Open a terminal or command prompt.
2. Install the libraries by running:
    ```bash
    pip install numpy matplotlib
    ```

---

## Usage

### 1. Clone or Download the Script
Download the Python script `tihlrayleigh.py` and place it in a directory of your choice. You can also copy the code directly into a new Python file.

### 2. Run the Script
1. Open a terminal or command prompt.
2. Navigate to the directory where you saved `tihlrayleigh.py`:
    ```bash
    cd /path/to/your/directory
    ```
3. Run the script:
    ```bash
    python tihlrayleigh.py
    ```

### 3. Input Parameters
After running the script, you will be prompted to input two parameters:
- `a`: The **scale parameter** (must be greater than 0).
- `k`: The **shape parameter** (must be greater than 0).

---

```bash
Enter the value for parameter 'a' (scale parameter, > 0): 1.5
Enter the value for parameter 'k' (shape parameter, > 0): 0.8
```
---
