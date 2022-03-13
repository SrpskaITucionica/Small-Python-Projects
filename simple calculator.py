'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''

'''
    IMPORTANT: In this type of calculator, division can not be used due to the simple fact that initial value 
    can't be put precisely.
    
    This calculator is just an example of how to connect different functions into one main function
    The use of this calculator is quite limited
'''


def main():
    user_option = int(input('''
    Select operation:
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    > '''))

    if user_option == 1:
        addition()
    elif user_option == 2:
        subtraction()
    elif user_option == 3:
        multiplication()


def addition():
    total = 0
    print('''
    Let's do some addition (Type 0 to stop)''')
    print('----------------------------------------------')
    user_input = None

    while True:
        user_input = float(input('> '))

        if user_input == 0:
            break
        else:
            total += user_input
            print(f'Current sum is: {total}')

    print(f'Total sum is: {total}')


def subtraction():
    total = 0
    print('''
    Let's do some subtraction (Type 0 to stop)''')
    print('----------------------------------------------')
    user_input = None

    while user_input != 0:
        user_input = float(input('> '))

        if user_input == 0:
            break
        else:
            total -= user_input
            print(f'Current difference is: {total}')

    print(f'Total difference is: {total}')


def multiplication():
    total = 1
    print('''
    Let's do some multiplication (Type 0 to stop)''')
    print('----------------------------------------------')
    user_input = None

    while user_input != 0:
        user_input = float(input('> '))

        if user_input == 0:
            break
        else:
            total *= user_input
            print(f'Current product is: {total}')

    print(f'Total product is: {total}')


main()
