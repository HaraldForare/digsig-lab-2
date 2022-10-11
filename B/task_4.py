

import numpy as np


from OFDM_transmission import OFDM_transmission


import os
os.chdir("..")


from A.task_1 import get_random_signal



alphaSeries = list()
errorSeries = list()


for alpha in np.linspace(-3, 3, 1_000):

    OFDM_transmission(get_random_signal(64), 0.5, 0.3)

    alpha = 0.3
    N = 64



    x_n = get_random_signal(N)
    S_tilde_k = x_n


    s_tilde_n = np.fft.ifft(S_tilde_k, N)

    #s_tilde_n += np.random.normal(0, 0.5, N)


    H = np.array([1, alpha])
    L = len(H)


    s_n = np.append(s_tilde_n[-(L-1):], s_tilde_n)

    r_n = np.convolve(s_n, H)


    r_tilde_n = r_n[L-1:-(L-1)]

    R_tilde_k = np.fft.fft(r_tilde_n, N)

    y_n = R_tilde_k

    H_k = np.fft.fft(H, N)


    x_n_recovered = y_n / H_k
    x_n_recovered = np.real(x_n_recovered)

    breakpoint()

    error = np.abs(x_n - x_n_recovered)
    max_error = np.max(error)
    num_errors = np.count_nonzero(error > 0.000001)
    percentage_errors = num_errors / N

    alphaSeries.append(alpha)
    errorSeries.append(percentage_errors)



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.plot(alphaSeries, errorSeries)
    #plt.savefig("task_5_noise_free_flex.svg")
    plt.show()







