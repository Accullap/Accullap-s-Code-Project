import numpy as np


def read_and_compute(filename):
    data = np.loadtxt(filename, delimiter=",", dtype=int)
    
    values = data[:, 1]
    
    mean = np.mean(values)
    std = np.std(values)
    
    unique_values, counts = np.unique(values, return_counts=True)
    most_common = unique_values[np.argmax(counts)]
    
    return mean, std, most_common



result = read_and_compute("test.csv")
print(result)
