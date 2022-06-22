class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end =" ")
            temp = temp.next

        
if __name__=='__main__':  #code starts from here
                          #lets create a list with three nodes

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2) 
    third = Node(3)

    llist.head.next = second;
    second.next = third;
    
    
    llist.print_list()

    #print("\n", llist.head.data) 
