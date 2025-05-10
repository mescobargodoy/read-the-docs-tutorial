import numpy as np

def line(x, m, b):
    """
    Computes linear equation for given
    slope, intercept and x-value.

    Parameters
    ----------
    x : ndarray
        independent variable
    m : float
        slope
    b : float
        intercept

    Returns
    -------
    ndarray
        Line equation
    """

    return m*x+b
