import numpy as np

class NeuralNetwork:

    def __init__(self, num_inputs, num_hidden_neurons, num_outputs):
        self.weights1 = 2 * np.random.random((num_inputs, num_hidden_neurons)) - 1
        self.weights2 = 2 * np.random.random((num_hidden_neurons, num_outputs)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, X, y, iterations):
        for _ in range(iterations):
            layer1_out, layer2_out = self.think(X)
            error2 = y - layer2_out
            delta2 = error2 * self.sigmoid_derivative(layer2_out)
            error1 = delta2.dot(self.weights2.T)
            delta1 = error1 * self.sigmoid_derivative(layer1_out)
            self.weights1 += X.T.dot(delta1)
            self.weights2 += layer1_out.T.dot(delta2)

    def think(self, X):
        layer1_out = self.sigmoid(np.dot(X, self.weights1))
        layer2_out = self.sigmoid(np.dot(layer1_out, self.weights2))
        return layer1_out, layer2_out

if __name__ == "__main__":
    np.random.seed(1)
    nn = NeuralNetwork(3, 4, 1) # 3 input neurons, 4 hidden neurons, 1 output neuron
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]) # Input data for AND gate
    y = np.array([[0], [0], [0], [1]]) # Expected output for AND gate

    print("Initial Weights:")
    print("Layer 1:", nn.weights1)
    print("Layer 2:", nn.weights2)

    nn.train(X, y, 60000)

    print("Trained Weights:")
    print("Layer 1:", nn.weights1)
    print("Layer 2:", nn.weights2)

    test_input = np.array([1, 0, 1]) # Test input for the AND gate
    print("Test Input:", test_input)

    prediction = nn.think(test_input)[1]
    print("Prediction for [1, 0, 1]:", prediction)
