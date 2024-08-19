import matplotlib.pyplot as plt
from sympy import simplify
from sympy.abc import x as sym_x


# A method that interpolates the value of y for a given xi using the Lagrange interpolation polynomial
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        yi = y_values[i]
        for j in range(n):
            if j != i:
                yi *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += yi
    return result


# Method for writing the interpolation Lagrange polynomial in abbreviated form
# (uses the simplification method from the sympy library)
def lagrange_polynomial_equation(x_values, y_values):
    n = len(x_values)
    equation = 0
    for i in range(n):
        yi = y_values[i]
        for j in range(n):
            if j != i:
                yi *= (sym_x - x_values[j]) / (x_values[i] - x_values[j])
        equation += yi
    equation = simplify(equation)
    return equation


def plot_interpolation(x, y, x_values, y_values):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Interpolation Nodes', color='red', s=70, zorder=8)
    plt.plot(x_values, y_values, label='Interpolation Lagrange Polynomial', marker='o')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrange Polynomial Interpolation')
    plt.grid(True)
    plt.show()


def input_data():
    file_input = input("Do you want to input values from a file? (y/n): ").lower()

    if file_input == 'y':
        file_name = input("Enter name of file: ")
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                if len(lines) != 2:
                    raise ValueError("File should contain exactly two lines.")
                x_values = [float(val) for val in lines[0].strip().split()]
                y_values = [float(val) for val in lines[1].strip().split()]
        except FileNotFoundError:
            print("File not found. Exiting.")
            exit()
        except ValueError as e:
            print(f"Error: {e}")
            exit()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            exit()
    else:
        x_str = input("Enter the values of x separated by spaces: ")
        y_str = input("Enter the values of y separated by spaces: ")
        x_values = [float(val) for val in x_str.split()]
        y_values = [float(val) for val in y_str.split()]

        if len(y_values) != len(x_values):
            raise ValueError("Number of y values should match number of x values.")

    return x_values, y_values


# Input data
x_vals, y_vals = input_data()

# Extended array x for a smoother polynomial graph
detailed_x = []
for i in range(len(x_vals) - 1):  # Walking through the X's
    detailed_x.extend([x_vals[i] + (x_vals[i + 1] - x_vals[i]) * j / 10 for j in range(11)])  # Add 10 values between the gaps between the initial x

# Calculate interpolation values using the Lagrange polynomial for a more detailed graph
interpolated_y_values_detailed = [lagrange_interpolation(x_vals, y_vals, xi) for xi in detailed_x]

# Calculation of interpolation values using the Lagrange polynomial for the main x_vals
interpolated_y_values = [lagrange_interpolation(x_vals, y_vals, xi) for xi in x_vals]

# Graphing an interpolation polynomial
plot_interpolation(x_vals, y_vals, detailed_x, interpolated_y_values_detailed)

print("Interpolated y values for the main x values:", interpolated_y_values)
print("Lagrange Polynomial Equation:", lagrange_polynomial_equation(x_vals, y_vals))
