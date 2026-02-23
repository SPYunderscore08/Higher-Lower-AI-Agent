from HigherLower import *
from NeuralNetwork import *

class Agent:
    def __init__(self, network: NeuralNetwork = NeuralNetwork()):
        self.network = network
        self.game = HigherLower()

    def play(self):  # playing the game, basically training, but i guess without mutation; i.e. performance check
        pass

    def train(self): # training process, todo could maybe call play()
        pass

