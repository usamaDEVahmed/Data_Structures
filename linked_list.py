
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    
    head = None
    size = 0

    def add(self, data):
        node = Node(data=data)
        
        if LinkedList.head is None:
            LinkedList.head = node
        else:
            temp = LinkedList.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def add_at_start(self, data):
        node = Node(data)
        temp = LinkedList.head
        LinkedList.head = node
        LinkedList.head.next = temp

    def add_at_position(self, data, position):
        node = Node(data)
        pos = 0

        temp = LinkedList.head

        while pos < position-1:
            pos += 1
            temp = temp.next
        
        temp2 = temp.next
        temp.next = node
        temp.next.next = temp2
    
    def reverse(self):
        prev = None
        curr = LinkedList.head

        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        LinkedList.head = prev
    
    def reverse_recursively(self):
        return self.do_reverse_recursively(LinkedList.head)
    
    # it will return the head of the reversed linked list
    def do_reverse_recursively(self, head, prev=None):
        if not head:
            return prev
        next_ = head.next
        head.next = prev
        return self.do_reverse_recursively(next_, head)


    def display(self):
        temp = LinkedList.head

        while temp is not None:
            print(str(temp.data) + ' -> ', end='')
            temp = temp.next
        print('None')

    def get_head(self):
        return LinkedList.head


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add(5)
    linked_list.add(4)
    linked_list.add(3)
    linked_list.add(2)
    linked_list.add(1)

    linked_list.display()

    h = linked_list.reverse_recursively()

    tmp = h
    while h:
        print(h.data, end=' -> ')
        h = h.next
    print('None')