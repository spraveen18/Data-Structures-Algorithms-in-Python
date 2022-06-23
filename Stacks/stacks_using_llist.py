# Stacks using Linked List

class stack_node:
    def __init__(self, data):
        self.data = data
        self.next = None
     

class Stack:
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return True if self.root is None else False
    
    def push(self ,data):
        new_node = stack_node(data)
        new_node.next = self.root
        self.root = new_node
        print(" %d pushed to stack" % (data))
        
    def pop(self):
        if (self.is_empty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    
    def peek(self):
        if (self.is_empty()):
            return float("-inf")
        return self.root.data
    
    
    def print_stack(self):
        temp = self.root
        while(temp):
            print (" %d " % (temp.data),end=" ")
            temp = temp.next
    
    
stack = Stack()
stack.push(10)
stack.push(15)
stack.push(20)

print("stack is:")  
stack.print_stack()

print("\n")
print("%d popped from stack" %(stack.pop()))

print("Top element is: %d " % (stack.peek()))

print("\n")
print("stack after popping an element: ")
stack.print_stack()


"""
output:
10 pushed to stack
 15 pushed to stack
 20 pushed to stack
stack is:
 20   15   10  

20 popped from stack
Top element is: 15 


stack after popping an element: 
 15   10  
 
"""
        
