import numpy as np

def my_mean(arr):
    if(isinstance(arr, np.ndarray) == False or arr.size == 0):
        print('invalid argument')
        return 0
    return (1/arr.size)*arr.sum()

def my_std(arr):
    if(isinstance(arr, np.ndarray) == False or arr.size == 0):
        print('invalid argument')
        return 0
    return np.sqrt(my_var(arr))

def my_var(arr):
    if(isinstance(arr, np.ndarray) == False or arr.size == 0 or arr.size == 1):
        print('invalid argument')
        return 0
    return (1/(arr.size-1))*((arr-my_mean(arr))**2).sum()
