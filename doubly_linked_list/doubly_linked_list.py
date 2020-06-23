"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.value = value
        self.prev = prev
        self.next_node = next_node

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointed to."""
    def insert_after(self, value):
        current_next = self.next_node
        self.next_node = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next_node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next_node = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next_node = self.next_node
        if self.next_node:
            self.next_node.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        if self.head is None and self.tail is None:
            self.length = 0
        else:
            current_node = self.head
            length = 1
            while current_node.next_node is not None:
                current_node = current_node.next_node
                print(length)
                self.length = length
        return self.length

    def __str__(self):
        return f'the length of the DLL is {self.length}, head : {self.head.value}, tail: {self.tail.value}'

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        old_head = self.head
        new_node = ListNode(value, None, old_head)
        self.length += 1
        if old_head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head.prev = new_node
            self.head = new_node
            new_node.next_node = old_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return None
        old_head = self.head
        self.delete(old_head)
        return old_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        old_tail = self.tail
        new_node = ListNode(value, old_tail, None)
        self.length += 1
        if old_tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail.next_node = new_node
            self.tail = new_node
            new_node.prev = old_tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        old_tail = self.tail
        self.delete(old_tail)
        return old_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None                
            self.tail = None
        elif self.head == node:
            self.head = node.next_node        
            node.delete()
        elif self.tail == node:
            self.tail = node.prev        
            node.delete()
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next_node
        return max_val

# node1 = ListNode(47)
# dll = DoublyLinkedList(node1)
# dll.add_to_head(41)
# dll.add_to_head(42)
# dll.add_to_head(43)

# print(dll)