import matplotlib.pyplot as plt


# A method for calculating linear polynomial approximation coefficients
def least_squares_linear(x, y):
    n = len(x)  # Find the number of elements in the list x

    # Calculating the sums for the formulas for calculating the coefficients a and b
    sum_x = sum(x)  # Sum of all X's
    sum_y = sum(y)  # Sum of all Y's
    sum_x_squared = sum(x[i] ** 2 for i in range(n))  # Sum of all squares of X's
    sum_xy = sum(x[i] * y[i] for i in range(n))  # The sum of all x * y

    # Calculating coefficients using the formulas of the least squares method for a linear polynomial
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b


# A method for calculating the approximation coefficients of a quadratic polynomial
def least_squares_quad(x, y):
    n = len(x)

    # Calculating the sums for the formulas for calculating the coefficients a, b and c
    sum_x = sum(x)  # Sum of all X's
    sum_y = sum(y)  # Sum of all Y's
    sum_x_squared = sum(x[i] ** 2 for i in range(n))  # Sum of all squares of X's
    sum_xy = sum(x[i] * y[i] for i in range(n))  # The sum of all x * y
    sum_x_cubed = sum(x[i] ** 3 for i in range(n))  # Sum of all X's to the third power
    sum_x_fourth = sum(x[i] ** 4 for i in range(n))  # Sum of all X's to the fourths power
    sum_x_squared_y = sum((x[i] ** 2) * y[i] for i in range(n))  # The sum of all x**2 * y

    # Formation of matrices for solving a system of equations
    a_matrix = [
        [sum_x_squared, sum_x, n],
        [sum_x_cubed, sum_x_squared, sum_x],
        [sum_x_fourth, sum_x_cubed, sum_x_squared]
    ]
    b_matrix = [sum_y, sum_xy, sum_x_squared_y]

    # Solving a system of equations by the Gaussian method
    coefficients = solve_by_gauss(a_matrix, b_matrix)

    return coefficients


# Method for solving a system of equations by the Gaussian method
def solve_by_gauss(a_matrix, b_matrix):
    n = len(a_matrix)
    matrix = [[a_matrix[i][j] for j in range(n)] + [b_matrix[i]] for i in range(n)]

    # Direct Gaussian method for reducing a matrix to a triangular shape
    for i in range(n):
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Reversal of the Gaussian method
    coefficients = [0] * n
    for i in range(n - 1, -1, -1):
        coefficients[i] = matrix[i][n]
        for j in range(i + 1, n):
            coefficients[i] -= matrix[i][j] * coefficients[j]
        coefficients[i] /= matrix[i][i]

    return coefficients


# Method for calculating the values of a polynomial
def calc_polynom(coefficients, x):
    if len(coefficients) == 2:  # If the number of coefficients is 2 (linear polynomial)
        return [coefficients[0] * xi + coefficients[1] for xi in x]
    elif len(coefficients) == 3:  # If the number of coefficients is 3 (quadratic polynomial)
        return [coefficients[0] * xi ** 2 + coefficients[1] * xi + coefficients[2] for xi in x]


# Sum of squares of deviations for a linear polynomial
def sum_squared_errors_linear(x, y, a, b):
    return sum((yi - (a * xi + b))**2 for xi, yi in zip(x, y))


# Sum of squares of deviations for a quadratic polynomial
def sum_squared_errors_quadratic(x, y, c, d, e):
    return sum((yi - (c * xi**2 + d * xi + e))**2 for xi, yi in zip(x, y))


# Method for building a graph of approximations
def plot_approximations(x, y, linear_cofs, quadratic_cofs, detail_x=None):
    # Building approximation graphs
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Approximation points', color='red', s=70, zorder=8)

    # Building a linear approximation graph
    linear_values = calc_polynom(linear_cofs, x)
    plt.plot(x, linear_values, label='Linear Approximation', marker='o')

    # Graphing the quadratic approximation
    quadratic_values = calc_polynom(quadratic_cofs, x)
    plt.plot(x, quadratic_values, label='Quadratic Approximation', marker='o')

    if detail_x:
        quadratic_values = calc_polynom(quadratic_cofs, detail_x)
        plt.plot(detail_x, quadratic_values, label='Quadratic Approximation (Detailed)')
        for i, xi in enumerate(x):
            if xi in detail_x:
                plt.scatter(xi, quadratic_values[detail_x.index(xi)], color='green', zorder=5)

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Approximation')
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

# Calculating coefficients for linear and quadratic polynomials
linear_coeffs = least_squares_linear(x_vals, y_vals)
quadratic_coeffs = least_squares_quad(x_vals, y_vals)

# Calculating sums of squared errors for linear and quadratic polynomials
linear_sse = sum_squared_errors_linear(x_vals, y_vals, *linear_coeffs)
quadratic_sse = sum_squared_errors_quadratic(x_vals, y_vals, *quadratic_coeffs)

# Calculate polynomial values for a more detailed graph
detailed_x = []
for i in range(len(x_vals) - 1):  # Walking through the X's
    detailed_x.extend([x_vals[i] + (x_vals[i + 1] - x_vals[i]) * j / 10 for j in range(11)])  # Add 10 values between the gaps between the initial x

# Building a graph of approximations
plot_approximations(x_vals, y_vals, linear_coeffs, quadratic_coeffs, detailed_x)

print("\nLinear Coefficients:", linear_coeffs)
print("Quadratic Coefficients:", tuple(quadratic_coeffs))

# Print the sums of squares of errors
print("\nLinear Sum of Squared Errors:", linear_sse)
print("Quadratic Sum of Squared Errors:", quadratic_sse)

if linear_sse < quadratic_sse:
    print("A linear polynomial is a better fit for this data set!")
elif quadratic_sse < linear_sse:
    print("A quadratic polynomial is a better fit for this data set!")
else:
    print("There is no difference in choosing the best polynomial for this data set!")
