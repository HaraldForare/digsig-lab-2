

from scipy.signal import lfilter as filter
import matplotlib.pyplot as plt
import numpy as np
import math


from task_1A import get_random_signal
from task_2A_receive import get_received_signal
from count_bit_errors import count_bit_errors


do_include_noise = True

do_processing_in_transmitter = True  # Modify this to change behaviour
do_processing_in_receiver = not do_processing_in_transmitter


inputted_signal = get_random_signal(10_000)


errorSeries = list()
alphaSeries = list()
for alpha in np.linspace(-3, 3, 1000):
    denominator = np.array([1, alpha])
    numerator = np.array([1])

    if do_processing_in_transmitter:
        transmitted_signal = filter(numerator, denominator, inputted_signal)

    else:
        transmitted_signal = inputted_signal


    received_signal = get_received_signal(transmitted_signal, alpha)[:len(inputted_signal)]

    if do_include_noise:
        received_signal += np.random.normal(0, math.sqrt(0.25), len(received_signal))


    if do_processing_in_receiver:
        recovered_signal = filter(numerator, denominator, received_signal)

    else:
        recovered_signal = received_signal


    # Perform bit detection
    recovered_signal = ((recovered_signal > 0).astype("float64") - 0.5) * 2

    num_bit_errors = count_bit_errors(recovered_signal, inputted_signal)

    errorSeries.append(100 * num_bit_errors / len(transmitted_signal))
    alphaSeries.append(alpha)



if __name__ == "__main__":
    plt.plot(alphaSeries, errorSeries)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage bit errors")
    plt.show()




