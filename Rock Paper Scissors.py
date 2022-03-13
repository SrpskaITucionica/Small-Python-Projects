from random import choice

'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''

def play_game():
    computer_choices = ['R', 'P', 'S']

    while True:

        computer_hand = choice(computer_choices)
        user_hand = input('''
        What would you like to play:
        R - Rock
        P - Paper
        S - Scissors
        > ''')

        if computer_hand == user_hand.upper():
            print("It's Tie!")
        elif computer_hand == 'R' and user_hand.upper() == 'S':
            print('I have rock')
            print('You have scissors')
            print("I win!")
        elif computer_hand == 'P' and user_hand.upper() == 'R':
            print('I have paper')
            print('You have rock')
            print("I win!")
        elif computer_hand == 'S' and user_hand == 'P':
            print('I have scissors')
            print('You have paper')
            print("I win!")
        else:
            print('You win!')

        play_again = input('''
        Do you want to play again:
        Y - yes
        N - no
        > ''')

        if play_again.upper() == 'N':
            break
