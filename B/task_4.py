

import numpy as np


import os
os.chdir("..")


from A.task_1 import get_random_signal



alpha = 0.3


N = 64

x_n = get_random_signal(N)

S_tilde_k = np.fft.fft(x_n, N)


s_tilde_n = np.fft.ifft(S_tilde_k, N)


L = int(round(N * 0.10))


s_n = np.append(s_tilde_n[-(L-1):], s_tilde_n)


r_n = np.convolve(s_n, [1, alpha])

r_tilde_n = r_n[L-1:-(L-1)]


R_tilde_k = np.fft.fft(r_tilde_n, N)

y_n = np.fft.ifft(R_tilde_k, N)

y_n = np.real(y_n)


breakpoint()



