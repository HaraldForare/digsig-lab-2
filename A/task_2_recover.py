

import matplotlib.pyplot as plt


import numpy as np


from task_1 import get_random_signal
from task_2_receive import get_received_signal



transmitted_signal = get_random_signal(10_000)



alphas = np.linspace(-3, 3, 1000)



errorSeries = list()
alphaSeries = list()


zero_errors = list()

for alpha in alphas:
    received_signal = get_received_signal(transmitted_signal, alpha)[:len(transmitted_signal)]

    # Add noise
    #received_signal += np.random.normal(0, 0.5, len(received_signal))




    recovered_signal = ((received_signal > 0).astype("float64") - 0.5) * 2

    errors = transmitted_signal - recovered_signal
    errors = np.count_nonzero(np.abs(errors) > 0.000001)
    errors /= len(recovered_signal)

    alphaSeries.append(alpha)
    errorSeries.append(errors * 100)

    """
    if errors == 0:
        zero_errors.append(alpha)
    """



if __name__ == "__main__":
    plt.plot(alphaSeries, errorSeries)
    plt.xlabel("reflection scaling coefficient")
    plt.ylabel("percentage errors")
    plt.savefig("output/task_2_number_of_errors.svg")










