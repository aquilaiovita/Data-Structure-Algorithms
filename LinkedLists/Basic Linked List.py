class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

# Print whole list
    def print_list(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

# Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        print(f"Inserted {new_node.data} at beginning")
    
# Insert Node at specific position
    def insert_at_position(self, data, index):
        # List follows 0 indexing like in python
        node = Node(data)
        if index == 0:
            self.insert_beginning(data)

        count = 0
        current_node = self.head
        while (count+1 != index and current_node.next is not None):
            count += 1
            current_node = current_node.next

        if current_node.next is None:
            print("Out of range index")
        else:
            node.next = current_node.next 
            current_node.next = node 
    

        
    
linkList = LinkedList()
linkList.insert_beginning(6)
linkList.insert_beginning(5)
linkList.insert_beginning(4)
linkList.insert_beginning(2)
linkList.insert_at_position(1,0)
linkList.insert_at_position(3,2)
linkList.print_list()
