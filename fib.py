
def fibrecursive(n):
    #fib_n = fib_n-1 +fib_n-2
    if n < 2:
        return n
    
    return fibrecursive(n-1) + fibrecursive(n-2)


print(fibrecursive(9))


def factorialrecursive(n):
    #base case
    if n == 1:
        return 1
   
    return n * factorialrecursive(n-1)


inputnumber = 5

print("The factorial of {0} is {1} ".format(inputnumber, factorialrecursive(inputnumber)))



