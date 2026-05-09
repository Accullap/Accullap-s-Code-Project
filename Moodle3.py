import numpy as np

def h(t, alpha):
    return np.exp(-2 * alpha * t) * np.sin(np.pi * t)

h(2,2)