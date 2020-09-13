import numpy as np
from scipy import linalg

savedir = 'Output'

def save_fig_as_png(figtitle):
    '''
    Saves the current figure into the output folder
    The figtitle should not contain the ".png".
    This helper function shoudl be easy to use and should help you create the figures 
    needed for the report
    
    The directory where images are saved are taken from savedir in "Code.py" 
    and should be included in this function.
    
    Hint: The plt.gcf() might come in handy
    Hint 2: read about this to crop white borders
    https://stackoverflow.com/questions/8218608/scipy-savefig-without-frames-axes-only-content
    
    '''

    raise NotImplementedError

    

def sum_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Sum two numbers.

    Args:
        x (int, float): first number in sum
        y (int, float): second number in sum
    Returns:
        Sum of x and y.
    """
    # replace the following line with an actual implementation that returns something
    raise NotImplementedError

def multiply_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Multiply two numbers.

    Args:
        x (int, float): first number in product
        y (int, float): second number in product
    Returns:
        Product of x and y.
    """
    
    # replace the following line with an actual implementation that returns something
    raise NotImplementedError

def create_add_matrix(x):
    """
    TODO: IMPLEMENT ME
    Step 1. Create a 3x3 numpy array whose elements are all ones.
    Step 2. Sum the array and the input array x.
    Step 3. Return the result
    
    Args:
        x (np.ndarray): a 2D numpy array
    Returns:
        output (np.ndarray): the operation result
    """

    # replace the following line with an actual implementation that returns something
    raise NotImplementedError
    
def indexing_aggregation(x, n):
    """
    TODO: IMPLEMENT ME
    Return the mean value of the first n elements of the input array x.

    Args:
        x (np.ndarray): a 1D numpy array
    Returns:
        output (float): the operation result

    """
    # replace the following line with an actual implementation that returns something
    raise NotImplementedError
  
def matrix_inverse(A):
    """
    TODO: IMPLEMENT ME
    Return the inverse of Matrix A.
    
    Checks for dimension mismatch

    Args:
        x (np.ndarray): a 2D numpy array
    Returns:
        output (np.ndarray): the operation result

    """
    # replace the following line with an actual implementation that returns something
    raise NotImplementedError

