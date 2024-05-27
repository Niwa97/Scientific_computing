import numpy as np
from numba import jit

@jit(nopython=True, parallel=True) #with numba around 5 seconds, without numba around 2 min
def monte_carlo_pi():
  N = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]

  for n in N:
    points = np.random.uniform(-1, 1, size=(n, 2))
    counter = 0
    for i in range(n):
      if( (points[i][0]**2 + points[i][1]**2) <= 1 ):
        counter += 1
    print(4.0 * counter / n)

monte_carlo_pi()
