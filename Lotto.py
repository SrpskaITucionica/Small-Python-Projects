import random


class Lotto:

    def __init__(self, *combinations):
        self.user_combinations = []
        self.winning_combination = []
        self.correct_numbers = []
        self.messages = []

        for combination in combinations:
            self.user_combinations.append(combination)

    def generate_winning_lotto_combination(self):
        counter = 0
        while counter < 7:
            rand = random.randint(1, 39)
            if rand not in self.winning_combination:
                self.winning_combination.append(rand)
                counter += 1
            else:
                continue
        return self.winning_combination

    def compare_combinations(self):

        total_correct_numbers = 0
        for combination in self.user_combinations:
            for winning_number in self.winning_combination:
                for number in combination:
                    if winning_number == number:
                        total_correct_numbers += 1
            self.correct_numbers.append(total_correct_numbers)
            total_correct_numbers = 0
        return self.correct_numbers

    def show_results(self):
        for i in range(len(self.correct_numbers)):
            self.messages.append(f'Combination {i+1} has {self.correct_numbers[i]} correct numbers.')
        return self.messages

