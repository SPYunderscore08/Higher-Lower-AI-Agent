from Neuron import *

class NetworkLayer:
    def __init__(self, size: int):
        self.neurons = [Neuron() for _ in range(size)]