49.Check if the two matrices are equal.


def identicalmatrices(a,b):
    if a==b:
        print ("matrices are equal")
    else:
        print ("matrices are not equal")
if __name__== "__main__":
    a =[ [1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]]
    
    b =[ [ 1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]]
    identicalmatrices(a,b)
