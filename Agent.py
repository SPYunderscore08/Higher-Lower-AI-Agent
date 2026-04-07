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
        guess = self.network.calculate_result([0.0, 0.0, self.game.tries])
        print("Guess: " + str(int(guess * 100)))
        output = self.game.try_guess(int(guess * 100))
        print("Output: " + str(output))

        while output != 0:
            guess = self.network.calculate_result(
                [
                    1 if output == 1 else 0,
                    1 if output == -1 else 0,
                    self.game.tries
                ]
            )
            print("Guess: " + str(int(guess * 100)))
            output = self.game.try_guess(int(guess * 100))
            print("Output: " + str(output))
            time.sleep(0.2)


    def train(self): # training process, todo could maybe call play()
        pass

