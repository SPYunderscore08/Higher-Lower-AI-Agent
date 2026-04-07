from Agent import *


def main():
    network: NeuralNetwork = NeuralNetwork(3, 2, 5, 100)
    ai: Agent = Agent(network)
    ai.play()

if __name__ == "__main__":
    main()