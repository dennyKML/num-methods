# Numerical Methods Project

This project contains Python implementations of various numerical methods for solving systems of linear equations, finding roots of equations, etc. Below is a brief description of the content in each directory.

## 00-gaussian-method

This directory contains code to solve systems of linear equations using the Gaussian elimination method.

- **`main.py`**: 
  - Contains the implementation of the Gaussian elimination method.
  - The script prompts the user to input a matrix either manually or from a file, performs the elimination process, and checks the correctness of the results.
  - It also includes functions to print matrices and calculate the determinant of a 3x3 matrix.

- **`matrix1.txt`** and **`matrix2.txt`**:
  - Sample data files containing a 3x4 matrix for testing the Gaussian elimination method.

## 01-simple-iterations

This directory contains code to solve systems of linear equations using the simple iterations method.

- **`main.py`**:
  - Implements the simple iterations method to solve linear systems.
  - It checks the convergence condition before iterating and calculates the solution iteratively.
  - The code also includes functions to check matrix conditions and calculate the determinant of a matrix.

## 02-dichotomy-method

This directory contains code to find roots of a cubic equation using the dichotomy method.

- **`main.py`**:
  - Implements the dichotomy method to find roots of a cubic equation within a specified interval.
  - The script allows the user to input the interval and precision, and then it finds the roots by iteratively halving the interval until the desired precision is reached.

## 03-approximation

This directory contains code for polynomial approximation using least squares method.

- **`main.py`**:
  - Implements both linear and quadratic polynomial approximations using the least squares method.
  - The script can input data from a file or manually, calculates the approximation coefficients, and visualizes the results using Matplotlib.
  - The code includes functions for calculating polynomial values, sum of squared errors, and plotting the approximation graphs.

- **`data1.txt`** and **`data2.txt`**:
  - Sample data files for testing Lagrange interpolation. Each file contains two lines: the first line represents the x-values, and the second line represents the corresponding y-values.

## 04-interpolation

This directory contains code for performing Lagrange polynomial interpolation.

- **`main.py`**:
  - Implements Lagrange interpolation to estimate the value of a function at any point within the interval of provided data points.
  - Includes methods to generate the Lagrange polynomial in its simplified form and to plot the interpolation results using Matplotlib.
  - The script prompts the user to input data either manually or from a file.

- **`data1.txt`** and **`data2.txt`**:
  - Sample data files for testing Lagrange interpolation. Each file contains two lines: the first line represents the x-values, and the second line represents the corresponding y-values.

## 05-numerical-integration

This directory contains code to perform numerical integration using different methods.

- **`main.py`**:
  - Implements three methods for numerical integration: the rectangle method, the trapezoidal method, and Simpson's method.
  - The script prompts the user to input the integration limits and the number of segments and then calculates the integral using each method.
  - The results of each method are displayed, along with their average.

## 06-differential-equations

This directory contains code for solving differential equations using the Euler method.

- **`main.py`**:
  - Implements the Euler method for solving first-order ordinary differential equations.
  - The script allows the user to define the differential equation, initial conditions, and step size.
  - The solution is computed and can be plotted using Matplotlib. Additionally, the results can be saved in an Excel file with proper formatting.
  - Includes methods for setting up and customizing Excel output using the openpyxl library.