# Queue follows order of First In First Out (FIFO)
# Array implementation Of Queue 

class Queue():
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity
        
        
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue already reached maximum capacity")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue" % str(item))
        
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size -1
        
        
    def queue_front(self):
        if self.is_empty():
            print("Queue is Empty")
        print("Front item is: ", self.Q[self.front])
        
        
    def queue_rear(self):
        if self.is_empty():
            print("Queue is Empty")
        print("Rear item is",  self.Q[self.rear])    
        
        
queue = Queue(30)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.queue_front()
queue.queue_rear()   


"""
output:
10 enqueued to queue
20 enqueued to queue
30 enqueued to queue
40 enqueued to queue
10 dequeued from queue
Front item is:  20
Rear item is 40

"""
        
