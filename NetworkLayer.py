import math

from Neuron import *

class NetworkLayer:
    def __init__(self, size: int):
        self.size = size

        self.prev_layer = None
        self.next_layer = None
        self.prev_weight_matrix = None
        self.next_weight_matrix = None

        self.neurons = [Neuron() for _ in range(size)]

    def do_forward_propagation_step(self):
        for i in range(len(self.neurons)):
            self.neurons[i].activation = self.sigmoid(self.sum_of_weight_products(i) + self.neurons[i].bias)

    def sum_of_weight_products(self, neuron_index: int):
        sum_of_weighted_products = 0
        for i in range(self.prev_layer.size):
            sum_of_weighted_products += self.prev_layer.neurons[i].activation * self.prev_weight_matrix[neuron_index][i]

        return sum_of_weighted_products

    @staticmethod
    def sigmoid(number):
        return 1 / (1 + math.e ** -number)