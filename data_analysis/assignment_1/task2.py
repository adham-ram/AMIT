import numpy as np

def secure_reshape_and_stack(data1, data2, new_shape):
    """
    1. Validates and converts inputs to NumPy arrays.
    2. Reshapes the first dataset to a specific dimension.
    3. Vertically stacks both datasets into one matrix.
    """
    try:
        # Convert inputs to ndarray
        arr1 = np.array(data1)
        arr2 = np.array(data2)
        
        
        reshaped_arr1 = arr1.reshape(new_shape)
        
        
        combined_dataset = np.vstack((reshaped_arr1, arr2))
        
        return combined_dataset
        
    except ValueError as e:
        raise ValueError(f"Company-grade Error: {e}")

new_array = secure_reshape_and_stack([1, 2, 3, 4], [[5, 6], [7, 8]], (2, 2))
print(new_array)