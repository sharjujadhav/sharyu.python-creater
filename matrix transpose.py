43.Create a matrix and find its transpose.

N = 4
def transpose(a,b):
 for i in range(N):
  for j in range(N):
    b[i][j] = a[j][i]
a = [ [1, 1, 1, 1],
 [2, 2, 2, 2],
 [3, 3, 3, 3],
 [4, 4, 4, 4]]
     
b = a[:][:]
transpose(a,b)
print("result matrix is")
for i in range(N):
  for j in range(N):
   print(b[i][j], " ", end='')
print()
