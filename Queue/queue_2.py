# Array implementation of Queue (with pop() and append() python list fucntions)

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = capacity
        
    def enqueue(self, data):
        if (self.capacity == self.rear):
            print("\n queue is full")
            
        else:
            self.queue.append(data)
            self.rear += 1
            
    def dequeue(self):
        if (self.front == self.rear):
            print("queue is empty")
            
        else:
            x = self.queue.pop(0)
            self.rear -= 1
            
    def queue_display(self):
        if (self.front == self.rear):
            print("queue is empty")
            
        for i in self.queue:
            print(i, "<--", end = " ")
            
    def queue_front(self):
         
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        print("\nFront Element is:",
              self.queue[self.front]) 



    
que = Queue(4)

que.queue_display()

que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)




que.queue_display()

que.enqueue(60)

que.dequeue()
que.dequeue() 
que.queue_display()

print("\n", len(que.queue))


que.enqueue(60)

que.queue_display()

que.queue_front()

"""
output:

queue is empty
20 <-- 30 <-- 40 <-- 50 <-- 
 queue is full
40 <-- 50 <-- 
 2
40 <-- 50 <-- 60 <-- 
Front Element is: 40

"""


        
