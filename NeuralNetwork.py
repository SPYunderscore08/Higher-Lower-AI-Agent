from Neuron import *
from NetworkLayer import *

class NeuralNetwork:
    def __init__(self):
        pass

    @classmethod
    def __init__other(cls, input_layer: NetworkLayer, hidden_layers: list, output_layer: NetworkLayer):
        cls.input_layer = input_layer
        cls.hidden_layers = hidden_layers
        cls.output_layer = output_layer