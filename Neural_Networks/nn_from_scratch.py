import pandas as pd
import numpy as np

# Create an NOR truth table
df = pd.DataFrame({'x1':  [0, 1, 0, 1],
                    'x2': [0, 0, 1, 1],
                    'y':  [1, 1, 1, 0]})

# Create activation function
def sigmoid(x):
    '''
    Sigmoid is good for 'squashing' values

    Good for probability based outcomes

    Keeps output from 0 to 1
    '''
    return 1 / (1 + np.exp(-x))

# Get deriviative of activation function
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Get inputs
inputs = np.array(df[['x1', 'x2']]).astype('float')

# Get correct output
correct_output = np.array(df['y']).reshape(-1, 1).astype('float')

# Initiate weights
weights = 2 * np.random.random((2, 1)) - 1

# Create a bias
bias = np.zeros(inputs.shape[0])

# Print Data
print(f'Inputs:\n{inputs}\n')
print(f'Correct Output:\n{correct_output}\n')
print(f'Weights:\n{weights}\n')
print(f'Bias:\n{bias}\n')

# Iterate through and update our weights and bias X amount of times
for iteration in range(10000):
    # Get our weighted sum
    weighted_sum = np.dot(inputs, weights) + bias.reshape(-1, 1)

    # Get our output
    activated_output = sigmoid(weighted_sum)

    # Get the error
    error = correct_output - activated_output

    # Create our adjustments
    adjustments = error * sigmoid_derivative(activated_output)
    
    # Update the weights with the adjustment
    weights = weights + np.dot(inputs.T, adjustments) 
    
    # Update our bias
    bias += np.sum(adjustments, axis=1)


# Since our output is 0 or 1, we'll create a rounded ouput
rounded_activated_output = []
for x in activated_output:
    rounded_activated_output.append([int(round(x[0]))])

# Print our end result
print(f'Weights:\n {weights}\n')
print(f'Activated Outputs:\n{activated_output}')
print(f'Activated Outputs(Rounded):\n{rounded_activated_output}')
print(f'Error:\n {error}\n')