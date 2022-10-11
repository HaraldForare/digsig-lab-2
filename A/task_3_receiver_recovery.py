

import matplotlib.pyplot as plt

import numpy as np
from scipy.signal import lfilter as filter

#from task_2_recover import alphas


from task_1 import get_random_signal
from task_2_receive import get_received_signal
from count_bit_errors import count_bit_errors


transmitted_signal = get_random_signal(10_000)


errorSeries = list()
alphaSeries = list()


alphas = np.linspace(-3, 3, 1000)

for alpha in alphas:
    received_signal = get_received_signal(transmitted_signal, alpha)[:len(transmitted_signal)]

    denominator = np.array([1, alpha])
    numerator = np.array([1])

    recovered_signal = filter(numerator, denominator, received_signal)

    num_bit_errors = count_bit_errors(recovered_signal, transmitted_signal)

    errorSeries.append(100 * num_bit_errors / len(transmitted_signal))
    alphaSeries.append(alpha)



if __name__ == "__main__":
    plt.plot(alphaSeries, errorSeries)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage bit errors")
    plt.savefig("output/task_3_filter_receiver_recovery.svg")
    plt.show()




