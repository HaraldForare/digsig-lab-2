

import numpy as np


def count_bit_errors(u, v, epsilon: float = 0.000001):
    return np.count_nonzero(np.abs(u - v) > epsilon)



