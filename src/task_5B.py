

import numpy as np

from OFDM_transmission import OFDM_transmission
from task_1A import get_random_signal

alpha_series = list()
error_series = list()

for alpha in np.linspace(-3, 3, 1000):
    X = get_random_signal(1000)
    Y = OFDM_transmission(X, 0.25, alpha)

    X_bits = (X > 0).astype("int8")
    Y_bits = (Y > 0).astype("int8")

    n_bit_errors = np.count_nonzero(X_bits - Y_bits)

    percentage_bit_errors = 100 * n_bit_errors / len(X)

    alpha_series.append(alpha)
    error_series.append(percentage_bit_errors)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.plot(alpha_series, error_series)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage bit errors")
    plt.show()








