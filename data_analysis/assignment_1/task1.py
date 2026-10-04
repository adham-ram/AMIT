import numpy as np
def array_operations (mode, shape, value=None):
    if mode == 'zeros':
        return np.zeros(shape)
    elif mode == 'ones':
        return np.ones(shape)
    elif mode == 'full':
        return np.full(shape, value)
    elif mode == 'identity':
        if len(shape) != 2 or shape[0] != shape[1]:
            raise ValueError("Identity matrix must be square (shape must be (n, n)).")
        return np.eye(shape[0])
    else:
        raise ValueError("Invalid mode. Choose from 'zeros', 'ones', or 'full'.")
input_mode = input("Enter the mode ('zeros', 'ones', 'full', or 'identity'): ")
input_shape = input("Enter the shape of the array (e.g., 2,3 for a 2x3 array): ")
input_value = input("Enter the value for the 'full' mode (optional): ")

if input_value:
    print(array_operations(input_mode, tuple(map(int, input_shape.split(','))), float(input_value)))
else:
    print(array_operations(input_mode, tuple(map(int, input_shape.split(',')))))