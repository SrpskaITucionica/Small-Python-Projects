'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''

'''
    Unit values are (string):
    C - celsius
    K - kelvin
    F - Fahrenheit
'''


def temperature_unit_converter(amount, unit1, unit2):
    result = 0

    if unit1 == 'C' and unit2 == 'K':
        result = amount + 273.15
        return f'{amount} Celsius is equal to {result} Kelvin'
    elif unit1 == 'C' and unit2 == 'F':
        result = 9 / 5 * amount + 32
        return f'{amount} Celsius is equal to {result} Fahrenheit'

    if unit1 == 'K' and unit2 == 'C':
        result = amount - 273.15
        return f'{amount} Kelvin is equal to {result} Celsius'
    elif unit1 == 'K' and unit2 == 'F':
        result = 9 / 5 * (amount - 273.15) + 32
        return f'{amount} Kelvin is equal to {result} Fahrenheit'

    if unit1 == 'F' and unit2 == 'C':
        result = 5 / 9 * (amount - 32)
        return f'{amount} Fahrenheit is equal to {result} Celsius'
    elif unit1 == 'F' and unit2 == 'K':
        result = 5 / 9 * (amount - 32) + 273.15
        return f'{amount} Fahrenheit is equal to {result} Kelvin'
