import time
from math import sin

from HigherLower import *
from NeuralNetwork import *

class Agent:
    def __init__(self, network: NeuralNetwork):
        self.network = network
        self.game = None

    def play(self):  # playing the game, basically training, but i guess without mutation; i.e. performance check
        self.game = HigherLower()
        guess = int(self.network.calculate_result([0.0, 0.0, self.game.tries]) * 100)
        print("Guess: " + str(guess))
        output = self.game.try_guess(guess)
        print("Output: " + str(output))

        while output != 0:
            guess = int(self.network.calculate_result(
                [
                    1 if output == 1 else 0,
                    1 if output == -1 else 0,
                    self.game.tries
                ]
            ) * 100)
            print("Guess: " + str(guess))
            output = self.game.try_guess(guess)
            print("Output: " + str(output))
            time.sleep(0.2)


    def train(self): # training process, todo could maybe call play()
        pass

