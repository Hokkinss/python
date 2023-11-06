import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.log(x) + np.cos(x)

x = np.linspace(0.001, 10, 1000)

y = func(x)

plt.plot(x, y, label="log(x) + cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции log(x) + cos(x)")
plt.legend()
plt.grid()
plt.show()
