class Node:
    def __init__(self,data=None,next=None):
        self.data= data
        self.next=next
class Sll:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            print("linked is not empty")
    def insert_at_start(self,value):
        n=Node(value,self.head)
        self.head=n
    def insert_at_last(self,value):
        n=Node(value)
        if self.head is not None:
            current = self.head
            while current.next:
                current=current.next
            current.next=n
        else:
            self.head=n
    def search(self,value):
        current=self.head
        while current is not None:

n1=Sll()
