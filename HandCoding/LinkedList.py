class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            here = self.head
            while here.next:
                here = here.next
            here.next = new_node
        else:
            self.head = new_node

    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next
            return
        else:
            prev = self.head
            here = prev.next
            crnt_idx = 1
            while here:
                if crnt_idx == idx:
                    prev.next = here.next
                    return
                prev = here
                here = here.next
                crnt_idx += 1

    def add_at_index(self, idx, data):
        new_node = Node(data)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            crnt_idx = 1
            prev = self.head
            here = prev.next
            while here:
                if crnt_idx == idx:
                    prev.next = new_node
                    new_node.next = here
                    return
                prev = here
                here = here.next
                crnt_idx += 1
            if crnt_idx == idx:
                prev.next = new_node

    def find(self, data):
        here = self.head
        while here:
            if here.data == data:
                return here
            here = here.next

    def print_all(self):
        here = self.head
        while here:
            print(here.data, end=' ')
            here = here.next
        print()


LL = LinkedList()
LL.append(3)
LL.append(6)
LL.append(4)
LL.append(2)
LL.append(5)
LL.print_all()

LL.add_at_index(5, 14)
LL.print_all()
LL.add_at_index(0, 11)
LL.print_all()

LL.delete(4)
LL.print_all()
LL.delete(0)
LL.print_all()