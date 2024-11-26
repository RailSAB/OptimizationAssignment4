import numpy as np
import math
def function_first(x):
    return x**3 - 6*(x**2) + 11*x - 6

def function_second(x):
    return (x-2)**2 + 3

def function_third(x):
    return -(x**2) + 4*x + 1

def der_of_function_third(x):
    return -2*x + 4

def bisection_method(f, a, b, eps):
    if f(a) * f(b) > 0:
        return
    n = math.ceil((np.log(b - a) - np.log(eps))/np.log(2))

    for i in range(n):
        mid = (a + b)/2

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid


    return (a + b) / 2


def golden_section_method(f, a, b, eps):
    tau = (5**0.5 - 1)/2

    while np.abs(b - a) > eps:
        c = b - (b - a) * tau
        d = a + (b - a) * tau

        if f(c) < f(d):
            b = d
        else:
            a = c


    return (a + b) / 2, f((a + b) / 2)


def gradient_ascent_method(f, d, x0, alpha, N):
    x = x0

    for i in range(N):
        x += alpha * d(x)

    return x, f(x)


def main():
    print(bisection_method(function_first, 1, 2, 1e-6))
    print(golden_section_method(function_second, 0, 5, 1e-4))
    print(gradient_ascent_method(function_third, der_of_function_third, 0, 0.1, 100))


if __name__ == '__main__':
    main()
