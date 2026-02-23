class Neuron:
    def __init__(self, previous_neuron_weights: list, next_neuron_weights: list):
        self.previous_neuron_weights = previous_neuron_weights
        self.next_neuron_weights = next_neuron_weights
        self.activation = 0.0
