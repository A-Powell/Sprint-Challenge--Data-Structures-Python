from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # Check is the storage is full
    # If it is not, add the item to the tail
    # update current
    # if it is full, remove the head since it is old
    # and add the item to the tail after space is free
    # check if the removed head is our current, if so set current to the tail.

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            remove = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if remove == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.current
        list_buffer_contents.append(node.value)

        if node.next is not None:
            node_2 = node.next
        else:
            node_2 = self.storage.head

        while node_2 != node:
            list_buffer_contents.append(node_2.value)
            if node_2.next is not None:
                node_2 = node_2.next
            else:
                node_2 = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = []
        pass

    def get(self):
        pass
