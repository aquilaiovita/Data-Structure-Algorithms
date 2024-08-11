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
            return

        count = 0
        current_node = self.head
        while (count+1 != index and current_node.next is not None):
            count += 1
            current_node = current_node.next

        if count+1 != index:
            print("Not not added: Index not found")
        else:
            node.next = current_node.next 
            current_node.next = node 
            print(f"Inserted node at index {index}")

    # Insert at the end
    def insert_end(self,data):
        node = self.head 
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        print(f"Inserted node at end")

    # Update node at index
    def update_node(self, data, index):
        current_node = self.head 
        count = 0
        while (count != index and current_node.next is not None):
            current_node = current_node.next
            count += 1 
        if count == index:
            current_node.data = data
            print(f"Node updated at index {index}")
        else:
            print("Not not updated: Index not found")
    
    # Delete first node from link list
    def delete_first(self):
        if self.head:
            first_node = self.head 
            self.head = first_node.next
            del first_node
        else:
            print("Empty list: No first node")

    # Delete last node
    def delete_last(self):
        if not self.head:
            print("Empty list: No last node")
            return
        current_node = self.head 
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    # Delete node at given index
    def del_at_index(self, index):
        if index == 0:
            self.delete_first()
            return
        
        count = 0
        current_node = self.head
        while (count+1 != index and current_node.next is not None):
            current_node = current_node.next 
            count += 1        

        if count+1 == index:
            current_node.next = current_node.next.next
        else:
            print("Index out of range")

    # Delete first node of given data
    def del_first_node_data(self, data):
        current_node = self.head 
        if current_node.data == data:
            self.delete_first()
        else:
            count = 0
            while (current_node.next is not None and current_node.next.data != data):
                current_node = current_node.next
                count += 1
            if current_node.next is not None:
                self.del_at_index(count+1)
            else:
                print(f"{data} not found in linked list")
                
        

linkList = LinkedList()
linkList.insert_beginning(6)
linkList.insert_beginning(5)
linkList.insert_beginning(4)
linkList.insert_beginning(2)
linkList.insert_at_position(1,0)
linkList.insert_at_position(3,2)
linkList.insert_end(7)
linkList.insert_end(7)
linkList.update_node(8,7)

linkList.print_list()

linkList.delete_first()
linkList.delete_last()
linkList.del_at_index(2)
linkList.del_first_node_data(7)
linkList.del_first_node_data(7)
linkList.print_list()