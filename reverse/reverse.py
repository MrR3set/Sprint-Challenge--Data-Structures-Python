class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if not self.head:
            return None
        current = node #head
        nextNode = current.get_next()
        if current is not None:
            current.set_next(prev)
            # print("Current",current.value, current.get_next())
            prev = current
            # print("prev",prev.value, prev.get_next())
            current = nextNode
            # print("Current",current.value, current.get_next().value)
            # print("next",current.value, current.get_next().value)
            if nextNode is not None:
                self.reverse_list(current,prev)
            else:
                self.head = prev
                

    def print(self):
        if not self.head:
            return None
        node = self.head
        while node is not None:
            print(node.get_value())
            node = node.get_next()

    


# nList = LinkedList()
# nList.add_to_head(1)
# nList.add_to_head(83)
# nList.add_to_head(34)
# nList.add_to_head(15)
# nList.add_to_head(1561)
# nList.add_to_head(198)
# nList.add_to_head(64)
# nList.add_to_head(0)


# nList.print()

# print("Rev","*"*50)

# nList.reverse_list(nList.head,None)

# nList.print()