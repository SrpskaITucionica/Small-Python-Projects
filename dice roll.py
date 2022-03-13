import random

'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''

def roll_dices_game():
    while True:
        dice_one = random.randint(1, 6)  # Generates number in range 1-6
        dice_two = random.randint(1, 6)  # Generates number in range 1-6
        print(f' You got {dice_one} and {dice_two}.')
        response = input('''
        Do you want to role again? 
        y - yes
        n - no
        > ''')
        if response.lower() == 'y':
            continue
        else:
            break


