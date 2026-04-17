import random

from NetworkLayer import *

"""
I want NeuralNetwork to be a super class of which its child class can use basic methods, like predict() <- more or less static method
Something like Backpropagation would be a inside a child class of NeuralNetwork, i.e. something like "BackpropagationNeuralNetwork", although this is quite long
I want to do this, because then I'll have no conflicts and matches inside the class methods
"""

class NeuralNetwork:
    def __init__(self, number_of_inputs: int, number_of_hidden_layers: int , hidden_layer_size: int, number_of_outputs: int):
        self.input_layer = NetworkLayer(number_of_inputs)
        self.hidden_layers = [NetworkLayer(hidden_layer_size) for _ in range(number_of_hidden_layers)]
        self.output_layer = NetworkLayer(number_of_outputs)

        self.layers = [self.input_layer] + self.hidden_layers + [self.output_layer]
        self.assign_weight_matrices()

    def assign_weight_matrices(self):
        for i in range(1, len(self.layers)):
            weight_matrix = self.generate_weight_matrix(self.layers[i].size, self.layers[i - 1].size)

            self.layers[i - 1].next_layer = self.layers[i]
            self.layers[i].prev_layer = self.layers[i - 1]

            self.layers[i - 1].next_weight_matrix = weight_matrix
            self.layers[i].prev_weight_matrix = weight_matrix

    def evaluate_inputs(self, input_list: list):
        for i in range(len(input_list)):
            self.input_layer.neurons[0].activation = input_list[i]

        self.do_forward_propagation()

    def predict(self, input_list: list): # Deterministic
        self.evaluate_inputs(input_list)
        return self.output_layer.neurons[0].activation

    def do_forward_propagation(self):
        for layer in self.hidden_layers:
            layer.do_forward_propagation_step()

        self.output_layer.do_forward_propagation_step()

    def train(self):
        pass

    @staticmethod
    def generate_weight_matrix(rows: int, columns: int):
        return list([random.random() for _ in range(columns)] for _ in range(rows))


class BackpropagationNetwork(NeuralNetwork): # todo
    def __init__(self, number_of_inputs: int, number_of_hidden_layers: int, hidden_layer_size: int, number_of_outputs: int):
        super().__init__(number_of_inputs, number_of_hidden_layers, hidden_layer_size, number_of_outputs)

    def train(self, desired_output: float): # todo might change int to list for scalability
        pass
