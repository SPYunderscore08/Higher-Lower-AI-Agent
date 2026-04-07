from Neuron import *
from NetworkLayer import *

class NeuralNetwork:
    def __init__(self, number_of_inputs: int, number_of_hidden_layers: int , hidden_layer_size: int, number_of_outputs: int):
        self.input_layer = NetworkLayer(number_of_inputs)
        self.hidden_layers = [NetworkLayer(hidden_layer_size) for _ in range(number_of_hidden_layers)]
        self.output_layer = NetworkLayer(number_of_outputs)

    def calculate_result(self, input_list: list):
        pass
