import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x) * np.cos(x)

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y = func(x)

plt.plot(x, y, label="sin(x) * cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции sin(x) * cos(x)")
plt.legend()
plt.grid()
plt.show()
