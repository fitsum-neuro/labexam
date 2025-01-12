import numpy as np
def compute_cross_product(A, B):
    C = A.dot(B)
    return C

A = np.array([1, 2, 3])
B = np.array([1, 2, 5])

compute_cross_product(A, B)