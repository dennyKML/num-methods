def f(x):
    return -(x ** 3) - 1.7 * (x ** 2) + 3.7 * x + 0.5
    # return (x ** 3) - 2.8 * (x ** 2) - 6.2 * x + 3.7


def solve_by_dichotomy(a, b, eps):
    # Until the search is over, we continue to divide the interval
    while abs(b - a) >= 2 * eps:
        mid = (a + b) / 2
        # If the modulus of the value in the middle of the interval is less than the accuracy (close to zero),
        # the root of the equation is found
        if abs(f(mid)) < eps:
            return mid
        # If f(a) * f(mid) < 0, the root is in the first half of the interval
        elif f(a) * f(mid) < 0:
            b = mid
        # Otherwise, the root is in the second half of the interval
        else:
            a = mid

    return (a + b) / 2


def find_roots(a, b, eps, step):
    roots = []
    current = a

    while current <= b:
        interval_begin = current
        interval_end = current + step

        if f(interval_begin) * f(interval_end) < 0:
            print(f"It is possible to find the root at [{interval_begin:.2f}; {interval_end:.2f}]")
            # If the gap has a root, let's find it
            root = solve_by_dichotomy(interval_begin, interval_end, eps)
            roots.append(root)

            current += step
        else:
            current += step

    return roots


leftBound = float(input("Enter the left boundary of the interval a: "))
rightBound = float(input("Enter the right boundary of the interval a: "))
intervalStep = float(input("Enter the interval step: "))
epsilon = float(input("Enter the epsilon (precision) value: "))

print()

answer = find_roots(leftBound, rightBound, epsilon, intervalStep)
print("\nRoots of the cubic equation: ", answer)
