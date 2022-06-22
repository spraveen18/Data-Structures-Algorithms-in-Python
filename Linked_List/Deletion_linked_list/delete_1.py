# Deleting a node (Deleting a given key)
"""
To delete a node from the linked list, we need to do the following steps. 
1) Find the previous node of the node to be deleted. 
2) Change the next of the previous node. 
3) Free memory for the node to be deleted.

"""


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
        
        
    def Delete_node(self, key):
        temp = self.head           # Store head node
        
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'    
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
            
        if (temp == None):
            return
        
        prev.next = temp.next
        temp = None
                
        
#The %d operator is used as a placeholder to specify integer values, decimals or numbers. 
#It allows us to print numbers within strings or other values. The %d operator is put where the integer 
#is to be specified. Floating-point numbers are converted automatically to decimal values.      
      
        
   
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data), end = " "),
            temp = temp.next   
        

        
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print ("Created Linked List: ")
llist.printList()       # 2  3  1  7 


print ("\nLinked List after Deletion of 1:")
llist.Delete_node(1)
llist.printList()    # 2  3  7 



        
        
        
