#######There are 5 exercise which is for warm up

#Exercise 1


import numpy as np
import matplotlib.pyplot as plt

a = np.random.standard_normal(1000)
b = np.array([i for i in range(1000)])
# print(a)
# plt.hist(a, bins = 10, range = (0,1), color="red", histtype="bar")
# plt.show()
# plt.plot(b,a)
# plt.show()

########Exercise 2##################

z = np.polyfit(b,a,1)

p = np.poly1d(z)

plt.scatter(p(b),b)
plt.show()
