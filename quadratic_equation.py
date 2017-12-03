from cmath import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant > 0:
        return root1, root2
    elif discriminant == 0:
        return root1, None
    elif discriminant < 0:
        return None, None


print("Введите коэффициент A")
a = int(input())
print("Введите коэффициент B")
b = int(input())
print("Введите коэффициент C")
c = int(input())
print(get_roots(a, b, c))
