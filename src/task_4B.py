

import numpy as np


from OFDM_transmission import OFDM_transmission



from task_1A import get_random_signal



alpha_series = list()
error_series = list()

for alpha in np.linspace(-3, 3, 1_000):
    X = get_random_signal(64)
    Y = OFDM_transmission(X, 0.0, alpha)

    Y = ((Y > 0).astype("float64") - 0.5) * 2

    number_of_errors = np.count_nonzero(np.abs(X - Y) > 10**(-8))
    percentage_errors = 100 * number_of_errors / len(X)

    alpha_series.append(alpha)
    error_series.append(number_of_errors)



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.plot(alpha_series, error_series)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage bit errors")
    plt.show()







