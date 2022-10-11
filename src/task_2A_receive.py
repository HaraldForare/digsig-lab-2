


import matplotlib.pyplot as plt
import numpy as np


from task_1A import get_random_signal

D = 1
alphas = (
    0.0,
    0.5,
    -0.99
)

transmitted_signal = get_random_signal(64)

def get_received_signal(transmitted_signal, reflection_scaling_coefficient):
    return np.convolve(transmitted_signal, np.array([1, reflection_scaling_coefficient]))


_doRenderGraphs = __name__ == "__main__"


if _doRenderGraphs:
    fig, axes = plt.subplots(1 + len(alphas), 1)
    fig.set_size_inches(9, 16)
    axes[0].set_title("Transmitted Signal")
    axes[0].stem(transmitted_signal)



for ax_index, alpha in enumerate(alphas, 1):
    if _doRenderGraphs:
        axes[ax_index].set_title(f"Received Signal - Reflection Scaling Coefficient = {alpha}")
        axes[ax_index].stem(get_received_signal(transmitted_signal, alpha)[:len(transmitted_signal)])



if _doRenderGraphs:
    plt.savefig("output/task_2_received_signals.svg")







