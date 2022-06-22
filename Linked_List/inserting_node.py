#INSERTING A NODE
      
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:                                         #  check if the given prev_node exists
            print("the previous node should be in linked list")
            return
    
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    
    
    # 3. Appends a new node at the end

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next
        
        last.next = new_node    
        
    
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end =" ")
            temp = temp.next

        

llist = LinkedList()

llist.append(6)

llist.print_list()    # output :6

print("\n")
llist.push(7);

llist.print_list()  # 7 6

print("\n")
llist.push(1);

llist.print_list()   # 1 7 6

print("\n")
llist.append(4)   
llist.print_list()   # 1 7 6 4

print("\n")
llist.insertAfter(llist.head.next, 8)  #insert 8,  after 7
llist.print_list()      # 1 7 8 6 4

print("\n")
print('Created linked list is: ')
llist.print_list()     # 1 7 8 6 4 





"""
# 1. Function to insert a new node at the beginning

def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


# 2. Inserts a new node after the given prev_node

def insertAfter(self, prev_node, new_data):
    if prev_node is None:                                         #  check if the given prev_node exists
        print("the previous node should be in linked list")
        return
    
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
 # 3. Appends a new node at the end

def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return
    
    last = self.head
    while (last.next):
        last = last.next
        
    last.next = new_node    
           
 """   
