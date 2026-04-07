import random

class HigherLower:
    def __init__(self):
        self.start_new_game()
        self.number_to_guess = random.randint(1, 100)
        self.tries = 0

    def start_new_game(self):
        self.number_to_guess = random.randint(1, 100)

    def try_guess(self, guess: int):
        self.tries += 1
        if guess < self.number_to_guess:
            print("Higher")
            return -1

        elif guess > self.number_to_guess:
            print("Lower")
            return 1

        print("Correct")
        return 0

    def get_tries(self):
        return self.tries
