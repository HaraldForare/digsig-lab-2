
import numpy as np


def OFDM_transmission(x_n, noise_variance, alpha):
    N = len(x_n)

    S_tilde_k = x_n

    s_tilde_n = np.fft.ifft(S_tilde_k, N)

    H_n = np.array([1, alpha])
    L = len(H_n)

    s_n = np.append(s_tilde_n[-(L - 1):], s_tilde_n)

    r_n = np.convolve(s_n, H_n)

    # Add noise
    noise = np.random.normal(0, np.sqrt(noise_variance / 64 / 2), len(r_n))
    noise = noise + 1j*noise

    r_n += noise

    breakpoint()

    r_tilde_n = r_n[L - 1:-(L - 1)]

    R_tilde_k = np.fft.fft(r_tilde_n, N)

    y_n = R_tilde_k

    H_k = np.fft.fft(H_n, N)

    x_n_recovered = y_n / H_k
    x_n_recovered = np.real(x_n_recovered)

    return x_n_recovered




