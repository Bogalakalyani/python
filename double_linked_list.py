class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def traverseLL(self):
        n = self.head
        while n is not None:
            print(f"{n.data} -->", end = " ")
            n = n.next
        n = self.tail
        print()
        while n is not None:
            print(f"{n.data} <--",end = " ")
            n = n.prev
    def add_empty(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            print("linked list is not empty")
    def add_starting(self,data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def add_last(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            new_node = Node(data)
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n 
            self.tail = new_node
    def add_afer(self,data,x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
        if n is None:
            print("There is no node")
        elif n == self.tail:
            n.next = new_node
            new_node.prev = n 
            self.tail = new_node
        else:
            new_node = Node(data)
            n.next.prev = new_node
            new_node.next = n.next
            new_node.prev = n
            n.next = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
        if n is None:
            print("There is no node")
        else:
            new_node = Node(data)
            n.next.prev = new_node
            new_node.next = n.next
            new_node.prev = n
            n.next = new_node
    def delete_begin(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
    def delete_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next.prev = None
            n.next = None
            self.tail = n
    def delete_by_value(self,x):
        if self.head == x:
            self.head = self.head.next
            self.head.next.prev = None
        elif self.tail == x:
            n.next.prev = None
            n.next = None
            self.tail = n
        elif self.tail == self.head == x:
            self.head = None
            self.tail = None
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n is None:
                print("node is not present")
            else:
                n.next.next.prev = n
                n.next = n.next.next
             

linked_list = DoubleLL()
linked_list.add_empty(10)
linked_list.add_starting(20)
linked_list.add_starting(30)
linked_list.add_last(40)
linked_list.add_afer(100,10)
linked_list.add_before(50,10)
linked_list.delete_begin()
linked_list.delete_end()
linked_list.delete_by_value(50)
linked_list.traverseLL()





            




            

