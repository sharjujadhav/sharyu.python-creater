41.Calculate the nth term of an arithmetic progression.


def nth_term_of_ap(a_1, n, d):
    if n < 1:
        return "invalid input: n should be a positive integer."
    a_n = a_1 + (n-1) * d 
    return a_n
a_1 = 2
n = 5
d = 3
result = nth_term_of_ap(a_1, n, d)
print(f"the {n}th term of the arithmetic progression is : {result}")
