def recur(input):
    if input <= 0:
        return input
    else:
        output = recur(input - 1)
        return output
    
    
    
print(recur(10))    



def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results ---> ")
tri_recursion(3)
