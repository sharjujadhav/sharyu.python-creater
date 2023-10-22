47.Extract a submatrix from a larger matrix.
import numpy as np 
arr = np.arange(16).reshape(4,4)
print("origanal matrix:\n",arr,"\n")
res = arr[np.ix_([0,3],[0,3])]
print("created submatrix:\n",res,"\n")

