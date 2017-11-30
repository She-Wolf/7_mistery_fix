from math import sqrt
import cmath


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = 0
        root2 = 0
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root1 =0
        root1 =  ((-b - sqrt(discriminant)) / (2 * a))
        return (root1, None)
    elif discriminant < 0:
        root1 = 0
        root2 = 0
        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return (None, None)
