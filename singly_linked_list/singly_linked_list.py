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

    def remove_head(self):
        if self.head is None and self.tail is None:
            return self.head
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next
        return head_value
    
    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        if self.head.next is None:
            max_value = self.head.value
            return max_value
        current_node = self.head
        max_value = 0
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
                return current_node.value

    def contains(self,value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        return f'The size of the stack is {self.size}.'
