import pandas as pd
import numpy as np

class Neural_Network:
    def __init__(self, input_size, hidden_size, output_size, learning_rate, max_gen):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.max_gen = max_gen
        self.create_weights()

    
    def create_weights(self):
        pass

input_frame = pd.read_csv('Lab6/Input/iris.data')
input_frame.columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'species name']

training_data = []
testing_data = []

for species in np.unique(input_frame['species name']):
    training_data.append(input_frame[input_frame['species name'] == species][:40])
    testing_data.append(input_frame[input_frame['species name'] == species][40:])
training_data = pd.concat(training_data)
testing_data = pd.concat(testing_data)
print('Training Data:\n', training_data, '\nTesting Data:\n', testing_data)
network = Neural_Network(2, 2, 1, 0.5, 100)