from HigherLower import *
from NeuralNetwork import *

class Agent:
    def __init__(self, network: NeuralNetwork):
        self.network = network
        self.game = HigherLower()

    def play(self):
        self.game.start_new_game()

        result = self.guess([0.0, 0.0, 0.0])

        while result != 0:
            self.guess(
                [
                    1 if result == 1 else 0,
                    1 if result == 2 else 0,
                    self.game.tries
                ]
            )

    def guess(self, input_list: list):
        guess = int(self.network.predict(input_list) * 100)
        print("Guess: " + str(guess))

        output = self.game.try_guess(guess)
        print("Output: " + str(output))
        print()

        return output

class SupervisedAgent(Agent):
    def __init__(self, network: NeuralNetwork):
        super().__init__(network)

    def train(self, iterations: int):
        for i in range(iterations):
            self.game.start_new_game()

            result = self.guess([0.0, 0.0, 0.0])
            self.network.train(self.game.number_to_guess)

            while result != 0:
                self.guess(
                    [
                        1 if result == 1 else 0,
                        1 if result == 2 else 0,
                        self.game.tries
                    ]
                )
                self.network.train(self.game.number_to_guess)

class UnsupervisedAgent(Agent):
    def __init__(self, network: NeuralNetwork):
        super().__init__(network)

    def train(self, iterations: int):
        for i in range(iterations):
            self.game.start_new_game()

            result = self.guess([0.0, 0.0, 0.0])
            self.network.train()

            while result != 0:
                self.guess(
                    [
                        1 if result == 1 else 0,
                        1 if result == 2 else 0,
                        self.game.tries
                    ]
                )
                self.network.train()