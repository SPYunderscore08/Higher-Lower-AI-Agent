import random

class HigherLower:
    number_to_guess: int # rename
    def __init__(self):
        self.start_new_game()

    def start_new_game(self):
        self.number_to_guess = random.randint(0, 100)

    def try_guess(self, guess: int):
        if guess < self.number_to_guess:
            print("Higher")
            return -1

        elif guess > self.number_to_guess:
            print("Lower")
            return 1

        print("Correct")
        return 0