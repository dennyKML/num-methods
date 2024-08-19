def solve_by_simple_iterations(matrix, b, appr_vector, eps):
    if not cond_conv_check(matrix):
        raise "The method of simple iterations may not converge to the solution of the system, or converge very slowly"

    n = len(b)
    x = list(map(float, appr_vector))
    iteration = 0

    # Also can be done with a for loop with statement max_iterations = 1000
    # Iterations of the simple iteration method
    while True:
        # Initialize the new approximation vector with the size of the response vector (and fill it with 0.0)
        next_x = [0.0] * n

        # Start calculating a new approximation for each unknown
        for i in range(n):
            suma = 0

            # Calculate the sum for each equation
            for j in range(n):
                if i != j:
                    suma += matrix[i][j] * x[j]

            # And also calculate the new value of unknown
            next_x[i] = (b[i] - suma) / matrix[i][i]

        print(f"Iteration {iteration}. Prev vector x:\n{x}\nNew vector x:\n{next_x}\n")

        # Check the condition for the end of the iterative process (if the condition is true, the solution is complete)
        if max(abs(next_x[i] - x[i]) for i in range(n)) < eps:
            return next_x, iteration + 1

        # Update the current approximation vector
        x = next_x
        iteration += 1


# Checking if the method convergence condition is met
def cond_conv_check(matrix):
    # If the determinant of the matrix is not zero, the method of simple
    # iterations may not converge to a solution of the system
    if det(matrix) == 0:
        raise ValueError("Det shouldn't be 0!")

    n = len(matrix)

    for i in range(n):
        suma = 0
        # Calculate the sum of the moduli of the non-diagonal elements for each equation
        for j in range(n):
            if i != j:
                suma += abs(matrix[i][j])
        # If the sum is less than (or equal to) the modulus of the diagonal element of its equation,
        # the method will not converge
        if suma >= abs(matrix[i][i]):
            return False

    return True


# Calculating the determinant of a matrix of any order
def det(matrix):
    n = len(matrix)

    # If the matrix has a size of 2x2, then we use a simple formula
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    suma = 0
    sign = -1

    for i in range(n):
        # Add to the sum, taking into account the sign and elements of the first line
        suma = suma + (sign ** i) * matrix[0][i] * det(minor_matrix(matrix, i))

    return suma


# Calculating the minor of a matrix
def minor_matrix(matrix, k):
    res = []

    # We go through the rows of the matrix, except for the first one
    # (each element of this row is already used as part of the determinant in the recursive calculation)
    for row in matrix[1:]:
        new_row = []

        # Go through the elements of the row, except for the k-th
        for j in range(len(row)):
            if j != k:
                new_row.append(row[j])

        res.append(new_row)  # Add a new row to the minor
    return res


# Given a system of equations and an initial approximation
m = int(input("Enter your number in the group: "))
a_matrix = [[5, 1, -1, 1], [1, -4, 1, -1], [-1, 1, 4, 1], [1, 2, 1, -5]]
b_matrix = [3 * m, m - 6, 15 - m, m + 2]
initial_appr = [0.7 * m, 1, 2, 0.5]

# Solution accuracy
epsilon = 0.005

solution, iterations = solve_by_simple_iterations(a_matrix, b_matrix, initial_appr, epsilon)
print(f"Solution: {solution}\n"
      f"Number of iterations: {iterations}")
