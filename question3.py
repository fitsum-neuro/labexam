import numpy as np

def reconstruct_matrix(U,S,V):
    remake =(U @ np.diag(S) @ V) 
    return remake

