# %load q02_zeros_reshaped/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q01_zeros_array.build import  array_zeros

# Write your code
def array_reshaped_zeros():
    arr = np.zeros((3,4,2))
    zeros_array_reshaped = arr.reshape((2,3,4))
    
    return zeros_array_reshaped

array_reshaped_zeros()


