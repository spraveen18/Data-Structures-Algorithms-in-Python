"""
the Fibonacci sequence, in which each number is the sum of the two preceding ones. 
The sequence commonly starts from 0 and 1

"""
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

         


n_terms = 10 
# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))
    
    
    
    
# fibonacci series (finding element on target position)
def get_fib(position):
    
    if position < 0:
        return -1
    
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)
    
    

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
print(get_fib(-2))    
