def f(x):
    return (x**2 - 4.9) / (x**3 + 1.8)
    # return (x + 1) * np.sin(x)


# The rectangle method
def rectangles_method(a, b, n):
    h = (b - a) / n  # Calculate the step of segment division
    integral = 0
    for i in range(n):  # Iterate along each segment up to n-1
        x = (a + i * h) + h / 2  # Calculate the midpoint of the segment using the formula xi + h/2
        integral += f(x)  # Add the value of the function at this point to the sum
    integral *= h  # Multiply the sum by the division step to get the final value of the integral
    return integral


# Trapezoid method
def trapezoidal_method(a, b, n):
    h = (b - a) / n  # Calculate the step of segment division
    integral = (f(a) + f(b)) / 2  # Find the f-values at the edges of the segment and calculate the average
    for i in range(1, n):  # Iterate over each segment from 1 to n-1
        xi = a + i * h  # We calculate xi
        integral += f(xi)  # Add the value of the function at xi to the average sum of the values of f-xi at the edges of the segment
    integral *= h  # Multiply the total sum by the division step to get the final value of the integral
    return integral


# Simpson's method
def simpsons_method(a, b, n):
    h = (b - a) / n  # Calculate the step of segment division
    integral = f(a) + f(b)  # Initialize the variable to save the final result
    for i in range(1, n, 2):  # Calculate the sum with a factor of 4 for odd numbers
        x = a + i * h
        integral += 4 * f(x)
    for i in range(2, n - 1, 2):   # Calculate the sum with a factor of 2 for even numbers (from 2 to n-1, in increments of 2)
        x = a + i * h
        integral += 2 * f(x)
    integral *= h / 3  # Multiply the total by h/3 to get the final value of the integral
    return integral


a_val = float(input("Enter 'a' value: "))
b_val = float(input("Enter 'b' value (b > a): "))
while b_val <= a_val:
    print("Value for 'a' must be less than 'b'. Try again.")
    b_val = float(input("Enter 'b' value (b > a): "))
amount_of_segments = int(input("Enter segments number: "))

rectangle_integral_res = rectangles_method(a_val, b_val, amount_of_segments)
trapezoidal_integral_res = trapezoidal_method(a_val, b_val, amount_of_segments)
simpsons_integral_res = simpsons_method(a_val, b_val, amount_of_segments)

print(f"\nRectangles method result: {rectangle_integral_res}")
print(f"Trapezoidal method result: {trapezoidal_integral_res}")
print(f"Simpson`s method result: {simpsons_integral_res}")

print(f"\nAvg: {(rectangle_integral_res + trapezoidal_integral_res + simpsons_integral_res) / 3}")
