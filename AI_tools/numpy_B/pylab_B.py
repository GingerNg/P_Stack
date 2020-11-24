import numpy as np
import pylab
# # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# mu, sigma = 2, 0.5
# v = np.random.normal(mu, sigma, 10000)
# # Plot a normalized histogram with 50 bins
# pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
# pylab.show()
# # Compute the histogram with numpy and then plot it
# (n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
# pylab.plot(.5*(bins[1:]+bins[:-1]), n)
# pylab.show()


a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])


def ufunc_reduce(ufct, *vectors):
    # todo
    vs = np.ix_(*vectors)
    # print(vs)
    r = ufct.identity
    for v in vs:
        r = ufct(r, v)
    return r


res = ufunc_reduce(np.add, a, b, c)
print(res)
print(res.shape)  # (4, 3, 5)
