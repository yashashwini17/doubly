class Node:
    def __init__(self,val):
       self.data=val
       self.next=None
def createLinkedList(arr):
    head=None
    for val in arr:
        if (head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    printLinkedList(head)
def printLinkedList(head):
    temp=head
    while(temp):
          print(temp.next)
          temp=temp.next
arr=list(map(int,input().split()))
createLinkedList(arr)
