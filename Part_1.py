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

# z = np.polyfit(b,a,1)
#
# p = np.poly1d(z)
#
# plt.scatter(p(b),b+a)
# plt.show()

#########Exercise 3############
# k = np.cumsum(a)
#
# plt.plot(b,k)
# plt.show()


###########Exercise 4 ########################


from scipy.stats import multivariate_normal as mlt

mean = [0,0]
co_var = [[1,-0.5],[-0.5,2]]


# mult_norm = mlt.rvs(mean=mean,cov=co_var , size=1000)
# plt.scatter(mult_norm[:,0], mult_norm[:,1])
# plt.show()
# print(mult_norm([2,3]))
# print(mult_norm)
