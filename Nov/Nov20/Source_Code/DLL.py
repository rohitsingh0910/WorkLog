class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class DLL:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            print("Linked List is not empty")

    def insert_at_start(self,value):
        n=Node(data=value,next=self.head)
        if self.head is not None:
            self.head.prev=n
        self.head=n

    def insert_at_end(self,value):
        if self.head is None:
            self.head=Node(data=value)
        else:
            current=self.head
            while current.next:
                current=current.next
            n=Node(prev=current,data=value)
            current.next=n

    def search(self,value):
        current=self.head
        while current:
            if current.data==value:
                return current
            current=current.next
        return None

    def insert_after(self,current,value):
        if self.head!=None:
            n=Node(current,value,current.next)
            if current.next!=None:
                current.next.prev=n
            current.next=n





obj1=DLL()
obj1.is_empty()