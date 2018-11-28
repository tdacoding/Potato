import numpy as np

a = np.array([[1,2,3], [4,5,6]])  # создаём массив
print(a.shape)
print(2*np.eye(3, 4, k=0) + np.eye(3, 4, k=1))