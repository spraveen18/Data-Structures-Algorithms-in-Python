# Stacks follow order of LIFO(Last In First Out) or FILO(First In Last Out)
# Stacks using Array

from sys import maxsize

def create_stack():
    stack  = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")
    
def pop(stack):
    if (is_empty(stack)):
        return str(-maxsize-1)   #return minus infinite
    
    return stack.pop()


def peek(stack):            #return top element of stack
    if (is_empty(stack)):
        return "stack is empty"
    
    return "the top element is: " + stack[len(stack) - 1]


stack = create_stack()
push(stack, str(5))
push(stack, str(10))
push(stack, str(15))
print("The stack is: ", stack)
print(peek(stack))
print(pop(stack) + " popped from stack")



"""
output:
5 pushed to stack
10 pushed to stack
15 pushed to stack
The stack is:  ['5', '10', '15']
the top element is: 15
15 popped from stack

"""
