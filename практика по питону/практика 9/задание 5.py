import time
import numpy as np
from scipy.stats import multivariate_normal


def logarifm(X, m, C):
    detCov = np.linalg.det(C)
    invCov = np.linalg.inv(C)


    X_centered = X - m


    exponent = -0.5 * np.sum(X_centered @ invCov * X_centered, axis=1)

    normalization = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(detCov)

    log = exponent + normalization
    return log



N = 10
D = 7
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T)

start_time = time.time()
result_custom = logarifm(X, m, C)
custom_duration = time.time() - start_time

start_time = time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time


print(result_custom)
print(result_scipy)


print(custom_duration)
print(scipy_duration)