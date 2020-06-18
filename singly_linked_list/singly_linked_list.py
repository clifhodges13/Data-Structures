class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None and self.tail is None:
            self.size = 0
        else:
            current_node = self.head
            size = 1
            while current_node.next is not None:
                current_node = current_node.next
                print(size)
                self.size = size
        return self.size

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None and self.tail is None:
            return None
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
            self.tail = current_node
        pass

    def remove_head(self):
        if self.head is None and self.tail is None:
            return self.head
        else:
            self.head = self.head.next
    
    def get_max(self):
        pass

    def contains(self,value=None):
        pass

    def __str__(self):
        return f'The size of the stack is {self.size}.'
