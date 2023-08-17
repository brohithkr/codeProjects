import matplotlib.pyplot as plt
import numpy as np

x = np.arange(40)
y = (np.exp(x))

plt.plot(x,y)
# plt.show()
plt.savefig("hello.svg")
# plt.close()
# plt.savefig("hello2.svg")