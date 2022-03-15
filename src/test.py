import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

c = [0]*2
c[0] = a
c[1] = b
c = np.concatenate(c)

print(c)


beta = b()
alpha = a(beta)
alpha.hello()


# converting map object to set
