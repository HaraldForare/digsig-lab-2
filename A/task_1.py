


import matplotlib.pyplot as plt

import numpy as np



def get_random_data(length: int):
    return np.random.randint(0, 2, length)



def get_random_signal(length: int):
    return (get_random_data(length) - 0.5) * 2



if __name__ == "__main__":
    random_signal = get_random_signal(64)


    plt.stem(random_signal)
    plt.savefig("output/task_1_random_signal.svg")

    print(f"Sequence: [{' '.join(map(str, map(int, random_signal)))}]")
    print(f"Average: {np.sum(random_signal) / len(random_signal)}")






