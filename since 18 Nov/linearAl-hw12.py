import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def parabola(t,d):

    A = np.array([np.ones(len(t)), t, t**2]).T
    ATA = A.T @ A
    ATb = A.T @ d
    [C,D,E] = np.linalg.inv(ATA) @ ATb

    e = []
    print("y = {0:f} {1:+f}t {2:+f}t^2".format(C,D,E))

    for i in range(0,10):
        error = C + (D*t[i]) + (D*(t[i]**2))
        error = d[i] - error
        e.append(error)

    print("errors: e = {}".format(e))
    y = C + D * t + E * (t ** 2)
    plt.ylabel("distance")
    plt.xlabel("time")
    plt.title("Least Squares Graph")
    plt.plot(t, y, linewidth = 3)
    plt.plot(t, d, 'ro')
    plt.show()

t = np.arange(10)
d = np.random.randint(24, 32, 10)

parabola(t, d)
