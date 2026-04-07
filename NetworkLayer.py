from Neuron import *

class NetworkLayer:
    def __init__(self, size: int):
        self.size = size

        self.prev_weight_matrix = None
        self.next_weight_matrix = None
        self.neurons = [Neuron() for _ in range(size)]