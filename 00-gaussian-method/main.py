def input_matrix():
    file_input = input("Do you want to input values from a file? (y/n): ").lower()

    if file_input == 'y':
        file_name = input("Enter name of file: ")
        try:
            with open(file_name, 'r') as file:
                matrix = [list(map(float, line.strip().split('\t'))) for line in file]
        except FileNotFoundError:
            print("File not found. Exiting.")
            exit()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            exit()
    else:
        matrix = []
        for i in range(3):
            row = [float(input(f"Enter element [{i + 1}, {j + 1}]: ")) for j in range(3 + 1)]
            matrix.append(row)

    print_precision = int(input("Enter precision for printing results: "))
    round_value = int(input("Enter round value for final answers: "))

    return matrix, round_value, print_precision


def solve_by_gauss(matrix, r_val, precision):
    n = len(matrix)

    copy_matrix = list(map(list, matrix))

    # Output of the initial matrix
    print("\nStart matrix:")
    print_matrix(matrix, precision)

    # If the determinant is zero, the system has many or zero solutions
    if not is_single_solution(matrix):
        print("\nThe system has an infinite number of solutions or no solutions!\n")
        return None

    count = 0
    for i in range(n):
        count = i
        # Step 1: Normalize the row
        pivot = matrix[i][i]
        for j in range(n + 1):
            matrix[i][j] /= pivot

        # Displaying interim results
        print(f"\nStep {i + 1}: Normalize row {i + 1} (pivot: {pivot})")
        print_matrix(matrix, precision)

        # Steps 2-3: Exclusions
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(n + 1):
                matrix[k][j] -= factor * matrix[i][j]

        # Displaying interim results
        print(f"\nStep {i + 1}: Exclude")
        print_matrix(matrix, precision)

    # Reversal of the Gaussian method
    for i in range(n - 1, 0, -1):
        count += 1
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(n + 1):
                matrix[k][j] -= factor * matrix[i][j]

        # Displaying interim results
        print(f"\nStep {count + 1}: Reversed exclusion")
        print_matrix(matrix, precision)

    # Displaying results
    print("\nFinal matrix:")
    print_matrix(matrix, precision)

    print("\nAnswers:")
    for i in range(n):
        x_i = round(matrix[i][n], r_val)
        print(f"x{i + 1} = {x_i}")

    print()

    # Checking the correctness of the results
    for i in range(n):
        equation_sum = sum(copy_matrix[i][j] * round(matrix[j][n], r_val) for j in range(n))
        print(f"{copy_matrix[i][0]} * {round(matrix[0][n], r_val)} + "
              f"{copy_matrix[i][1]} * {round(matrix[1][n], r_val)} + "
              f"{copy_matrix[i][2]} * {round(matrix[2][n], r_val)} = {equation_sum}")
        print(f"Equation {i + 1}: {equation_sum} == {copy_matrix[i][n]}")

        print(f"Abs. tolerance = {abs(equation_sum - copy_matrix[i][n])}. "
              f"Rel. tolerance = {(abs(equation_sum - copy_matrix[i][n]) / abs(equation_sum)) * 100}%\n")


def print_matrix(matrix, precision):
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            print(f"{num:.{precision}f}", end="")
            if i < len(row) - 1:
                print(", ", end="")
        print("]")


def is_single_solution(matrix):
    # Crop the matrix to a 3x3 size
    result_matrix = [row[:3] for row in matrix]

    # Calculate the determinant for a cropped matrix
    det = det_3x3(result_matrix)

    return det != 0


def det_3x3(matrix):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix should be 3x3")

    det = (
            matrix[0][0] * matrix[1][1] * matrix[2][2] +
            matrix[0][1] * matrix[1][2] * matrix[2][0] +
            matrix[0][2] * matrix[1][0] * matrix[2][1] -
            matrix[0][2] * matrix[1][1] * matrix[2][0] -
            matrix[0][0] * matrix[1][2] * matrix[2][1] -
            matrix[0][1] * matrix[1][0] * matrix[2][2]
    )

    return det


start_matrix, round_val, precis = input_matrix()
solve_by_gauss(start_matrix, round_val, precis)
