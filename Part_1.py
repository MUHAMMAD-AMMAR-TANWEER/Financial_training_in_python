#######There are 5 exercise which is for warm up

#Exercise 1


import numpy as np
import matplotlib.pyplot as plt

a = np.random.standard_normal(1000)
b = np.array([i for i in range(1000)])
print(a)
plt.hist(a, bins = 10, range = (0,1), color="red", histtype="bar")
plt.show()
plt.plot(b,a)
plt.show()