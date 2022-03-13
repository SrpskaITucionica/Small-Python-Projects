import math

'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''


def solve_quadratic_equation(a, b, c):
    solutions = []
    under_root = (b ** 2) - 4 * a * c
    if under_root < 0:
        temp = math.sqrt(abs((under_root))) * 1.0j
        x1 = (-b / (2 * a)) - temp / (2 * a)
        x2 = (-b / (2 * a)) + temp / (2 * a)
    else:
        x1 = (-b - math.sqrt(under_root)) / (2 * a)
        x2 = (-b + math.sqrt(under_root)) / (2 * a)

    solutions.append(x1)
    solutions.append(x2)
    return solutions
