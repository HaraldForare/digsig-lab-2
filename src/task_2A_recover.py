

import matplotlib.pyplot as plt

import numpy as np

from count_bit_errors import count_bit_errors
from task_1A import get_random_signal
from task_2A_receive import get_received_signal

transmitted_signal = get_random_signal(10_000)

alphas = np.linspace(-3, 3, 1000)


errorSeries = list()
alphaSeries = list()


for alpha in alphas:
    received_signal = get_received_signal(transmitted_signal, alpha)[:len(transmitted_signal)]

    # Add noise, (can be commented out)
    received_signal += np.random.normal(0, 0.5, len(received_signal))

    # Signal thresholding detection (not exactly the data format but 1:1 bijective encoding of it and comparable to transmitted signal)
    recovered_signal = ((received_signal > 0).astype("float64") - 0.5) * 2

    num_errors = count_bit_errors(transmitted_signal, recovered_signal)
    percentage_errors = 100 * num_errors / len(recovered_signal)

    alphaSeries.append(alpha)
    errorSeries.append(percentage_errors)



if __name__ == "__main__":
    plt.plot(alphaSeries, errorSeries)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage errors")










