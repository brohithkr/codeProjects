import matplotlib.pyplot as plt
import numpy as np

rand = np.random.RandomState(283728)
x = rand.randint(20,60,5)
y = rand.randint(40,80,5)

plt.scatter(x,y)

plt.errorbar(
    x = x[y<60],
    y = y[y<60],
    xerr = 1,
    yerr = 2,
    fmt = 'o',
    color = 'red'
)
print(x,y)
# print()
plt.show()