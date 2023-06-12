import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = 3*x ** 2 + 2*x + 1
plt.plot(x, y)
plt.axis([0,max(x),0,max(y)])
plt.xlabel("x")
plt.ylabel("y = 3*x ** 2 + 2*x + 1")
plt.title("Quadratic Equations")
plt.show()
