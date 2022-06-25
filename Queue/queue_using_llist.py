# Queue – Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def is_empty(self):
        return self.front == None
    
    def enqueue(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.rear = self.front = temp
            return
        
        self.rear.next = temp
        self.rear = temp
        
    def dequeue(self):
        
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None
            
    def print_queue(self):
        temp = self.front
        while(temp):
            print (" %d " % (temp.data), end=" <-- ")
            temp = temp.next        
            

queue = Queue() 

queue.enqueue(10)
queue.enqueue(20)

queue.print_queue()
    
    
queue.dequeue()
queue.dequeue()

print("\n")
queue.print_queue()


queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.print_queue()
queue.dequeue()
print("\n")
queue.print_queue()
print("\n")
print("Queue front: ", str(queue.front.data))
print("Queue rear: ", str(queue.rear.data))


"""

output:

10  <--  20  <-- 

 30  <--  40  <--  50  <-- 

 40  <--  50  <-- 

Queue front:  40
Queue rear:  50

"""
