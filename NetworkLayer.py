from math import e

from Neuron import *

class NetworkLayer:
    def __init__(self, neurons: list, previous_layer: 'NetworkLayer', next_layer: 'NetworkLayer'):
        self.neurons = neurons
        self.previous_layer = previous_layer
        self.next_layer = next_layer

    def calculate_next_layer(self):
        for neuron in self.next_layer.neurons:
            neuron.activation = 1 / (1 + e ** (self.do_linear_transformation(neuron)))


    def do_linear_transformation(self, neuron: Neuron):
        linear_transformation: float = 0.0
        for i in self.neurons:
            linear_transformation += self.neurons[i].activation * neuron.previous_neuron_weights[i]
            
        linear_transformation += neuron.bias
        return linear_transformation