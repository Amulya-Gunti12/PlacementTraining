#Linked list in python
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def delete(self,key):
         temp=self.head
         if temp and temp.data==key:
             self.head=temp.next
             return

         prev=None
         while temp and temp.data!=key:
             prev=temp
             temp=temp.next
         prev.next=temp.next

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print(None)

ll=Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()
ll.delete(20)
ll.display()

