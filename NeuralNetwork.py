import random

from Neuron import *
from NetworkLayer import *

class NeuralNetwork:
    def __init__(self, number_of_inputs: int, number_of_hidden_layers: int , hidden_layer_size: int, number_of_outputs: int):
        self.input_layer = NetworkLayer(number_of_inputs)
        self.hidden_layers = [NetworkLayer(hidden_layer_size) for _ in range(number_of_hidden_layers)]
        self.output_layer = NetworkLayer(number_of_outputs)
        self.assign_weight_matrices()

    def assign_weight_matrices(self):
        tmp = self.generate_weight_matrix(self.input_layer.size, self.hidden_layers[0].size)
        self.input_layer.next_weight_matrix = tmp
        self.hidden_layers[0].prev_weight_matrix = tmp

        for i in range(1, len(self.hidden_layers)):
            tmp = self.generate_weight_matrix(self.hidden_layers[i].size, self.hidden_layers[i - 1].size)
            self.hidden_layers[i - 1].next_weight_matrix = tmp
            self.hidden_layers[i].prev_weight_matrix = tmp

        tmp = self.generate_weight_matrix(self.hidden_layers[-1].size, self.output_layer.size)
        self.hidden_layers[-1].next_weight_matrix = tmp
        self.output_layer.prev_weight_matrix = tmp

    def generate_weight_matrix(self, rows: int, columns: int):
        return list([random.random() for _ in range(columns)] for _ in range(rows))

    def calculate_result(self, input_list: list):
        pass
