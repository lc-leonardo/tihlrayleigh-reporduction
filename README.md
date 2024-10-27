# TIHLR Distribution Plotter

This Python script generates the Probability Density Function (PDF) and Cumulative Distribution Function (CDF) for the Type I Half Logistic Rayleigh (TIHLR) distribution, based on user-provided parameters.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [Citation](#citation)

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

## Example

```bash
Enter the value for parameter 'a' (scale parameter, > 0): 1.5
Enter the value for parameter 'k' (shape parameter, > 0): 0.8
```
---

## Troubleshooting

### Common Issues

1. **'python' is not recognized as an internal or external command'**
   - **Cause:** Python is not installed correctly or not added to your system's PATH.
   - **Solution:** 
     - Ensure that you installed Python and **checked the "Add Python to PATH" option** during installation.
     - You may need to manually add Python to your system's PATH. [Learn how to add Python to PATH](https://docs.python.org/3/using/windows.html#the-full-installer).

2. **Invalid Input Error**
   - **Cause:** An invalid value (e.g., a negative number or a non-numeric value) was input for parameters `a` or `k`.
   - **Solution:** 
     - The parameters `a` and `k` must be positive numbers. If you input an invalid value, the script will display an error message and prompt you to try again.

### Additional Help
If you encounter any other issues or need further assistance, please feel free to open an issue in the repository or reach out for help.

## Citation

This work is inspired by the paper:

Al-Babtain, A. A. (2020). *A new extended Rayleigh distribution*. Journal of King Saud University – Science, 32(4), 2576-2581. [https://doi.org/10.1016/j.jksus.2020.04.015](https://doi.org/10.1016/j.jksus.2020.04.015)

If you use this code or are inspired by it, please also consider citing the original paper.
